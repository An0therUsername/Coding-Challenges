#Exercise 22 (and Solution)
'''
Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file, and print out the results to the screen. I have a .txt file for you, if you want to use it!

Extra:

Instead of using the .txt file from above (or instead of, if you want the challenge), take this .txt file, and count how many of each “category” of each image there are. This text file is actually a list of files corresponding to the SUN database scene recognition database, and lists the file directory hierarchy for the images. Once you take a look at the first line or two of the file, it will be clear which part represents the scene category. To do this, you’re going to have to remember a bit about string parsing in Python 3. I talked a little bit about it in this post.'''

#Main

filename = '#22 - nameslist.txt'
count = 0

with open(filename, 'r') as fileobj:
	names = []
	for line in fileobj:
		line = line.rstrip('\n')
		if line not in names:
			names.append(line)
		count += 1

print('Total lines in file: ' + str(count))
print('Total unique names: ' + str(len(names)))
print('Names: ' + str(names))

#Extra

print('\nExtra:\n')

from collections import Counter

extra_file = '#22 - Training_01.txt'

with open(extra_file, 'r') as f:
	all_categories = []
	dict = []
	for line in f:
		line = line.rstrip('\n')
		all_categories.append(line.split('/')[2])

	for key, value in Counter(all_categories).items():
		print(key.title() + ':\t' + str(value))

