#   Created by Elshad Karimov
#   Copyright © AppMillers. All rights reserved.


def stringifyNumbers(obj):
    # TODO
    for key in obj:
        if type(obj[key]) == int:
            obj[key] = str(obj[key])
        if type(obj[key]) == dict:
            stringifyNumbers(obj[key])
    return obj

obj = {
    "num": 1,
    "test": [],
    "data": {
        "val": 4,
        "info": {
            "isRight": True,
            "random": 66
        }
    }
}

print(stringifyNumbers(obj))
