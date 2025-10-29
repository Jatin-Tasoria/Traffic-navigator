# 🚦 Traffic Controller Mini Project

A **mini traffic control and route optimization system** built using **Python**, **PostgreSQL**, and **Dijkstra’s algorithm** to find the shortest (fastest) path between intersections.  
It also uses **Matplotlib** to visualize:
- A **bar chart** of travel times for each segment in the selected route.
- A **network graph** showing all intersections, roads, and travel times.

---

## 🧩 Features

✅ Implements **Dijkstra’s Algorithm** to find the fastest path  
✅ Connects to a **PostgreSQL** database for storing intersections and roads  
✅ Visualizes **all nodes and roads** in a **network graph**  
✅ Highlights the **selected route in red**  
✅ Displays **travel time (hours)** on every road  
✅ Shows a **bar chart** comparing travel times per segment  
✅ Uses **Matplotlib only** for all graphs (no external graph libraries)

---

## 🗂️ Project Structure

traffic-controller/
│
├── main.py # Entry point of the project
├── dijkstra.py # Contains Dijkstra’s algorithm
├── config.py # Database connection setup
├── visualization.py # All Matplotlib visualizations
├── requirements.txt # Python dependencies
└── README.md # Project documentation (this file)


---

## 🛠️ Requirements

### Prerequisites
Make sure you have:
- **Python 3.8+**
- **PostgreSQL 13+**
- `pip` package manager

### Python Libraries
Install required dependencies:
  pip install psycopg2 matplotlib
