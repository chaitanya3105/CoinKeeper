import requests
import csv

GITHUB_USER = "chaitanya3105"
REPO_NAME = "CoinKeeper"
# ACCESS_TOKEN = "your_github_pat"  # Use for private repos

url = f"https://api.github.com/repos/{GITHUB_USER}/{REPO_NAME}"

headers = {
    "Authorization": f"token {ACCESS_TOKEN}" if ACCESS_TOKEN else None,
    "Accept": "application/vnd.github.v3+json",
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    repo_data = response.json()
    with open("repo_data.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Repo Name", "Stars", "Forks", "Open Issues"])
        writer.writerow([repo_data["name"], repo_data["stargazers_count"], repo_data["forks_count"], repo_data["open_issues_count"]])
    
    print("Data saved to repo_data.csv")
else:
    print("Failed to fetch repository data")
