#!/usr/bin/env python3
from operator import concat
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
    return User.user_exists(email)

def display_user():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()


