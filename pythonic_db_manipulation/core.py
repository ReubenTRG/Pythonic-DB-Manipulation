
class Table:
	rows: list[list] = list()
	columns: list = list()

	def __init__(self, name="", columns=[]):
		self.name = name
		self.columns = columns

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
	def get_rows(self):
		return self.rows
	
	def set_row(self, index, row):
		self.rows[index] = row
	
	def row_exists(self, row):
		return row in self.rows

	def remove(self, row):
		self.rows.remove(row)

	def __getitem__(self, index: int):
		return self.rows[index]

	def __setitem__(self, index, row):
		self.rows[index] = row

	def __del__(self):
		self.rows = []

	def __delitem__(self, index):
		del self.rows[index]
	
	def __len__(self):
		return len(self.rows)

	def __iter__(self):
		return iter(self.rows)

	# Column commands
	def get_columns(self):
		return self.columns

	def set_column(self, index, column):
		self.columns[index] = column

	def column_exists(self, column):
		return column in self.columns

	# Table commands
	def union(self, table: "Table"):
		result = Table()
		result.columns = self.columns.copy() + list(set(table.columns) - set(self.columns))
		
	
	def intersection(self, table: "Table"):
		for i in table.rows:
			if i in self.rows:
				self.rows.remove(i)
	
	def difference(self, table: "Table"):
		for i in table.rows:
			if i in self.rows:
				self.rows.remove(i)