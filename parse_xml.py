import xml.etree.ElementTree as ET
import time
import sys


tree = ET.parse('curated_dataset copy.xml')
root = tree.getroot()

# ET.dump(root)



# stats we want:
#  - avg_convo_length
#  - avg_users_per_convo
#  - avg_post_per_user
#  - avg_OP_responses




# for neighbour in root.iter():
# 	print neighbour.tag, neighbour.get('uid'), neighbour.text



def extract(root):

	convo_lengths = []
	convo_users = []
	OP_scores = []
	# V2_validation = []

	index = 0
	for n1 in root.iter():
		# for each <s> (conversation)
		if n1.tag == 's':
			index += 1
			count_length = 0
			count_users = 0
			OP_score = 0

			# for each <utt> (post)
			for n2 in n1.iter():
				if n2.tag == 'utt':
					count_length+=1
					# count users
					if int(n2.get('uid')) > count_users:
						count_users = int(n2.get('uid'))
					# get OP score
					if count_users == 1 and int(n2.get('uid')) == 1:
						OP_score = int(n2.get('score'))
			# update stats
			convo_lengths.append(count_length)
			convo_users.append(count_users)
			OP_scores.append(OP_score)

	return [convo_lengths, convo_users, OP_scores]
			
def analysis(data):
	avg_convo_length = float(sum(data[0])/len(data[0]))
	avg_users_per_convo = float(sum(data[1])/len(data[1]))
	avg_OP_score = float(sum(data[2])/len(data[2]))
	return [avg_convo_length, avg_users_per_convo, avg_OP_score]

print analysis(extract(root))
 