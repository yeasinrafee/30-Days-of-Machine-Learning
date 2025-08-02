import json
x = '{"name": "Yeasin Rafi", "age": 30, "city": "Dhaka"}'
y = json.loads(x)       # JSON to python
print(y)

a = {
    "name": "Rafee",
    "age": 60,
    "city": "Dhaka"
}
b = json.dumps(a)
print(b)

c = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(json.dumps(c, indent=4, separators=(".", "="), sort_keys=True))       # Formatting the JSON data