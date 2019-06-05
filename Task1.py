"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""

#sets are unordered and it has unique elements (duplicates are not allowed)
text = set(i[0] for i in texts).union(set(i[1] for i in texts))
call = set(i[0] for i in calls).union(set(i[1] for i in calls))

num = len(text.union(call)) #length of the union of texts and calls

print("There are", num, "different telephone numbers in the records.")

#Big O analysis
"""
union operation set: O(n)
"""
