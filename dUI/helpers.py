import requests
import re


def get_sqlep(token, hostname=notebook_hostname):
    apiurl = f"https://{hostname}/api/2.0/sql/endpoints"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    return requests.get(apiurl, headers=headers).json()['endpoints']


def format_str(detail_dict=None):
    if detail_dict:
        return "\n".join([f'{k:<15}{str(v):>30}' for k, v in sorted(detail_dict.items())])
    else:
        return "NOTHING DOING, BOSS"
