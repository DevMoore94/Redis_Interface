#Authored by: Brandon Moore
#November 28th 2014
#Purose: Create an interface to easily interact with redis database

import redis
import urlparse
import sys
    

def newKeyValue():
    key = raw_input("Enter key: ")
    value = raw_input("Enter value for key: ")
    try:
        redisControl.set(key,value) 
    except Exception as e:
        print("ERROR: " + str(e)) 

def getKey():
    key = raw_input("Enter key to retrieve: ")
    try:
        print redisControl.get(key)

    except Exception as e:
        print("ERROR: " + str(e))

def getKeyList():
    key = raw_input("Enter key to retrieve list: ")
    try:
        list = redisControl.lrange(key,0,-1)

    except Exception as e:
        print("ERROR: " + str(e))

def deleteKey():
    key = raw_input("Enter key to delete: ")
    try:
        print redisControl.delete(key)

    except Exception as e:
        print("ERROR: " + str(e))

def createList():
    key = raw_input("Enter key for list to create: ")
    value = raw_input("Enter value for key: ")
    try:
        redisControl.lpush(key,value)
    except Exception as e:
        print("ERROR: " + str(e))

def addToList():
    key = raw_input("Enter key for list to add to: ")
    value = raw_input("Enter value for key: ")
    try:
        redisControl.lpushx(key,value)
    except Exception as e:
        print("ERROR: " + str(e))
def menu():
    
    while True:
        print "1: Create new Key/Value pair"
        print "2: Create new key/List"
        print "3: Add to list"
        print "4: Retrieve Key"
        print "5: Retrieve List"
        print "6: Delete a key"
        print "0: Exit"
        selection = int(raw_input("Choose Action: "))
        if selection == 1:
            newKeyValue()
        elif selection == 2:
            createList()
        elif selection == 3:
            addToList()
        elif selection == 4:
            getKey()
        elif selection == 5:
            getKeyList()
        elif selection == 6:
            deleteKey()
        elif selection == 0:
            sys.exit()
        else:
            print("That is not a valid selection.")
            

user_input = raw_input("Enter redis URL: ")
url = urlparse.urlparse(user_input)
redisControl = redis.Redis(host=url.hostname, port=url.port, db=0, password=url.password)
menu()

