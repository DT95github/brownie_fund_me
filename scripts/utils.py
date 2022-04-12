from brownie import network, accounts
from brownie import MockV3Aggregator
from web3 import Web3

FORKED_BLOCKCHAIN_ENVS = ['mainnet-fork-dev']
LOCAL_BLOCKCHAIN_ENVS = ['development','ganache-local']
DECIMALS = 8
STARTING_ETH_USD = 200000000000


def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVS or network.show_active() in FORKED_BLOCKCHAIN_ENVS:
        return accounts[0] ## Test accounts
    else:
        return accounts.load('eth_rinkeby') ## My added account

def deploy_mocks():
    if len(MockV3Aggregator) <= 0: # No deployed MockV3Aggregators
        print("Deploying mocks...")
        MockV3Aggregator.deploy(
            DECIMALS
            # , Web3.toWei(STARTING_ETH_USD, 'ether')
            , STARTING_ETH_USD
            , {'from': get_account()}
        )
        print("Mocks deployed.")