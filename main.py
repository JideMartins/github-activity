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
try:
    # conditionals
    if response.status_code == 200:
        user_data = response.json() # returns dictionary
        user_json = json.dumps(user_data, indent=4)
        with open("user_data.json", "w") as f:
            f.write(user_json)
            print("user data exported!")
        
    else:
        print(f"Error fetching data: Status Code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Network error occured; {e}")
except json.JSONDecodeError as e:
    print(f"Error parsing JSON response: {e}")
except IOError as e:
    print(f"Error writing to file: {e}")



