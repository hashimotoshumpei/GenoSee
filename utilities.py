# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import json

def print_welcome_message():
    
    part1 = r"""      _____                       _____
     / ____|                     / ____|
    | |  __   ___  _ __    ___  | (___    ___   ___"""

    part2 = r"""    | | |_ | / _ \| '_ \  / _ \  \___ \  / _ \ / _ \
    | |__| ||  __/| | | || (_) | ____) ||  __/|  __/"""

    part3 = r"""     \_____| \___||_| |_| \___/ |_____/  \___| \___|"""
    red = "\033[91m"
    green = "\033[92m"
    blue = "\033[94m"
    reset = "\033[0m"
    print(red + part1 + '\n' + green + part2 + '\n' + blue + part3 + reset)
    print("---------------------------------------------------------------")
    print("Documentation: https://github.com/hashimotoshumpei/GenoSee\n")
    print("Type --help for help.\n")
    print("Version 1.0.0 (2024-5-8)")
    print("---------------------------------------------------------------")

def check_colnames(dataframe):
    print('Checking column names... : ', end='')
    is_colname_ok = False
    if sum(dataframe.columns.values[:3] == ['chr', 'marker_name', 'pos']) == 3:
        is_colname_ok = True
    return is_colname_ok

def round_up_second_digit(number):
    first_digit = int(str(number)[0])
    number_of_digits = len(str(number))
    rounded_number = (first_digit + 1) * 10 ** (number_of_digits - 1)
    return rounded_number

def get_value_from_database(json_file_path, key):
    """
    A function that reads the specified JSON file and returns the value for the specified species key
    
    Args:
    json_file_path (str): The path to the JSON file
    species (str): The key of the species to retrieve

    Returns:
    str: The value of the species (if exists)
    """
    # Read the JSON file
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    value = data.get(key, None)

    if value is None:
        print(f'{key} is not existed in the database.')
    
    # Return the value for the specified species
    return value

