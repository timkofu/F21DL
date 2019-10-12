"""
All data reading operations.
"""

import os
from pathlib import Path

import pandas


class Reader:
    """
    Reads a given CSV file from silo and returns a pandas dataframe.
    """

    __slots__ = ('data_path',)

    def __init__(self):
        self.data_path = Path(  # Path to the data folder
            os.path.join(os.path.dirname(os.path.abspath(__file__)), "silo")
        )

    def list_csvs(self):
        """
        Lists available CSVs
        """

        for file in self.data_path.glob("**/*.csv"):
            print(os.path.split(file)[1])

    def load(self, csv_name):
        """
        Reads given CSV and returns a pandas dataframe of it.
        :param csv_name:
        :return: pandas.Dataframe
        """

        pass
