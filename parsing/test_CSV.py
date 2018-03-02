from unittest import TestCase
import parsing


class TestCSV(TestCase):

    def test_read_line(self):
        file = parsing.CSV().from_file("sample.csv")
        header = file.read_line()
        if len(header) != 4:
            self.fail()
        if header[0] != "col_1" or header[1] != "col_2" or header[2] != "col_3" or header[3] != "col_4":
            self.fail()
        first_line = file.read_line()
        if len(first_line) != 4:
            self.fail()
        if first_line[0] != "1" or first_line[1] != "2" or first_line[2] != "3" or first_line[3] != "4":
            self.fail()
        file.close()

    def test_read_n_line(self):
        file = parsing.CSV().from_file("sample.csv")
        header = file.read_line()
        if len(header) != 4:
            self.fail()
        if header[0] != "col_1" or header[1] != "col_2" or header[2] != "col_3" or header[3] != "col_4":
            self.fail()
        lines = file.read_n_line(2)
        if len(lines) != 2:
            self.fail()
        if len(lines[0]) != 4:
            self.fail()
        for i in range(8):
            if lines[i // 4][i % 4] != str(i + 1):
                self.fail()
        file.close()

    def test_read_all_line(self):
        file = parsing.CSV().from_file("sample.csv")
        header = file.read_line()
        if len(header) != 4:
            self.fail()
        if header[0] != "col_1" or header[1] != "col_2" or header[2] != "col_3" or header[3] != "col_4":
            self.fail()
        lines = file.read_all_line()
        if len(lines) != 3:
            self.fail()
        if len(lines[0]) != 4:
            self.fail()
        for i in range(12):
            if lines[i // 4][i % 4] != str(i + 1):
                self.fail()
        file.close()

    def test_get(self):
        file = parsing.CSV()
        file_name, stream = file.get()
        if file_name != "" or stream is not None:
            self.fail()
        file.from_file("sample.csv")
        file_name, stream = file.get()
        if file_name != "sample.csv" or stream is None:
            self.fail()
        file.close()
