
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
# searching usernames with bio as BlockChain developer
dict1 = {}

for i in range(1,11):
	results = twitter.users.search(q = '"Blockchain developer"',page = i)
	for user in results:
		dict1[user["screen_name"]] = user["location"]


csv = open("RanchiMallCsv.csv","wb")
columnTitleRow = b"handle_name,location\n"
csv.write(columnTitleRow)

# storing the handle name and location in the dictonary


# getting data from dictonary to csv
for key in dict1.keys():
	encoded = key.encode('utf-8')
	handle_name = encoded
	encoded1 = dict1[key].encode("utf-8")
	location = encoded1
	row = handle_name + b"," + location + b"\n"
	csv.write(row)

