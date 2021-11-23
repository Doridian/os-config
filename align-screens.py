#!/usr/bin/env python3

DISPLAYPLACER = "displayplacer"

from subprocess import check_output, call
from yaml import load, SafeLoader

currentState = load(check_output([DISPLAYPLACER, "yaml"]), SafeLoader)["screens"]

SETUP = [
    {
        "match": {
            "built_in": True,
        },
        "target": "res:3456x2234 scaled:1728x1117 pixel_encoding:--------RRRRRRRRGGGGGGGGBBBBBBBB origin:(3840,0) degree:0 hz:120.000000",
    },
    {
        "match": {
            "built_in": False,
            "size_inches": 32, # Actually 27, but LG...
        },
        "target": "res:2560x1440 scaled:2560x1440 pixel_encoding:--------RRRRRRRRGGGGGGGGBBBBBBBB origin:(-2560,0) degree:0 hz:120.000000",
    },
    {
        "match": {
            "built_in": False,
            "size_inches": 38,
        },
        "target": "res:3840x1600 scaled:3840x1600 pixel_encoding:--------RRRRRRRRGGGGGGGGBBBBBBBB origin:(0,0) degree:0 hz:120.000000",
    }
]

cmdline = [DISPLAYPLACER]

for screenSetup in SETUP:
    for screenState in currentState:
        if "built_in" in screenSetup["match"] and screenState["built_in"] is not screenSetup["match"]["built_in"]:
            continue
        if "size_inches" in screenSetup["match"] and screenState["size_inches"] != screenSetup["match"]["size_inches"]:
            continue
        cmdline.append(f'id:{screenState["id"]["persistent"]} {screenSetup["target"]}')
        screenState["has_match"] = screenSetup

for screenState in currentState:
    if "has_match" not in screenState:
        print(f'No screen match found for size_inches:{screenState["size_inches"]} built_in:{screenState["built_in"]}')
    else:
        print(f'Matched screen size_inches:{screenState["size_inches"]} built_in:{screenState["built_in"]} to UUID {screenState["id"]["persistent"]}')

call(cmdline)
