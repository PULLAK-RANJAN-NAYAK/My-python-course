# There are many methods 

marks = {
    "Ranjan":50,
    "Pullak":78,
    "Nayak":100,
    567 : "Hello"
}
print(marks.items()) # dict_items([('Ranjan', 50), ('Pullak', 78), ('Nayak', 100), (567, 'Hello')])
print(marks.keys())  # dict_keys(['Ranjan', 'Pullak', 'Nayak', 567])
print(marks.values())# dict_values([50, 78, 100, 'Hello'])
marks.update({"Ranjan": 79, "Helll" : 89}) # It shows that you can update the existing value and even add some new value 
print(marks.get("Ranjan")) # It returns the value of the specified key (79)
print(marks["harry2"]) # The get function will give none but this function will give error 
print(marks,type(marks))