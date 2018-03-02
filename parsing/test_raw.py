from unittest import TestCase
import parsing


class TestRaw(TestCase):

    def check_line(self, lines, n, peer, odd):
        if len(lines[n]) != 7:
            self.fail()
        for i in range(7):
            if i % 2 == 0 and lines[n][i] != peer:
                self.fail()
            if i % 2 == 1 and lines[n][i] != odd:
                self.fail()

    def test_read_line(self):
        file = parsing.Raw().from_file("sample.raw")
        first_line = file.read_line()
        self.check_line([first_line], 0, 'M', 'T')
        file.close()

    def test_read_n_line(self):
        file = parsing.Raw().from_file("sample.raw")
        lines = file.read_n_line(2)
        if len(lines) != 2:
            self.fail()
        self.check_line(lines, 0, 'M', 'T')
        self.check_line(lines, 1, 'T', 'M')
        file.close()

    def test_read_all_line(self):
        file = parsing.Raw().from_file("sample.raw")
        lines = file.read_all_line()
        if len(lines) != 4:
            self.fail()
        for i in range(4):
            if i % 2 == 0:
                self.check_line(lines, i, 'M', 'T')
            else:
                self.check_line(lines, i, 'T', 'M')
        file.close()

    def test_get(self):
        file = parsing.Raw()
        file_name, stream = file.get()
        if file_name != "" or stream is not None:
            self.fail()
        file.from_file("sample.csv")
        file_name, stream = file.get()
        if file_name != "sample.csv" or stream is None:
            self.fail()
        file.close()
