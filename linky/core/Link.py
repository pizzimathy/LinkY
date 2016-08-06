#!/usr/bin/env python3

import json
import os
import os.path
from linky import load_command
from linky import load_package


class Link:

    def __init__(self):
        self.options = {}

        with open(os.path.join(os.getcwd(), "linky.json")) as f:
            self.options = json.loads(f.read())

    def create_command(self):
        print("loading command")

        command = list(self.options["bin"].keys())[0]
        file = self.options["bin"][command]
        path = ""

        if not self.options.get("src"):
            path = os.getcwd()
        else:
            path = self.options["src"]

        self.options["command"] = load_command(command, file, path)

    def create_package(self):
        print("loading package")

        path = ""

        if not self.options.get("src"):
            path = os.getcwd()
        else:
            path = self.options["src"]

        self.options["package"] = load_package(self.options["name"], path)

    def save_options(self):
        print("saving options")
        with open(os.path.join(os.getcwd(), "linky.json"), "w") as f:
            f.write(json.dumps(self.options))

    def tear_down(self):
        os.unlink(self.options["command"]["dest"])
        os.unlink(self.options["package"]["dest"])

