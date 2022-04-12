from brownie import FundMe, network, accounts, exceptions
from scripts.utils import LOCAL_BLOCKCHAIN_ENVS, get_account
from scripts.deploy import deploy
import pytest



def test_can_fund_and_withdraw():
    account = get_account()
    fund_me = deploy()
    entrance_fee = fund_me.getEntranceFee() + 100
    tx = fund_me.fund({'from':account, 'value':entrance_fee})
    tx.wait(1)
    #Assert
    assert fund_me.addressToAmountFunded(account.address) == entrance_fee
    
    tx2 = fund_me.withdraw({'from':account})
    tx2.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == 0


def test_only_owner_can_withdraw():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVS:
        pytest.skip("Skipping test - Only for local testing.")
    account = get_account()
    fund_me = deploy()

    not_owner = accounts[2]
    with pytest.raises(exceptions.VirtualMachineError):
        tx3 = fund_me.withdraw({'from': not_owner})
