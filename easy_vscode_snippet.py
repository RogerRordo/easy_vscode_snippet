#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: RogerRordo

import os
import json


def main():
    res = {}
    wk = os.walk("code")
    for root, dirs, files in wk:
        for file in files:
            with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                sname = os.path.splitext(file)[0]
                sprefix = sname
                sdesc = sname
                sbody = f.read().splitlines()
                res[sname] = {"prefix": sprefix, "description": sdesc, "body": sbody}
    with open("res.json", "w", encoding="utf-8") as f:
        print(json.dumps(res, indent=4, sort_keys=True), file=f)


if __name__ == '__main__':
    main()
