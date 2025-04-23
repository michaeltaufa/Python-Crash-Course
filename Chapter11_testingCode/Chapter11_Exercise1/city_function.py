"""
Program Name: Program Exercise 11-1 City Country
Description: 
    Write a function that accepts (2) parameters (city, country)
    Function should return a single string
    Store function in a module called 'city_functions.py'
    Store files in a new folder to seperate pytest
    
    Create file test_cities.py to test function
    Run test to ensure function pass test 
Name: Michael Taufa
Date: 2025-04-21
"""

def formatted_city_country_name(city, country):

    formatted_city_country_name = f"{city}, {country}"
    return formatted_city_country_name.title()

def formatted_city_population(city, country, population = ''):
    if population:
        formatted_city_population = f"{city}, {country} - Population: {population}"
    else:
        formatted_city_population = f"{city, {country}}"

    return formatted_city_population.title()
