# 🗺️ GBFS Route Planner — Greedy Best-First Search Visualizer

This project is an interactive, visual routing application that demonstrates the **Greedy Best-First Search (GBFS)** pathfinding algorithm on a map of cities based on the classic artificial intelligence problem. It uses a frontend script to animate node expansion, calculate real-time path properties, and compare the estimated straight-line cost to goals with actual layout topologies.

Please note that the frontend implementation for this project is entirely integrated within **`index.html`**.

---

## ✨ Features

* **Greedy Best-First Search Engine:** Uses the straight-line Haversine distance formula to calculate the heuristic values $h(n)$ (estimated cost from any given node to the destination target).


* **Step-by-Step Visualization:** Animates node transitions dynamically through JavaScript intervals, logging exploration order side-by-side with localized values.


* **Variable Animation Speeds:** An interactive range slider component adjusts visualization frame intervals on the fly.


* **Comprehensive Metrics Panel:** Tracks and displays algorithmic statistics such as accumulated travel distances, node hop limits, total expanded counts, and overall routing search efficiency.


* **Responsive SVG Mapping:** Vector layout utilizes custom coordinate projections supporting node grouping elements, glow paths, layout grids, and interactive vector tooltips.



---

## 🛠️ Tech Stack

* **Core Languages:** HTML5, CSS3, JavaScript (ES6+ Vanilla), and Python 3.x.


* **UI Typography:** *Syne* (for headings and stylistic display elements) and *JetBrains Mono* (for data tables, metrics, and technical labels).


* **Data Layout:** Scalable Vector Graphics (SVG) with inline pathing properties and geometric math bindings.



---

## 📁 Project Structure

```text
gbfs-route-planner/
│
├── app.py                  # Main Flask server hosting the web layout
├── gbfs_planner.py         # Standalone Python module managing the graph logic & heaps
└── templates/
    └── index.html          # Monolithic view layer incorporating layout structure, styles, & canvas engines

```

---

## 🚀 Getting Started

Follow these steps to explore or host the routing visualizer on your local architecture.

### 1. Verify Environment

Ensure your local host environment runs an updated installation of Python:

```bash
python --version

```

### 2. Standalone Terminal Application

To process routing data calculations instantly without launching a browser layout, run the core algorithm script using your preferred terminal interface:

```bash
python gbfs_planner.py

```

### 3. Full Web Application Deployment

Launch the standard application runtime via the Flask server module to view the visual interface:

```bash
python app.py

```

Once initialized, open your browser profile and navigate to the local host address:

```text
http://127.0.0.1:5000/

```

---

## 🧠 Algorithmic Behavior Reference

Unlike optimal pathfinding models like Dijkstra or $A^*$, Greedy Best-First Search makes a locally optimal choice at each stage.

$$h(n) = \text{Haversine Distance to Goal}$$

It strictly expands the immediate adjacent neighbor that possesses the **smallest heuristic value $h(n)$** relative to the target city. While this structural behavior typically reduces processing overhead and finishes paths rapidly, it is **not optimal** and can occasionally skip shorter paths due to physical terrain blockages or indirect road networks.
