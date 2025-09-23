import urllib.request
from urllib.error import URLError, HTTPError
import json
import argparse
from json import JSONDecodeError

parser = argparse.ArgumentParser(
    description='Input your Github username to fetch your recent activity')

parser.add_argument('username',help='Enter your Github username')

def format_data(data: dict) -> str:
    event_id = data.get('id')
    event_type = data.get('type')
    event_actor = data.get('actor', {}).get('login')
    event_repo = data.get('repo', {}).get('name')
    event_created_at = data.get('created_at')
    event_payload = data.get('payload', {}).get('ref_type') 

    if event_payload:
        return f'<{event_id}> {event_type} by {event_actor} on {event_payload} on repository {event_repo} at time {event_created_at}'
    elif event_payload == None or event_payload == '':
        return f'<{event_id}> {event_type} by {event_actor} on {event_repo} at time {event_created_at}'

def main():
    args = parser.parse_args()
    username = args.username
    API_url = 'https://api.github.com/users/{}/events'.format(username)
    try:
        with urllib.request.urlopen(API_url) as response:
            response_string = response.read().decode('utf-8')
            data = json.loads(response_string)
            for event in data:
                print('-', format_data(event))
            
    except (URLError, HTTPError) as e:
        print(f'Error {e} while fetching data')
    
    except JSONDecodeError as e:
        print(f'Error {e}, failed to decode jason')

if __name__ == '__main__':
    main()