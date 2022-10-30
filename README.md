# Immutable X Chain Project

### Description

This code pulls down relevant God's Unchained collection data from the Immutable X chain found here: https://immutascan.io/address/0xacb3c6a43d15b907e8433077b6d38ae40936fe2c?tab=1&forSale=true


### What's the point? 

Unlike the f2p space, web3 has a dearth of central analytics reporting. It can be difficult to understand how chains are performing, let alone specific projects. The goal here is to productionalize the process of retrieving data from immutable x's top collection so that it can drive insights into the performance of the chain itself, as well as serve as a baseline for future web3 products. 


### Considerations 

1. To query data from multiple collections, a separate api call needs to be made. This, obviously will drastically slow down the performance of the program
2. Pulling data even for one collection takes some time. To get 1 days of data across the meaninful endpoints, it takes ~ 1 hour 


### Future Development Ideas 

1. Database integration 
2. Analysis across a large cross section of data 
3. Combining data with ETH-USD conversion 
4. Automating code execution (cron, EC2 instance, etc.) 
