from unittest import TestCase
import exporting
import parsing


class TestCSV(TestCase):

    def test_write_line(self):
        file = exporting.CSV().from_file("sample.csv")
        file.write_line(['M', 'T', 'M'])
        file.close()
        file = parsing.CSV().from_file("sample.csv")
        line = file.read_line()
        if len(line) != 3:
            self.fail()
        if line[0] != 'M' or line[1] != 'T' or line[2] != 'M':
            self.fail()
        file.close()

    def test_write_n_line(self):
        file = exporting.CSV().from_file("sample.csv")
        file.write_n_line([['M', 'T', 'M'], ['T', 'M', 'T'], ['M', 'T', 'M']], 2)
        file.close()
        file = parsing.CSV().from_file("sample.csv")
        lines = file.read_n_line(n=2)
        if len(lines) != 2:
            self.fail()
        if lines[0][0] != 'M' or lines[0][1] != 'T' or lines[0][2] != 'M':
            self.fail()
        if lines[1][0] != 'T' or lines[1][1] != 'M' or lines[1][2] != 'T':
            self.fail()
        file.close()

    def test_write_all_line(self):
        file = exporting.CSV().from_file("sample.csv")
        file.write_all_line([['M', 'T', 'M'], ['T', 'M', 'T'], ['M', 'T', 'M']])
        file.close()
        file = parsing.CSV().from_file("sample.csv")
        lines = file.read_all_line()
        if len(lines) != 3:
            self.fail()
        if lines[0][0] != 'M' or lines[0][1] != 'T' or lines[0][2] != 'M':
            self.fail()
        if lines[1][0] != 'T' or lines[1][1] != 'M' or lines[1][2] != 'T':
            self.fail()
        if lines[2][0] != 'M' or lines[2][1] != 'T' or lines[2][2] != 'M':
            self.fail()
        file.close()

    def test_get(self):
        file = exporting.CSV()
        file_name, stream = file.get()
        if file_name != "" or stream is not None:
            self.fail()
        file.from_file("sample.csv")
        file_name, stream = file.get()
        if file_name != "sample.csv" or stream is None:
            self.fail()
        file.close()
