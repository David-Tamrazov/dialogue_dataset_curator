import xml.etree.ElementTree as ET
tree = ET.parse('curated_dataset.xml')
root = tree.getroot()

# ET.dump(root)




# for neighbour in root.iter():
# 	print neighbour.tag, neighbour.get('uid'), neighbour.text


def analytics(root):

	avg_convo_length = 0 # sum(convo_length)/nb_convos
	avg_OP_responses = 0 # #_op_utt/#_utt
	avg_post_per_user = 0

	for n1 in root.iter():
		if n1.tag == 's':
			convo_length = 0
			for n2 in n1.iter():
				if n2.tag == 'utt':
					convo_length+=1
			print convo_length
			

	


analytics(root)