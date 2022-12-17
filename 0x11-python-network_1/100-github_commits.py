import requests
import sys

def main(repo_name, owner_name):
  # Make a request to the GitHub API to get the repository information
  url = f'https://api.github.com/repos/{owner_name}/{repo_name}'
  response = requests.get(url)

  # Check if the rate limit was exceeded
  if response.status_code == 403:
    print('Rate limit exceeded. Try again later.')
    return

  # Print the repository name and description
  repo_info = response.json()
  print(f'Repository name: {repo_info["name"]}')
  print(f'Description: {repo_info["description"]}')

if name == 'main':
  # Get the repository name and owner name from the command line arguments
  repo_name = sys.argv[1]
  owner_name = sys.argv[2]

  main(repo_name, owner_name)
