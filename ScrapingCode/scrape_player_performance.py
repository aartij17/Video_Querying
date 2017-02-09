'''
See the schema for batsmen and bowler table in schema.txt
'''

from __future__ import print_function
import csv
import requests
from bs4 import BeautifulSoup


start = 419106
for count in range(5):
	url = "http://www.espncricinfo.com/ipl2010/engine/match/"+str(start)+".html"
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')
	#print(soup.prettify().encode('utf-8', 'ignore'))

	with open("batsmen_performance.csv","a") as f:
		writer = csv.writer(f)
		#Batsmen Info
		batsman_table = soup.find_all('table',class_='batting-table innings')
		for i in batsman_table:
			for row in i.find_all('tr',class_=""):
				data = row.find_all('td')
				writer.writerow(["IPL_2010_"+str(count+1),data[1].get_text().encode('utf-8', 'ignore'), data[3].get_text(),data[4].get_text(), data[5].get_text(), data[6].get_text(),data[7].get_text()])

	
	with open("bowler_performance.csv","a") as f:
		writer = csv.writer(f)
		#Bowler Info
		bowler_data = soup.find_all('td',class_="bowler-name")
		for i in bowler_data:
			row =  i.parent
			data = row.find_all('td')
			writer.writerow(["IPL_2010_"+str(count+1),data[1].get_text(), data[2].get_text(),data[3].get_text(), data[4].get_text(),data[5].get_text(),data[6].get_text(), data[7].get_text(),data[8].get_text(), data[9].get_text()])

	start +=1
	
	
'''
import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()
# Create table
c.execute("CREATE TABLE batsmen_performance
             (Match_No text, Name text, Runs integer, Balls integer, Fours integer, Sixes integer, SR real)")

# Create table
c.execute("CREATE TABLE bowler_performance
             (Match_No text, Name text, Overs integer, Maiden integer, Runs integer, Wickets integer, Economy real, Zeroes integer, Fours integer, Sixes integer)")
             
# Insert a row of data
c.execute("INSERT INTO batsmen_performance VALUES ()",entry)

# Save (commit) the changes
conn.commit()
'''
