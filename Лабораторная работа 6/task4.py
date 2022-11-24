import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(INPUT_FILE) -> list[dict]:
    list_ = []
    with open(INPUT_FILE) as f:
        header = f.readline().strip('\n').split(",")
        for row in f:
            values = row.strip("\n").split(",") #strip("\n") -> replace("\n", "")
            list_.append(dict(zip(header, values)))
    return list_



#csv_to_list_dict()

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
