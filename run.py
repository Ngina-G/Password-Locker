#!/usr/bin/env python3
import email
from operator import concat
import re

from click import password_option
from httplib2 import Credentials
from credential import Account
from user import User
import random
import string

def create_user(user_name, email, password):
    '''
    Function to create a new user
    '''
    new_user = User(user_name, email, password)
    return new_user
def save_user(user):
    '''
    Function to save user
    '''
    return user.save_user()

def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()

def find_user(email):
    '''
    Function to find a user by email and return the user
    '''
    return User.find_by_user_email(email)

def existing_user(user_name, password):
    '''
    Function to check if a contact exists with that number and return a Boolean
    '''
    return User.user_exists(user_name, password)

def display_user(self):
    '''
    Function that returns all the saved users
    '''
    return self.user_list

# user login functions
def user_login(email,password):
    '''
    Function that returns the user login
    '''
    user = User.user_login(email, password)
    if not user:
        user_name, password = ask_for_login_details()
        return user_login(user_name, password)
    return user

def ask_for_login_details():
    email = input('Enter email: ')
    password = input('Enter password: ')
    return [email, password]

# account functions
def create_account(the_account, account_user_name, login_email, login_password):
    '''
    Function that creates account
    '''
    new_account = Account(the_account, account_user_name, login_email, login_password)
    return new_account

def save_account(account):
    '''
    Function that saves the account
    '''
    return account.save_account()

def del_account(the_account):
    '''
    Function to delete an account
    '''
    the_account.delete_account()


def display_accounts():
    '''
    Function that returns all the saved accounts
    '''
    # credentials = Account.show_account()
    # for credential in credentials:
    #     print(credential.the_account)
    #     print(credential.account_user)
    #     print(credential.email)
    #     print(credential.password)
    return Account.display_accounts()

def find_account(the_account):
    '''
    Function to find an account by email and return the account
    '''
    return Account.find_by_account_name(the_account)

def check_existing_account(the_account):
    '''
    Function to check if a account exists with that number and return a Boolean
    '''
    return Account.account_exists(the_account)



def main():
    user = None

    print('Hi, kindly sign up to use password locker.')
  
    print('Create your User Name?')
    user_name= input()

    print(f'Hi, {user_name}!')
    email= input('Add your email address: ')
    print("\n")

    print('Now enter your numerical 6 figure pasword')
    password = input()
    print("\n")

    user_created = save_user(create_user(user_name, email, password))
    # if user_created:
    print(f'\n Account created successfully')
    print("\nLOGIN")
    print("-"*7)
    print("Enter your username")
    user_name = input().strip(' ')
    print("Enter your password")                   
    password = input().strip(' ')
    if existing_user(user_name, password):

            while True:
                    print('\nPlease choose an action')
                    print('\n Use these short codes: \nca- create a new account, \nda- to  display accounts, \nfa- to find an account, \nde- to delete an account and \nex- to exit.')
                    short_code= input().lower()

                    if short_code == 'ca':
                        the_acc = input('\nEnter the account name (Twitter): ')
                        acc_user_name = input('\nEnter your account user name: ')
                        log_email = input('\nEnter your account email: ')
                        print('\nWould you like us to generate a password for you? y/n')
                        no = input().lower()
                        # yes = input().lower()

                        if no == 'n':
                            log_password=input('Enter your password: ')
                            print(log_password)
                        else:
                            print('Generating one for you')
                            length = int(input('Enter the length of password: '))
                            lower = string.ascii_lowercase
                            upper = string.ascii_uppercase
                            num = string.digits
                            symbols = string.punctuation
                            all = lower + upper + num + symbols
                            temp = random.sample(all,length)
                            log_password = "".join(temp)
                            print(log_password)

                        save_account(create_account(the_acc, acc_user_name, log_email, log_password))
                        print('\nYour account details are as follows:')
                        print(f'\nNew {the_acc} account with the username {acc_user_name} email- {log_email} and password {log_password} created')


                    elif short_code == 'da':
                        if display_accounts():
                            print('Here is a list of all your accounts')
                            print('\n')

                            for account in display_accounts():
                                print(f'~For account: {account.account_name} user name: {account.account_user} email: {account.email} and password: {account.password}')
                                print('\n')

                        else:
                            print('\n')
                            print("You don\'t seem to have any accounts saved yet")
                            print('\n')

                    elif short_code =='fa':
                            print("Enter the account name you want to search for")

                            search_account_name = input()

                            if check_existing_account(search_account_name):
                                search_account= find_account(search_account_name)
                                print(f'{search_account.account_name}, User name...{search_account.account_user}')
                                print('-'*20)

                                print(f'Email address..{search_account.email}')
                                print(f'Account password ...{search_account.password}')
                            else:
                                print('That contact does not exist')

                    elif short_code == 'de':
                        print('Enter account you want to delete: ')
                        search_account_name = input()

                        if check_existing_account(search_account_name):
                            search_account= find_account(search_account_name)
                            print(f'Deleting {search_account.account_name} account!')
                            del_account(search_account)
                        else:
                            print('That contact does not exist')

                    elif short_code == 'ex':
                        print('Bye ....')
                        break
                    else:
                        print('I really didn\'t get that. Please use the short codes.')

if __name__ =='__main__':
    main()