from scripts.helpful_scripts import getAccount, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from scripts.deploy import deploy_fund_me
from brownie import network, accounts, exceptions
import pytest


def test_can_fund_and_withdraw():
    account = getAccount()
    fund_me = deploy_fund_me()
    print(f"FundMe deployed at  {fund_me}")
    entrance_fee = fund_me.getEntranceFee() + 100
    print(f"Entrance fee es  {entrance_fee}")
    # entrance_fee = 5000000000000000

    # Pruebo a fundear
    tx = fund_me.fund({"from": account, "value": entrance_fee})
    tx.wait(1)

    assert fund_me.addressToAmountFunded(account.address) == entrance_fee

    # Pruebo el withdraw
    tx2 = fund_me.withdraw({"from": account})
    tx2.wait(1)

    assert fund_me.addressToAmountFunded(account.address) == 0


def test_only_owner_can_withdraw():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("only for local testing")
    fund_me = deploy_fund_me()
    bad_actor = accounts.add()
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from": bad_actor})
