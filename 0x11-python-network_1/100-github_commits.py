#!/usr/bin/python3
"""
Module that takes repository name and owner name and list 10 commits
(from most recent to oldest
"""
import sys
import requests

if __name__ == '__main__':

    repo_name, repo_owner = sys.argv[1:3]
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/activity"

    r = requests.get(url)
    if r.status_code == 200:
        commits = []
        for activity in r.json():
            if activity.get("activity_type") == "push":
                sha = activity.get("after")
                author_url = activity.get("actor").get("url")
                commits.append(dict(sha=sha, author_url=author_url))
                if len(commits) == 10:
                    break

        for commit in commits:
            r = requests.get(commit.get("author_url"))
            if r.status_code == 200:
                print(f'{commit.get("sha")}: {r.json().get("name")}')
