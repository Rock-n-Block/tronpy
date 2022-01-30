import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, *[os.pardir] * 2)))

from tronpy import Tron
from tronpy.exceptions import AddressNotFound
from tronpy.providers import HTTPProvider
from pprint import pprint


client = Tron(HTTPProvider('https://nile.trongrid.io'))

contract = client.get_contract('TUb1dQS6mH9GRtJFCQzodsHawGin22JX2t')
    
events = contract.get_events('TransferToOtherBlockchain', 20657300, 20657400)
print(events)
