class Matrix:
    def __init__(self, matrix_string: str) -> None:
        self.rows = self._read_rows(matrix_string)
        self.columns = self._read_columns(matrix_string)

    def _read_rows(self, matrix_string: str) -> list[list[int]]:
        return [
            [int(number) for number in row.split()]
            for row in matrix_string.splitlines()
        ]

    def _read_columns(self, matrix_string: str) -> list[list[int]]:
        return [list(column) for column in zip(*self.rows)]

    def row(self, index: int) -> list[int]:
        return self.rows[index - 1]

    def column(self, index: int) -> list[int]:
        return self.columns[index - 1]
