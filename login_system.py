#Basic console based login/registration system 
Enter=int(input('To Log-in press 1, To sign-up press 2: '))
if Enter==1:
    username=input('enter username: ')
    password=input('enter password: ')
    print(f'Welcome {username}')
elif Enter==2:
    first_name=input('enter ur first name: ')
    last_name=input('enter ur last name: ')
    email=input('enter ur email address: ')
    user_name=input('enter ur username: ')
    pass_word=input('enter a strong password(7 or more characters): ')
    C_password=input('confirm ur password: ')
    if C_password==pass_word:
        print('Account successfully created')
        user_details=f''' User details:
        Username= {user_name}
        Password= {pass_word}
        name= {first_name} {last_name}
        email address= {email}
        '''
        x=open('user_details.txt','x')
        x.write(user_details)
    else:
        print('incorrect password; enter password again')
else:
    print('Log-in(1) or sign-up(2)')
            