def collectStrings(obj):
    # TODO
    res = []
    for key in obj:
        if type(obj[key]) == str:
            res.append(obj[key])
        if type(obj[key]) == dict:
            return res+collectStrings(obj[key])
    return res

obj = {
    "stuff": 'foo',
    "data": {
        "val": {
            "thing": {
                "info": 'bar',
                "moreInfo": {
                    "evenMoreInfo": {
                        "weMadeIt": 'baz'
                    }
                }
            }
        }
    }
}

print(collectStrings(obj))
