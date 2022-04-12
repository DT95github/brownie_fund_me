from brownie import FundMe
from scripts.utils import get_account


def fund():
    fund_me = FundMe[-1] # Instantiate the deployed contract
    account = get_account() # Get dev account
    entrance_fee = fund_me.getEntranceFee()
    print(f"Current entrace fee: {entrance_fee}")

    fund_me.fund({"from":account, "value": entrance_fee})

def withdraw():
    fund_me = FundMe[-1] # Instantiate the deployed contract
    account = get_account() # Get dev account
    fund_me.withdraw({"from":account})


def main():
    withdraw()