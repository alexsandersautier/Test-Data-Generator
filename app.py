import os
import random
#list of options: 

#to generate names
def generate_names(save):
    names = ['Alexsander Sautier','Harvey Specter', 'Mike Ross', 'Donna Paulsen', 'Rachel Zane']
    print(generate_random(names))
    generate_file(save, generate_random(names))

#to generate emails
def generate_emails(save):
    emails = ['ceo@personhardman.com','juniorpartner@personhardman.com', 'seniorpartner@personhardman.com','secretary@personhardman.com', 'legalassistent@personhardman.com']
    print(generate_random(emails))
    generate_file(save,generate_random(emails))

#to generate phone number
def generate_phone_number(save):
    number = ['(79) 3579-3926','(66) 3597-5162', '(74) 3261-4108', '(63) 2421-7885', '(95) 2832-5476']
    print(generate_random(number))
    generate_file(save,generate_random(number))

#to generate city
def generate_city(save):
    city = ['New York','Orlando','Miami','Curitiba','Lisboa']
    print(generate_random(city))
    generate_file(save,generate_random(city))

#to generate states
def generate_states(save):
    state = ['SC','PR','RS','SP','ES']
    print(generate_random(state))
    generate_file(save,generate_random(state))

#finish program
def exit_app():
    print('Closing the program')
    print('©Sautier Alexsander\n')
    os._exit(0)

#to generate random option
def generate_random(option):
    return random.choice(option)

#to generate file txt
def generate_file(save,option):
    if save == 'y':
        with open('data.txt', 'a', newline='') as file:
            file.write(option + os.linesep)            

#create menu
def main(option, save):
    if option == 'stop':
        exit_app()
    elif option == '1':
        generate_names(save)    
    elif option == '2':
        generate_emails(save)
    elif option == '3':
        generate_phone_number(save)        
    elif option == '4':
        generate_city(save)        
    elif option == '5':
        generate_states(save) 
    else:
        print('\nwrong option\n')           

#program
while True:
    print('--------------------------------------')
    print('Welcome to Test Data Generator - For finish program, type "stop"')
    print('--------------------------------------')
    print('''
    [1] - Name
    [2] - Email
    [3] - Phone Number
    [4] - City
    [5] - State
    ''')
    try:
        option = input('Choose one of the options: ')

        options = option.split(',')

        save = input('\nDo you like save data in file txt? (y/n): ')  if option[0] in options else print ('')
        print('\n')

        for option in options:
            main(option, save)
    except:
        print('Check!')