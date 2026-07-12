import requests
from confi import GITHUB_TOKEN,GOOGLE_API_KEY,BASE_URL







def connect_git_api():
    headers = {
        "Authorization": f"Bearer{GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }


    session = requests.Session()
    session.headers.update(headers)

    return session


'''def clone_fastapi_repo():
   pass





def fetch_commit_history():

    session = connect_git_api()

    url = f"{BASE_URL}/commits"
    response = session.get(url)
    return response.json()






def fetch_pull_req():
    session = connect_git_api()
    url = f"{BASE_URL}/pulls?state=all"
    response = session.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print("Error:",response.status_code)

        return []





def fetch_issue_threads():
    session = connect_git_api()
    url = f"{BASE_URL}/issues?state=all"
    response = session.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(response.status_code)
        return[]'''


# add pagination 


def fetch_all_pages(endpoint):
    session = connect_git_api()

    page = 1
    all_data = []

    while True:

        url = f"{BASE_URL}/{endpoint}?state=all&per_page=100&page={page}"

        response = session.get(url)

        if response.status_code != 200:
            print("Error:", response.status_code)
            break

        data = response.json()

        if not data:
            break

        all_data.extend(data)

        print(f"Downloaded Page {page} ({len(data)} records)")

        page += 1

    return all_data


def fetch_commit_history():
    return fetch_all_pages("commits")


def fetch_pull_req():
    return fetch_all_pages("pulls")


def fetch_issue_threads():
    return fetch_all_pages("issues")




