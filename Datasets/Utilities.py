import os
import pathlib
import pickle
from datetime import datetime


def save_file(file, name):
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(file, f, pickle.HIGHEST_PROTOCOL)
    print("Saved as {}.".format(name))


def load_file(name):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)


def format_date(pre_date):
    """Convert a date of the form "Fri Oct 20, 2006"
    to "20-10-2006" """
    month_dict = {
        "Jan": 1,
        "Feb": 2,
        "Mar": 3,
        "Apr": 4,
        "May": 5,
        "Jun": 6,
        "Jul": 7,
        "Aug": 8,
        "Sep": 9,
        "Oct": 10,
        "Nov": 11,
        "Dec": 12
    }
    pre_date = pre_date.split()
    return datetime(int(pre_date[4]), month_dict[pre_date[2]], int(pre_date[3].strip(',')))


def format_data(path, nbr_sub):
    pathlist = list(pathlib.Path(path).glob('*'))
    nbr_files = len(pathlist)
    print("{} files found".format(nbr_files))
    files_per_sub = round(nbr_files / nbr_sub)
    ctr = 1
    for i in range(0, nbr_files, files_per_sub):
        print("Extracting partition {}...".format(ctr))
        ctr += 1
        data = {'title': [], 'text': [], 'date': []}
        paths = pathlist[i:i + files_per_sub]
        for p in paths:
            if not p.stem == ".DS_Store":
                read_dir(p, data)
        save_file(data, "financial_news_dataset_" + data['date'][0].strftime("%Y%m%d") + "-" + data['date'][-1].strftime("%Y%m%d"))


def read_dir(dir_path, data):
    """Reads the documents in a directory and returns the date, title
    and text as a dictionary. """
    date_str = dir_path.stem
    remove_list = []
    doclist = dir_path.glob('*')
    for doc in doclist:
        # If there are empty documents, delete them.
        if not read_doc(doc, data):
            remove_list.append(doc)
    if len(remove_list) > 0:
        for r in remove_list:
            os.remove(r)
            print("Deleted {}, empty file.".format(r))


def read_doc(doc_path, data):
    with open(doc_path) as fp:
        all_lines = fp.readlines()
        if len(all_lines) > 0:
            data['title'].append(all_lines[0])
            data['date'].append(format_date(all_lines[2]))
            data['text'].append(''.join(all_lines[7:]))
            return True
        else:
            return False
