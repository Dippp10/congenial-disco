import os
import requests

username = os.getenv("GITHUB_USER")
token = os.getenv("PERSONAL_GITHUB_TOKEN")

headers = {
    "Authorization": f"token {token}",
    "Accept": "application/vnd.github+json"
}

url = "https://api.github.com/users/github/following"

response = requests.get(url, headers=headers)

if response.status_code == 200:
    users = response.json()

    for user in users[:5]:
        follow_url = f"https://api.github.com/user/following/{user['login']}"
        r = requests.put(follow_url, headers=headers)
        print(f"Followed {user['login']} -> {r.status_code}")
else:
    print("Failed to fetch users")
