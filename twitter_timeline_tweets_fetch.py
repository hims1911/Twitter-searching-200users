# twitter-user-search
#  - performs a search for users matching a certain query

from twitter import *
import sys
import config

# Creating twitter API object for initialising username in python")
twitter = Twitter(auth = OAuth(config.access_key,
                  config.access_secret,
                  config.consumer_key,
                  config.consumer_secret))
## fetching the data from twitter timeline about the developers into the dictonary
dict1 = {}
ab = open("status.txt","w")

for i in range(1,2):
	results = twitter.users.search(q = '"Blockchain developer"',page = i)
	for user in results:
		dict1[user["screen_name"]] = user["location"]
		string1 = user["screen_name"]
		result1 = twitter.statuses.user_timeline(screen_name = string1)
		for status in result1:
			hims = "(%s) %s" % (status["created_at"], status["text"].encode("ascii", "ignore"))
			ab.write(hims + "\n")
		ab.write("----------------------------------------------------------------------------------------------\n")	


## importing csv 
csv = open("RanchiMallCsv1.csv","wb")
columnTitleRow = b"handle_name,location\n"
csv.write(columnTitleRow)


for key in dict1.keys():
	encoded = key.encode('utf-8')
	handle_name = encoded
	encoded1 = dict1[key].encode("utf-8")
	location = encoded1
	row = handle_name + b"," + location + b"\n"
	csv.write(row)