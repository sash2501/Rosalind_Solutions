# Problem Given: Two positive integers a and b (a<b<10000).

# Return: The sum of all odd integers from a through b, inclusively.

start = 4892
stop = 9603
tsum = 0
for i in range(start, stop+1):
	if i% 2 == 1:
		tsum = tsum + i
print(tsum)

# output= 17076288
