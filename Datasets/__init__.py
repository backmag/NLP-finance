from Datasets import Utilities
from pathlib import Path
import pandas as pd
import os


def main():
    extract_data = False
    if extract_data:
        nbr_subsets = 1
        data_path = Path("C:/Users/gusta/Documents/Skola/Lund/Indek år "
                         "5/Exjobb/Datasets/financial-news-dataset-master/financial-news-dataset-master"
                         "/ReutersNews106521")
        Utilities.format_data(data_path, nbr_subsets)
    news_data = Utilities.load_file(str(os.getcwd() + "/data/financial_news_dataset_20061020-20131119"))
    print("News data loaded successfully.")
    ts_data = pd.read_pickle(Path(os.getcwd() + "/data/stock_data.pkl"))
    print("Stock data loaded successfully. ")


if __name__ == '__main__':
    main()
