#!/usr/bin/python3
import requests
import sys

# Get repository name and owner name from command line arguments
repo_name = sys.argv[1]
owner_name = sys.argv[2]

# Make API call to get commits
url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
response = requests.get(url)

# Print commit information
for commit in response.json():
  sha = commit['sha']
  author = commit['commit']['author']['name']
  print(f"{sha}: {author}")
