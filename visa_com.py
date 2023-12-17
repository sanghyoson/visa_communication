import pyvisa
from pyvisa import ResourceManager, VisaIOError, constants
from pyvisa.resources import MessageBasedResource

# PSW30-36
ip_address = '192.168.0.xx'
port = 2268

rm = ResourceManager()
mode = 'tcpip'

if mode == 'tcpip':
    instruments = f'TCPIP::{ip_address}::{port}::SOCKET'
    inst = rm.open_resource(instruments, resource_pyclass=MessageBasedResource)
    inst.read_termination = '\n'
    inst.write_termination = '\n'
else:
    inst_list = rm.list_resources()
    inst = rm_usb.open_resource(inst_list[0])
    inst.read_termination = '\n'
    inst.write_termination = '\n'
    
print(inst.query("*IDN?"))
