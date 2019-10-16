from websocket import create_connection
from ConsoleNotify import notify
try:
    import thread
except ImportError:
    import _thread as thread
import time


def run(address):
    #time.sleep(50)
    address ="unconfirmed_sub" # Remove this after getting the list of active addresses.

    ws = create_connection("wss://ws.blockchain.info/inv")
    ws.send("""{"op":"""+address+"""}""")
    '''
        Setup rules of engagement with the websocket 
    '''
    '''
    Create a Long Websocket Listen connection after active addresses. 
    '''
    #ws.send("""{"op":"addr_sub","addr":""" + address + """}""")
    while True:
        tx = ws.recv()
        print(tx)
        with open("walletAddressInfo.json", "a") as f:
            f.write(tx + "\n")
            '''
            Some rules for the notification, what sort of alerts and on what purposes we need them 
            '''
            time.sleep(10)
            notify(address)
    time.sleep(1)
    ws.close()
    print("thread terminating...")


addresses = ['34xp4vRoCGJym3xR7yCVPFHoCNxv4Twseo','3KF9nXowQ4asSGxRRzeiTpDjMuwM2nypAN']
for a in addresses:
    thread.start_new_thread(run(a), ())
