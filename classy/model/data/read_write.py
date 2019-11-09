"""
Read and Write parent class.
"""

import os


class ReadWrite:

    __slots__ = ('data_path', 'file_types')

    def __init__(self):
        self.data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "silo")
        self.file_types = ('csv', 'hdf')
