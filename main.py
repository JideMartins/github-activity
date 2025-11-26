import requests

GITHUB_API_URL = "https://api.github.com/"
username = "JideMartins"

# State url here
url = f"{GITHUB_API_URL}/users/{username}"

# Get response
response = requests.get(url)

# conditionals
if response == 200:
    user_data = response.json()
    print(user_data)
else:
    print(f"Error fetching data: Status Code: {response.status_code}")
    print(response.json())


