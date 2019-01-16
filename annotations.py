# Distributed under the MIT software license, see the accompanying
# file LICENSE or https://www.opensource.org/licenses/MIT.

import json
from pathlib import Path
import os
import re

from cli_caller import CliCaller
from help_parser import HelpParser


class Annotations:
    def __init__(self, filename):
        self.filename = filename
        self.load()

    def load(self):
        with open(self.filename) as file:
            self.annotations = json.load(file)

    def annotation(self, command):
        if command in self.annotations:
            return self.annotations[command]
        else:
            return {}

    def import_see_also(self, dir):
        with open(self.filename) as file:
            annotations = json.load(file)
        for filename in os.listdir(dir):
            command = filename.partition(".")[0]
            print(command)
            see_also_commands = []
            with open(Path(dir) / filename) as file:
                found_see_also = False
                for line in file:
                    if line.startswith("*See also*"):
                        found_see_also = True
                        continue
                    if found_see_also and line.startswith("* "):
                        match = re.match(r"^\* .*\[rpc (.*)\]", line)
                        if match:
                            print("  ", match.group(1))
                            see_also_commands.append(match.group(1))
            if see_also_commands:
                if not command in annotations:
                    annotations[command] = {}
                commands = {
                    "commands": see_also_commands
                }
                if "see_also" in annotations[command]:
                    annotations[command]["see_also"].update(commands)
                else:
                    annotations[command]["see_also"] = commands
        with open(self.filename, "w") as file:
            file.write(json.dumps(annotations, indent=2, sort_keys=True))

    def clean_annotations(self):
        with open(self.filename) as file:
            annotations = json.load(file)
        to_be_removed = []
        for command in annotations:
            annotation = annotations[command]
            if "see_also" in annotation:
                if annotation["see_also"] == {"commands": [""]}:
                    annotation.pop("see_also")
            if annotation == {}:
                to_be_removed.append(command)
        for command in to_be_removed:
            annotations.pop(command)
        with open(self.filename, "w") as file:
            file.write(json.dumps(annotations, indent=2, sort_keys=True))
