bluetooth.onBluetoothConnected(function () {
    basic.showIcon(IconNames.Yes)
})
bluetooth.onBluetoothDisconnected(function () {
    basic.showIcon(IconNames.No)
})
bluetooth.startAccelerometerService()
basic.showIcon(IconNames.Happy)
basic.forever(function () {
	
})
