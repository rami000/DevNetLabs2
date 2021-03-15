import requests

from env import config

s = requests.Session()
s.headers.update({
    'Authorization': f"Bearer {config['WEBEX_ACCESS_TOKEN']}"
})

WEBEX_BASE_URL = config['WEBEX_BASE_URL']

url = f"{WEBEX_BASE_URL}/v1/rooms"
payload = {
    'title': "Rami's room"
}
Id = None
 
resp = s.post(url, data=payload)

if resp.status_code == 200:
    Id = resp.json()['id']
    with open("env.py", "a") as fo:
        fo.write(f"\nconfig['TESTING_ROOM'] = \"{Id}\"") 

#Id = config['TESTING_ROOM']

url = f"{WEBEX_BASE_URL}/v1/memberships"
add_to_space = ['ramhadda@cisco.com']

for iduser in add_to_space:
    payload = {
        'Id': Id,
        'personEmail': iduser
        }
    resp = s.post(url, data=payload)

url = f"{WEBEX_BASE_URL}/v1/messages"
payload = {
    'Id': Id,
    'text': 'Test'.encode('latin-1')
    }
resp = s.post(url, data=payload)