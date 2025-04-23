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

from city_function import formatted_city_country_name, formatted_city_population

def test_formatted_city_country_name():
    test_city_name = formatted_city_country_name('san francisco', 'united states')
    assert test_city_name == 'San Francisco, United States'


def test_fortmatted_city_population():
    test_population = formatted_city_population('dallas', 'united states', 5_000)
    test_population1 = formatted_city_population('dallas', 'united states', 5_000_000)

    assert test_population == "Dallas, United States - Population: 5000"
    assert test_population1 == "Dallas, United States - Population: 5000000"



