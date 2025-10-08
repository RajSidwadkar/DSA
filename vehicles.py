def vehicles(v, w) :
	if v<=0 or w< 2 or w%2 != 0 or w < 2*v or w > 4*v :
		print("Invalid Input")

	else :
		fw = (w - v*2)//2
		tw = v - fw
		print("No. of fourwheelers =", fw, "\nNo. of twowheelers =", tw )
v = int(input("Enter number of vehicles:"))
w = int(input("Enter number of wheels:"))
vehicles(v,w)
