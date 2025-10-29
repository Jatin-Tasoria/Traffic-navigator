# visualization.py
import matplotlib.pyplot as plt
import math
from config import get_connection

def show_route_visuals(path):

    conn = get_connection()
    cur = conn.cursor()

    # --- Fetch intersections and roads from DB ---
    cur.execute("SELECT id, name FROM intersections;")
    intersections = cur.fetchall()

    cur.execute("""
        SELECT 
            s.id AS source_id,
            d.id AS dest_id,
            s.name || ' - ' || d.name AS road,
            r.distance,
            r.speed_limit,
            r.traffic_factor
        FROM roads r
        JOIN intersections s ON r.source_id = s.id
        JOIN intersections d ON r.destination_id = d.id;
    """)
    all_roads = cur.fetchall()
    conn.close()

    if not all_roads or not intersections:
        print("No data available to visualize.")
        return

    # --- Selected route edges ---
    selected_roads = []
    if path and len(path) >= 2:
        for i in range(len(path) - 1):
            a, b = path[i], path[i + 1]
            for road in all_roads:
                if (road[0] == a and road[1] == b) or (road[0] == b and road[1] == a):
                    selected_roads.append(road)
                    break

    # --- Bar chart data for selected route ---
    road_names = [r[2] for r in selected_roads]
    travel_times = [(r[3] / r[4]) * r[5] for r in selected_roads] if selected_roads else []

    # --- Figure setup (2 charts side by side) ---
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))
    fig.suptitle("Traffic Control Visualization", fontsize=15, fontweight="bold")

    # ---------------- BAR CHART ----------------
    if selected_roads:
        bars = ax1.bar(road_names, travel_times, color="skyblue", width=0.5)
        for bar, time in zip(bars, travel_times):
            ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height()/2,
                     f"{time:.2f} h", ha="center", va="center", fontsize=10)
        ax1.set_xlabel("Road Segments")
        ax1.set_ylabel("Travel Time (hours)")
        ax1.set_title("Selected Route Travel Times")
    else:
        ax1.text(0.5, 0.5, "No Route Selected", ha="center", va="center",
                 fontsize=12, color="gray")
        ax1.axis("off")

    ax1.grid(axis="y", linestyle="--", alpha=0.7)

    # ---------------- NODE GRAPH ----------------
    n = len(intersections)
    positions = {}
    for i, (id, name) in enumerate(intersections):
        # Simple circular layout for visualization
        angle = 2 * math.pi * i / n
        x = 10 * math.cos(angle)
        y = 10 * math.sin(angle)
        positions[id] = (x, y)

    ax2.set_title("All Intersections and Roads (with Travel Times)")
    ax2.axis("off")

    # --- Draw all roads (gray lines + time labels) ---
    for road in all_roads:
        s, d, _, dist, speed, traffic = road
        x1, y1 = positions[s]
        x2, y2 = positions[d]
        time = (dist / speed) * traffic
        ax2.plot([x1, x2], [y1, y2], color="lightgray", linestyle="--", linewidth=1)
        mid_x, mid_y = (x1 + x2)/2, (y1 + y2)/2
        ax2.text(mid_x, mid_y, f"{time:.2f}h", color="gray", fontsize=8, ha="center", va="center")

    # --- Highlight selected route (red edges + red labels) ---
    if selected_roads:
        for road in selected_roads:
            s, d = road[0], road[1]
            x1, y1 = positions[s]
            x2, y2 = positions[d]
            time = (road[3] / road[4]) * road[5]
            ax2.plot([x1, x2], [y1, y2], color="red", linewidth=3, zorder=5)
            mid_x, mid_y = (x1 + x2)/2, (y1 + y2)/2
            ax2.text(mid_x, mid_y, f"{time:.2f}h", color="red", fontsize=9,
                     fontweight="bold", ha="center", va="center")

    # --- Draw all intersections (nodes) ---
    for id, name in intersections:
        x, y = positions[id]
        ax2.scatter(x, y, color="skyblue", s=300, edgecolors="black", zorder=10)
        ax2.text(x, y, name, ha="center", va="center", fontsize=10, fontweight="bold")

    plt.tight_layout()
    plt.show()