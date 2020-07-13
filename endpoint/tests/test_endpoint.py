import endpoint.main as e
# H0,090121,"Coffee; roasted, not decaffeinated",0901,6,1
def test_main_COFEE():
    d = {"hscode": "090121"}
    a = {
            "result":[
                {'Classification': 'H5',
                 'Code': '090121',
                 'Description': 'Coffee; roasted, not decaffeinated',
                 'Code Parent': '0901',
                 'Level': '6',
                 'isLeaf': '1'}]
         }
    r = e.main(d)
    assert r == a
