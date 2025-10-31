import dht
import machine

high_temp = 72 # temp where it turns off
low_temp = 68  # temp where it turns on

sensor = dht.DHT11(machine.Pin(4))
relay_pin = machine.Pin(5, machine.Pin.PULL_UP)

target_state = 0 # closed circuit = 1, open circuit = 0
current_state = 0

def get_temp():
    temp_c = sensor.temperature()
    return (temp_c * 9 / 5) + 32

def get_state(temp_f):
    if temp_f >= high_temp:
        set_relay(current_state, 0)
    elif temp_f <= low_temp:
        set_relay(current_state, 1)
    else:
        set_relay(current_state, 0)

def set_relay(current_state, target_state):
    if current_state == target_state & current_state == 1:
        relay_pin.on()
    else:
        relay_pin.off()
    current_state = target_state
