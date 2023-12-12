import streamlit as st
from nevermined import nevermined

# time/buyer: did:nv:94695d1a2f88f1de82ebff727185cc80def231ad7f974b1d46ebf961b9e76be9
# credits/owner (400 credits left): did:nv:f83ebdb36803ceca6ce0e7aa1e9cea1da7a0388dde03aac03c3bcbcb97497cc8
# credits/buyer: did:nv:4a72bef4b755094f70f40e17b9edf82ea0efafc466098b61a2a47ee9874d4251
# url = 'http://localhost:3000/streamlit?did=did:nv:4a72bef4b755094f70f40e17b9edf82ea0efafc466098b61a2a47ee9874d4251'

token = nevermined(did='did:nv:4a72bef4b755094f70f40e17b9edf82ea0efafc466098b61a2a47ee9874d4251')

print(token)
