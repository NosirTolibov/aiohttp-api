# product_recommendations/utils.py
import csv
import pickle

from settings import CSV_RECOMMENDS_FILE_PATH, PICKLE_RECOMMENDS_FILE_PATH


def getstuff(filename):
    """
    Make generator function from csv file
    :param filename:
    :return:
    """
    with open(filename, "r") as csvfile:
        datareader = csv.reader(csvfile)
        for row in datareader:
            yield row


def convert_csv_pickle(input_file_name):
    """
    Create dict and write to pickle file
    :param input_file_name:
    :return:
    """
    product_dict = {}
    for row in getstuff(input_file_name):
        if row[0] not in product_dict:
            product_dict[row[0]] = []
            product_dict[row[0]].append({'recommendation': row[1], 'rank': row[2]})
        else:
            product_dict[row[0]].append({'recommendation': row[1], 'rank': row[2]})
    with open(PICKLE_RECOMMENDS_FILE_PATH, 'wb') as picklefile:
        pickle.dump(product_dict, picklefile, protocol=pickle.HIGHEST_PROTOCOL)
    return


"""
Read pickle file
"""
with open(PICKLE_RECOMMENDS_FILE_PATH, 'rb') as picklefile:
    pickle_data = pickle.load(picklefile)


def get_recommendation_list(sku: str, min_threshold: str) -> list:
    """
    Get recommendation sku from pickle dict
    :param sku:
    :param min_threshold:
    :return:
    """
    if min_threshold is None:
        return pickle_data[sku]
    else:
        filter_row = [d for d in pickle_data[sku] if float(d['rank']) >= float(min_threshold)]
        return filter_row

