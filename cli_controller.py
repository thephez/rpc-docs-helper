# Distributed under the MIT software license, see the accompanying
# file LICENSE or https://www.opensource.org/licenses/MIT.

import os

from generator import Generator
from cli_caller import CliCaller
from annotations import Annotations
from help_parser import HelpParser


class CliController:
    def generate(self, cli, renderer, command=None):
        generator = Generator(cli, renderer)
        if command:
            generator.generate_command(command)
        else:
            generator.generate_overview()

    def get_help(self, cli, command):
        print(CliCaller(cli).help(command))

    def import_see_also(self, markdown_dir, annotations_file):
        annotations = Annotations(annotations_file)
        annotations.import_see_also(markdown_dir)

    def clean_annotations(self, annotations_file):
        annotations = Annotations(annotations_file)
        annotations.clean_annotations()

    def show_removed(self, cli, markdown_dir):
        commands = HelpParser().parse_help_overview(CliCaller(cli).help()).flat()
        removed_commands = []
        for markdown_file in os.listdir(markdown_dir):
            command = os.path.splitext(markdown_file)[0]
            if not command in commands:
                removed_commands.append(command)
        for command in sorted(removed_commands):
            print(command)
