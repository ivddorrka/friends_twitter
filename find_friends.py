import requests
import pprint
import json
# from bog import register
# namee = register().split()[0]
# bearer_token = 'AAAAAAAAAAAAAAAAAAAAAH7tMwEAAAAASSQEjZvKGl4bLt8CWxRd3BEHBzg%3DEsUX6N1SBtdBuZMkbKqQiMBGjW3yL5dGVZTjNXl3XVP1l06Qsg'

def generate_1(bearer_token, namee):

    base_url = 'https://api.twitter.com/'

    search_url = '{}1.1/friends/list.json'.format(base_url) #endpoint
    search_headers = {
        'Authorization': 'Bearer {}'.format(bearer_token)
    }
    search_params = {
        'screen_name': f'@{namee}', 
        'count': 100
    }
    response = requests.get(search_url, headers=search_headers, params=search_params)

    json_response = response.json()
    return json_response

# pprint.pprint(json_response)

def write_to_file(bearer_token, namee):
    """
    To write to file in process
    """
    what_to_write = generate_1(bearer_token, namee)
    with open("friends_here.json", "w") as file_1:
        return json.dump(what_to_write, file_1, ensure_ascii=False, indent=4)
# print(write_to_file())