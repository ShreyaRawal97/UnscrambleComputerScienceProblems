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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

set1 = set()
set2 = set()
set3 = set()
set4 = set()

for i in calls:
    if i[0][0] == "7" or i[0][0] == "8" or i[0][0] == "9" or i[0][0] == "(" or i[0][:3] == "140":
        set1.add(i[0])
    if i[1][0] == "7" or i[1][0] == "8" or i[1][0] == "9" or i[1][0] == "(" or i[1][:3] == "140":
        set2.add(i[1])

set3 = set1.difference(set2)

for i in texts:
    set4.add(i[0])
    set4.add(i[1])

telemarketers_set = set()
telemarketers_set = set3.difference(set4)
print("These numbers could be telemarketers:")
print("\n".join(sorted(telemarketers_set)))
