#making a gET request
import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts')

if response.status_code == 200:
    print("request was successful")

    posts = response.json()
    for post in posts:
        print(F"Title: {post['title']}")

else:
    print(F"request failed with status code:- {response.status_code}")


#making post request
data = {
    'Title': 'foo',
    'body' : 'bar',
    'userID' : 1
}
 
response = requests.post('https://jsonplaceholder.typicode.com/posts', json=data)

if response.status_code == 201:
    print("resource created successfully.")
    print("response data:", response.json())

else:
    print(F"request failed with status code:--", {response.status_code})



    