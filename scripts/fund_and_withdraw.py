from brownie import FundMe
from scripts.helpful_scripts import getAccount


def fund():
    fund_me = FundMe[-1]
    print(f"El contrato es {fund_me.address}")
    account = getAccount()
    print(account)
    entrance_fee = fund_me.getEntranceFee()
    print(f"The current entry fee is {entrance_fee}")
    # print(f"Y mi saldo es {account.value}")
    print("Funding")
    fund_me.fund({"from": account, "value": entrance_fee})

def withdraw():
    fund_me = FundMe[-1]
    account = getAccount()
    print("Withdrawing")
    fund_me.withdraw({"from": account})


def main():
    fund()
    withdraw()