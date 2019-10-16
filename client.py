import asyncio
import time

import websockets
'''
async def hello(uri):
    async with websockets.connect(uri) as websocket:
        await websocket.send("1NDpZ2wyFekVezssSXv2tmQgmxcoHMUJ7u")
        await websocket.recv()

asyncio.get_event_loop().run_until_complete(
    hello('wss://ws.blockchain.info/inv'))
'''
async def main():
    websocket_address='wss://ws.blockchain.info/inv'
    bitcoin_address="1NDpZ2wyFekVezssSXv2tmQgmxcoHMUJ7u"
    async with websockets.connect(websocket_address) as websocket:
        i=1
        while i<=2:
            try:
                #a = readValues() #read values from a function
               # insertdata(a) #function to write values to mysql

                #await websocket.send({"op":"addr_sub", "addr":bitcoin_address})
                await websocket.send("""{"op":"ping"}""")

                res = websocket.recv()
                print(res)
                await asyncio.sleep(2)
                #res1=websocket.data_received()

                #print(websocket.response_headers)


                time.sleep(20) #wait and then do it again

            except Exception as e:
                print(e)

asyncio.get_event_loop().run_until_complete(main())



'''
1NDpZ2wyFekVezssSXv2tmQgmxcoHMUJ7u (SatoshiDICE Hot Wallet )	397265
18uvwkMJsg9cxFEd1QDFgQpoeXWmmSnqSs (SatoshiDICE Hot Wallet )	397148
14719bzrTyMvEPcr7ouv9R8utncL9fKJyf (SatoshiDICE Hot Wallet )	397096
'''

'''
try:
    import thread
except ImportError:
    import _thread as thread
import time

def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    def run(*args):
        for i in range(3):
            time.sleep(1)
            ws.send("Hello %d" % i)
        time.sleep(1)
        ws.close()
        print("thread terminating...")
    thread.start_new_thread(run, ())


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://echo.websocket.org/",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()

'''