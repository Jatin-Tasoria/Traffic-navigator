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

## 🧠 Technologies Used

| Component                | Technology                                  |
| ------------------------ | ------------------------------------------- |
| **Programming Language** | Python 3.10+                                |
| **Database**             | PostgreSQL                                  |
| **Libraries**            | psycopg2, matplotlib                        |
| **Algorithm Used**       | Dijkstra’s Algorithm (Shortest Path)        |
| **IDE**                  | VS Code / PyCharm                           |
| **Operating System**     | Linux Mint / Windows 10+                    |

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Jatin-Tasoria/Traffic-Controller.git
cd Traffic-Controller
````

### 2️⃣ Install Required Libraries

Ensure Python (3.8 or higher) is installed.
Then install dependencies using pip:

```bash
pip install psycopg2 matplotlib
```

### 3️⃣ Setup PostgreSQL Database

Open **pgAdmin** or **psql** and run:

```sql
CREATE DATABASE traffic_db;

CREATE TABLE intersections (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE roads (
    id SERIAL PRIMARY KEY,
    source_id INT REFERENCES intersections(id),
    destination_id INT REFERENCES intersections(id),
    distance FLOAT,
    speed_limit FLOAT,
    traffic_factor FLOAT
);
```

### 4️⃣ Insert Sample Data

```sql
INSERT INTO intersections (name) VALUES
('A'), ('B'), ('C'), ('D'), ('E');

INSERT INTO roads (source_id, destination_id, distance, speed_limit, traffic_factor) VALUES
(1, 2, 10, 60, 1.2),
(2, 3, 15, 50, 1.0),
(3, 4, 8, 40, 1.5),
(4, 5, 12, 60, 1.1),
(1, 5, 25, 80, 1.3),
(2, 4, 10, 50, 1.4);
```

### 5️⃣ Configure Database Connection

In your `config.py` file:

```python
import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="traffic_db",
        user="your_username",
        password="your_password"
    )
```

### 6️⃣ Run the Project

```bash
python3 main.py
```

## 🧮 Sample Input

```
Available Intersections:
1: A
2: B
3: C
4: D
5: E

Enter Start Intersection ID: 1
Enter Destination Intersection ID: 4
```

---

## 📊 Output Features

* ✅ Displays the **fastest path** (e.g., A → B → D)
* ✅ Calculates **total travel time (in hours)**
* ✅ Shows **bar chart** with travel time per segment
* ✅ Displays **network graph** showing:

  * All intersections and roads
  * Travel times on each edge
  * Highlighted selected route in red

---

## 📈 Screenshots (Suggested)

You can include:

| Screenshot                                     | Description                          |
| ---------------------------------------------- | ------------------------------------ |
| ![Terminal Output](assets/terminal_output.png) | Console path and time output         |
| ![Bar Chart](assets/bar_chart.png)             | Travel time comparison per segment   |
| ![Network Graph](assets/node_graph.png)        | All intersections and selected route |
| ![Full Visualization](assets/full_view.png)    | Combined view of chart + graph       |

*(Store screenshots in an `assets/` folder for GitHub preview.)*

---

## 🧠 Concepts Applied

* **Graph Theory:** Representation of intersections and roads as weighted graphs
* **Shortest Path Algorithm:** Dijkstra’s algorithm to minimize travel time
* **Database Management:** Data storage and retrieval using PostgreSQL
* **Data Visualization:** Graphical route analysis using Matplotlib
* **Software Design:** Modular and maintainable Python project structure

---

## 🚀 Future Enhancements

* Add **real-world map coordinates (x, y)** for realistic layouts
* Integrate **live traffic API** for dynamic updates
* Build a **GUI interface** using Tkinter or Flask
* Export route report to **PDF format**
* Add **user roles** for admin and traffic operator management

---

## 🧾 Author

👨‍💻 **Jatin Tasoria**
📚 MCA Department
🏫 University of Computing
📅 Project Duration: October 2025

---

## 📜 License

This project is created for **academic and educational purposes**.
You are free to use, modify, and distribute it with proper credit to the author.

---

### ⭐ Show Some Support!

If you found this project helpful, don’t forget to **star ⭐ this repository** on GitHub!

---

```

---

Would you like me to generate this as a **ready-to-download `README.md` file** (so you can upload it directly to your GitHub repo)?  
I can create and give you the file link immediately.
```

