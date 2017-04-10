from node import Node
import sys
import math

def ID3(examples, default):
  '''
  Takes in an array of examples, and returns a tree (an instance of Node) 
  trained on the examples.  Each example is a dictionary of attribute:value pairs,
  and the target class variable is a special attribute with the name "Class".
  Any missing attributes are denoted with a value of "?"
  '''
  if not examples:
  	return default
  else:
  	flag = 0
  	c2 = examples[0]["Class"]
  	for item in examples:
  		if item["Class"]!=examples[0]["Class"]:
  			flag = 1
  			break 
  	if not flag:
  		return c2

  # compute entropy and choose the smallest
  max1 = -sys.maxint-1
  min = sys.maxint
  location=""
  for attr in examples[0].keys():
   	sum = {}
   	for i in examples:
   		if i.get(attr) not in sum:
   			sum[i.get(attr)] = 0
   		sum[i.get(attr)] += 1
   	entropy = 0
   	for i in sum.values():
   		p = i*1.0/len(examples)
   		entropy += math.log(p,2)*p
   	if entropy < min:
   		min = entropy
   		location = attr
   	if entropy > max1:
   		max1 = entropy
  if min == max1:
  	c={}
  	for i in examples:
  		if i.get("Class") not in c:
  			c[i.get("Class")] = 0
  		c[i.get("Class")] += 1
  	return max(c, key = c.get)

  # split the data and create the nodes
  split={}
  for i in examples:
  	temp = i.get(location)
  	temp2 = i.copy()
  	del temp2[location]
  	if temp not in split:
  		split[temp]=[temp2]
  	else:
  		split[temp].append(temp2)
  root = Node()
  root.set_label(location)
  for i in split.keys():
  	child = Node()
  	root.add_children(i,ID3(split.get(i),default))
  return root

def prune(node, examples):
  '''
  Takes in a trained tree and a validation set of examples.  Prunes nodes in order
  to improve accuracy on the validation data; the precise pruning strategy is up to you.
  '''

  # get all the parent nodes of leaves
  update=1.0
  previous = self.test(node,examples)
  while update>0:
  	root = node.copy()
  	while root.get_children():
  		dic = root.get_children()
  		parent = root
  		root = dic.get(i[root.get_label()])
  		if not isinstance(root,Node):
  			break




def test(node, examples):
  '''
  Takes in a trained tree and a test set of examples.  Returns the accuracy (fraction
  of examples the tree classifies correctly).
  '''
  total=0
  for i in examples:
  	root = node
  	while root.get_children() :
  		dic = root.get_children()
  		root = dic.get(i[root.get_label()])
  		if not isinstance(root,Node) :
  			break
  	if root==i["Class"]:
  		total+=1
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
  	if not isinstance(root,Node) :
  		break
  return root