import requests
import json
import os
from datetime import datetime


def write_file(data, filename):
    directory = os.path.dirname(os.path.abspath(__file__))

    file_path = os.path.join(directory, "static", filename)

    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)


def get_team(user):
    team_one = ["sof202", "lw371" "bethan-mallabar-rimmer"]
    team_two = ["ew267", "alicemfr", "marinafloresp", "gtw99"]

    if user in team_one:
        return 1
    elif user in team_two:
        return 2
    return 0


def get_open_issues(owner, repo, headers):
    url = f"https://api.github.com/repos/{owner}/{repo}/issues?state=open"

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        issues = response.json()

        return issues
    except requests.exceptions.RequestException as error:
        print("Error fetching pull request data:", error)


def get_pull_requests_since_date(owner, repo, since_date, headers):
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls?state=closed"

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        pull_requests = response.json()

        filtered_prs = [pr['number'] for pr in pull_requests if
                        pr['created_at'] > since_date
                        and pr['merged_at'] is not None]
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
            "label": "Lines of code changed",
            "data": lines_changed_data,
            "backgroundColor": [
                "rgba(255, 138, 0, 0.9)",
                "rgba(185, 255, 6, 0.9)"
            ],
            "borderColor": [
                "rgba(255, 138, 0, 1)",
                "rgba(185, 255, 6, 1)"
            ],
            "tension": 0.1
        }]
    }
    write_file(data, "lines_changed.json")


def create_pull_requests_closed_data(owner, repo, pull_requests, headers):
    users = [get_users(owner, repo, number, headers)[0]
             for number in pull_requests]
    team_involved = [get_team(user) for user in users]
    pull_requests_closed = [0, 0]
    for team in team_involved:
        if team == 1:
            pull_requests_closed[0] += 1
        if team == 2:
            pull_requests_closed[1] += 1
    data = {
        "labels": ["Team One", "Team Two"],
        "datasets": [{
            "label": "Pull requests closed",
            "data": pull_requests_closed,
            "backgroundColor": [
                "rgba(255, 138, 0, 0.9)",
                "rgba(185, 255, 6, 0.9)"
            ],
            "borderColor": [
                "rgba(255, 138, 0, 1)",
                "rgba(185, 255, 6, 1)"
            ],
            "tension": 0.1
        }]
    }
    write_file(data, "pull_requests_closed.json")


def create_collaborative_pr_data(owner, repo, pull_requests, headers):
    users_on_pr = [get_users(owner, repo, number, headers)
                   for number in pull_requests]
    number_of_users = [len(users) for users in users_on_pr]
    team_involved = [get_team(users[0]) for users in users_on_pr]
    collaborative_prs = [0, 0]
    for index in range(len(team_involved)):
        if team_involved[index] == 1 and number_of_users[index] > 1:
            collaborative_prs[0] += 1
        if team_involved[index] == 2 and number_of_users[index] > 1:
            collaborative_prs[1] += 1
    data = {
        "labels": ["Team One", "Team Two"],
        "datasets": [{
            "label": "Number of collaborative pull requests",
            "data": collaborative_prs,
            "backgroundColor": [
                "rgba(255, 138, 0, 0.9)",
                "rgba(185, 255, 6, 0.9)"
            ],
            "borderColor": [
                "rgba(255, 138, 0, 1)",
                "rgba(185, 255, 6, 1)"
            ],
            "tension": 0.1
        }]
    }
    write_file(data, "collaborative_pull_requests.json")


def create_issues_worked_on_data(owner, repo, headers):
    open_issues = get_open_issues(owner, repo, headers)
    issue_assignees = [issue['assignee']['login']
                       for issue in open_issues if issue['assignee']]
    team_involved = [get_team(assignee) for assignee in issue_assignees]
    issues_worked_on = [0, 0]
    for team in team_involved:
        if team == 1:
            issues_worked_on[0] += 1
        if team == 2:
            issues_worked_on[1] += 1
    data = {
        "labels": ["Team One", "Team Two"],
        "datasets": [{
            "label": "Number of issues currently worked on",
            "data": issues_worked_on,
            "backgroundColor": [
                "rgba(255, 138, 0, 0.9)",
                "rgba(185, 255, 6, 0.9)"
            ],
            "borderColor": [
                "rgba(255, 138, 0, 1)",
                "rgba(185, 255, 6, 1)"
            ],
            "tension": 0.1
        }]
    }
    write_file(data, "issues_worked_on.json")


def write_update_time(filename):
    def get_suffix(d):
        return {1: 'st', 2: 'nd', 3: 'rd'}.get(d % 20, 'th')

    def custom_strftime(format, time):
        time = time.strftime(format).replace(
            '{S}',
            str(time.day) + get_suffix(time.day)
        )
        return time

    formatted_string = custom_strftime(
        "Last updated on %A {S} %B at %H:%M", datetime.now())
    directory = os.path.dirname(os.path.abspath(__file__))

    file_path = os.path.join(directory, "static", filename)
    with open(file_path, 'w') as date_file:
        date_file.write(formatted_string)


if __name__ == "__main__":
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
    OWNER = 'ejh243'
    REPO = 'BrainFANS'
    START_TIME = "2024-11-25T09:00:00Z"
    OUTPUT_FILE = 'data/data.json'
    if GITHUB_TOKEN is None:
        print("GITHUB_TOKEN was not found, ensure it is set in env")
        exit(1)

    HEADERS = {
        'Authorization': f'Bearer {GITHUB_TOKEN}',
        'Accept': 'application/vnd.github+json',
        'X-GitHub-Api-Version': '2022-11-28'
    }
    pull_requests = get_pull_requests_since_date(
        OWNER,
        REPO,
        START_TIME,
        HEADERS
    )

    create_pull_requests_closed_data(OWNER, REPO, pull_requests, HEADERS)
    create_lines_changed_data(OWNER, REPO, pull_requests, HEADERS)
    create_collaborative_pr_data(OWNER, REPO, pull_requests, HEADERS)
    create_issues_worked_on_data(OWNER, REPO, HEADERS)
    write_update_time("update_time.txt")
