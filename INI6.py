# Problem Given: A string s of length at most 10000 letters.

# Return: The number of occurrences of each word in s, where words are separated by spaces. Words are case-sensitive, and the lines in the output can be in any order.

string = 'abc'
word_counts = {}
for s in string.split():
    word_counts[s] = word_counts.get(s,0) + 1

for w in word_counts:
    print w, word_counts[w]
