class Node:
    def __init__(self):
    	# label: name of attribute for splitting
        self.label = None
        self.children = {}
	# you may want to add additional fields here...

	def set_label(self, label):
		self.label = label

	def get_label(self):
		return self.label

	def get_children(self):
		return self.children

	# attribute value + child node
	def add_children(self, attribute_val, child):
		self.children[attribute_val] = child

