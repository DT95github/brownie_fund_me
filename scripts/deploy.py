from brownie import network, accounts, config
from brownie import FundMe, MockV3Aggregator
from scripts.utils import get_account, deploy_mocks, LOCAL_BLOCKCHAIN_ENVS
from web3 import Web3


def deploy():
    account = get_account()
    
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVS:
        price_feed_address = config['networks'][network.show_active()]['eth_usd_price_feed']
    
    else:
        # if len(MockV3Aggregator) <= 0: # No deployed MockV3Aggregators
        #     print("Deploying mocks...")
        #     MockV3Aggregator.deploy(18, Web3.toWei(2000, 'ether'), {'from': account})
        #     print("Mocks deployed.")
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_feed_address
        , {'from': account}
        , publish_source=config['networks'][network.show_active()].get('verify')
    )
    print(f'Contract deployed to address: {fund_me.address}')

    return fund_me

def main():
    deploy()