from ciscoconfparse import CiscoConfParse
import re

cisco_cfg = CiscoConfParse("cisco_ipsec.txt")

crypt_map = cisco_cfg.find_objects(r"^crypto map CRYPTO")

for i in crypt_map: 
	print i.text 
	for child in i.children:
		print child.text

print "\nPFS Groups\n"
pfs_groups = cisco_cfg.find_objects(r"pfs group2")
for i in pfs_groups: 
	print i.parent
	print i.text 

print "\nTransform Sets\n"
#transform_sets = cisco_cfg.find_objects(r"transform-set")
#for i in transform_sets: 
	#print i.parent
	#print i.text 

trans_sets = list()
for obj in crypt_map:
	if obj.re_search_children(r"transform-set 3DES"):
		trans_sets.append(obj)
for i in trans_sets:
	print i

print "\nTransform Sets 2\n"

noAES = cisco_cfg.find_objects_wo_child(parentspec=r"^crypto map CRYPTO", childspec=r"transform-set AES")
for i in noAES:
	print i
	pattern = ("transform-set")
	for child in i.children:
		if re.search(pattern, child.text):
			print child

