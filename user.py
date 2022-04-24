import pyperclip

class User:
    '''
    Class that instantiates the user and their details.
    '''

    user_list =[]
    def __init__(self, user_name, email, password):
        '''
        init method for the user details 
        '''

        self.user= user_name
        self.user_email= email
        self.user_pass= password