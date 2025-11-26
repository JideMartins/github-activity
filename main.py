import os
import requests
import json

GITHUB_API_URL = "https://api.github.com/"
username = "JideMartins"

def convert_json(json_string):
    return json.loads(json_string)

def convert_dictionary(data_dict):
    return json.dumps(data_dict, indent=4)

def load_json(json_file):

    if not os.path.exists(json_file):
        # create file if it doesn't exists
        with open(json_file, "w"):
            pass
    with open(json_file) as f:
        json_string = f.read().strip()

    if not json_string:
        return "{}"
    
    return json_string

def dump_json(json_file, data_json):
    with open(json_file, "w") as f:
        f.write(data_json)


# State url here
url = f"{GITHUB_API_URL}/users/{username}"

# Get response
response = requests.get(url)

# conditionals
if response == 200:
    user_data = response.json()
    # print(user_data)
    
else:
    print(f"Error fetching data: Status Code: {response.status_code}")
    print(response.json())


