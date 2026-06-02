"""
Greedy Best-First Search (GBFS) Route Planner
==============================================
Finds a path from start to goal using heuristic (straight-line distance).
GBFS always expands the node with the smallest h(n) (estimated cost to goal).

Usage:
    python gbfs_planner.py
"""

import heapq
import math
from typing import Optional


# ----- Graph definition -----

# Each city: (latitude, longitude) for heuristic (haversine distance)
CITIES: dict[str, tuple[float, float]] = {
    "Arad":          (46.1866, 21.3123),
    "Zerind":        (46.6225, 21.5172),
    "Oradea":        (47.0458, 21.9189),
    "Sibiu":         (45.8000, 24.1500),
    "Fagaras":       (45.8416, 24.9730),
    "Rimnicu Vilcea":(45.0997, 24.3695),
    "Pitesti":       (44.8565, 24.8692),
    "Timisoara":     (45.7489, 21.2087),
    "Lugoj":         (45.6910, 21.9030),
    "Mehadia":       (44.9040, 22.3640),
    "Dobreta":       (44.6369, 22.6566),
    "Craiova":       (44.3302, 23.7949),
    "Bucharest":     (44.4268, 26.1025),
    "Giurgiu":       (43.9037, 25.9699),
    "Urziceni":      (44.7165, 26.6413),
    "Hirsova":       (44.6894, 27.9459),
    "Eforie":        (44.0614, 28.6336),
    "Vaslui":        (46.6407, 27.7276),
    "Iasi":          (47.1585, 27.6014),
    "Neamt":         (46.9759, 26.3819),
}

# Undirected edges: (city_a, city_b, distance_km)
EDGES: list[tuple[str, str, float]] = [
    ("Arad",          "Zerind",         75),
    ("Arad",          "Sibiu",          140),
    ("Arad",          "Timisoara",      118),
    ("Zerind",        "Oradea",         71),
    ("Oradea",        "Sibiu",          151),
    ("Sibiu",         "Fagaras",        99),
    ("Sibiu",         "Rimnicu Vilcea", 80),
    ("Fagaras",       "Bucharest",      211),
    ("Rimnicu Vilcea","Pitesti",        97),
    ("Rimnicu Vilcea","Craiova",        146),
    ("Pitesti",       "Bucharest",      101),
    ("Pitesti",       "Craiova",        138),
    ("Timisoara",     "Lugoj",          111),
    ("Lugoj",         "Mehadia",        70),
    ("Mehadia",       "Dobreta",        75),
    ("Dobreta",       "Craiova",        120),
    ("Craiova",       "Bucharest",      180),  # (not in classic map, added for connectivity)
    ("Bucharest",     "Giurgiu",        90),
    ("Bucharest",     "Urziceni",       85),
    ("Urziceni",      "Hirsova",        98),
    ("Hirsova",       "Eforie",         86),
    ("Urziceni",      "Vaslui",         142),
    ("Vaslui",        "Iasi",           92),
    ("Iasi",          "Neamt",          87),
]


def build_graph(edges: list) -> dict[str, list[tuple[str, float]]]:
    """Build adjacency list from edge list."""
    graph: dict[str, list[tuple[str, float]]] = {city: [] for city in CITIES}
    for a, b, dist in edges:
        graph[a].append((b, dist))
        graph[b].append((a, dist))
    return graph


def haversine(city_a: str, city_b: str) -> float:
    """Straight-line (great-circle) distance in km — used as h(n)."""
    lat1, lon1 = CITIES[city_a]
    lat2, lon2 = CITIES[city_b]
    R = 6371.0
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
    return R * 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))


def gbfs(
    graph: dict[str, list[tuple[str, float]]],
    start: str,
    goal: str,
) -> dict:
    """
    Greedy Best-First Search.

    Returns a dict with:
      - path: list of city names from start → goal (or [] if not found)
      - total_distance: sum of edge weights along the path (km)
      - explored: ordered list of cities expanded during search
      - found: bool
    """
    # Priority queue: (h_value, city, path_so_far, cost_so_far)
    h_start = haversine(start, goal)
    frontier: list[tuple[float, str, list[str], float]] = [(h_start, start, [start], 0.0)]
    visited: set[str] = set()
    explored: list[str] = []

    while frontier:
        h, current, path, cost = heapq.heappop(frontier)

        if current in visited:
            continue
        visited.add(current)
        explored.append(current)

        if current == goal:
            return {
                "path": path,
                "total_distance": round(cost, 1),
                "explored": explored,
                "found": True,
            }

        for neighbor, edge_cost in graph[current]:
            if neighbor not in visited:
                h_n = haversine(neighbor, goal)
                heapq.heappush(
                    frontier,
                    (h_n, neighbor, path + [neighbor], cost + edge_cost),
                )

    return {"path": [], "total_distance": 0.0, "explored": explored, "found": False}


# ----- Demo -----

if __name__ == "__main__":
    graph = build_graph(EDGES)

    test_cases = [
        ("Arad", "Bucharest"),
        ("Timisoara", "Iasi"),
        ("Oradea", "Eforie"),
        ("Dobreta", "Neamt"),
    ]

    for start, goal in test_cases:
        result = gbfs(graph, start, goal)
        print(f"\n{'='*55}")
        print(f"  GBFS: {start} → {goal}")
        print(f"{'='*55}")
        if result["found"]:
            print(f"  Path     : {' → '.join(result['path'])}")
            print(f"  Distance : {result['total_distance']} km")
            print(f"  Explored : {', '.join(result['explored'])}")
            print(f"  Steps    : {len(result['path']) - 1} hops, {len(result['explored'])} nodes expanded")
        else:
            print("  No path found.")
