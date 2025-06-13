class Table:
    def __init__(self, name="", columns=None, rows=None):
        self.name = name
        self.columns = columns if columns is not None else []
        self.rows = rows if rows is not None else []

    def __str__(self):
        string = f"Name: {self.name}\nTable:\n"
        string += "\t".join(self.columns) + "\n"
        for row in self.rows:
            string += "\t".join(str(cell) for cell in row) + "\n"
        return string

    def push(self, row: list):
        if len(row) != len(self.columns):
            raise ValueError("Row length must match number of columns")
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
        if len(row) != len(self.columns):
            raise ValueError("Row length must match number of columns")
        self.rows[index] = row

    def row_exists(self, row):
        return row in self.rows

    def remove(self, row):
        self.rows.remove(row)

    def __getitem__(self, index: int):
        return self.rows[index]

    def __setitem__(self, index, row):
        self.set_row(index, row)

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

    # Table operations
    def union(self, table: "Table"):
        if self.columns != table.columns:
            raise ValueError("Cannot union tables with different columns")
        new_rows = self.rows.copy()
        for row in table.rows:
            if row not in new_rows:
                new_rows.append(row)
        return Table(f"{self.name}_union_{table.name}", self.columns.copy(), new_rows)

    def intersection(self, table: "Table"):
        if self.columns != table.columns:
            raise ValueError("Cannot intersect tables with different columns")
        common_rows = [row for row in self.rows if row in table.rows]
        return Table(f"{self.name}_inter_{table.name}", self.columns.copy(), common_rows)

    def difference(self, table: "Table"):
        if self.columns != table.columns:
            raise ValueError("Cannot diff tables with different columns")
        diff_rows = [row for row in self.rows if row not in table.rows]
        return Table(f"{self.name}_diff_{table.name}", self.columns.copy(), diff_rows)

    # Operator overloads
    def __add__(self, other):
        return self.union(other)

    def __and__(self, other):
        return self.intersection(other)

    def __sub__(self, other):
        return self.difference(other)
