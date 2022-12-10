# Creating a simple phonebook

n = int(input("Enter the number of entries: "))

# entries to the phone book
entries = dict()
for i in range(n):
    entry = input("Enter the name add space and enter the 8-digit number: ").strip()
    entry = entry.split()
    
    for k in entry:
        entries[entry[0]] = entry[1]
        
print(entries)

# making queries
queries = [] # A list of queries

query = ' '
while query != '':
    query = input('Enter the name you want to look up: ')
    if query:
        queries.append(query)
    
print(queries)

# validate the query
for query in queries:
    item = query
    if item in entries.keys():
        # for key, value in entries.items():
        print(f'{item}={entries[item]}')
        
    else:
        print("Not found")