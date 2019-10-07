"""
All data reading operations.
"""

import pandas


class Reader:
    """
    Reads a given CSV file from silo and returns a pandas dataframe.
    """

    __slots__ = ('data_path',)

    def __init__(self):
        self.data_path = None

    def list_csvs(self):
        """
        Lists available CSVs
        """
        pass

    def load(self, csv_name):
        """
        Reads given CSV and returns a pandas dataframe of it.
        :param csv_name:
        :return: pandas.Dataframe
        """

        pass
