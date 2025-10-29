from config import get_connection
from dijkstra import dijkstra
from chart import show_route_visuals

def load_graph():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT id, name FROM intersections;")
    intersections = {i[0]: i[1] for i in cur.fetchall()}

    cur.execute("SELECT source_id, destination_id, distance, traffic_factor, speed_limit FROM roads;")
    roads = cur.fetchall()

    graph = {}
    for s, d, dist, traffic, speed in roads:
        travel_time = (dist / speed) * traffic
        graph.setdefault(s, []).append((d, travel_time))
        graph.setdefault(d, []).append((s, travel_time))

    cur.close()
    conn.close()
    return graph, intersections

def main():
    graph, intersections = load_graph()

    print("\nAvailable Intersections:")
    for k, v in intersections.items():
        print(f"{k}: {v}")

    start = int(input("\nEnter Start Intersection ID: "))
    end = int(input("Enter Destination Intersection ID: "))

    total_time, path = dijkstra(graph, start, end)

    if path:
        names = " → ".join(intersections[i] for i in path)
        print(f"\nFastest Path: {names}")
        print(f"Estimated Travel Time: {total_time:.2f} hours")

        print("\nGenerating combined visualization...")
        show_route_visuals(path)
    else:
        print("No available path found.")

if __name__ == "__main__":
    main()