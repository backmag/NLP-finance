import numpy as np
import os
import pathlib


class DataFormatter:

    def __init__(self, path):
        self.path = path

    def format_data(self):
        path = self.path / 'businesspro-energy-exxonmobil-alaska-dc-idUSN2021166720061020'
        txt = path.read_text()
        #print(txt)

    def read_doc(self):
        # Write code to read one document.
        # Should output three features, date, title and text.
        return False

    def read_dir(self):
        # Write code to read all documents in one file.
        return False
