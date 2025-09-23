import urllib.request
from urllib.error import URLError, HTTPError
import json
import sys

url = "https://jsonplaceholder.typicode.com/posts/1" #This is the specific endpoint for the data we want

print(f'Sending a GIT request to: {url}')

try:
    with urllib.request.urlopen(url) as response: #This sends the GET request
        data_bytes = response.read() #With read the response comes in as raw bytes
        data_string = data_bytes.decode('utf-8') #decode converts the bytes into utf-8 string
        print(data_string)
        post_data = json.loads(data_string) #Loads the json string into a python dictonary
except HTTPError or URLError as e:
    print('Error', e)

