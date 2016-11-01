"""
this is a python module
which takes name as input
and concatenate the name
with a random intiger between 
6 and 15 and return it"""
import random
def fun(name):
    return name+" "+str(random.randint(6,15))

#this is used for calling fun
if __name__=="__main__":
    print(fun(input()))

