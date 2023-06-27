from brownie import Collection, accounts, config

def main():
    account = accounts.add(config['wallets']['from_key'])
    Collection.deploy({'from': account})