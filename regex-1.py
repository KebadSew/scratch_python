import re

text = """Dave dave@google.com
    Steve steve@gmail.com
    Rob rob@gmail.com
    Ryan ryan@yahoo.com
    """
pattern = r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}'

# re.IGNORECASE makes the regex case-insensitive
regex = re.compile(pattern, flags=re.IGNORECASE)
all_emails = regex.findall(text)
print(all_emails)


m =regex.search(text)
email = text[m.start():m.end()]

print(email)
print("------")

print(text)
redacted = regex.sub('*****',text)
print(redacted)
print(text)

# segmentation: username, domain name and domain suffix
# group1: ([A-Z0-9._%+-]+)
# group2: ([A-Z0-9.-]+)
# group3: ([A-Z]{2,4})

pattern = r'([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\.([A-Z]{2,4})'
regex = re.compile(pattern,flags=re.IGNORECASE)

# better solution *** more efficient ***
all_groups= regex.findall(text)
print(all_groups)
print('++++++++++++++++')
for group in all_groups:
    print('userName: ',group[0])
    print('domain:',group[1])
    print('domain suffix:',group[2])
    print('-------------')
print('++++++++++++++++')


print('   ----------- ')
first_match = regex.match('steve@gmail.com')
first_group = first_match.groups()
print(first_group)

# the longest approach  ** very slow performance **
print(' -----------------------')
for email in all_emails:
    match = regex.match(email) # not recommended
    groups = match.groups() # not recommended
    print('username: ',groups[0])
    print('domain: ',groups[1])
    print('domain suffix: ',groups[2])
    print(' ============== ')
print(' -------------------------- ')

print(regex.sub(r'Username: \1, Domain: \2, Suffix: \3', text))


# text = """Dave dave@google.com
# Steve steve@gmail.com
# Rob rob@gmail.com
# Ad adem@gmail.com
# Ryan ryan@yahoo.com"""
#
# fname_pattern = r'[A-Z]{1}[a-z]+'
# fname_regex = re.compile(fname_pattern)
# print(fname_regex.findall(text))
