
"""
All data writing operations.
"""

import os

import pandas

from classy.model.data.read_write import ReadWrite


class Writer(ReadWrite):
    """
    Writes given data into HDF5 container in the silo folder.
    """

    __slots__ = ()

    def store_dataframe(self, dataframe, file_name):
        """
        :param dataframe:
        :param file_name:
        :return: None or raises exception on fail
        """

        datastore_path = os.path.join(os.path.join(self.data_path, "hdf5"), file_name+".hdf")

        # This will just bark if something goes wrong, which is preffered in a jupyter notebook
        dataframe.to_hdf(datastore_path, key=file_name)
