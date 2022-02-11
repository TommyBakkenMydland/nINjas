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
    
    button = board.digital[2] 
    LED =board.digital[13]
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

       
        LED.write(button.read())
       