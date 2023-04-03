# websocket Programming Testing

from SharekhanApi.sharekhanWebsocket import SharekhanWebSocket
access_token = "Your Access-Token"
params = {
    "access_token": access_token
}
action = 1
mode = 1

token_list = {"action": "subscribe", "key": ["feed"], "value": [""]}
feed = {"action": "feed", "key": ["depth"], "value": ["MX250715"]}

sws = SharekhanWebSocket(access_token)


def on_data(wsapp, message):
    print("Ticks: {}".format(message))


def on_open(wsapp):
    print("on open")
    # sws.subscribe(token_list)
    sws.fetchData(feed)
    # sws.unsubscribe(feed)


def on_error(wsapp, error):
    print(error)


def on_close(wsapp):
    print("Close")


# Assign the callbacks.
sws.on_open = on_open
sws.on_data = on_data
sws.on_error = on_error
sws.on_close = on_close

sws.connect()