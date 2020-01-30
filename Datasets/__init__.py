from Datasets.DataFormatter import DataFormatter
import os
from pathlib import Path
cwd = Path.cwd().parent.parent.parent
data_path = cwd / 'Datasets' / 'financial-news-dataset-master' / 'financial-news-dataset-master' / 'ReutersNews106521' /\
            '20061020'
df = DataFormatter(data_path)
df.format_data()
