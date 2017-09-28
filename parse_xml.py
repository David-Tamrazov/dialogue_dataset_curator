import xml.etree.ElementTree as ET
import time
import sys


tree = ET.parse('curated_dataset13000.xml')
root = tree.getroot()

# ET.dump(root)



# stats we want:
#  - avg_convo_length
#  - avg_users_per_convo
#  - avg_post_per_user
#  - avg_OP_responses
#  - avg_liked_posts_per_convo
#  - avg_words_per_convo
#  - avg_words_per_utt


# for neighbour in root.iter():
# 	print neighbour.tag, neighbour.get('uid'), neighbour.text



def extract(root):

	convo_lengths = []
	convo_users = []
	convo_liked_posts = [] # not including posts by OP
	OP_scores = []
	# V2_validation = []

	index = 0
	for n1 in root.iter():
		# for each <s> (conversation)
		if n1.tag == 's':
			count_length = 0
			count_users = 0
			count_liked = 0
			OP_score = 0
			posts_per_user = {}

			# for each <utt> (post)
			for n2 in n1.iter():
				if n2.tag == 'utt':
					count_length+=1
					# count users
					if int(n2.get('uid')) > count_users:
						count_users = int(n2.get('uid'))
					# get OP score
					# if count_users == 1 and int(n2.get('uid')) == 1:
					# 	OP_score = int(n2.get('score'))
					# count posts w/ > 0 likes
					# elif int(n2.get('uid')) != 1 and int(n2.get('score')) > 0:
					# 	count_liked += 1
					# count posts_per_user
					# for x in xrange(1,count_users):

						# posts_per_user[x] += 1

			# update stats
			convo_lengths.append(count_length)
			convo_users.append(count_users)
			convo_liked_posts.append(count_liked)
			OP_scores.append(OP_score)
			

	return [convo_lengths, convo_users, OP_scores, convo_liked_posts]
			
def analysis(data):
	avg_convo_length = float(sum(data[0]))/float(len(data[0]))
	avg_users_per_convo = float(sum(data[1]))/float(len(data[1]))
	avg_liked_posts_per_convo = float(sum(data[2]))/float(len(data[2]))
	avg_OP_score = float(sum(data[3]))/float(len(data[3]))

	return {
		"avg_convo_length": avg_convo_length,
		"avg_users_per_convo": avg_users_per_convo,
		"avg_OP_score": avg_OP_score,
		"avg_liked_posts_per_convo": avg_liked_posts_per_convo
		}

print analysis(extract(root))
 