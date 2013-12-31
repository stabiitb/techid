from misc.models import *
import re
def loaddata_skills():
	f = open("./fixtures/skill.txt","r")
	l = f.readlines()
	for i in l:
		i = i.strip()
		k = i.split(",")
		print k
		a=Skill(name=k[1].strip(),short_name=k[2].strip())
		a.save()

loaddata_skills()