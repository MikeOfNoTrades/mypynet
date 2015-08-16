import yaml, json
from pprint import pprint as pp

with open("my_list.yml") as f:
	my_yaml_list = yaml.load(f)

with open("my_list.json") as f:
	my_json_list = json.load(f)

print "yaml: ", my_yaml_list
print "json: ", my_json_list

print "yaml: \n"
print "-----------------------------------\n"
pp(my_yaml_list)
print"\n"
print "json: \n"
print "-----------------------------------\n"
pp(my_json_list)
print"\n"
