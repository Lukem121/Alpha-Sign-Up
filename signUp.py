import mechanize
import time
import string
from random import *
import re
from tempMail import tempMail


#This code genarates a email ###################################################


m = tempMail.mailer()
email = m.getEmail()


#This code genarates a username ################################################

min_char = 8
max_char = 20

allchar = string.ascii_letters + string.digits
usernameGen = "".join(choice(string.lowercase) for x in range(randint(min_char, max_char)))
passwordGen = "".join(choice(string.lowercase) for x in range(randint(min_char, max_char)))


###############################################################################


#This code sets the password

password = "ThisIsARandomPassword"

print("Code is running please allow up to 30 seconds")


###############################################################################

#makes the browser
br = mechanize.Browser() #<--------------------------------------------------- This code make the browser
#opens web page
response = br.open("https://users.bolehvpn.net/")#<--------------------------- WEBSITE URL GOES HERE!! Visit the current url to inspact the page

#selects the form
br.form = list(br.forms())[1] #<---------------------------------------------- This code selects the HTML form on the webpage


password = "ThisIsARandomPassword"

br['username'] = usernameGen #<----------------------------------------------- Change the 'username' to the name of the input box in the HTML fourm.
br['email'] = email #<-------------------------------------------------------- Change the 'email' to the name of the input box in the HTML fourm.
br['password'] = password #<-------------------------------------------------- Change the 'password' to the name of the input box in the HTML fourm.
br['password_confirmation'] = password #<------------------------------------- Change the 'password_confirmation' to the name of the input box in the HTML fourm.
br.find_control("policy").items[0].selected=True #<--------------------------- This code checks a tick box on the webpage


response = br.submit() #<------------------------------------------------------This code submits the HTML form
time.sleep(3)

################################################################################

#This code waits for the email

while 1:
    result = m.mailBox()
    if result:
    	emailHTML = result
        print("Email Recived")
        break
    time.sleep(1)

href = emailHTML['body']
 
###############################################################################


#This code finds the activation link and pulls the activation code from it.

confCode = re.search(r"(?<=confirm/).*?(?=target)", href).group(0)

###############################################################################

#This code removes unnecessary characters from the string

for char in ' ?."/;:':  
	confCode = confCode.replace(char,'')  


###############################################################################


#This code activates the new account

linkPartA = "https://users.bolehvpn.net/account/confirm/" # I had issues getting the whole link from the email. I already know the first part of the link so I only needed to extract the activation code.

activationLink = linkPartA + confCode

br.open(activationLink) #<----------------------------------------------------- This code goes to the activation url 

time.sleep(5)

print("User Name: " +usernameGen + "   Email: " +email + "   Password:" + password)

