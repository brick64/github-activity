import argparse
import requests

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("username")
    args = parser.parse_args()
    username:str = args.username
    response = requests.get(f"https://api.github.com/users/{username}/events")
    if response.status_code!=200:
        print('Something went wrong! Did you type in the correct username?')
        return -1
    data = response.json()
    for event in data:
        type = event["type"]
        match type:
            case "CommitCommentEvent":
                pass
            case "CreateEvent":
                pass
            case "DeleteEvent":
                pass
            case "ForkEvent":
                repo_name = event['repo']['name']
                print(f'-Forked {repo_name}')
            case "GollumEvent":
                pass
            case "IssueCommentEvent":
                pass
            case "IssuesEvent":
                payload = event['payload']
                action = payload['action']
                repo_name = event['repo']['name']
                print(f'-{action.title()} an issue in {repo_name}')
            case "MemberEvent":
                pass
            case "PublicEvent":
                pass
            case "PullRequestEvent":
                pass
            case "PullRequestReviewEvent":
                pass
            case "PullRequestReviewCommentEvent":
                pass
            case "PullRequestReviewThreadEvent":
                pass
            case "PushEvent":
                repo_name = event['repo']['name']
                payload = event['payload']
                number_commits = len(payload['commits'])
                print(f'-Pushed {number_commits} commit{'' if number_commits==1 else 's'} to {repo_name}')
            case "ReleaseEvent":
                pass
            case "SponsorshipEvent":
                pass
            case "WatchEvent":
                pass


if __name__ == "__main__":
    main()
