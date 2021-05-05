# Write a program that asks for a users name, and greets them with their name
friend = input("Greetings! What's your name?" )
print(f'Pleased to meet you {friend}')
# If the name given is the same as your name, say "Hey, that's my name too!"
if friend == 'Sean':
    print(f"Hey, that's my name too!")
#Ask for 10 names and keep a record of them.  After 10 names are given, say 'It was nice to meet all of you'.
friendlist = []
for x in range(10):
    z = input("Greetings! What's your name?" )
    friendlist.append(z)
print(f"{friendlist} It was nice to meet all of you.")
#4
friendlist = []
for x in range(10):
    z = input("Greetings! What's your name?" )
    if z in friendlist:
        print("Requesting a new name.")
    else:
        friendlist.append(z)
print(f"{friendlist} It was nice to meet all of you.")
