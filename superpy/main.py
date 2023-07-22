# Imports
import argparse
import pandas as pd
from export import export
from buy_product import buy_product
from sell_product import sell_product
from profit import profit
from statistics import statistics
from reset_files import reset_files
from advanced_time import advanced, setdate

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"

# Your code below this line.

def handle_args(args):
    if args.command == "buy":
        buy_product(
            id=id,
            product=args.product,
            quantity=args.quantity,
            price=args.price,
            buy_date=args.buy_date,
            exp_date=args.exp_date,
        )
    elif args.command == "sell":
        sell_product(
            product=args.product,
            price=args.price,
            quantity=args.quantity,
            sell_date=args.sell_date,
        )

    elif args.command == "export":
        export(selection=args.file, date=args.date)
    elif args.command == "profit":
        profit(args.date)
    elif args.command == "plot":
        statistics(args.file)
    elif args.command == "reset":
        reset_files(args.file)
    elif args.command == "advance_time":
        advanced(args.advance_time)
    elif args.command == "setdate":
        setdate(args.setdate)


def main():
    # Here all the command lines
    parser = argparse.ArgumentParser(prog="main.py", description="Keeps track of supermarket inventory.")
    subparsers = parser.add_subparsers(help="type of action", dest="command")
    subparsers.required = True

    # Buy Command
    buy_parser = subparsers.add_parser("buy", help="Buys a product")
    buy_parser.add_argument("--product", dest="product", type=str, help="product name", required=True)
    buy_parser.add_argument("--buy-price", type=float, dest="price", help="buy price per product", required=True)
    buy_parser.add_argument("--quantity", type=int, dest="quantity", help="quantity of product", default=1)
    buy_parser.add_argument("--buy-date", type=str, dest="buy_date", help="product buy date (format YYYY-MM-DD)", required=True)
    buy_parser.add_argument("--exp-date", type=str, dest="exp_date", help="product expiration date (format YYYY-MM-DD)", required=True)

    # Sell Command
    sell_parser = subparsers.add_parser("sell", help="Sells a product")
    sell_parser.add_argument("--product", type=str, dest="product", help="product name", required=True)
    sell_parser.add_argument("--sell-price", type=float, dest="price", help="sell price per product", required=True)
    sell_parser.add_argument("--quantity", type=int, dest="quantity", help="quantity of product", default=1)
    sell_parser.add_argument( "--sell-date", type=str, dest="sell_date", help="product sell date (format YYYY-MM-DD)", required=True)
    
    # Export Command
    export_parser = subparsers.add_parser("export", help="Export selection of data on a specific date",)
    export_parser.add_argument("--file", type=str, dest="file", help="Data to be exported to .csv file", choices=["expired", "bought", "sold"], required=True)
    export_parser.add_argument("--date", type=str, dest="date", help="Choose date of interest(format YYYY-MM-DD)", required=True)

    # Profit Command
    profit_parser = subparsers.add_parser("profit", help="Calculate profit on a specific date")
    profit_parser.add_argument("--date", type=str, dest="date", help="Choose date of interest(format YYYY-MM-DD)", required=True)

    # Plot Command
    plot_parser = subparsers.add_parser("plot", help="Plot bar graph of products in inventory, bought or sold list",)
    plot_parser.add_argument("--file", type=str, dest="file", help="File to be plotted", choices=["inventory", "bought", "sold"], required=True)

    # Reset files Command
    reset_parser = subparsers.add_parser("reset", help="Reset files or all files")
    reset_parser.add_argument("--file", type=str, dest="file", help="Files to be resetted", choices=["inventory", "bought", "sold", "all"], default="all")

    # Advanced Time Command
    advanced_parser = subparsers.add_parser("advance_time", help='Number of days to advance the date')
    advanced_parser.add_argument('--advance_time', type=int, help='Choose a number to leap')

    # Set Date Command
    setdate_parser = subparsers.add_parser("setdate", help='chance todays date')
    setdate_parser.add_argument('--setdate', type=str, help='Choose a date')

    args = parser.parse_args()
    return handle_args(args)

if __name__ == "__main__":
    main()