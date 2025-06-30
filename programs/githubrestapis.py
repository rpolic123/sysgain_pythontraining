##################################################
#################### display all repos ############
import requests
username = "octocat"
url = f"https://api.github.com/users/{username}/repos"

response = requests.get(url)
repos = response.json()
for repo in repos:
    print(f"{repo['name']} - {repo['html_url']}")


##################################################
#################### create new repo ###############
##################################################

import requests
import os

token = "your token" # Set your GitHub token in environment variable
headers = {
    "Authorization": f"token {token}",
    "Accept": "application/vnd.github.v3+json"
}

data = {
    "name": "my-new-repo",
    "description": "Created via REST API",
    "private": False
}

response = requests.post("https://api.github.com/user/repos", headers=headers, json=data)
print(response.json())

##################################################
##################### requests.delete() ################
##################################################
import requests
owner = "your-username"
repo = "repo-to-delete"
token = ""
url = f"https://api.github.com/repos/{owner}/{repo}"
headers = {
    "Authorization": f"token {token}",
    "Accept": "application/vnd.github.v3+json"
}

response = requests.delete(url, headers=headers)
print("Deleted!" if response.status_code == 204 else response.text)