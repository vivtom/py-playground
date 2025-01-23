#Given n names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers. You will then be given an unknown number of names to query your phone book for. For each name queried, print the associated entry from your phone book on a new line in the form name=phoneNumber; if an entry for name is not found, print Not found instead.
#Note: Your phone book should be a Dictionary/Map/HashMap data structure.

k = int(input())
phonebook = {}
for _ in range(k):
    a,b = input().split()
    phonebook[a] = b 

while True:
    try:
        query = input().strip()
        if query in phonebook:
            print(f"{query}={phonebook[query]}")
        else:
            print('Not found')
    except EOFError:
        break
