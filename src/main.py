import argparse
from PriceHistory import PriceHistory
from WineRetriever import WineRetriever


def price_history(wine_id):
    # Specify the path to your SQLite database file
    db_file = "wine_db.db"

    # Create an instance of the PriceHistory class
    price_history = PriceHistory(db_file)

    # Call the get_price_history method to retrieve price history for the specified wine
    history = price_history.get_price_history(wine_id)

    if history:
        print(f"Price history for Wine ID {wine_id}:")
        for date, price in history:
            print(f"Date: {date}, Price: {price}")
    else:
        print(f"No price history found for Wine ID {wine_id}.")

    # Close the database connection
    price_history.close()


def retrieve_wines(min_price, max_price):
    # Specify the path to your SQLite database file
    db_file = "wine_db.db"

    # Create an instance of the WineRetriever class
    wine_retriever = WineRetriever(db_file)

    # Call the retrieve_wines_by_score_mean method to retrieve wines in the specified price range
    wine_results = wine_retriever.retrieve_wines_by_score_mean(min_price, max_price)

    if wine_results:
        print("Wines sorted by the mean of score averages:")
        for wine in wine_results:
            print(f"Wine ID: {wine[0]}, Name: {wine[1]}, Price: {wine[2]}, Avg. Score: {wine[3]}")
    else:
        print("No wines found within the specified price range.")

    # Close the database connection
    price_history.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Retrieve price history for a specific wine.")
    parser.add_argument("--action_id", type=int, help="(1) Retrieve price history; (2) Retrieve sold wines")
    parser.add_argument("--wine_id", type=int, help="The ID of the wine for which to retrieve price history.")
    parser.add_argument("--min_price", type=float, help="Minimum price for wine selection.")
    parser.add_argument("--max_price", type=float, help="Maximum price for wine selection.")

    args = parser.parse_args()

    if args.action_id == 1:
        if args.wine_id is not None:
            price_history(args.wine_id)
        else:
            print("Please provide both --min_price and --max_price arguments.")
    elif args.action_id == 2:
        if args.min_price is not None and args.max_price is not None:
            retrieve_wines(args.min_price, args.max_price)
        else:
            print("Please provide a valid --wine_id argument.")
    else:
        print("Please provide a valid action --action_id argument.")