CREATE TABLE IF NOT EXISTS Ships
(
    ship TEXT PRIMARY KEY,
    weapon TEXT,
    hull TEXT,
    engine TEXT,
    FOREIGN KEY (weapon) REFERENCES Weapons(weapon)
    FOREIGN KEY (hull) REFERENCES Hulls(hull)
    FOREIGN KEY (engine) REFERENCES Engines(engine)
);

CREATE TABLE IF NOT EXISTS Weapons
(
    weapon TEXT PRIMARY KEY,
    reload_speed INT,
    rotation_speed INT,
    diameter INT,
    power_volley INT,
    count INT
);

CREATE TABLE IF NOT EXISTS Hulls
(
    hull TEXT PRIMARY KEY,
    armor INT,
    type INT,
    capacity INT
);

CREATE TABLE IF NOT EXISTS Engines
(
    engine TEXT PRIMARY KEY,
    power INT,
    type INT
);