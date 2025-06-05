
class Table:
	rows = list()
	sizeofcolumns = 0

	def __init__(self, name="", columns=[]):
		self.name = name
		self.columns = columns
		self.sizeofcolumns = len(columns)

	def __str__(self):
		string  = f"Name: {self.name}\nTable:\n"
		for i in self.columns:
			string += f"{i}\t"
		string += f"\n"
		for i in self.rows:
			for j in i:
				string += f"{j}\t"
			string += f"\n"
		return string
	
	def push(self, row: list):
		if len(row) != self.sizeofcolumns:
			raise Exception("Different size")
		else:
			self.rows.append(row)
	
	def pop(self, index=-1):
		return self.rows.pop(index)

	# Name commands
	def get_name(self):
		return self.name
	
	def set_name(self, name):
		self.name = name
	
	# Row commands
	def get_row(self, index):
		return self.rows[index]

	def get_rows(self):
		return self.rows
	
	def set_row(self, index, row):
		self.rows[index] = row
	
	def set_rows(self, rows):
		self.rows = rows
	
	# Column commands
	def get_column(self, index):
		return self.columns[index]
	
	def get_columns(self):
		return self.columns

	def set_column(self, index, column):
		self.columns[index] = column

	def set_columns(self, columns):
		self.columns = columns

	# Size commands
	def get_sizeofcolumns(self):
		return self.sizeofcolumns

	# Table commands
	def union(self, table: Table):
		for i in table.rows:
			if i not in self.rows:
				self.rows.append(i)
	
	def intersection(self, table):
		for i in table.rows:
			if i in self.rows:
				self.rows.remove(i)