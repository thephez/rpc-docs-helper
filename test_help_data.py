# Distributed under the MIT software license, see the accompanying
# file LICENSE or https://www.opensource.org/licenses/MIT.

from help_data import display_name, capitalize, uncapitalize


def test_display_name():
    assert display_name("abandontransaction") == "AbandonTransaction"
    assert display_name("addmultisigaddress") == "AddMultiSigAddress"
    assert display_name("addnode") == "AddNode"
    assert display_name("disconnectnode") == "DisconnectNode"
    assert display_name("listsinceblock") == "ListSinceBlock"
    assert display_name("listwallets") == "ListWallets"
    assert display_name("setban") == "SetBan"
    assert display_name("signmessagewithprivkey") == "SignMessageWithPrivKey"
    assert display_name("listaccounts") == "ListAccounts"
    assert display_name("listtransactions") == "ListTransactions"
    assert display_name("listwallets") == "ListWallets"
    assert display_name("getaddressesbyaccount") == "GetAddressesByAccount"


def test_capitalize():
    assert capitalize("word") == "Word"
    assert capitalize("x") == "X"
    assert capitalize("") == ""


def test_uncapitalize():
    assert uncapitalize("Word") == "word"
    assert uncapitalize("X") == "x"
    assert uncapitalize("") == ""
