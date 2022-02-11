import time
import pyfirmata
import StepperLib
import time
import datetime
import imageprocessor

#'COM3' is the USB port mine was plugged into
board = pyfirmata.Arduino("/dev/ttyACM0") # remember to go to arduino ide, examples, firmata, standard firmata
reader = pyfirmata.util.Iterator(board)
reader.start()


if __name__ == '__main__':
    # Initiate communication with Arduino
    board = pyfirmata.Arduino("/dev/ttyACM0")
    print("Communication Successfully started")
    
    # Create bunch of useful variables
    button = board.digital[4]
    
    button_states = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] 
    button_pressed_at = time.time()
    # Start iterator to receive input data
    it = pyfirmata.util.Iterator(board)
    it.start()
    button.mode = pyfirmata.INPUT
    index = 0    
    motor = StepperLib.Stepper(2038, board, reader, 8, 9, 10, 11)
    motor.set_speed(5)

    while True:
        motor.step(5)
        time.sleep(0.01)
        
        if index > 9:
            index = 0

        button_state = button.read()
        button_states[index] = button_state
        
        if button_pressed_at < time.time() - 5 and button_state == 0 and all(state == 0 for state in button_states):
            imageprocessor.AnalyseImage()
            print("press")
            button_pressed_at = time.time()
            for i in range(0, len(button_states)):
                button_states[i] = True

        index += 1