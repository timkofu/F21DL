"""
All data reading operations.
"""

import os
from pathlib import Path

from classy.model.data.read_write import ReadWrite

import pandas


class Reader(ReadWrite):
    """
    Reads a given CSV file from silo and returns a pandas dataframe.
    """

    __slots__ = ()

    def list_data_files(self, file_type="hdf"):
        """
        Lists available CSV and HDF5 files
        """

        if file_type not in self.file_types:
            raise ValueError("Only csv and hdf supported")

        files = []
        if file_type == "csv":
            files = [os.path.split(file)[1] for file in Path(self.data_path).glob(f"**/*.{file_type}")]
        elif file_type == "hdf":
            hdf_data_path = os.path.join(self.data_path, "hdf5")
            files = [os.path.split(file)[1] for file in Path(hdf_data_path).glob(f"**/*.{file_type}")]

        return files

    def load_data(self, file_name, file_type="hdf"):
        """
        Reads given CSV and returns a pandas dataframe of it.
        :param file_name: No file extension needed, just the name
        :param file_type:
        :return: pandas.Dataframe
        """

        if file_type not in self.file_types:
            raise ValueError("Only csv and hdf supported")

        file_path = None
        if file_type == "csv":
            file_path = os.path.join(self.data_path, file_name+".csv")
        elif file_type == "hdf":
            file_path = os.path.join(os.path.join(self.data_path, "hdf5"), file_name+".hdf")

        # Does the file exist? (was it misspelt maybe)
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"I couldn't find {file_name}")

        if file_type == "csv":
            return pandas.read_csv(file_path)
        return pandas.read_hdf(file_path)
