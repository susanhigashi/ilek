-- Sample data for wine_properties
INSERT INTO wine_properties (name, type, flavor, description, country, region, producer, year, score_avg)
VALUES
    ('Wine 1', 'Red', 'Fruity', 'A fruity red wine with a rich flavor.', 'France', 'Bordeaux', 'Winery A', 2015, 4.2),
    ('Wine 2', 'White', 'Citrus', 'A crisp white wine with citrus notes.', 'Italy', 'Tuscany', 'Winery B', 2018, 4.5),
    ('Wine 3', 'Red', 'Spicy', 'A spicy red wine with a bold taste.', 'Spain', 'Rioja', 'Winery C', 2014, 4.0),
    ('Wine 4', 'Rosé', 'Fruity', 'A refreshing rosé with a fruity profile.', 'USA', 'California', 'Winery D', 2017, 4.3),
    ('Wine 5', 'White', 'Buttery', 'A smooth and buttery white wine.', 'New Zealand', 'Marlborough', 'Winery E', 2019, 4.7),
    ('Wine 6', 'Red', 'Oak', 'A red wine with oak-aged character.', 'Argentina', 'Mendoza', 'Winery F', 2016, 4.1),
    ('Wine 7', 'White', 'Crisp', 'A crisp and refreshing white wine.', 'Australia', 'Barossa Valley', 'Winery G', 2020, 4.6),
    ('Wine 8', 'Red', 'Cherry', 'A red wine with hints of cherry and spice.', 'Italy', 'Piedmont', 'Winery H', 2017, 4.4),
    ('Wine 9', 'Rosé', 'Strawberry', 'A rosé wine with notes of ripe strawberries.', 'France', 'Provence', 'Winery I', 2021, 4.8),
    ('Wine 10', 'White', 'Tropical', 'A white wine with tropical fruit flavors.', 'Chile', 'Maipo Valley', 'Winery J', 2018, 4.2);

-- Sample data for sales
INSERT INTO sales (sale_date, total_price)
VALUES
    ('2023-10-01', 120.50),
    ('2023-10-02', 85.75),
    ('2023-10-03', 210.25),
    ('2023-10-04', 65.90),
    ('2023-10-05', 150.00),
    ('2023-10-06', 75.20),
    ('2023-10-07', 320.75),
    ('2023-10-08', 110.40),
    ('2023-10-09', 95.60),
    ('2023-10-10', 200.00);

-- Sample data for sale_details
INSERT INTO sale_details (sale_id, wine_id, price)
VALUES
    (1, 1, 25.00),
    (1, 1, 30.00),
    (2, 1, 20.50),
    (2, 4, 18.75),
    (3, 5, 45.90),
    (3, 6, 38.25),
    (4, 7, 22.50),
    (4, 8, 28.00),
    (5, 9, 12.75),
    (5, 10, 16.80);

-- Sample data for users
INSERT INTO users (username, email, password, full_name)
VALUES
    ('user1', 'user1@example.com', 'password1', 'User One'),
    ('user2', 'user2@example.com', 'password2', 'User Two'),
    ('user3', 'user3@example.com', 'password3', 'User Three'),
    ('user4', 'user4@example.com', 'password4', 'User Four'),
    ('user5', 'user5@example.com', 'password5', 'User Five'),
    ('user6', 'user6@example.com', 'password6', 'User Six'),
    ('user7', 'user7@example.com', 'password7', 'User Seven'),
    ('user8', 'user8@example.com', 'password8', 'User Eight'),
    ('user9', 'user9@example.com', 'password9', 'User Nine'),
    ('user10', 'user10@example.com', 'password10', 'User Ten');

-- Sample data for wine_scores
INSERT INTO wine_scores (wine_id, user_id, score, comment)
VALUES
    (1, 1, 4.5, 'Great wine!'),
    (1, 2, 4.8, 'Excellent choice.'),
    (2, 3, 3.7, 'Good white wine.'),
    (2, 4, 3.2, 'Not bad, but not my favorite.'),
    (3, 5, 4.1, 'Spicy and bold.'),
    (3, 6, 4.2, 'Enjoyed it with dinner.'),
    (4, 7, 4.6, 'Refreshing rosé!'),
    (4, 8, 4.3, 'Nice summer wine.'),
    (5, 9, 3.5, 'Decent, but could be better.'),
    (5, 10, 4.0, 'Tropical flavors stand out.');

-- Sample data for user_search_criteria
INSERT INTO user_search_criteria (user_id, name, wine_type, flavor, country, region, producer, max_price, min_year, max_year, min_score, max_score)
VALUES
    (1, 'My Criteria 1', 'Red', NULL, 'France', 'Bordeaux', NULL, 50.0, 2010, 2015, NULL, 4.0),
    (1, 'My Criteria 2', NULL, 'Fruity', NULL, NULL, 'Winery A', NULL, NULL, NULL, 3.5, NULL),
    (2, 'User 2 Criteria', 'White', 'Citrus', 'Italy', NULL, NULL, NULL, 2015, NULL, 4.5, 4.8),
    (2, NULL, 'Rosé', NULL, 'USA', NULL, 'Winery B', 35.0, NULL, 2019, NULL, NULL),
    (3, 'Criteria 3', 'Red', 'Spicy', 'Spain', 'Rioja', 'Winery C', 40.0, 2012, 2017, 4.0, 4.3),
    (4, 'Criteria 4', 'Rosé', 'Fruity', NULL, 'California', NULL, 60.0, NULL, NULL, 4.2, NULL);
