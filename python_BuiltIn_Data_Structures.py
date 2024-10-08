
"""Key Differences:

Feature         	List	    Tuple       	Set         	Dictionary
Order	          Ordered	    Ordered	        Unordered	    Unordered (insertion order preserved in Python 3.7+)
Mutability	        Mutable 	Immutable	    Mutable     	Mutable
Duplicates	        Allowed	    Allowed	        Not allowed 	Not allowed for keys, allowed for values
Indexing	        Yes	        Yes	            No          	No (access using keys)
Key-value pairs    	No	        No	            No          	Yes

Export to Sheets
Choosing the Right Data Structure:

Lists: Use for ordered collections of elements that need to be modified.
Tuples: Use for ordered collections of elements that should not be modified (e.g., representing coordinates, database records).
Sets: Use for collections of unique elements where order doesn't matter (e.g., checking for duplicates, performing set operations).
Dictionaries: Use for storing key-value pairs where you need to quickly access values based on their keys (e.g., representing data about objects or people).
By understanding these differences, you can choose the appropriate data structure for your specific use case and write more efficient and effective Python code."""

tapule = (1,2,3,3)
print(tapule)

for i in tapule:
    print(i, sep=" ")

set = set([1, 2, 3, 3, 6])
print(set)

