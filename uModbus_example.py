from umodbus.serial import Serial as ModbusRTUMaster

host = ModbusRTUMaster(
    pins=(25, 26),      # given as tuple (TX, RX), check MicroPython port specific syntax
    # baudrate=9600,    # optional, default 9600
    # data_bits=8,      # optional, default 8
    # stop_bits=1,      # optional, default 1
    # parity=None,      # optional, default None
    # ctrl_pin=12,      # optional, control DE/RE
    # uart_id=1         # optional, see port specific documentation
)

# address of the target/client/slave device on the bus
slave_addr = 10
coil_address = 123
coil_qty = 1

coil_status = host.read_coils(
    slave_addr=slave_addr,
    starting_addr=coil_address,
    coil_qty=coil_qty)
print('Status of coil {}: {}'.format(coil_address, coil_status))