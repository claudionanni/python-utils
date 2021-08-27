#!/usr/bin/env python3

import json

people = [
  {
    "name": "Sabrina Green",
    "username": "sgreen",
    "phone": {
      "office": "802-867-5309",
      "cell": "802-867-5310"
    },
    "department": "IT Infrastructure",
    "role": "Systems Administrator"
  },
  {
    "name": "Eli Jones",
    "username": "ejones",
    "phone": {
      "office": "684-348-1127"
    },
    "department": "IT Infrastructure",
    "role": "IT Specialist"
  }
]

print("Will write a list of dictionaries to a file in json format (json can handle automatic conversion from list of dicts to json)")
print("""\nSample conversion table:
Python:		Json:
----------------------
dict 		object
list, tuple 	array
str		string
int,float...	number
""")

with open('people.json', 'w') as people_json:
    json.dump(people, people_json, indent=2)

people_json = json.dumps(people,indent=2)
print(people_json)


print("Now read back the json file")

with open('people.json', 'r') as people_json:
    people = json.load(people_json)

print(people)
