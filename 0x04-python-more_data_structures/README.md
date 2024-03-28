A Python dictionary is a data structure that allows us to easily write very efficient code. In many other languages, this data structure is called a hash table because its keys are hashable. We'll understand in a bit what this means.

A Python dictionary is a collection of key:value pairs. You can think about them as words and their meaning in an ordinary dictionary. Values are said to be mapped to keys. For example, in a physical dictionary, the definition science that searches for patterns in complex data using computer methods is mapped to the key Data Science.

In this Python tutorial, you'll learn how to create a Python dictionary, how to use its methods, and dictionary comprehension, as well as which is better: a dictionary or a list. To get the most out of this tutorial, you should be already familiar with Python lists, for loops, conditional statements, and reading datasets with the reader() method. If you aren't, you can learn more at Dataquest.

What Are Python Dictionaries Used for?
Python dictionaries allow us to associate a value to a unique key, and then to quickly access this value. It's a good idea to use them whenever we want to find (lookup for) a certain Python object. We can also use lists for this scope, but they are much slower than dictionaries.

This speed is due to the fact that dictionary keys are hashable. Every immutable object in Python is hashable, so we can pass it to the hash() function, which will return the hash value of this object. 
