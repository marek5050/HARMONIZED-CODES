import csv

import pandas as pd


def retrieve_document():
    d2 = pd.read_excel("http://unstats.un.org/unsd/tradekb/Attachment439.aspx?AttachmentType=1")
    return d2

def save_document(dataframe):
    dataframe.to_csv("data/harmonized_codes.csv", index=False,quoting=csv.QUOTE_ALL)
    dataframe.to_excel("data/harmonized_codes.xlsx", index=False)

if __name__ == "__main__":
    d2 = retrieve_document()
    save_document(d2)