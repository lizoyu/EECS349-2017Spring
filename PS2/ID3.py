from node import Node
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
  elif not (item for item in examples if item["Class"] != examples[0]["Class"]).next():
    return examples[0]["Class"]
  max = sys.minint
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
   		p = i/len(examples)
   		entropy += math.log2(p)*p
   	if entropy < min:
   		min = entropy
   		location = attr
   	if entropy > max:
   		max = entropy
  if min == max:
  	c={}
  	if i.get("class") in examples:
  		
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


def evaluate(node, example):
  '''
  Takes in a tree and one example.  Returns the Class value that the tree
  assigns to the example.
  '''
