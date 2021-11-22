#!/usr/bin/env python3

from subprocess import check_output, call
from yaml import load, SafeLoader

currentState = load(check_output(["displayplacer", "yaml"]), SafeLoader)["screens"]

SETUP = [
    {
        "match": {
            "built_in": True,
        },
        "target": "res:1728x1117 hz:120 color_depth:8 scaling:on origin:(3840,0) degree:0",
    },
    {
        "match": {
            "built_in": False,
            "size_inches": 32, # Actually 27, but LG...
        },
        "target": "res:2560x1440 hz:120 color_depth:8 scaling:off origin:(-2560,0) degree:0",
    },
    {
        "match": {
            "built_in": False,
            "size_inches": 38,
        },
        "target": "res:3840x1600 hz:120 color_depth:7 scaling:off origin:(0,0) degree:0",
    }
]

cmdline = ["displayplacer"]

for screenSetup in SETUP:
    for screenState in currentState:
        if "built_in" in screenSetup["match"] and screenState["built_in"] is not screenSetup["match"]["built_in"]:
            continue
        if "size_inches" in screenSetup["match"] and screenState["size_inches"] != screenSetup["match"]["size_inches"]:
            continue
        cmdline.append(f'id:{screenState["id"]["persistent"]} {screenSetup["target"]}')

call(cmdline)
