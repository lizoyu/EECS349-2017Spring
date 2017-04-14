from node import Node
import sys
import math
import copy

def ID3(examples, default):
  '''
  Takes in an array of examples, and returns a tree (an instance of Node) 
  trained on the examples.  Each example is a dictionary of attribute:value pairs,
  and the target class variable is a special attribute with the name "Class".
  Any missing attributes are denoted with a value of "?"
  '''

  # when 'examples' is empty
  if not examples:
  	return default
  else:
  	# return the class if all the data have the same class
  	test_class = examples[0]['Class']
  	class_counter = 0
  	for item in examples:
  		if item['Class'] == test_class:
  			class_counter += 1
  	if class_counter == len(examples):
  		return test_class

  # compute entropy and choose the smallest
  max_entropy = -sys.maxint - 1
  min_entropy = sys.maxint
  label_class = ""
  for attr in examples[0].keys():
  	if attr != 'Class':
   		sum = {}
   		# count the appearance of attribute values 
   		for i in examples:
   			if i.get(attr) not in sum:
   				sum[i.get(attr)] = 0
   			sum[i.get(attr)] += 1
   		# compute the entropy
   		entropy = 0
   		for i in sum.values():
   			if i != 0:
   				p = i*1.0/len(examples)
   				entropy += math.log(p,2)*p
   		# choose the smallest one
   		if entropy < min_entropy:
   			min_entropy = entropy
   			label_class = attr
   		if entropy > max_entropy:
   			max_entropy = entropy
  	# when all data have the same attribute value, they have the same entropy,
  	# so minimum equals maximum, then we return the mode class
  	if min_entropy == 0 and min_entropy == max_entropy:
  		count = {}
  		for data in examples:
  			if data.get('Class') not in count:
  				count[data.get('Class')] = 0
  			count[data.get('Class')] += 1
  		return max(count, key = count.get)

  # split the data and create the root node with its children (nodes)
  split={}
  for data in examples:
  	temp = data.get(label_class)
  	temp2 = copy.deepcopy(data)
  	
  	del temp2[label_class]
  	# put data into different keys(attribute value)
  	if temp not in split:
  		split[temp]=[temp2]
  	else:
  		split[temp].append(temp2)
  # create the node with the label
  root = Node()
  root.set_label(label_class)
  # create the children for the node and add each child node from recursive ID3
  for attr_val in split.keys():
  	count = {}
  	for data in split.get(attr_val):
  		if data.get('Class') not in count:
  			count[data.get('Class')] = 0
  		count[data.get('Class')] += 1
  	root.add_children( attr_val, ID3(split.get(attr_val),max(count, key = count.get)) )

  return root

def prune(node, examples):
  '''
  Takes in a trained tree and a validation set of examples.  Prunes nodes in order
  to improve accuracy on the validation data; the precise pruning strategy is up to you.
  '''

  # keep until even the best one cannot improve accuracy
  while True:
    accuracy = test(node,examples)
    # get all the parent nodes of leaves
    parents = []
    queue = [node]
    while queue:
      parent = queue.pop(0)
      if isinstance(parent, Node):
        children = parent.get_children()
        leaf_counter = 0
        for child in children.values():
          if not isinstance(child, Node):
           leaf_counter += 1
          elif child.isChecked:
           leaf_counter += 1
          else:
           queue.append(child)
        if leaf_counter == len(children):
        	parent.isBottom = True
      parents.append(parent)

    # count the mode class for each parent node using validation sets
    class_counter = {}
    for parent in parents:
      class_counter[parent.get_label()] = {}
    for data in examples:
      root = node
      while not root.isBottom:
        children = root.get_children()
        root = children.get(data[root.get_label()])
        if not isinstance(root, Node):
        	break
      if isinstance(root, Node) and root.isChecked:
      	continue
      if isinstance(root, Node):
      	if data['Class'] not in class_counter[root.get_label()]:
        	class_counter[root.get_label()][data['Class']] = 0
      	class_counter[root.get_label()][data['Class']] += 1

    # compute the accuracy change and choose the best
    children_cutted = {}
    best_node = None
    best_acc = 0
    children_cut = {}
    for parent in parents:
    	children_cut = copy.deepcopy(parent.get_children())
    	mode = ""
    	num = 0
    	for Class, count in class_counter[parent.get_label()].items():
    		if count > num:
					mode = Class
					num = count
    	if num == 0:
    		continue
    	for key in parent.children.keys():
    		parent.children[key] = mode
    	delta_acc = test(node, examples) - accuracy
    	if delta_acc > best_acc:
    		best_acc = delta_acc
    		if best_node:
    			best_node.children = children_cutted
    		best_node = parent
    		children_cutted = children_cut
    	else:
    		parent.children = children_cut
    if best_node:
    	best_node.isChecked = True
    if best_acc <= 0.01:
    	if best_node:
    		best_node.children = children_cutted
    	break

def test(node, examples):
  '''
  Takes in a trained tree and a test set of examples.  Returns the accuracy (fraction
  of examples the tree classifies correctly).
  '''
  total = 0
  for i in examples:
  	root = node
  	if not isinstance(root,Node):
  		return root
  	while root.get_children():
  		dic = root.get_children()
  		root = dic.get(i[root.get_label()])
  		if not isinstance(root,Node):
  			break
  	if root == i["Class"]:
  		total += 1
  return total*1.0/len(examples)

def evaluate(node, example):
  '''
  Takes in a tree and one example.  Returns the Class value that the tree
  assigns to the example.
  '''
  root = node
  if not isinstance(root,Node):
  	return root
  while root.get_children() :
  	dic = root.get_children()
  	root = dic.get(example[root.get_label()])
  	if not isinstance(root,Node):
  		break
  return root