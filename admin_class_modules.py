# This program will be focused on Exercise 9-8 of importing classes
# and create instances to call methods
    # This program has been created by Michael Taufa

class User():
    def __init__(self, firstName, lastName, age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age

    def display_userName(self):
        print(f"{self.firstName.title()} {self.lastName.title()}")


class special_Privileges():
    def __init__(self, privileges = ['Add Post', 'Delete Post', 'Ban User']):
        self.privileges = privileges 

    def display_specialPrivileages(self):

            print("The following is all Special Privileages:")

            for privileage in self.privileges:
                print(f"-{privileage}")


class Admin(User):
    def __init__(self, firstName, lastName, age):
        super().__init__(firstName, lastName, age)
        self.privileages = ['Can add posts', 'Can delete post', 'Can ban user']
        self.special = special_Privileges()

    def display_adminPrivileages(self):

        print("The following is all Admin Privileages:")

        for privileage in self.privileages:
            print(f"-{privileage}")
