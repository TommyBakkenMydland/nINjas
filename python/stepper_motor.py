#!/usr/bin/env python3

import pyfirmata
import time

if __name__ == '__main__':
    # Initiate communication with Arduino
    board = pyfirmata.Arduino("/dev/ttyACM0")
    print("Communication Successfully started")
    
    # Create bunch of useful variables
    button = board.digital[4]
    LED = board.digital[13]
    
    button_states = [1, 1, 1, 1, 1, 1, 1, 0, 0, 0] 
    
    # Start iterator to receive input data
    it = pyfirmata.util.Iterator(board)
    it.start()

    # Setup LEDs and button
    button.mode = pyfirmata.INPUT
    previous_button_state = 0
    index = 0
    LED.write(0)

    # The "void loop()"
    while True:
        # We run the loop at 100Hz
        time.sleep(0.01)
        
        if index > 9:
            index = 0

        # Get button current state
        button_state = button.read()
        button_states[index] = button_state
        
        # Check if button has been released
        if button_state == 0 and all(state == button_state for state in button_states):
            # and power on next LED
            print("press")
            for i in range(0, len(button_states)):
                button_states[i] = True
            time.sleep(1)
        
        index += 1

