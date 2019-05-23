# Distributed under the MIT software license, see the accompanying
# file LICENSE or https://www.opensource.org/licenses/MIT.

import os
import sys
from pathlib import Path


class CliDash:
    def __init__(self):
        cli_path = os.environ.get("CLI_PATH")
        if not cli_path:
            sys.exit("CLI_PATH is not set. Set this to the command to "
                     "run the dash-cli including any options. Exiting now.")

        self.cli_path = Path(cli_path.split(" ")[0])
#        self.cli_path = Path(cli_path.split(" ")[0]).expanduser()
        self.cli_args = cli_path.split(" ")[1:]
