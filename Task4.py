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

set1 = set(i[0] for i in calls)
set2 = set(i[1] for i in calls)
set3 = set1.difference(set2)
set4 = set(i[0] for i in texts)
set4 = set(i[1] for i in texts)

telemarketers_set = set()
telemarketers_set = set3.difference(set4)
print("These numbers could be telemarketers:")
print("\n".join(sorted(telemarketers_set)))


#Big-O Analysis
"""
O(cardinality of telemarketers_set)
"""
