class Node:
	def __init__(self):
    	# label: name of attribute for splitting
		self.label = None
		self.children = {}
		self.isBottom = False
		self.isChecked = False

	def set_label(self, label):
		self.label = label

	def get_label(self):
		return self.label

	def get_children(self):
		return self.children

	# attribute value + child node
	def add_children(self, attribute_val, child):
		self.children[attribute_val] = child

def tester():
	a = Node()
	b = Node()
	a.set_label('y')
	a.add_children('y',b)
	print a.get_children()
	a.set_label('do the test')
	print a.get_label()

tester()