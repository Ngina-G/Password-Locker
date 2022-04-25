#!/usr/bin/env python3
import email
from operator import concat
import re

from click import password_option
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
    user.save_user()

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

def check_existing_user(email):
    '''
    Function to check if a contact exists with that number and return a Boolean
    '''
    new_user_entered = User.user_list(email)
    return new_user_entered

def display_user():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()

# user login functions
def user_login(email,password):
    '''
    Function that returns the user login
    '''
    this_user = User.user_list(email, password)
    if not this_user:
        user_name, password = ask_for_login_details()
        return user_login(user_name, password)
    return this_user

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

def del_account(account):
    '''
    Function to delete an account
    '''
    account.delete_account()

def display_account():
    '''
    Function that returns all the saved accounts
    '''
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
    new_account = Account.account_list(the_account)
    return new_account



def main():
    user = None

    print('Hi, kindly sign up to use password locker.')
    print("\n")
  
    print('Create your User Name?')
    user_name= input()

    print(f'hello {user_name}. Add your email address.')
    email= input()
    print("\n")

    print(f'Email entered: {email}. Add your password.')
    password = input()
    print("\n")

    user_created = save_user(create_user(user_name, email, password))
    if user_created:
        print(f'\n Account created successfully')
        email, password = ask_for_login_details()
        new_user = user_login(email, password)
        if new_user:
            user = new_user

    while True:

        if user:
            print('\n Use these short codes: \n ca- create a new account, \nda- to  display accounts, \nfa- to find an account, \nde- to delete an account and \nex- to exit.')
            short_code= input().lower()

        if short_code == 'cc':
            the_account = input('\nEnter the account name (Twitter): ')
            account_user_name = input('\nEnter your account user name: ')
            login_email = input('\nEnter your account email: ')
            print('\nDo you have a password? y/n')
            no = input().lower()
            yes = input().lower()
            if yes == 'y':
                length = int(input('\nEnter the length of password: '))
                lower = string.ascii_lowercase
                upper = string.ascii_uppercase
                num = string.digits
                symbols = string.punctuation
                all = lower + upper + num + symbols
                temp = random.sample(all,length)
                login_password = "".join(temp)
                print(login_password)
                return login_password
            elif no == 'n':
                login_password=input('\nEnter your password: ')

            save_account(create_account(the_account, account_user_name, login_email, login_password))
            print(f'\nYour accoutn details are as fllows:')
            print(f'\nNew {the_account} account with the username {account_user_name} email- {login_email} and password {login_password} created')


        elif short_code == 'da':
            if display_account():
                print('Here is a list of all your accounts')
                print('\n')

                for account in display_account():
                    print(f'{account.the_account} {account.account_user_name} ....{account.login_email} ....{account.login_password}')
                    print('\n')
                    print('You don\'t seem to have any accounts saved yet')
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
                    print(f'{search_account.account_name}, {search_account.account_user}')
                    print('-'*20)

                    print(f'Email address..{search_account.email}')
                    print(f'Email adress ...{search_account.password}')
                else:
                    print('That contact does not exist')

        elif short_code == 'de':
            print('Are you sure you want to delete?')
            account = input('Enter account you want to delete: ')
            print('Account to be deleted: ', account)
            del_account(account)

        elif short_code == 'ex':
            print('Bye ....')
            break
        else:
            print('I really didn\'t get that. Please use the short codes.')

if __name__ =='__main__':
    main()