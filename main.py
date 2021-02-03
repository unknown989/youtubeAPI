from youtubesearchpython import ChannelsSearch
import argparse
import json

def csn(x):
	nmap = {"K":1000,"M":1000000}
	x = str(x)
	if x[-1] in nmap.keys(): 
		s = nmap.get(x[-1])
		return int(float(x.replace(x[-1],""))*s)
	else:
		return int(x)

ap = argparse.ArgumentParser()
ap.add_argument("-q","--query",required=True,help="Query to search for a channel")
ap.add_argument("-l","--limit",required=True,help="Limit The search results")
ap.add_argument("-s","--subscribers",required=False,help="(Optional) Subscribers count filter by ,default 500K")
args = vars(ap.parse_args())
subf = (500000 if not args["subscribers"] else int(args["subscribers"]))

allSearch = ChannelsSearch(str(args["query"]), limit = int(args["limit"]))

with open("test.json","w") as f:
	f.write(json.dumps(allSearch.result()))

for i in allSearch.result()["result"]:
	subs = csn(i["subscribers"].replace("subscribers","").replace(" ",""))
	try:
		if subs >= subf:
			print(i["title"])
		else:
			pass
	except Exception as e:
		print("|>"+str(e))
		print(i["id"])
		print(i["title"])
		print(i["type"])
		print(i["subscribers"])
		print("<|")

