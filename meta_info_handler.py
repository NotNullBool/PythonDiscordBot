""" Handler for bot meta info
"""
import json
from typing import Dict
from discord import LoginFailure


def get_token(token_file_path: str = "./token.json") -> str:
    """get_token Get Discord Bot Token
    Returns:
        str: Token
    """
    token_dict: Dict[str, str] = {"token": ""}
    try:
        with open(token_file_path, 'r', encoding="utf-8") as file_:
            token_dict = json.load(file_)
    except IOError as err:
        print(f"Exception: {err}, token.json does not yet exist")
        with open(token_file_path, 'w', encoding="utf-8") as file_:
            json.dump(token_dict, file_)
    finally:
        if token_dict["token"] == "":
            raise LoginFailure(f"token at {token_file_path} needs to be set")
    return token_dict["token"]
