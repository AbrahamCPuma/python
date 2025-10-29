print('-----Initialize-----\n')
user_name = input('Write your user name\t')
age = input('\nwrite your age\t')
pwd = input('\nwrite your password\t')
email = input('\nwrite your email\t')
role = input('\nwrite your role\t')
banned_list = ['abraham94','abraham95']
#------------------ VALIDATIONS------------------
user_age_val = user_name is not '' and int(age) >= 18
pwd_val = len(pwd) >= 8 and ' ' not in pwd
email_val = '@' in email and email.endswith('.com') and not ''
user_name_val = not None and type(user_name) == str and len(user_name) > 5 and ' ' not in user_name


#----------------- RESULTS----------------------

print('\n-----Results-----\n')
if user_name in banned_list:
    print(f'\nthe user name is {user_name} and it is BANNED\n')
else:

    print(f'\nthe user name is {user_name} and the age is {age}, \nUser name is not blank and age is 18 or more is {user_age_val}\n')

    if pwd_val == True:
        print(f'Your password is accepted\n')
    else:
        print(f'Your password is not accepted, \'{pwd}\' is not valid\nTry again\n')


    if email_val == True:
        print(f'Your email is accepted\n')
    else:
        print(f'Your email is not accepted, \'{email}\' is not valid\nTry again\n')

    if user_name_val == True:
        print(f'Your user name is accepted\n')
    else:
        print(f'Your user name is not accepted, \'{user_name}\' is not valid\nTry again')

    if role == 'Admin':
        print(f'you registered as Admin')
    elif role == 'Moderator':
        print(f'you registered as Moderator')
    else:
        print(f'your role is not valid\nTry again writing \'Admin\' or \'Moderator\'\n')