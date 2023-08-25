keys = ['One', 'Two', 'Three']
values = [1, 2, 3]
def create_dict(keys: list, values: list) -> dict:
  return {key: value for key, value in zip(keys, values)}

my_dict = create_dict(keys, values)
print(my_dict) # {'One': 1, 'Two': 2, 'Three': 3}

client_dict = {
	"name": "John",
	"age": 25,
	"salary": 5000,
	"city": "Moscow"
}
def extract_keys(dictionary: dict, keys: list = None) -> dict:
    if keys is None:
        keys = list(dictionary.keys())
    return {key: dictionary[key] for key in keys if key in dictionary}

input_dict = {'name': 'John Doe', 'age': 30, 'city': 'New York'}
keys = ['name', 'age']
result = extract_keys(input_dict, keys)
print(result) # {'name': 'John Doe', 'age': 30}