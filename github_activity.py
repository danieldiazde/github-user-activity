import urllib.request
from urllib.error import URLError, HTTPError
import json
import argparse

parser = argparse.ArgumentParser(
    description='Input your Github username to fetch your resent activity')

parser.add_argument('username',help='Enter your Github username')

stock_url = 'https://api.github.com/users/<username>/events'

def format_data(data: list):
    print('Output:')


def main():
    args = parser.parse_args()
    username = args.username
    url = stock_url.replace('<username>', username)
    try:
        with urllib.request.urlopen(url) as response:
            response_string = response.read().decode('utf-8')
            response_data = json.dumps(json.loads(response_string))
            print(response_data)
            

    except (URLError, HTTPError) as e:
        print(f'Error{e} while fetching data')


if __name__ == '__main__':
    main()



