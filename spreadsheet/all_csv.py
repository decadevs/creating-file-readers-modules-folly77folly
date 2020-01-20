from . import files_contract

class AllCsvs(Files):

    def read_all(self):
        print(' All lines')

    def read_first_two_lines(self):
        print('2lines')

    def read_last_two_lines(self):
        print('last 2lines')