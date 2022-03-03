-- DROP DATABASE tube;
CREATE DATABASE tube;

CREATE TABLE stations (
  id VARCHAR(400) PRIMARY KEY, -- MySQL
  station_name VARCHAR(400) NOT NULL,
  longitude FLOAT,
  latitude FLOAT
);

CREATE TABLE tube_lines (
  id INT PRIMARY KEY AUTO_INCREMENT,
  line_name VARCHAR(400) NOT NULL
);

CREATE TABLE line_stations (
  line_id INT REFERENCES tube_lines,
  station_id VARCHAR(400) REFERENCES stations
);
