import urllib.request
from urllib.error import URLError, HTTPError
import json
import argparse

parser = argparse.ArgumentParser(
    description='Input your Github username to fetch your resent activity')

parser.add_argument('username',help='Enter your Github username')

API_url = 'https://api.github.com/users/<username>/events'

def format_data(data: dict): #Each dictionary is an event of actions on Github with "id, "type", "actor", "repo", "created_at", "payload"
    event_id = data.get('id')
    event_type = data.get('type')
    event_actor = data.get('actor', {}).get('login')
    event_repo = data.get('repo', {}).get('name')
    event_created_at = data.get('created_at')
    event_payload = data.get('ref_type') 
    print(f'Event {event_type} on repository {event_repo} at time {event_created_at}')


def main():
    args = parser.parse_args()
    username = args.username
    url = API_url.replace('<username>', username)
    try:
        with urllib.request.urlopen(url) as response:
            response_string = response.read().decode('utf-8')
            data = json.loads(response_string)
            for event in data:
                print('-', format_data(event))
            
    except (URLError, HTTPError) as e:
        print(f'Error {e} while fetching data')

if __name__ == '__main__':
    main()