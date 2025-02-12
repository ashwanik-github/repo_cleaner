import requests
import os
import json
from datetime import datetime, timedelta

# GitHub Credentials
github_username = "ashwanik-github" #replace your github username 
github_token = os.getenv("GITHUB_TOKEN")

# Constants
STALE_DAYS = 365
GITHUB_API_URL = "https://api.github.com"
SUMMARY_FILE = "repo_cleaner_summary.json"
MASTER_REPO_LIST = "/Users/ashwanik/Desktop/masterRepoList.txt" # replace with the absolute path of the masterRepoList.txt


def get_repos_from_file():
    with open(MASTER_REPO_LIST, "r") as file:
        return [line.strip().split("/")[-1] for line in file.readlines() if line.strip()]


def get_branches(repo):
    url = f"{GITHUB_API_URL}/repos/{github_username}/{repo}/branches"
    headers = {"Authorization": f"token {github_token}"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching branches for {repo}: {response.status_code} - {response.text}")
        return []



def get_stale_branches(repo):
    stale_branches = []
    cutoff_date = datetime.now() - timedelta(days=STALE_DAYS)
    headers = {"Authorization": f"token {github_token}"}

    for branch in get_branches(repo):
        commit_url = branch["commit"]["url"]
        commit_date = requests.get(commit_url, headers=headers).json()["commit"]["committer"]["date"]
        if datetime.strptime(commit_date, "%Y-%m-%dT%H:%M:%SZ") < cutoff_date:
            stale_branches.append(branch["name"])

    return stale_branches


def delete_branches(repo, branches):
    headers = {"Authorization": f"token {github_token}"}
    for branch in branches:
        url = f"{GITHUB_API_URL}/repos/{github_username}/{repo}/git/refs/heads/{branch}"
        requests.delete(url, headers=headers)
        print(f"Deleted branch: {branch} from {repo}")


def save_summary(summary):
    with open(SUMMARY_FILE, "w") as file:
        json.dump(summary, file, indent=4)


def main():
    summary = {}
    for repo in get_repos_from_file():
        branches = get_branches(repo)
        stale_branches = get_stale_branches(repo)
        total_branches = len(branches)
        summary[repo] = {"total_branches": total_branches, "deleted_branches": []}

        if stale_branches:
            print(f"Stale branches in {repo}: {stale_branches}")
            user_input = input("Delete all stale branches? (yes/no): ")
            if user_input == "yes":
                delete_branches(repo, stale_branches)
                summary[repo]["deleted_branches"] = stale_branches

        if total_branches == len(stale_branches):
            summary[repo]["recommend_delete_repo"] = True

    save_summary(summary)
    print("Summary saved to repo_cleaner_summary.json")


if __name__ == "__main__":
    main()
