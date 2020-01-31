from Datasets import Utilities
from pathlib import Path


def main():
    extract_data = False
    if extract_data:
        nbr_subsets = 1
        data_path = Path("C:/Users/gusta/Documents/Skola/Lund/Indek år "
                         "5/Exjobb/Datasets/financial-news-dataset-master/financial-news-dataset-master/ReutersNews106521")
        Utilities.format_data(data_path, nbr_subsets)
    data = Utilities.load_file("financial_news_dataset_20061020-20131119")


if __name__ == '__main__':
    main()
