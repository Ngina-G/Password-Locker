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

    def save_user(self):
        '''
        Class that saves the new user details to the user_list
        '''

        User.user_list.append(self)

    @classmethod
    def find_by_user_email(cls, email):
        '''
        Method that finds the account user name and object by the user's email

        Args:
            User: Account user name to search for 
        Returns:
            User details that match the user name.
        '''

        for user in cls.user_list:
            if user.user_email == email:
                return user

    @classmethod
    def display_users(cls):
        '''
        method that returns the users list
        '''
        return cls.user_list
