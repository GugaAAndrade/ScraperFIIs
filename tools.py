import os
import pandas as pd
from typing import List


class CSVManager:
    """Manipulates csv files based on objects"""

    @staticmethod
    def print(directory: str) -> None:
        """Prints all the data from a csv file

        >>> column (dictkey) : value 1 (dictlist[0])
        >>> ...
        >>> column (dictkey) : value 3 (dictlist[2])

        """
        if os.path.exists(directory):
            df = CSVManager.load(directory)
            columns = list(df.keys())
            total_rows = len(df[columns[0]])

            # For each row prints all the columns 
            # And corresponding values
            for index in range(total_rows):
                for column, row in df.items():
                    print(f"{column}: {row[index]}")
                print()

    @staticmethod
    def load(directory: str) -> dict:
        """Opens a existing csv file and returns a dict of the data"""
        if os.path.exists(directory):
            df = pd.read_csv(directory, dtype=str)
            columns = df.columns.tolist()
            data = {}

            # Sets the corresponding columns in dict
            # and its list of values
            for column in columns:
                data[column] = list(df[column])
            return data
            
    @staticmethod
    def add_object(object: object, directory=f"{object.__class__.__name__}.csv".lower()) -> None:
        """Creates or Opens a csv file and appends the attributes of a object"""
        values = list(object.__dict__.items())

        if os.path.exists(directory):
            data = CSVManager.load(directory)

            # Appends each attribute of object at
            # the end of the list and creates dataframe
            for value in values:
                data[value[0]].append(value[1])
            df = pd.DataFrame(data, dtype=str)
            df.to_csv(directory, index=False)

        else:
            data = {}

            # In case the directory doesnt exists
            # creates a 1 index list inside dict
            # and creates the file
            for value in values:
                data[value[0]] = [value[1]]
            df = pd.DataFrame(data, dtype=str)
            df.to_csv(directory, index=False)

    @staticmethod
    def filter(directory: str, value: str, column: str) -> bool:
        """Opens a existing csv file and checks if value exists in column"""
        if os.path.exists(directory):
            data = CSVManager.load(directory)
            if value in data[column]:
                return True
            return False
        return False


    @staticmethod
    def index(directory: str, value: str) -> int:
        """Returns the row index based on value inside"""
        if os.path.exists(directory):
            data = CSVManager.load(directory)

            for row in data.values():
                if value in row:
                    index = row.index(value)
                    return index

    @staticmethod
    def row(directory: str, value: str) -> List[str]:
        """Returns a list of a row in order"""
        if os.path.exists(directory):
            data = CSVManager.load(directory)
            index = CSVManager.index(directory, value)
            row = []
            
            for rows in data.values():
                row.append(rows[index])
            return row

    @staticmethod
    def change(directory: str, check_value, column, change_value) -> None:
        """Checks a value in one column to change another in the same row"""
        if os.path.exists(directory):
            data = CSVManager.load(directory)
            index = CSVManager.index(directory, check_value)
            data[column][index] = str(change_value)
            
            df = pd.DataFrame(data, dtype=str)
            df.to_csv(directory, index=False)