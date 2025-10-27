"""Inventory system management
This module provides basic inventory system management functions
1.add_item
2.remove item
3.get_qty
4.load_data
5.save_data
6.print_data
7.check_low items"""
import json
import logging
import ast
from datetime import datetime

logging.basicConfig(
    filename='inventory.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def add_item(stock_data, item="default", qty=0, logs=None):
    '''This function helps to add a particular item with
    specified quantity from an inventory'''
    if logs is None:
        logs = []
    if not item:
        return stock_data
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")
    logging.info(f"Added {qty} of {item}")
    return stock_data


def remove_item(stock_data, item, qty):
    '''This function helps to remove a particular item
    with specified quantity from an inventory'''
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        logging.warning(f"Item '{item}' not found in stock data.")
    except TypeError:
        logging.error("Invalid quantity type. Please enter a number.")
    return stock_data


def get_qty(stock_data, item):
    '''Helps to get quantity of a particular item in inventory'''
    return stock_data.get(item, 0)


def load_data(file="inventory.json"):
    '''Loads the json file with all inventory records'''
    try:
        with open(file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        logging.warning("File not found. Starting with empty inventory.")
        return {}
    except json.JSONDecodeError:
        logging.error("Error reading JSON file.")
        return {}


def save_data(stock_data, file="inventory.json"):
    '''saves the updated data into the json file'''
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(stock_data, f, indent=4)


def print_data(stock_data):
    '''Helps to generate report of the inventory'''
    print("Items Report")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(stock_data, threshold=5):
    '''returns item with low quantity'''
    return [item for item, qty in stock_data.items() if qty < threshold]


def main():
    '''Entry point of the inventory system program'''
    stock_data = load_data()

    stock_data = add_item(stock_data, "apple", 10)
    stock_data = add_item(stock_data, "banana", 5)
    stock_data = remove_item(stock_data, "apple", 2)
    stock_data = remove_item(stock_data, "orange", 1)

    print("Apple stock:", get_qty(stock_data, "apple"))
    print("Low items:", check_low_items(stock_data))

    save_data(stock_data)
    print_data(stock_data)

    safe_data = ast.literal_eval("{'key': 'value'}")
    print("Safe data:", safe_data)


main()
