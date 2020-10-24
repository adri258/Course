people = [
  {"name": "Adka", "house": "Domcek"},
  {"name": "Luki", "house": "Daleko prec"},
  {"name": "Spolu", "house": "Nevieme"},
]
"""
def f(person):
    return person["name"]
"""

people.sort(key=lambda person: person ["name"])

print(people)
