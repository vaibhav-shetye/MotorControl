from machine import Pin


class StepperMotor(object):
    def __init__(self, p1, p2, p3, p4):
        #self.MODEL = model
        self.pins = list()
        self.pins.append(Pin(p1, Pin.OUT))
        self.pins.append(Pin(p2, Pin.OUT))
        self.pins.append(Pin(p3, Pin.OUT))
        self.pins.append(Pin(p4, Pin.OUT))
        self.signal_stepper(0,0,0,0)

    def signal_stepper(self, *signals):
        for p, s in zip(self.pins, signals):
            print(p, " : ", s, end=', ')
            if s == 0:
                p.off()
            else:
                p.on()

    def half_step(self):
        HALF_STEP = [
            [0, 0, 0, 1],
            [0, 0, 1, 1],
            [0, 0, 1, 0],
            [0, 1, 1, 0],
            [0, 1, 0, 0],
            [1, 1, 0, 0],
            [1, 0, 0, 0],
            [1, 0, 0, 1],
        ]
        for step in HALF_STEP:
            self.signal_stepper(*step)

    def full_step(self):
        FULL_STEP = [
            [1, 0, 1, 0],
            [0, 1, 1, 0],
            [0, 1, 0, 1],
            [1, 0, 0, 1],
        ]
        for step in FULL_STEP:
            self.signal_stepper(*step)


if __name__ == "__main__":
    motor_pins = list()
    s = StepperMotor(16, 5, 4, 0)
