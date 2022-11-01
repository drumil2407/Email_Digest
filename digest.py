#a simple mail protocol library which provide service to send mail by python to user
import smtplib
import random
from email.message import EmailMessage
#a python library which provide the random facts
import randfacts

#using beautiful library lets scrape the inspirtional quotes

from bs4 import BeautifulSoup

import requests, json


#Number 3: Take quote with web Scraping
#make list to scrape the data
authors = []
quotes = []

URL = 'https://www.goodreads.com/quotes/tag/inspirational?page=0'

#request to the website
webpage = requests.get(URL)

#parse the text from website
soup = BeautifulSoup(webpage.text, 'html.parser')
quoteText = soup.find_all('div', attrs = {'class':'quoteText'})


#print all quotes in the webpage given
for i in quoteText:
    quote = i.text.strip().split('\n')[0]
    author = i.find('span', attrs = {'class':'authorOrTitle'}).text.strip()



#function to scrape the website
def scrapeWeb(pageNum):

    #typecast to string
    pageNumber = str(pageNum)
    URL = 'https://www.goodreads.com/quotes/tag/inspirational?page=' + pageNumber
    webpage = requests.get(URL)
    soup = BeautifulSoup(webpage.text, 'html.parser')
    quoteText = soup.find_all('div', attrs = {'class':'quoteText'})

    for i in quoteText:
        quote = i.text.strip().split('\n')[0]
        author = i.find('span', attrs = {'class':'authorOrTitle'}).text.strip()
        quotes.append(quote)
        authors.append(author)


n = 10
for num in range(0,n):
  scrapeWeb(num)

#Combine the lists
combined_list = []
for i in range(len(quotes)):
    combined_list.append(quotes[i]+'-'+authors[i])

qt = random.choice(combined_list)




#Number1 get fact from library
fact = randfacts.get_fact()

#Number2 weather check
# import required modules


# Enter your API key here
api_key = "992bf81c1a659549bc32424203494ca7"

# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Give city name
cityName = "Sudbury"

# complete_url variable to store
# complete url address
complete_url = base_url + "appid=" + api_key + "&q=" + cityName

# get method of requests module
# return response object
response = requests.get(complete_url)

# json method of response object
# convert json format data into
# python format data
x = response.json()

# Now x contains list of nested dictionaries
# Check the value of "cod" key is equal to
# "404", means city is found otherwise,
# city is not found
if x["cod"] != "404":

    # store the value of "main"
    # key in variable y
    y = x["main"]

    # store the value corresponding
    # to the "temp" key of y
    current_temperature = y["temp"]

    # store the value corresponding
    # to the "pressure" key of y
    current_pressure = y["pressure"]

    # store the value corresponding
    # to the "humidity" key of y
    current_humidity = y["humidity"]


else:
    print(" City Not Found ")


#typpecast float to string

temp = str(current_temperature)
press = str(current_pressure)
hum = str(current_humidity)



#create server for email

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('dummy12email24@gmail.com','Geraltofrivia@123')

email = EmailMessage()

#darft a message in email
email['From'] = 'dummy12email24@gmail.com'
email['To'] =  'mananparekh0188@yahoo.com'
email['subject'] = 'Daily Digest'

#pass the random fact in set cotent
email.set_content("Your Fact!!!"+"\n\n" + fact + "\n"+"\n"+"Your Quote!!!"+"\n\n"+qt + "\n" + "Today's Weather!!!!" +"\n"+"\n"+"\n"+ "Temperrature" + "\n" +temp+"K"+"\n"+"Pressure"+"\n"+press+"Pa"+"\n"+"humidity"+"\n"+hum)


#email.set_content(qt)


#send mail to users
server.send_message(email)
