fruits = {
    "apples": 10,
    "bananas": 20,
    "mangoes": 15,
    "oranges": 200,
    "watermelons": 50
}
fruitss=[]
old_key=input("Enter the key to rename: ")
new_key=input("Enter the new key: ")
for i in fruits:
    tuple_a=[]
    if i==old_key:
        tuple_a.append(new_key)
        tuple_a.append(fruits[i])
    else:
        tuple_a.append(i)
        tuple_a.append(fruits[i])
    fruitss.append(tuple(tuple_a))
print(fruitss)
    
