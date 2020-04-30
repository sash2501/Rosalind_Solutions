#Problem Given: A string s of length at most 200 letters and four integers a, b, c and d.

#Return: The slice of this string from indices a through b and c through d (with space in between), inclusively. In other words, we should include elements s[b] and s[d] in our slice.

string = "TEC1QWX1l83Ytb0zBnxvhyRcTSH81pIgBV01JdIQ7G5Gzf1MStLBQbIfBlR3f7EeSTwEssYcJIEdESHCqGRlTursiopsMkn08DYNxNL3ShG9QANHdIBnTbSguuEen1xEBQa7eStevferrugineafqajt2rJk1Ac5TY47Q4l3xd6IV2fYi5uGPf"
a, b, c, d = 84 , 91 , 137 , 146
print(string[a:b+1], string[c:d+1])

# Output = Tursiops ferruginea

