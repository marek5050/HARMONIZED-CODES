import pandas as pd
from io import StringIO

d2=StringIO(db)
def main(d):
    hscode = d.get("hscode")
    exact = d.get("exact",True)
    names = "Classification,Code,Description,Code Parent,Level,isLeaf".split(",")
    # arr = [x.split(",", maxsplit=len(names)-1) for x in db.split('\n')[1:]]
    frame = pd.pd.read_csv(d2, columns=names, sep=",")
    resp = {"result": []}

    if exact:
        resp["result"] = frame[frame['Code']==hscode][-1:].to_dict("records")
    else:
        resp["result"] = frame[frame['Code'].str.contains(hscode) == True][:20].to_dict("records")

    return resp
