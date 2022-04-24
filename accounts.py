import pyperclip

class Account:
    '''
    Class that instantiates the accounts and their details.
    '''

    account_list =[]
    def __init__(self, the_account, user_name, login_email, password):
        '''
        init method for the account list details
        '''

        self.account_name= the_account
        self.account_user= user_name
        self.email= login_email
        self.password= password

    def save_account(self):
        '''
        Class that saves the new account details to the account_list
        '''

        Account.account_list.append(self)

    def delete_account(self):
        '''
        Class that delete an instance of an account object
        '''

        Account.account_list.remove(self)

    @classmethod
    def find_by_account_name(cls, the_account):
        '''
        Method that finds the account user name and object by the account's name

        Args:
            account_name: Account name to search for 
        Returns:
            Account details that match the account name.
        '''

        for account in cls.account_list:
            if account.account_name == the_account:
                return account
