# Distributed under the MIT software license, see the accompanying
# file LICENSE or https://www.opensource.org/licenses/MIT.
from renderer_markdown import RendererMarkdown
from help_parser import HelpParser
from pathlib import Path
import os

test_data_dir = Path(os.path.dirname(__file__)) / "test_data.markdown"


def test_process_command_help():
    cmds = [
        'abandontransaction',
        'addmultisigaddress',
        'addnode',
        'getbestblockhash',
        'getblock',
        'gettxoutproof',
        'pruneblockchain',
        'getmemoryinfo',
    ]
    for cmd in cmds:
        with open(test_data_dir / cmd) as file:
            input = file.read()
            help_data = HelpParser().parse_help_command(input)
        with open(test_data_dir / (cmd + ".md")) as file:
            expected_output = file.read()
        assert RendererMarkdown("").process_command_help(
            help_data) == expected_output


def test_code_block():
    r = RendererMarkdown("")

    assert r.code_block("abc") == "    abc\n"
    assert r.code_block("  def") == "    def\n"
    assert r.code_block("     xxx\n     yyy") == "    xxx\n    yyy\n"
    assert r.code_block("  {\n    x\n  }\n") == "    {\n      x\n    }\n"
    assert r.code_block(
        "      {\n        x\n      }\n") == "    {\n      x\n    }\n"


def test_yaml_escape():
    r = RendererMarkdown("")

    assert r.yaml_escape('a "string"') == 'a \\"string\\"'
