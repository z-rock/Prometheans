# Prometheans
Python script that mints monks from the Prometheans project.  
Make sure you have the lastest version of Python and Web3.py installed on your device. https://web3py.readthedocs.io/en/v5/quickstart.html  
You'll need to manually input three items into the script for it to function.  
1) An ETH node HTTPS link (Line 8) https://medium.com/quiknode/what-is-quiknode-api-6fcfeef172f6 | https://www.infura.io/  
2) An Etherscan API key (Line 9) https://etherscan.io/apis
3) The private key for the wallet you want to use for minting (Line 13) https://metamask.zendesk.com/hc/en-us/articles/360015289632-How-to-Export-an-Account-Private-Key.  


The free tier apis have a cap on how many calls can be performed within a certain amount of time so if you are running this script for multiple days you need to keep an eye on it.  
Keep in mind that once the script reaches the more sought after monks you may be competing in a gas war to mint the monk. So feel free to make changes to the "MAX_GAS_FEE" and "PRIORITY_FEE" located at the top of the script.  
This script will not mint duplicates, even if you have minted monks prior to running the script. If you are interested in farming a certain monk or have any questions lmk.
