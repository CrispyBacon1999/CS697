password = input("Enter a password: ")

rules = [
    # Test whether the length is at least 8
    lambda p: len(p) >= 8,
    # Test if the password is alphanumeric
    lambda p: p.isalnum(),
    # Iterate through letters and count the digits
    lambda p: sum([lett.isdigit() for lett in p]) >= 2,
    # Find capitals and return True if there is at least 1 match
    lambda p: not p.islower()
]

if(all([rule(password) for rule in rules])):
    print("valid password")
else:
    print("invalid password")
