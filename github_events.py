import os
import requests
import json
from pprint import pprint

BASE_URL = "https://api.github.com"
# set token to env variable
github_token = os.environ.get("GITHUB_PAT")

# add header
headers = {
    "Authorization": f"token {github_token}",
    "accept": "application/vnd.github+json",
    "User-Agent": "github-activity/0.1",
}


def get_events(username):

    # from GitHub API doc
    events_url = f"{BASE_URL}/users/{username}/events/public"
    event_params = {"per_page": 10}

    # handle errors
    try:
        response = requests.get(url=events_url, headers=headers, params=event_params)
        response.raise_for_status()
        activities = response.json()
    except:
        print("failed to fetch Github Data")
        activities = []

    # Main Logic
    print(f"Recent Activity Feed for {username}: ")
    print("-" * 50)

    for activity in activities:
        event_type = activity.get("type")
        repo_name = activity["repo"]["name"]

        output_message = ""

        # Push event
        if event_type == "PushEvent":
            # The 'size' field in the payload often correctly reports the number of commits
            commit_count = activity["payload"].get("size", 0)
            if commit_count > 0:
                output_message = f"Pushed {commit_count} commit{'s' if commit_count > 1 else ''} to {repo_name}"
            else:
                # Handle the specific case where 'size' is 0 or missing (your previous error case)
                output_message = f"Pushed code to {repo_name} (details unavailable)"

        # Issue Events (Open a new issue)
        elif event_type == "IssuesEvent":
            action = activity["payload"].get("action")  # e.g., 'opened', 'closed'
            issue_title = activity["payload"]["issue"]["title"]
            output_message = f"{action.capitalize()} issue: '{issue_title}' in {repo_name}"

        # Pull Request Events
        elif event_type == "PullRequestEvent":
            action = activity["payload"].get("action")
            pr_title = activity["payload"]["pull_request"]["title"]
            output_message = (
                f"{action.capitalize()} Pull Request: '{pr_title}' in {repo_name}"
            )

        # Create Events (New repository/branch)
        elif event_type == "CreateEvent":
            ref_type = activity["payload"].get("ref_type")  # e.g., 'repository', 'branch'
            if ref_type == "repository":
                output_message = f"Created new repository: {repo_name}"
            elif ref_type == "branch":
                branch_name = activity["payload"].get("ref")
                output_message = f"Created branch {branch_name} in {repo_name}"

        # WatchEvent (Starring a repository)
        elif event_type == "WatchEvent":
            output_message = f"Starred repository {repo_name}"

        # Default/Unknown Events
        else:
            output_message = f"Performed a {event_type} in {repo_name}"

        # return message
        if output_message:
            return f"- {output_message}"     




# test
print(get_events("octocat"))

# # endpoint url
# url = f"{GITHUB_API_URL}/users/{USERNAME}"


# # Get response
# response = requests.get(url)
# try:
#     # conditionals
#     if response.status_code == 200:
#         user_data = response.json() # returns dictionary
#         user_json = json.dumps(user_data, indent=4)
#         with open("user_data.json", "w") as f:
#             f.write(user_json)
#             print("user data exported!")

#     else:
#         print(f"Error fetching data: Status Code: {response.status_code}")
# except requests.exceptions.RequestException as e:
#     print(f"Network error occured; {e}")
# except json.JSONDecodeError as e:
#     print(f"Error parsing JSON response: {e}")
# except IOError as e:
#     print(f"Error writing to file: {e}")
