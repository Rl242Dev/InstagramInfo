from cgi import print_form
from instagrapi import Client
import sys

cl = Client()
cl.login(username='**********', password='********')
account = cl.account_info().dict()

if len(sys.argv) < 2:
    print('''
    Help for InstaInfo:

    Usage : python info.py arg[1]

    arg[1] = name of the user you want the Info

    Exemples :

    python info.py github
    ''')
    try:
        print(sys.argv[3])
    except IndexError:
        pass
    quit()

name = str(sys.argv[1])

info = cl.user_info_by_username(name).dict()
print('Profil Id: '+info['pk'])
print('Profil Name: '+info['username'])
print('Profil Full Name: '+info['full_name'])
private = str(info['is_private'])
verified = str(info['is_verified'])
print('Profil Private: '+private)
print('Verified: '+verified)
print('\n'+'Business:')
business = str(info['is_business'])
print('Business: '+business)
email = str(info['public_email'])
print('Business Email: '+email)
