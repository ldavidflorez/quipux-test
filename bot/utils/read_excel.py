import pandas as pd


# Class to read excel file and return the data
class ReadExcel:
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        try:
            data = pd.read_excel(self.file_path)
            # Transform data to dictionary of lists
            data = data.to_dict(orient="records")
            return data
        except Exception as e:
            print(e)
            return None
