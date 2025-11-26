import os
import requests
import json
from pprint import pprint



GITHUB_API_URL = "https://api.github.com"
USERNAME = "JideMartins"

# endpoint url
url = f"{GITHUB_API_URL}/users/{USERNAME}"


# Get response
response = requests.get(url)

# conditionals
if response.status_code == 200:
    user_data = response.json() # returns dictionary
    user_json = json.dumps(user_data, indent=4)
    with open("user_data.json", "w") as f:
        f.write(user_json)
    # print(user_json)
    # print(type(user_data))
    # pprint(user_data)
    
else:
    print(f"Error fetching data: Status Code: {response.status_code}")


