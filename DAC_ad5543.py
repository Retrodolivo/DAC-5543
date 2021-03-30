################################
## GUI Module is controlling DAC ad5543  
################################

import tkinter as tk
import spidev

#_______________DEFINES_________________
MAX_CODE = 2**16
VREF = 10.0

def reverse_bits(byte):
    byte = ((byte & 0xF0) >> 4) | ((byte & 0x0F) << 4)
    byte = ((byte & 0xCC) >> 2) | ((byte & 0x33) << 2)
    byte = ((byte & 0xAA) >> 1) | ((byte & 0x55) << 1)
    return byte

def set_vout(event):
    vout = entry.get()
    dac_code = MAX_CODE * float(vout) / VREF
    print(int(dac_code))
    print(int(dac_code).to_bytes(2, "big"))
    dac_data_bytes = bytearray(int(dac_code).to_bytes(2, "big"))
    dac_spi.writebytes(dac_data_bytes)
    
#_____________DEFINES END________________
if __name__ == "__main__":
    win = tk.Tk()
    entry = tk.Entry(win, width = 20, justify = "center")
    button = tk.Button(win, text = "Set")

    dac_spi = spidev.SpiDev(1, 2) 
    dac_spi.max_speed_hz = 1000000
    
    button.bind("<Button-1>", set_vout)

    entry.pack()
    button.pack()

    win.mainloop()
