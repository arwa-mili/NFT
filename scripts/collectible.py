import json
from brownie import (
    accounts,
    config,
    Collection
)

def main():
    account = accounts.add(config['wallets']['from_key'])
    # Get the most recent deployment of our contract
    collection = Collection[-1]
    # Get the metadata hash
    meta_data_hash = json.load(open(f"metadata/metadata.json"))
    # Call our createToken function to mint a token
    transaction = collection.mintToken(meta_data_hash, {'from': account})