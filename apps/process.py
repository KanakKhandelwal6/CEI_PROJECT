import json

def load_json(filepath):
    with open(filepath,"r",encoding="utf-8") as file:
        data = json.load(file)

        return data
    



def clean_commit_data(commits):

    cleaned_commits = []

    for commit in commits:

        cleaned_doc = {

            "id": commit["sha"],

            "type": "commit",

            "title": commit["commit"]["message"],

            "content": commit["commit"]["message"],

            "author": commit["commit"]["author"]["name"],

            "date": commit["commit"]["author"]["date"],

            "url": commit["html_url"]

        }

        cleaned_commits.append(cleaned_doc)

    return cleaned_commits


def clean_pull_request_data(pull_requests):

    cleaned_prs = []

    for pr in pull_requests:

        cleaned_doc = {

            "id": f'pr_{pr["number"]}',

            "type": "pull_request",

            "title": pr["title"],

            "content": pr["body"] if pr["body"] else "",

            "author": pr["user"]["login"],

            "date": pr["created_at"],

            "url": pr["html_url"]

        }

        cleaned_prs.append(cleaned_doc)

    return cleaned_prs


def clean_issue_data(issues):

    cleaned_issues = []

    for issue in issues:

        cleaned_doc = {

            "id": f'issue_{issue["number"]}',

            "type": "issue",

            "title": issue["title"],

            "content": issue["body"] if issue["body"] else "",

            "author": issue["user"]["login"],

            "date": issue["created_at"],

            "url": issue["html_url"]

        }

        cleaned_issues.append(cleaned_doc)

    return cleaned_issues


def merge_docu(commits,prs,issues):
    documents=[]
    documents.extend(commits)
    documents.extend(prs)
    documents.extend(issues)

    return documents