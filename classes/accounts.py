import pyperclip

class Accounts:
    '''
    Class that instantiates the accounts and their details.
    '''

    account_list =[]
    def __init__(self, account_name, user_name, login_email, password):
        '''
        init method for the account list details
        '''

        self.account= account_name
        self.account_user= user_name
        self.email= login_email
        self.password= password



