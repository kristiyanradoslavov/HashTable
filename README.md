Workshop HashTable
1. Overview
Create a HashTable class that should have the needed functionality for a hash table, such as:

•	hash(key: str) - a function that should figure out where to store the key-value pair  
•	add(key: str, value: any) - adds a new key-value pair usign the hash function  
•	get(key: str) - returns the value corresponding to the given key  
•	additional "magic" methods, that will make the code in the example work correctrly  

The HashTable should have an attribute called array of type: list, where all the values will be stored. Upon initialization the default length of the array should be 4. After each addition of an element if the HashTable gets too populated, double the length of the array and re-add the existing data.
You are not allowed to inherit any classes. Feel free to implement your own functionality (and unit tests) or to write the methods by yourself.


<i><b>Test Code<i><B>:

table = HashTable()  
table["name"] = "Peter"  
table["age"] = 25  
print(table)  
print(table.get("name"))  
print(table["age"])  
