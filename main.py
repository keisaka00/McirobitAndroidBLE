def on_bluetooth_connected():
    basic.show_icon(IconNames.YES)
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_bluetooth_disconnected():
    basic.show_icon(IconNames.NO)
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)

bluetooth.start_accelerometer_service()
basic.show_icon(IconNames.HAPPY)

def on_forever():
    pass
basic.forever(on_forever)
