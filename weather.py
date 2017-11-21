# Make sure to pip install BeautifulSoup4

# import libraries
import urllib2
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import time

# Asks for your name and says hello
your_name = input("What is your name?(Use quotation marks) ")
print ("Hello " + your_name)
time.sleep(2)
print "Welcome to the Portland Weather Monitoring Program"
time.sleep(2)

# Asks for how many times a day for how many days the program will run
days = input("How many days do you want the program to run for(Cannot = 0)? ")
times_per_day = input("How many times a day?(Cannot = 0) ")
counter = times_per_day * days 

def monitor():
	# specify the url
	weather_page = 'https://weather.com/weather/today/l/USOR0275:1:US'

	# query the website and return the html to the variable 'page'
	page = urllib2.urlopen(weather_page)
	
	# parse the html using beautiful soup and store in cariable 'soup'
	soup = BeautifulSoup(page, 'html.parser')
	
	#Take out the <div> of name and get its value
	temp_box = soup.find('div', attrs={'class': 'today_nowcard-temp'})
	temp = temp_box.text.strip() # strip () is used to remove starting and trialing
	print temp
	
#	with open ('index.csv', 'a') as csv_file:
#		writer = csv.writer(csv_file)
#		writer.writerow([temp, datetime.now()])
	
	# Stops the program for x amount of seconds
	time.sleep(86400 / times_per_day) 
	
while True:
	if (counter == 0):
		break
	else: 
		monitor()
		counter -= 1

# The line 39 doesn't work. I believe it is because of the degree character from 'temp'