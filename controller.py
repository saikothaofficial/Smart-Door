from pyfirmata import Arduino,SERVO

port = 'COM3'

board = Arduino(port)

pin = 10

board.digital[pin].mode = SERVO


def rotateServo(pin,angle):
    board.digital[pin].write(angle)


def doorAutomate(val):
    if val == 'Mask':
        print('[DOOR OPENED]...')
        rotateServo(pin,120)
    elif val == 'No Mask':
        print('[DOOR CLOSED]...')
        rotateServo(pin,0)


    

