#### For the departments of the IIT bombay
department = { "cse" : "Computer Science and Engineering",
				"ee" : "Electrical Engineering",
				"aero" :"Aerospace engineering",
				"bios":"Biosciences and Bioengineering",
				"che": "Chemical Engineering",
				"chem":"chemistry",
				"geos":"Earth sciences",
				"es":	"energy sciences",
				"hss":"Humanities and social science",
				"idc": "Industrial Design center",
				"phy": "physics",
				"met": "Metallurigcal engineering",
				"oth": "Other",
				 "me":  "mechanical", 
			}
def get_dept(dept):
	if dept in department.keys():
		return department.get(dept)
	else:
		return "unknown"

