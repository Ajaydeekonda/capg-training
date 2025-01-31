import json

# Python dictionary
data = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Convert to JSON string
json_string = json.dumps(data, indent=4)  # indent makes it readable
print(json_string)


json_data = '{"name": "Alice", "age": 25, "city": "New York"}'

# Convert JSON string to Python dictionary
data = json.loads(json_data)

print(data["name"])  # Output: Alice
print(data["age"])  