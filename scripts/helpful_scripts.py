from brownie import network, config, accounts, MockV3Aggregator
from web3 import Web3

DECIMALS = 8
STARTING_PRICE = 200000000000
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]
FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork"]


def getAccount():
    print(f"The current network is: {network.show_active()}")
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        print(f"The current account is: {accounts[0]}")
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deployMocks():
    print(f"The current network is: {network.show_active()}")
    print("Deploying Mocks...")
    starting_price = Web3.toWei(STARTING_PRICE, "ether")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(
            #    DECIMALS, Web3.toWei(STARTING_PRICE, "ether"), {"from": getAccount()}
            DECIMALS,
            starting_price,
            {"from": getAccount()},
        )
    print(f"The starting price is: {starting_price}")
    print("Mocks deployed!")
    print(f"The Mock address is: {MockV3Aggregator[-1].address}")
