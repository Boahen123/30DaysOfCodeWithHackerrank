# Alternative to the day 8 code

n = int(input())

phone_dict = {}

for i in range(n):
    name, phone_number = input().split()
    phone_dict[name] = phone_number
    
while True:
    try:
        name_ = input()
        if name_ in phone_dict:
            print("=".join([name_ , phone_dict[name_]]))
        else:
            print("Not found")
            
    except EOFError:
        break