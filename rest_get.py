#!/usr/bin/env python2
import requests
import json
import _mysql

def getFromAPI():

	print 'API connection example'

	url = "http://api.duckduckgo.com/"
	payload = {'q':'chandra','format':'json'}

	r = requests.get(url,params = payload)

	if r.ok:
		jData = json.loads(r.content.decode("utf-8")) # content is in bytes => to string => json (dictionary)
	
		print type(jData) #dictionary

		#print(format(len(jData))+"\n")

		for key in jData:
			print key+" : " + format(jData[key])

	else:
		r.raise_for_status()


def getFromDB():

	print('mysql example')

	db_server = 'http://mysql14.000webhost.com/'
	user_name = 'a1313712_root'
	password = 'praneeth0875'
	db_name = 'a1313712_stock'

	db = _mysql.connect(host = db_server,user = user_name,passwd = password,db = db_name)

	cursor = db.execute('select * from sample')
	data = cursor.fetchall()

	for row in data:
		print row[0]+" "+row[1]+" "+row[2]+" "+row[3]+" "+row[4]+" "

	cursor.close()
	db.close()

def main():

	getFromAPI()
	#		getFromDB()

if __name__ == '__main__':
	main()
