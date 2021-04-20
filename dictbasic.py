dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
phone_numbers = {'boss' : 5551234567, 'Suzy' : 22657854310}
empty_dictionary = {}
print(dictionary)
print(phone_numbers)
print(empty_dictionary)
for key in dictionary.keys():
    print(key, "->", dictionary[key])
dictionary['cat'] = 'minou'
print(dictionary)

