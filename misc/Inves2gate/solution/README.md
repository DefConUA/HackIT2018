Part 1: https://ropsten.etherscan.io/tx/0xb61227a91466026ea2f2670bd7725ac00bd7eb198ed71799ecadb6de3647f91e
(flag{5cann1ng_)

Part 2: https://ropsten.etherscan.io/tx/0xc02fc19b9c2587af1d1aab6aef9093f4b5fca6a0731e373ab4b584bb15a0170e
(wh013_bl0ckch41n_4)

Part 3: https://ropsten.etherscan.io/tx/0x1bc37a84ae691623c4043457fd3084044354ee656d349213fd63e5da1450ac9e
The contract 0xb4c5ef28a38ffbd1095cc8d1ba947fb0e9a61e4a has storage which needs to be leaked
web3.eth.getStorageAt('0xb4c5ef28a38ffbd1095cc8d1ba947fb0e9a61e4a', 1, function(x, y) {alert(web3.toAscii(y))});
(ctf_fl4g_i5_4_skill)

Part 4: https://ropsten.etherscan.io/tx/0xd4e690ebfeabc1d61fabc2eda20df666633d9caf466f3e0dafdcc5616035df52
https://ropsten.etherscan.io/address/0x0ea92008f4ccc6295e99908e35469fe9ca63787d
web3.eth.getStorageAt('0x0ea92008f4ccc6295e99908e35469fe9ca63787d', 0, function(x, y) {alert(web3.toAscii(y))});
(_to_nuture})

overall : flag{5cann1ng_wh013_bl0ckch41n_4ctf_fl4g_i5_4_skill_to_nuture}