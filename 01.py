# pip install requests
import requests

# mryazdan_response = requests.get("https://mryazdan.ir/")
# aparat_response = requests.get("https://www.aparat.com/")
# zoomit_response = requests.get("https://www.zoomit.ir/")

# Status Code:
# print(mryazdan_response.status_code)
# print(aparat_response.status_code)
# print(zoomit_response.status_code)

# with open('aparat-text.html', 'w') as f:
#     f.write(aparat_response.text)
#
# with open('aparat-content.html', 'wb') as f:
#     f.write(aparat_response.content)

# print('Reza' in mryazdan_response.text)

# Api Requests:
# user_response = requests.get('https://jsonplaceholder.typicode.com/users/1')
# print(user_response.status_code)
# print(user_response.text)
# print(user_response.content)

# Hard way :
# import json
# print(type(json.loads(user_response.content)))
# print(type(json.loads(user_response.text)))

# Easy:
# print(type(user_response.json()))
# print(user_response.json()['website'])

# users_response = requests.get('https://jsonplaceholder.typicode.com/users')
# print(users_response.text)
# print(type(users_response.json()))
# users = users_response.json()
# print(*[user["website"] for user in users], sep="\n")


# my_ip = requests.get("https://icanhazip.com").text
# print(my_ip)


# Browser Hijacking :
# cookies = {
#     '_pk_id.14.284a': 'c035b99a81948bd9.1721282110.',
#     '_pk_ses.14.284a': '1',
#     '_z_sess': '227cd002-d943-4a0e-9ff3-63905b84d046',
# }

# headers = {
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#     'accept-language': 'en-US,en;q=0.9,fa;q=0.8,fr;q=0.7,ar;q=0.6',
#     'cache-control': 'max-age=0',
#     'dnt': '1',
#     'if-none-match': '"14m4961oxxpjylw"',
#     'priority': 'u=0, i',
#     'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Linux"',
#     'sec-fetch-dest': 'document',
#     'sec-fetch-mode': 'navigate',
#     'sec-fetch-site': 'same-origin',
#     'sec-fetch-user': '?1',
#     'sec-gpc': '1',
#     'upgrade-insecure-requests': '1',
#     'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
# }

# response = requests.get('https://www.zoomit.ir/', cookies=cookies, headers=headers)

# Digikala SMS:
# sms_response = requests.post('https://api.digikala.com/v1/user/authenticate/', json={
#     "backUrl": "/",
#     "username": "09303024537",
#     "otp_call": False
# })

# print(sms_response.status_code)
# print(sms_response.text)

# ...
# session = requests.Session()


# ...
# counter = 1
# response_stream = requests.get("https://httpbin.org/stream/10", stream=True)
# for line in response_stream.iter_lines():
#     if line:
#         print(counter, end=", ")
#         counter += 1

