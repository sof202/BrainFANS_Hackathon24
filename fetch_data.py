import requests
import json
import os


def write_file(data, filename):
    directory = os.path.dirname(os.path.abspath(__file__))

    file_path = os.path.join(directory, "static", filename)

    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)


def get_pull_requests_since_date(owner, repo, since_date, headers, state):
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls?state={state}"

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        pull_requests = response.json()

        filtered_prs = [pr['number'] for pr in pull_requests if
                        pr['created_at'] > since_date]
        return filtered_prs
    except requests.exceptions.RequestException as error:
        print("Error fetching pull request data:", error)


def get_lines_changed(owner, repo, pull_number, headers):
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pull_number}/files"

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        files = response.json()

        total_lines_changed = sum(file['changes'] for file in files)
        return total_lines_changed
    except requests.exceptions.RequestException as error:
        print("Error fetching pull request data:", error)


def get_users(owner, repo, pull_number, headers):
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pull_number}/commits"

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        commits = response.json()

        users = {commit['commit']['author']['name']
                 for commit in commits}
        return list(users)
    except requests.exceptions.RequestException as error:
        print("Error fetching pull request data:", error)


def get_commits(owner, repo, pull_number, headers):
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pull_number}/commits"

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        commits = response.json()

        return len(commits)
    except requests.exceptions.RequestException as error:
        print("Error fetching pull request data:", error)


def get_team(user):
    team_one = ["sof202", "marinafloresp", "siyiSEA"]
    team_two = ["ew267", "alicemfr", "rhaigh5"]

    if user in team_one:
        return 1
    elif user in team_two:
        return 2
    return 0


def create_lines_changed_data(owner, repo, pull_requests, headers):
    lines_changed = [get_lines_changed(
        owner, repo, number, headers) for number in pull_requests]
    users = [get_users(owner, repo, number, headers)[0]
             for number in pull_requests]
    team_involved = [get_team(user) for user in users]

    lines_changed_data = [0, 0]
    for index in range(len(team_involved)):
        if team_involved[index] == 1:
            lines_changed_data[0] += lines_changed[index]
        if team_involved[index] == 2:
            lines_changed_data[1] += lines_changed[index]
    data = {
        "labels": ["Team One", "Team Two"],
        "datasets": [{
            "data": lines_changed_data,
            "backgroundColor": [
                "rgba(255, 99, 132, 0.2)",
                "rgba(255, 159, 64, 0.2)"
            ],
            "borderColor": "rgb(75, 192, 192)",
            "tension": 0.1
        }]
    }
    write_file(data, "lines_changed.json")


def create_pull_requests_closed_data(owner, repo, start_time, headers):
    closed_pull_requests = get_pull_requests_since_date(owner,
                                                        repo,
                                                        start_time,
                                                        headers,
                                                        "closed")
    users = [get_users(owner, repo, number, headers)[0]
             for number in closed_pull_requests]
    team_involved = [get_team(user) for user in users]
    pull_requests_closed = [0, 0]
    for index in range(len(team_involved)):
        if team_involved[index] == 1:
            pull_requests_closed[0] += 1
        if team_involved[index] == 2:
            pull_requests_closed[1] += 1
    data = {
        "labels": ["Team One", "Team Two"],
        "datasets": [{
            "data": pull_requests_closed,
            "backgroundColor": [
                "rgba(255, 99, 132, 0.2)",
                "rgba(255, 159, 64, 0.2)"
            ],
            "borderColor": "rgb(75, 192, 192)",
            "tension": 0.1
        }]
    }
    write_file(data, "pull_requests_closed.json")


if __name__ == "__main__":
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
    OWNER = 'ejh243'
    REPO = 'BrainFANS'
    START_TIME = "2023-07-08T13:41:09Z"
    OUTPUT_FILE = 'data/data.json'
    if GITHUB_TOKEN is None:
        print("GITHUB_TOKEN was not found, ensure it is set in env")

    HEADERS = {
        'Authorization': f'Bearer {GITHUB_TOKEN}',
        'Accept': 'application/vnd.github+json',
        'X-GitHub-Api-Version': '2022-11-28'
    }
    pull_requests = get_pull_requests_since_date(
        OWNER,
        REPO,
        START_TIME,
        HEADERS,
        "all"
    )

    create_pull_requests_closed_data(OWNER, REPO, START_TIME, HEADERS)
    create_lines_changed_data(OWNER, REPO, pull_requests, HEADERS)
