import json
from argparse import ArgumentParser

from tqdm import tqdm
from .utils import iterate


def filter_dict(row: dict) -> dict:
    del row["quoteID"]
    del row["urls"]
    del row["phase"]
    del row["probas"]

    return row


def filter_empty_row(row: dict) -> bool:
    return (row["speaker"] != "None") and (row["qids"])


def preprocess(it_):
    rows = map(json.loads, it_)
    rows = filter(filter_empty_row, rows)
    rows = map(filter_dict, rows)

    tags = ['climate change']
    rows = filter(lambda rows_: any([tag in rows_['quotation'].lower() for tag in tags]), rows)
    return rows


if __name__ == "__main__":
    arg_parser = ArgumentParser()
    arg_parser.add_argument("--file", type=str)
    args = arg_parser.parse_args()

    filename, _ = args.file.split(".")

    it = preprocess(iterate(args.file))
    with open(f"{filename}-processed.json", "w+") as file:
        for row in tqdm(it):
            json.dump(row, file)
            file.write("\n")

        file.seek(0)
        selected_rows = []
        for line in file:
            selected_rows.append(json.loads(line))

        file.seek(0)
        json.dump(selected_rows, file)
