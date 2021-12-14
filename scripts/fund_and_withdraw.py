from brownie import FundMe
from scripts.init_account import init_account


def fund():
    fund_me = FundMe[-1]
    account = init_account()
    entrance_fee = fund_me.getEntranceFee()
    print(f"The current entry fee is {entrance_fee}")
    print("Funding")
    fund_me.fund({"from": account, "value": entrance_fee})


def withdraw():
    fund_me = FundMe[-1]
    account = init_account()
    fund_me.withdraw({"from": account})


def main():
    fund()
    withdraw()
