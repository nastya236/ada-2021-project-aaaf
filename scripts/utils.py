from argparse import ArgumentParser

from tqdm import tqdm
from wikidata.client import Client
import json
from utils import iterator_from_file
from urllib.error import HTTPError


def iterate(file_name):
    with open(file_name, "r") as file:
        for line in file:
            yield line


def create_voc(path, ids):
    id2obj = {}
    for id_ in tqdm(ids):
        try:
            id2obj[id_] = str(client.get(id_, load=True).label)
        except HTTPError:
            continue

    with open(path, "a") as file:
        json.dump(id2obj, file)


if __name__ == "__main__":
    arg_parser = ArgumentParser()
    arg_parser.add_argument("--file", type=str)
    args = arg_parser.parse_args()

    client = Client()

    it = map(json.loads, list(iterator_from_file(args.file)))
    occ = set()
    countries = set()
    for i in tqdm(it):
        for j in i["occupation_ids"]:
            if j is not None:
                occ.update(j)
        for k in i["citizenship_id"]:
            if k is not None:
                countries.update([k, ])
    create_voc("dataset/count_vocab.json", countries)
    create_voc("dataset/occ_vocab.json", occ)
