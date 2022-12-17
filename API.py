# API
# Aplication Programming Interface
# Base on command and query will search and return
# information
# API will be alink to connect to the web server
# API will provide info in JSON format (JavaScript Object Notation)
# A query is "latets" in the link below

# RapidAPI, to find available API
# requests
# API format
import requests
import json
import pandas as pd


# this function draws the shape of the data :) - DATAQUEST
# def jprint_format(response_obj):
#     '''
#     This function uses the json library and uses the method json.dumps()
#     to take a Python obj (the dictionary return after the response.json() line of code)
#     and prints the shape of the data.
#     :param response_obj:
#     :return:
#     '''
#     format_text = json.dumps(response_obj, sort_keys=True, indent=4)
#     print(format_text)

#
# url_API = "https://api.exchangerate-api.com/v4/latest/USD"
# # Often there will be multiple APIs available on a particular server.
# # Each of these APIs are commonly called **endpoints**.
#
# # the data from API comes as response
# response = requests.get(url_API)
# # The response is [200] which is succesful. If
# # the response is 404, is an error conectivity.
#
# # Entire dictironary
# rates_dict = response.json() # to see the data we received back from the API, it will return a dictionary
# # Who is JSON?
# # JSON (JavaScript Object Notation) is the language of APIs. JSON is a way to encode data structures
# # that ensures that they are easily readable by machines. JSON is the primary format in which data is
# # passed back and forth to APIs, and most API servers will send their responses in JSON format.
#
# print(rates_dict)
# jprint_format(rates_dict)
# # Only keys of the maiin dictionary
# key_rates = rates_dict.keys()
# print(key_rates)
# rates_only_dict = rates_dict["rates"] # to get the dictionary with the rates per currency
# print(rates_only_dict)
#
#
# # •••• 10 USD - 36.7 AED
#
# # •••• For euro into rupees :
# currency_a = input("Enter the currency abbreviation you wish to convert to: ").upper()
# currency_b = input("Enter the currency abbreviation you wish to convert from: ").upper()
# conversion_factor = rates_only_dict[currency_a]/rates_only_dict[currency_b]
# amount = float(input("Please enter the amount to be converted: "))
# converted_amount = amount * conversion_factor
# print(f"{amount:,.2f} {currency_b} = {converted_amount:,.2f} {currency_a}.")
# # Copy into a CSV file
# # Delete the source dictionary and only the first ten

print("\n")
print("ISS API")
# • • • • API from ISS - Dataquest Tutorial

parameters = {
    "lat": 40.71,
    "lon": -74
}

# STEPS:
# 1) store the endpoint(link) in a variable
url_iss_API = "http://api.open-notify.org/astros.json"

# 2) using the requests library, use the .get() method to ask for the endpoint. Usually named as response
response_iss = requests.get(url_iss_API)

# 3) print the status of the response by accessing the attribute .status_code. If 200 we are solid, if not cry.
print(response_iss.status_code)

# 4) take the response and make into a json format using the .json() method.
# Store it in a variable. This will return a dictionary. You could also print it.
response_dict_from_json = response_iss.json()
# print(response_dict_from_json)
# 5) Make your life easier by formatting the json file. Import the json library to the file and use the .dumps() method
# You can create a function for this purpose. Then call the function. :) - DATAQUEST
def jprint_format(response_obj):
    '''
    This function uses the json library and uses the method json.dumps() to take a Python obj
    (the dictionary returned after with response.json()) and prints the shape of the data.
    It takes 3 parameters: the dictionary object, sort_keys = True, indent = 4.
    :param response_obj
    :return:
    '''
    format_text = json.dumps(response_obj, sort_keys=True, indent=4)
    print(format_text)
jprint_format(response_dict_from_json)
# 6) This will vary by case, but a good portion of the data (stored as a dictionary) might be a list of dictionaries.
# To see it, you can access to it by dictionary["key_name"]. Store it in a variable and print it.
people_list = response_dict_from_json["people"]
print(people_list)
# 7) This might also will vary by case. Take the first element of the list at index [0] just to see how each dictionary
# inside the list looks.
people_list_sample = people_list[0]
print(people_list_sample)
# 8) This might vary by case, but in case you want to see the keys of each inner dictionary, use the .keys() method
print(people_list_sample.keys())
# 9) Here you could do things to each dictionary. In this case I am just printing the names with a loop.
# Here I am iterating through a list of dictionaries where people is a Dictionary inside the people_list List.
for people in people_list:
    astronaut_name = people["name"]
    print(astronaut_name)
# 10) Here I want to convert my data into dataframe. To do so I need the pandas library and use
# the pd.DataFrame.from_dict(name_of_variable_with_list_of_dicts, orient="columns") method.
astronauts_dataframe = pd.DataFrame.from_dict(people_list, orient="columns")
print(astronauts_dataframe)
# 11) Make the dataframe a CSV file by using the method .to_csv("desired_named_for_csv_file")
astronauts_csv = astronauts_dataframe.to_csv("Astronauts at ISS")