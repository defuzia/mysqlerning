from tabletter.code_writer import display_table

import unittest
import pandas


class ProgramTest(unittest.TestCase):
    def test_display_table(self):
        self.assertIsInstance(display_table(), pandas.DataFrame)


if __name__ == '__main__':
    unittest.main()
