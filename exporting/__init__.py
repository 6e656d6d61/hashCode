import os


class CSV:

    def __init__(self):
        self.file_name = ""
        self.file = None

    def from_file(self, file_name):
        if os.path.exists(file_name):
            os.remove(file_name)
        self.file_name = file_name
        self.file = open(file_name, 'w')
        return self

    def from_stream(self, file_name, stream):
        self.file_name = file_name
        self.file = stream
        return self

    def write_line(self, cols, sep=","):
        line = [elem for elem in cols]
        self.file.write(sep.join(line) + '\n')

    def write_n_line(self, rows, n, sep=","):
        for i in range(n):
            self.write_line(rows[i], sep=sep)

    def write_all_line(self, rows, sep=","):
        for row in rows:
            self.write_line(row, sep=sep)

    def get(self):
        return [self.file_name, self.file]

    def close(self):
        self.file.close()


class Raw:

    def __init__(self):
        self.file_name = ""
        self.file = None

    def from_file(self, file_name):
        if os.path.exists(file_name):
            os.remove(file_name)
        self.file_name = file_name
        self.file = open(file_name, 'w')
        return self

    def from_stream(self, file_name, stream):
        self.file_name = file_name
        self.file = stream
        return self

    def write_line(self, cols):
        line = [elem for elem in cols]
        self.file.write("".join(line) + '\n')

    def write_n_line(self, rows, n):
        for i in range(n):
            self.write_line(rows[i])

    def write_all_line(self, rows):
        for row in rows:
            self.write_line(row)

    def get(self):
        return [self.file_name, self.file]

    def close(self):
        self.file.close()