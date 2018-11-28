import websocket
try:
    import thread
except ImportError:
    import _thread as thread
import time


def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print("error",error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    print("started ........")

def creat_socket():
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://192.168.1.4:8000/call/",
                              on_open = on_open,
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.run_forever()
    return ws