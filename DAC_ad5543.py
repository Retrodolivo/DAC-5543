from tkinter import *
import spidev
import sys

max_code = 2**16
vref = 10

def reverse_bits(byte):
    byte = ((byte & 0xF0) >> 4) | ((byte & 0x0F) << 4)
    byte = ((byte & 0xCC) >> 2) | ((byte & 0x33) << 2)
    byte = ((byte & 0xAA) >> 1) | ((byte & 0x55) << 1)
    return byte

def set_vout(event):
    global max_code
    global vref
    vout = entry.get()
    if float(vout) > 10:
        vout = 10
    dac_code = max_code * float(vout) / vref

    print(int(dac_code))
    print(int(dac_code).to_bytes(2, "big"))
    dac_data_bytes = bytearray(int(dac_code).to_bytes(2, "big"))
    dac_spi.writebytes(dac_data_bytes)

dac_spi = spidev.SpiDev(1, 2) 
dac_spi.max_speed_hz = 1000000

root = Tk()
entry = Entry(root, width = 20, justify = "center")
button = Button(root, text = "Set")

button.bind("<Button-1>", set_vout)

entry.pack()
button.pack()


root.mainloop()
