import json
import csv
with open(r'followers.csv', 'a') as f:
	writer = csv.writer(f)
	with open('data.json') as data_file:    
	    data = json.load(data_file)
	    for node in data["data"]["user"]["edge_followed_by"]["edges"]:
	    	writer.writerow([node["node"]["username"]])
