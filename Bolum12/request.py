import requests

# url="https://jsonplaceholder.typicode.com/posts"
# response=requests.get(url=url)

# print(type(response))
# print(response.status_code)
#print(response.text)

# posts=response.json()

# #print(type(posts))

# for i in posts[:2]:
#     print(i)

# query_p={
#     "userId":1,
#     "id":5
# }
# url="https://jsonplaceholder.typicode.com/posts"
# response=requests.get(url=url, params=query_p)

# result=response.json()

# print(result)

# url="https://jsonplaceholder.typicode.com/comments"

# post_id=input("Hangi kullanıcı Id bilgisi:")
# payload={"postId":post_id}

# response=requests.get(url=url, params=payload)

# result=response.json()

# print(result)

url="https://jsonplaceholder.typicode.com/posts"

new_post={
    "title": "BTK",
    "body": "istek oluşturuldu",
    "userId": 1
}

headers={"Content-type":"application/json; charSet:UTF-8"}

response=requests.post(url=url, json=new_post, headers=headers)

print(response.status_code)