from abc import ABC,abstractmethod
class UserAuthentication(ABC):
    def login(self):
        pass
    def logout(self):
        pass
class GoogleAuth(UserAuthentication):
    def login(self):
        print("logged in")
    def logout(self):
        print("logged out")
class FacebookAuth(UserAuthentication):
    def login(self):
        print("Facebook-Logged in")
    def logout(self):
        print("Facebook logged out")
        
def main():
    get_input=input("Enter google or Facebook: ")
    if get_input.lower=="google":
        res=GoogleAuth()
    else:
        res=FacebookAuth()
    res.login()
    res.logout()
main()