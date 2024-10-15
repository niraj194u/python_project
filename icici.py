#icici.py--File Name and acts as modules Name
bname="ICICI"
addr="HYD"  # Global Varaibles
def  calsimpmeint():  # Function Defintions
	p=float(input("Enter Principle Amount:"))
	t=float(input("Enter Time:"))
	r=float(input("Enter Rate of Interest:"))
	#Cal si
	si=(p*t*r)/100
	totamt=p+si
	print("-"*50)
	print("\tSimple Interest Cal")
	print("-"*50)
	print("\tPrinciple Amount:{}".format(p))
	print("\tTime:{}".format(t))
	print("\tRate of Interest:{}".format(r))
	print("\tSimple Interest:{}".format(si))
	print("\tTotal Amount to Pay:{}".format(totamt))
	print("-"*50)