import json
import requests

Bearer = ""

def get_from_url(url):
    """
    Gets json data from a url
    :param url: the url where the json file is located
    :return: a dictionary with the data
    """
    # type: str -> dict
    headers = {"Accept": "application/json", "Authorization": "Bearer " + Bearer}
    json_obj = requests.get(url=url, headers=headers)
    return json_obj.json()


def get_from_file(path):
    """
    Gets the dictionary from a json file
    :param path: the path of the file
    :return: the dictionary from the json file
    """
    # type: str -> dict()
    with open(path + '.json') as data_file:
        data = json.load(data_file)

    return data


def write_on_file(data, path):
    """
    Overwrites a json file with the current data
    :param data: a dictionary that represents the data
    :param path: the path of the file
    """
    # type: (dict(), str) -> None
    with open(path + '.json', 'w') as outfile:
        json.dump(data, outfile)
