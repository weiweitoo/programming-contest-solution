count = int(input())
for i in range(count):
	# Update here
	size = input()
	lydia = input()
	lydia = lydia.replace("S","T")
	lydia = lydia.replace("E","S")
	lydia = lydia.replace("T","E")
	print("Case #{0}: {1}".format(i+1,lydia))