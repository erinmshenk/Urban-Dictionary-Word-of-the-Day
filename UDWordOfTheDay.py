#!/usr/bin/python3
"""
python script to create word of the day from urban dictionary
"""

import requests
from bs4 import BeautifulSoup
import smtplib 
from email.mime.text import MIMEText


# requests urban dictionary home page 
r = requests.get('https://www.urbandictionary.com')

#print(r.text[0:500])

soup = BeautifulSoup(r.text, 'html.parser')

# finds the title
title = soup.find('title').text


# finds the definition
definition = soup.find('meta', attrs={'property': 'og:description'}) 


cariers = {
        'verizon': '@vtext.com',
        'cc': '@mms.att.net'
        }

phone_numbers = [
        
        ''+ cariers['verizon'],
        
        '' + cariers['verizon'],
        
        '' + cariers['verizon'], 
        
        ]

def send(message, number):
    to_number = number
    auth = ('sendingmessages99@gmail.com', 'Charlie2017')
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    
    server.starttls()

    server.login(auth[0], auth[1])
    
    server.sendmail(auth[0], to_number, message)
    
    print("\nmessage has sent")
    
    server.quit()

body = title + "\n" + definition['content']
msg = MIMEText(body, 'plain')

text = msg.as_string()

for x in phone_numbers:
    send(text,x)


