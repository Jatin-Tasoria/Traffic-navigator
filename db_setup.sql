CREATE TABLE intersections (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE roads (
    id SERIAL PRIMARY KEY,
    source_id INT REFERENCES intersections(id) ON DELETE CASCADE,
    destination_id INT REFERENCES intersections(id) ON DELETE CASCADE,
    distance FLOAT NOT NULL,
    traffic_factor FLOAT DEFAULT 1.0,
    speed_limit INT DEFAULT 60
);

-- Sample Data
INSERT INTO intersections (name) VALUES 
('A'), ('B'), ('C'), ('D'), ('E');

INSERT INTO roads (source_id, destination_id, distance, traffic_factor, speed_limit) VALUES
(1, 2, 5.0, 1.2, 60),
(2, 3, 3.0, 1.5, 50),
(1, 3, 10.0, 1.0, 80),
(3, 4, 2.0, 1.1, 40),
(4, 5, 4.0, 1.0, 70),
(2, 5, 12.0, 1.3, 60);
