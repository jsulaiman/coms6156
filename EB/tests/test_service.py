
from CustomerInfo.Users import UsersService as UserService
import json

def t1():

    r = UserService.get_by_email('metus.vitae@nibhAliquamornare.edu')
    print("Result = \n", json.dumps(r, indent=2))

t1()