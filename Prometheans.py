from requests import get
import json
import time
from web3 import Web3
import sys
import math

w3 = Web3(Web3.HTTPProvider("ENTER YOUR ETH NODE (QUICKNODE, INFURA, ETC.) HTTPS LINK HERE"))
API_KEY = "ENTER YOUR ETHERSCAN API KEY HERE"
BASE_URL = "https://api.etherscan.io/api"
MAX_GAS_FEE = "40"
PRIORITY_FEE = "3"
PRIVATE_KEY = "ENTER YOUR WALLETS PRIVATE KEY HERE"

acct = w3.eth.account.from_key(PRIVATE_KEY)
public_address = acct.address
contract_address = "0xc4a5025c4563Ad0ACC09d92c2506e6744DAd58Eb"
abi = '[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":true,"internalType":"uint256","name":"id","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":false,"internalType":"bool","name":"approved","type":"bool"}],"name":"ApprovalForAll","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":false,"internalType":"uint256","name":"id","type":"uint256"},{"indexed":true,"internalType":"uint256","name":"blockNumber","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"index","type":"uint256"}],"name":"Minted","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":true,"internalType":"uint256","name":"id","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[],"name":"DURATION","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"MATURITY","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"id","type":"uint256"}],"name":"approve","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"owner_","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"currentEmber","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"currentId","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"emberOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"getApproved","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_name","type":"string"},{"internalType":"string","name":"_symbol","type":"string"},{"internalType":"uint256","name":"duration_","type":"uint256"},{"internalType":"uint256","name":"maturity_","type":"uint256"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"isApprovedForAll","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"lastMinted","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"lowestEmber","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"mint","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"destination_","type":"address"}],"name":"mintTo","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"owner_","type":"address"}],"name":"minted","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"open","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"owner_","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"ownerOf","outputs":[{"internalType":"address","name":"owner_","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"id","type":"uint256"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"operator","type":"address"},{"internalType":"bool","name":"approved","type":"bool"}],"name":"setApprovalForAll","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bool","name":"open_","type":"bool"}],"name":"setOpen","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"tokenURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"id","type":"uint256"}],"name":"transferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"destination","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"withdraw","outputs":[],"stateMutability":"nonpayable","type":"function"}]'
prometheans_contract = w3.eth.contract(address=contract_address, abi=abi)

def make_api_url(module, action, contract_address, address, page, offset, startblock, endblock, sort):
    # Creates a base api url that can be used to query data from Etherscan
    url = BASE_URL + f"?module={module}&action={action}&contractaddress={contract_address}&address={address}&page={page}&offset={offset}&startblock={startblock}&endblock={endblock}&sort{sort}&apikey={API_KEY}"

    return url

def get_minted_ids():
    # Retrieves token ids of the monks that are already minted by the address
    txns = make_api_url("account", "tokennfttx", contract_address, public_address, 1, 1000, 0, 999999999, "asc")
    response = get(txns)
    data = response.json()["result"]
    token_id = [txn["tokenID"] for txn in data]
    return token_id

def get_mint_block(input):
    # Takes in the monks position from the minting list and assigns it an ember(minting number) 
    if input == 14:
        return 75
    elif input == 13:
        return 71
    elif input == 12:
        return 66
    elif input == 11:
        return 61
    elif input == 10:
        return 56
    elif input == 9:
        return 51
    elif input == 8:
        return 46
    elif input == 7:
        return 41
    elif input == 6:
        return 36
    elif input == 5:
        return 31
    elif input == 4:
        return 26
    elif input == 3:
        return 21
    elif input == 2:
        return 16
    elif input == 1:
        return 11
    elif input == 0:
        return 6

def mint():
    # Mints the NFT
    nonce = w3.eth.getTransactionCount(public_address)

    txn = prometheans_contract.functions.mint().build_transaction({
        "nonce": nonce,
        "gas": 100000,
        "from": public_address,
        "maxFeePerGas": Web3.toWei(MAX_GAS_FEE, "gwei"),
        "maxPriorityFeePerGas": Web3.toWei(PRIORITY_FEE, "gwei"),
        "chainId": 1
    })

    signed_tx = w3.eth.account.sign_transaction(txn, PRIVATE_KEY)
    hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_receipt = w3.eth.wait_for_transaction_receipt(hash)
    return tx_receipt

def get_number():
    # Gets the ember id of the nft that was just minted
    minted_ids = get_minted_ids()
    id = minted_ids[-1]
    num = prometheans_contract.functions.emberOf(int(id)).call()
    return num

monk_1 = 0
monk_2 = 0
monk_3 = 0
monk_4 = 0
monk_5 = 0
monk_6 = 0
monk_7 = 0
monk_8 = 0
monk_9 = 0
monk_10 = 0
monk_11 = 0
monk_12 = 0
monk_13 = 0
monk_14 = 0
monk_15 = 0

embers = [prometheans_contract.functions.emberOf(int(id)).call() for id in get_minted_ids()]
# Loops through all of the previously minted ids and assigns them to a monk
for ember in embers:
    if ember in range(71, 76):
        monk_1 += 1
    elif ember in range(66, 71):
        monk_2 += 1
    elif ember in range(61, 66):
        monk_3 += 1
    elif ember in range(56, 61):
        monk_4 += 1
    elif ember in range(51, 56):
        monk_5 += 1
    elif ember in range(46, 51):
        monk_6 += 1
    elif ember in range(41, 46):
        monk_7 += 1
    elif ember in range(36, 41):
        monk_8 += 1
    elif ember in range(31, 36):
        monk_9 += 1
    elif ember in range(26, 31):
        monk_10 += 1
    elif ember in range(21, 26):
        monk_11 += 1
    elif ember in range(16, 21):
        monk_12 += 1
    elif ember in range(11, 16):
        monk_13 += 1
    elif ember in range(6, 11):
        monk_14 += 1
    elif ember in range(1, 5):
        monk_15 += 1

monks = [monk_15, monk_14, monk_13, monk_12, monk_11, monk_10, monk_9, monk_8, monk_7, monk_6, monk_5, monk_4, monk_3, monk_2, monk_1]

monk_positions = [pos for pos, monk_minted in enumerate(monks) if not monk_minted] # Filters out monks that are already minted and returns monks in their respective minting order

for position in reversed(monk_positions):
    while True:
        try:
            ember = prometheans_contract.functions.currentEmber().call()
            if int(ember) == get_mint_block(position):
                mint()
                time.sleep(25)
                number = get_number()
                print(f"MINTED MONK NUMBER {math.ceil(number / 5)}!")
                if number / (position + 1) <= 5:
                    break
                else:
                    continue
            else:
                time.sleep(1)
                pass
        except KeyboardInterrupt:
            sys.exit()
        except:
            print(sys.exc_info()[0])
