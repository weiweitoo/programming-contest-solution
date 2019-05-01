count = int(input())
for i in range(count):
	# Update here
	N = input()
	A = int(N.replace("4","3"))
	print("Case #{0}: {1} {2}".format(i+1,A,int(N)-A))
