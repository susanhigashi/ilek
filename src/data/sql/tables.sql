--- Wine Properties 
CREATE TABLE wine_properties (
    wine_id INTEGER PRIMARY KEY,
    name TEXT,
    type TEXT,
    flavor TEXT,
    description TEXT,
    country TEXT,
    region TEXT,
    producer TEXT,
    year INTEGER,
    score_avg REAL 
);

--- Wine sales
CREATE TABLE sales (
    sale_id INTEGER PRIMARY KEY,
    sale_date DATE,
    total_price REAL
);

CREATE TABLE sale_details (
    detail_id INTEGER PRIMARY KEY,
    sale_id INTEGER,
    wine_id INTEGER,
    price REAL,
    FOREIGN KEY (sale_id) REFERENCES sales(sale_id),
    FOREIGN KEY (wine_id) REFERENCES wine_properties(wine_id)
);

--- Wine evaluation 
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    full_name TEXT
);

CREATE TABLE wine_scores (
    score_id INTEGER PRIMARY KEY,
    wine_id INTEGER,
    user_id INTEGER,
    score INTEGER,
    comment TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (wine_id) REFERENCES wine_properties(wine_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

--- Alerting
CREATE TABLE user_search_criteria (
    criteria_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    name TEXT,
    wine_type TEXT,
    flavor TEXT,
    country TEXT,
    region TEXT,
    producer TEXT,
    max_price REAL,
    min_year INTEGER,
    max_year INTEGER,
    min_score REAL,
    max_score REAL,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
