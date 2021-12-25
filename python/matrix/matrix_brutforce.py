class Matrix:
    def __init__(self, matrix_string: str) -> None:
        self.rows = self._read_rows(matrix_string)
        self.columns = self._read_columns()

    def _read_rows(self, matrix_string: str) -> list[list[int]]:
        rows = []
        for line in matrix_string.splitlines():
            row = []
            for number in line.split():
                row.append(int(number))
            rows.append(row)
        return rows

    def _read_columns(self):
        columns_count = len(self.rows[0])
        columns = []
        for i in range(columns_count):
            column = []
            for row in self.rows:
                column.append(row[i])
            columns.append(column)
        return columns

    def row(self, index: int) -> list[int]:
        return self.rows[index - 1]

    def column(self, index: int) -> list[int]:
        return self.columns[index - 1]
