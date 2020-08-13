# Python 3.4.3
# Username and Password...
# The programs purpose: A user must enter the correct username and password for a site called FaceSnap...
# The correct username is elmo and the correct password is blue.


userName = input("Hello! Welcome to FaceSnap! \n\nUsername: ") #Ask's the User for Username input
password = input("Password: ") # Ask's the user for their password


count = 0 # Create a variable, to ensure the user has limited attempts at entering their correct username and password
count += 1 # The user has already had one attempt above, therefore count has been incremented by 1 already.


while userName == userName and password == password: # The Input will always lead to this while loop, so we can see if their username and password is wrong or correct.


    if count == 3: # Counter, to make sure the user only gets a limited number (3)of attempts
        print("\nThree Username and Password Attempts used. Goodbye") # Lets the user know they have reached their limit
        break # Leave the Loop and the whole program


    elif userName == 'elmo' and password == 'blue': # The userName and password is equal to 'elmo' and 'blue', which is correct, they can enter FaceSnap!
        print("Welcome! ") # Welcomes the User, the username and password is correct
        break # Leave the loop and the whole program as the username and passowrd is correct


    elif userName != 'elmo' and password != 'blue': # The userName and password is NOT equal to 'elmo' and 'blue', the user cannot enter FaceSnap
        print("Your Username and Password is wrong!") # Lets the user know that the Username and password entered is wrong.
        userName = input("\n\nUsername: ") # Requests the user to have another attempt at entering their correct username
        password = input("Password: ") # Requests the user to have another attempt at entering their correct password
        count += 1 # Increments the count by 1
        continue # Continue, as the user hasn't managed to get their username and password correct yet


    elif userName == 'elmo' and password != 'blue': # The userName is equal to 'elmo', but password is NOT equal to 'blue', the user cannot enter FaceSnap
        print("Your Password is wrong!") # Lets the user know that their password is wrong
        userName = input("\n\nUsername: ") # Requests the user to have another attempt at entering their correct username
        password = input("Password: ") # Requests the user to have another attempt at entering their correct password
        count += 1 # increments the count by 1
        continue # Continue, as the user hasn't managed to get their username and password correct yet


    elif userName != 'elmo' and password == 'blue': # The userName is NOT equal to 'elmo', however password is equal to 'blue', the user cannot enter FaceSnap
        print("Your Username is wrong!") # Lets the user know that their username is wrong
        userName = input("\n\nUsername: ") # Requests the user to have another attempt at entering their correct username
        password = input("Password: ") # Requests the user to have another attempt at entering their correct password
        count += 1 # Increments the count by 1
        continue # Continue, as the user hasn't managed to get their username and password correct yet

def testAddrExclude(self):
        addr1 = ipaddress.ip_network('10.1.1.0/24')
        addr2 = ipaddress.ip_network('10.1.1.0/26')
        addr3 = ipaddress.ip_network('10.2.1.0/24')
        addr4 = ipaddress.ip_address('10.1.1.0')
        addr5 = ipaddress.ip_network('2001:db8::0/32')
        addr6 = ipaddress.ip_network('10.1.1.5/32')
        self.assertEqual(sorted(list(addr1.address_exclude(addr2))),
                         [ipaddress.ip_network('10.1.1.64/26'),
                          ipaddress.ip_network('10.1.1.128/25')])
        self.assertRaises(ValueError, list, addr1.address_exclude(addr3))
        self.assertRaises(TypeError, list, addr1.address_exclude(addr4))
        self.assertRaises(TypeError, list, addr1.address_exclude(addr5))
        self.assertEqual(list(addr1.address_exclude(addr1)), [])
        self.assertEqual(sorted(list(addr1.address_exclude(addr6))),
                         [ipaddress.ip_network('10.1.1.0/30'),
                          ipaddress.ip_network('10.1.1.4/32'),
                          ipaddress.ip_network('10.1.1.6/31'),
                          ipaddress.ip_network('10.1.1.8/29'),
                          ipaddress.ip_network('10.1.1.16/28'),
                          ipaddress.ip_network('10.1.1.32/27'),
                          ipaddress.ip_network('10.1.1.64/26'),
                          ipaddress.ip_network('10.1.1.128/25')]) 

