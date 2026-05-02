import json

#json.dumps()
# person_dict={"name": "Ali", "languages": ["C#", "Python"]}

# result=json.dumps(person_dict)

# print(result)

# print(type(person_dict))
# print(type(result))

#json.dump()
person_dict={
    "name": "Ebru Aydoğan",
    "languages": ["C#", "Python"]
    }

with open('person.json', 'w', encoding='utf-8') as file:
    json.dump(person_dict, file, indent=4, ensure_ascii=False)