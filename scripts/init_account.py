from brownie import network, config, accounts

LOCAL_BLOCKCHAIN_ENV = ["development", "ganache-local"]
FORKED_LOCAL_ENV = ["mainnet-fork-dev"]


def init_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENV
        or network.show_active() in FORKED_LOCAL_ENV
    ):
        # ganache-cli or ganache-local
        return accounts[0]
    else:
        # private key .env
        return accounts.add(config["wallets"]["from_key"])
