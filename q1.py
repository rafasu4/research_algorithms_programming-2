import re

pattern = '^([a-zA-Z0-9]+([._-]{0,1}[a-zA-Z0-9]+)*)@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]{2,})$'
valid_emails = []
invalid_emails = []

file = open('emails.txt', 'r')
lines = file.readlines()
for line in lines:
    if(re.search(pattern, line)):
        valid_emails.append(line)
    else:
        invalid_emails.append(line)

print('The valid email are:')
for email in valid_emails:
    print(email + ' ')

print('\nThe invalid email are:')
for email in invalid_emails:
    print(email + ' ')