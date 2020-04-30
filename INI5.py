# Problem Given: A file containing at most 1000 lines.

# Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.


f = open("Data/rosalind_ini5.txt", "r")
output = open("Output/exercise_INI5.txt", "w")
i = 1

for line in f.readlines():
	if i % 2 == 0:
		output.write(line)
	i = i + 1
