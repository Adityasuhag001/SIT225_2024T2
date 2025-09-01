# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.17.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
"""
    Ahsan Habib (habib@deakin.edu.au),
    School of Information Technology,
    Deakin University, Australia.
"""

import serial
import random

# set baud rate, same speed as set in your Arduino sketch.
boud_rate = 9600

# set serial port as suits your operating system
s = serial.Serial("/dev/cu.usbmodem1101", boud_rate, timeout=5)

while True:  # infinite loop, keep running

    #  a random number between 5 and 50.
    data_send = random.randint(5, 50)

    # write to serial port, set data encoding. 
    # Raw bytes are sent through serial ports, Python bytes() needs 
    # to know the encoding to generate bytes from string.
    # 
    # We send a single integer which is read from Arduino sketch.
    # 
    d = s.write(bytes(str(data_send), 'utf-8'))
    print(f"Send >>> {data_send} ({d} bytes)")

    # Read from serial port. 
    # 
    # readline keeps reading until a newline found in the data stream.
    # Unlike write above, we just send an integer with no newline.
    # You should receive data the same way as it is sent.
    # 
    d = s.readline().decode("utf-8")
    print(f"Recv <<< {d}")

# %%
