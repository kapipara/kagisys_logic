# -*- coding: utf-8 -*-

"""Storage Model.

This is Storage Model of Kagisys
"""

# import os


class StorageModel():
    """StorageModel for Kagisys."""

    def __init__(self):
        """Set file name."""
        self.file_name = "kagisys.toggle"
        """
        self.path = ""
        os.system(
            "cd " + self.directry + self.file_name
        )
        """

    def update_file(self, data):
        """Update file to set data."""
        file_ = open(self.file_name, 'w')
        file_.write(data)
        file_.close()
