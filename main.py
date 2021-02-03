from youtubesearchpython import ChannelsSearch
import argparse
import json

# Algorithm to Transform a string to int (10K to 10000)
def csn(x):
	nmap = {"K":1000,"M":1000000}
	x = str(x)
	if x[-1] in nmap.keys(): 
		s = nmap.get(x[-1])
		return int(float(x.replace(x[-1],""))*s)
	else:
		return int(x)

# Parsing Arguments
ap = argparse.ArgumentParser()
# Adding arguments to the Parser
ap.add_argument("-q","--query",required=True,help="Query to search for a channel")
ap.add_argument("-l","--limit",required=True,help="Limit The search results")
ap.add_argument("-s","--subscribers",required=False,help="(Optional) Subscribers count filter by ,default 500K")
# Initialize Arguments tot args
args = vars(ap.parse_args())
# Load Subscribers Filter to 500K if the user didn't provide it ,if he/she did it will transform it to an integer
subf = (500000 if not args["subscribers"] else int(args["subscribers"]))

# Search Channels using the Query and The Limit arguments
allSearch = ChannelsSearch(str(args["query"]), limit = int(args["limit"]))

# Main Loop
for i in allSearch.result()["result"]:
	# Getting the subscribers count to filter with
	subs = csn(i["subscribers"].replace("subscribers","").replace(" ",""))
	try:
		# Checking if subscribers is greater than subscribers count 
		if subs >= subf:
			desc = list()
			for o in i["descriptionSnippet"]:
				desc.append(o["text"])
			print(desc)
			print("="*50)
			print("Channel ID : "+i["id"])
			print("Channel Name : "+i["title"])
			print("Channel Subscribers : "+i["subscribers"])
			print("Channel Videos Count : "+i["videoCount"])
			print("Channel Description : "+" ".join(desc))
			print("Channel Link : "+i["link"])
		else:
			pass
	except Exception as e:
		# Exception Handling , prints id ,title,type,subs
		print("|>"+str(e))
		print(i["id"])
		print(i["title"])
		print(i["type"])
		print(i["subscribers"])
		print("<|")
