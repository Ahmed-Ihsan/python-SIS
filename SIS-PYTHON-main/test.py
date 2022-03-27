class node():
	def __init__(self,val):
		self.data=val
		self.next=None

class linklist():
	def __init__(self):
		self.head=None

	def add(self,val):
		new = node(val)
		new.next = self.head
		self.head = new
		del new

	def isEmpty(self):
		return not(self.head is None)

	def print(self):
		pr=self.head
		while self.isEmpty() :
			if not (pr.next is None):
				print(pr.data ,end=" - ")
				pr=pr.next
			else:
				print(pr.data)
				del pr
				break

	def addIndex(self,indax,val):
		first_node=self.head
		for _ in range(0,indax+1):
			if not (first_node.next is None):
				first_node=first_node.next
			else:
				print("noue")
				del new , first_node

	def pop(self):
		dele=self.head
		self.head=dele.next
		del dele

	def remov_all(self):
		re=self.head
		while self.isEmpty():
			if not (re.next is None):
				self.pop()
				re=self.head
			else:
				self.pop()
				self.head=None
				del re
				break

	def ATend(self,val):
		first_node=self.head
		while True:
			if not (first_node.next is None):
				first_node=first_node.next
			else:
				new = node(val)
				first_node.next = new
				del new , first_node
				break

q= linklist()
q.add(5)
q.add('ahmed')
q.add([1,2,3,4,5,6])
q.print()
q.pop()
q.print()
q.add([1,2,3,4,5,6])
q.print()
q.ATend("ali")
q.print()
q.pop()
q.print()
q.remov_all()
q.print()
q.add('ahmed')
q.add([1,2,3,4,5,6])
q.print()
print(q.isEmpty())