# QUE ES ESTA LINEA from ssl import VerifyFlags
from brownie import FundMe, network, config, MockV3Aggregator
from scripts.helpful_scripts import (
    getAccount,
    deployMocks,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)


def deploy_fund_me():
    account = getAccount()
    # pass the priceFeed to the constructor
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deployMocks()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    return fund_me


def main():
    deploy_fund_me()
