from helpers import *

# Create Ocean instance
from ocean_lib.web3_internal.utils import connect_to_network
connect_to_network("goerli") # mumbai is "polygon-test"

import os
from ocean_lib.example_config import get_config_dict
from ocean_lib.ocean.ocean import Ocean
config = get_config_dict("goerli")
ocean = Ocean(config)

from ocean_lib.ocean.ocean import Ocean
ocean = Ocean(config)

# Create OCEAN object. ocean_lib knows where OCEAN is on all remote networks 
OCEAN = ocean.OCEAN_token

# Create Alice's wallet
from brownie.network import accounts
accounts.clear()

alice_private_key = os.getenv('TEST_PRIVATE_KEY1')
alice = accounts.add(alice_private_key)
assert alice.balance() > 0, "Alice needs ETH"
print("Alice's ETH:", alice.balance())

# Compact wei <> eth conversion
from ocean_lib.ocean.util import to_wei, from_wei

testurl = "https://arweave.net/qctEbPb3CjvU8LmV3G_mynX74eCxo1domFQIlOBH1xU"
url = "https://v2.akord.com/public/vaults/active/glhAAuokuVaFGDwTXrHxOX9RZ8UVZ4-4a8nTFMcCpfo/gallery#public/17dd137d-ae48-48a8-8875-d8754e655358"
name = "ETH predictions " + str(time.time()) #time for unique name
(data_nft, datatoken, ddo) = ocean.assets.create_url_asset(name, testurl, {"from":alice, "gas":3000000}, wait_for_aqua=False)
metadata_state = 5
data_nft.setMetaDataState(metadata_state, {"from":alice})
print(f"New asset created, with did={ddo.did}, and datatoken.address={datatoken.address}")
print(ddo)

from web3.main import Web3
to_address="0xA54ABd42b11B7C97538CAD7C6A2820419ddF703E" #official judges address
datatoken.mint(to_address, Web3.toWei(10, "ether"), {"from": alice})
