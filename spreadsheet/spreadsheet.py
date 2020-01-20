from csv_contract import Files
import pandas as pd

class AllCsvFiles(Files):

    def __init__(self, filename):
        self.filename = filename
        self.file = pd.read_csv(filename)
        self.num = 0

    def __enter__(self):
        self.file  = pd.read_csv(self.filename)
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()        

    def __iter__(self):
        
        return self

    def __next__(self):
        try:
            self.num += 1
            return self.file.iloc[[self.num],:]
        except:
            raise StopIteration
            
        

    def read_all(self):
        return self.file.info

    def fetch_first_two_rows(self):
        return self.file.head(2)
            
    def fetch_last_two_rows(self):
        return self.file.tail(2)
