import yaml, json
#import json

mylist = [{'format1': 'yaml', 'format2':'json'},  { 'platform1': 'cisco',  'platform2':'juniper', 'platform3':'brocade' }]
#print "mylist: ", mylist
#print "yaml dump: \n", yaml.dump(mylist)
#print "condensed yaml dump: \n", yaml.dump(mylist, default_flow_style=True)
#print "non-condensed yaml dump: \n", yaml.dump(mylist, default_flow_style=False)


with open("my_list.yml", "w") as f:
	f.write("---\n")

with open("my_list.yml", "a") as f:
	f.write( yaml.dump(mylist, default_flow_style=False))

print json.dumps(mylist)

with open("my_list.json", "w") as f:
	json.dump(mylist, f)
