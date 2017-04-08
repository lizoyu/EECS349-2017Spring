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
  	for item in examples:
  		if item["Class"]!=examples[0]["Class"]:
  			flag = 1
  			break 
  	if not flag:
  		c2 = examples[0]["Class"]
    	return c2
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
  split={}
  for i in examples:
  	temp = i.get(location)
  	del i[location]
  	if temp not in split:
  		split[temp]=[i]
  	else:
  		split[temp].append(i)
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


def test(node, examples):
  '''
  Takes in a trained tree and a test set of examples.  Returns the accuracy (fraction
  of examples the tree classifies correctly).
  '''
  total=0
  for i in examples:
  	root = node
  	while root.get_children() :
  		root = root.get_children().get(i[root.get_label()])
  	if root["Class"]==i["Class"]:
  		total+=1
  return total*1.0/len(examples)

def evaluate(node, example):
  '''
  Takes in a tree and one example.  Returns the Class value that the tree
  assigns to the example.
  '''
