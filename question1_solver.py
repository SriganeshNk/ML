import re, math

class Question1_Solver:
	def __init__(self):
		self.demo_dist = []
		self.rep_dist = []
		self.learn('train.data');
		return;
	# Add your code here.
	# Read training data and build your decision tree
	# Store the decision tree in this class
	# This function runs only once when initializing
	# Please read and only read train_data: 'train.data'
	def learn(self, train_data):
		data = []
		demo_count = []
		rep_count = []
		intance = []
		votes = []
		congress = []
		democrat, republican = 0, 0
		with open(train_data, 'r') as f:
			data = f.read().splitlines()
		for d in data:
			instance = d.split('\t')
			congress.append(instance[0])
			votes.append(instance[1].split(','))
		[demo_count.append((0,0,0)) for i in votes[0]]
		[rep_count.append((0,0,0)) for i in votes[0]]
		for i in range(len(votes)):
			if congress[i] == 'democrat':
				democrat += 1
			if congress[i] == 'republican':
				republican += 1
			for j in range(len(votes[i])):
				if votes[i][j] == 'y':
					if congress[i] == 'democrat':
						demo_count[j] = (demo_count[j][0]+1, demo_count[j][1], demo_count[j][2])
					if congress[i] == 'republican':
						rep_count[j] = (rep_count[j][0]+1, rep_count[j][1], rep_count[j][2])
				if votes[i][j] == 'n':
					if congress[i] == 'democrat':
						demo_count[j] = (demo_count[j][0], demo_count[j][1]+1, demo_count[j][2])
					if congress[i] == 'republican':
						rep_count[j] = (rep_count[j][0], rep_count[j][1]+1, rep_count[j][2])
				if votes[i][j] == '?':
					if congress[i] == 'democrat':
						demo_count[j] = (demo_count[j][0], demo_count[j][1], demo_count[j][2]+1)
					if congress[i] == 'republican':
						rep_count[j] = (rep_count[j][0], rep_count[j][1], rep_count[j][2]+1)
		for i in range(len(demo_count)):
			self.demo_dist.append((float(demo_count[i][0])/float(democrat), float(demo_count[i][1])/float(democrat), float(demo_count[i][2])/float(democrat)))
			self.rep_dist.append((float(rep_count[i][0])/float(republican), float(rep_count[i][1])/float(republican),float(rep_count[i][2])/float(republican)))
		return
	
	# Add your code here.
	# Use the learned decision tree to predict
	# query example: 'n,y,n,y,y,y,n,n,n,y,?,y,y,y,n,y'
	# return 'republican' or 'republican'
	def solve(self, query):
		choice = str()
		control = 0
		attributes = query.split(',')
		for i in range(len(attributes)):
			if attributes[i] == 'y' and self.demo_dist[i][0] < self.rep_dist[i][0]:
				control -= 1
			if attributes[i] == 'n'  and self.demo_dist[i][1] < self.rep_dist[i][1]:
				control -= 1
			if attributes[i] == '?'  and self.demo_dist[i][2] < self.rep_dist[i][2]:
				control -= 1
			if attributes[i] == 'y' and self.demo_dist[i][0] > self.rep_dist[i][0]:
				control += 1
			if attributes[i] == 'n'  and self.demo_dist[i][1] > self.rep_dist[i][1]:
				control += 1		
			if attributes[i] == '?'  and self.demo_dist[i][2] > self.rep_dist[i][2]:
				control += 1
		if control > 0:
			choice = 'democrat'
		else:
			choice = 'republican'
		return choice
