# Imports
import pandas as pd
import os
from datetime import datetime
from record_sell import record_sell
from check_date import dated

pd.options.mode.chained_assignment = None  # default='warn'

def sell_product(product, price, sell_date, quantity):
    # check if sell_date is of the YYYY-MM-DD format
    if dated(sell_date) == False:
        (print(+"This is the incorrect date string format. It should be YYYY-MM-DD"))
        return

    # check if inventory already exists
    if os.path.isfile("df_inventory.csv") == False:
        print("There is nothing in the current inventory")

    # check if item with Product_name is present in inventory and if quantity is enough
    elif os.path.isfile("df_inventory.csv"):
        df_inventory = pd.read_csv("df_inventory.csv")
        df_inventory["Quantity"] = pd.to_numeric(df_inventory["Quantity"])
        product_exists = ((df_inventory["Product_name"] == product)& (df_inventory["Quantity"] >= quantity)).any()

    # checks if product is not expired
        list_id = []
        for index, row in df_inventory.iterrows():
            datestring = row["Expiration_date"]
            if pd.to_datetime(datestring, format="%Y-%m-%d") >= pd.to_datetime(sell_date, format="%Y-%m-%d"):
                product_exists = True
                list_id.append(row["Product_ID"])

        if product_exists == False:
            print(f"There is not enough {product} to sell from the inventory")
        if len(list_id) == 0:
            print(f"All {product} are expired")
            pass

        # if product is already present in inventory, get the product_index
        elif product_exists:
            product_index = df_inventory[((df_inventory["Product_name"] == product) & (df_inventory["Quantity"] >= quantity) & (df_inventory["Product_ID"].isin(list_id)))].index.tolist()

            # Start selling products that were added first
            product_index = product_index[0]

            # If quantity and Sell_date are OK, product is sold and quantity is updated
            id = df_inventory["Product_ID"].iloc[product_index]
            record_sell(id, product, price, sell_date, quantity)
            new_quantity = int(df_inventory["Quantity"].iloc[product_index]) - int(quantity)

            # if all products are sold, row will be deleted
            if new_quantity == 0:
                df_inventory = df_inventory.drop(df_inventory.index[product_index])
                print("Updated inventory:")
                print(df_inventory.to_string(index=False))
                return df_inventory.to_csv("df_inventory.csv", index=False)
            else:
                # update quantity
                df_inventory["Quantity"].iloc[product_index] = new_quantity
                print("Updated inventory:")
                print(df_inventory.to_string(index=False))
                return df_inventory.to_csv("df_inventory.csv", index=False)