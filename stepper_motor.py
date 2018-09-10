from machine import Pin
import time


class StepperMotor(object):
    def __init__(self, p1, p2, p3, p4):
        self.debug = False
        self.half_step_delay = 2
        self.full_step_delay = 10
        #self.MODEL = model
        self.pins = list()
        self.pins.append(Pin(p1, Pin.OUT))
        self.pins.append(Pin(p2, Pin.OUT))
        self.pins.append(Pin(p3, Pin.OUT))
        self.pins.append(Pin(p4, Pin.OUT))
        self.signal_stepper(0, 0, 0, 0)

    def signal_stepper(self, *signals):
        if self.debug:
            print(self.pins, ":", signals)
        for p, s in zip(self.pins, signals):
            if s == 0:
                p.off()
            else:
                p.on()

    def half_step(self, direction=1):
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
        self._take_step(HALF_STEP, direction, self.half_step_delay)

    def full_step(self, direction=1):
        FULL_STEP = [
            [1, 0, 1, 0],
            [0, 1, 1, 0],
            [0, 1, 0, 1],
            [1, 0, 0, 1],
        ]
        self._take_step(FULL_STEP, direction, self.full_step_delay)

    def _take_step(self, step_matrix, direction, delay):
        for step in step_matrix:
            self.signal_stepper(*step[::direction])
            time.sleep_ms(delay)


if __name__ == "__main__":
    motor_pins = list()
    s = StepperMotor(16, 5, 4, 0)
