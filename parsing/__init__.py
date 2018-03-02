#!/usr/bin/env python3.6


class CSV:

    def __init__(self):
        self.file_name = ""
        self.file = None

    def from_file(self, file_name):
        self.file_name = file_name
        self.file = open(file_name, 'r')
        return self

    def from_stream(self, file_name, stream):
        self.file_name = file_name
        self.file = stream
        return self

    def read_line(self, sep=","):
        line = self.file.readline()
        if line[-1] == '\n':
            line = line[:-1]
        return line.split(sep=sep)

    def read_n_line(self, n, sep=","):
        lines = []
        for i in range(n):
            lines.append(self.read_line(sep))
        return lines

    def read_all_line(self, sep=","):
        lines = []
        for line in self.file:
            if line[-1] == '\n':
                line = line[:-1]
            lines.append(line.split(sep=sep))
        return lines

    def get(self):
        return [self.file_name, self.file]

    def close(self):
        self.file.close()


class Raw:

    def __init__(self):
        self.file_name = ""
        self.file = None

    def from_file(self, file_name):
        self.file_name = file_name
        self.file = open(file_name, 'r')
        return self

    def from_stream(self, file_name, stream):
        self.file_name = file_name
        self.file = stream
        return self

    def read_line(self, nb_char=1):
        line = self.file.readline()
        if line[-1] == '\n':
            line = line[:-1]
        return [line[i:i + nb_char] for i in range(0, len(line), nb_char)]

    def read_n_line(self, n, nb_char=1):
        lines = []
        for i in range(n):
            lines.append(self.read_line(nb_char=nb_char))
        return lines

    def read_all_line(self, nb_char=1):
        lines = []
        for line in self.file:
            if line[-1] == '\n':
                line = line[:-1]
            lines.append([line[i:i + nb_char] for i in range(0, len(line), nb_char)])
        return lines

    def get(self):
        return [self.file_name, self.file]

    def close(self):
        self.file.close()