import json

#json.load()
# with open('products2.json', 'r', encoding='utf-8') as file:
#     data=json.load(file)

#     #print(data)

# print(data["product_name"])
# print(data["price"])
# print(data["category"])

#json.loads()
str='{"id": 1,"product_name": "Iphone 15","price": 90000,"category": "Telefon","is_published": "true"}'

results=json.loads(str)

#print(results)
print(results["product_name"])
print(results["price"])
print(results["category"])