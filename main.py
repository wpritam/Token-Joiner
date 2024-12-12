    # Code Uploaded By Pritam & Qualwin
try:
    import requests
    import pyfiglet
    import os.path
    import sys
except ImportError:
    exit("Please install requests and try again...")

ascii_banner = pyfiglet.figlet_format("Coded by Pritam & Qualwin")
print(ascii_banner)

link = input('Enter the Discord Invite Link: ')
if len(link) > 6:
    link = link[19:]
apilink = "https://discordapp.com/api/v6/invite/" + str(link)

print("Invite Code: ", link)

with open('tokens.txt', 'r') as handle:
    tokens = handle.readlines()
    for x in tokens:
        token = x.rstrip()
        headers = {
            'Authorization': token
        }
        requests.post(apilink, headers=headers)
    print("Verified tokens have been added to the server.")
