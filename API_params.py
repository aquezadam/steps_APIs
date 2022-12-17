# • • • • API from ISS with params - Dataquest Tutorial with params
import requests
import json
import pandas as pd

parameters = {
    "lat": 40.71,
    "lon": -74
}

# STEPS:
# 1) store the endpoint(link) in a variable
url_iss_nyc_API = "https://api.open-notify.org/iss-pass.json"

# 2) using the requests library, use the .get(variable_with_url, params = variable_with_params)
# method to ask for the endpoint. Usually named as response and params as parameters
response_iss_nyc = requests.get(url_iss_nyc_API, params=parameters)

# 3) print the status of the response by accessing the attribute .status_code. If 200 we are solid, if not cry.
print(response_iss_nyc.status_code)

# 4) take the response and make into a json format using the .json() method.
# Store it in a variable. This will return a dictionary. You could also print it.
response_iss_nyc_dict = response_iss_nyc.json()
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
jprint_format(response_iss_nyc_dict)
# 6) This will vary by case, but a good portion of the data (stored as a dictionary) might be a list of dictionaries.
# To see it, you can access to it by dictionary["key_name"]. Store it in a variable and print it.
response_iss_nyc_list = response_iss_nyc_dict["response"]
print(response_iss_nyc_list)
# 7) This might also will vary by case. Take the first element of the list at index [0] just to see how each dictionary
# inside the list looks.
response_iss_nyc_list_sample = response_iss_nyc_list[0]
print(response_iss_nyc_list_sample)
# 8) This might vary by case, but in case you want to see the keys of each inner dictionary, use the .keys() method
print(response_iss_nyc_list_sample.keys())
# 9) Here you could do things to each dictionary. In this case I am just printing the duration with a loop.
# Here, I am iterating through a list of dictionaries where duration is a Dictionary inside the
# response_iss_nyc_list List.
for response in response_iss_nyc_list:
    duration = response["duration"]
    print(duration)
# 10) Here I want to convert my data into dataframe. To do so I need the pandas library and use
# the pd.DataFrame.from_dict(name_of_variable_with_list_of_dicts, orient="columns") method.
duration_dataframe = pd.DataFrame.from_dict(response_iss_nyc_list, orient="columns")
print(duration_dataframe)
# 11) Make the dataframe a CSV file by using the method .to_csv("desired_named_for_csv_file")
duration_csv = duration_dataframe.to_csv("Duration ISS over NYC")