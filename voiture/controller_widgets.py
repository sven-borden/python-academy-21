from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.uix.widget import Widget
from kivy.vector import Vector
import numpy as np

class Robot(Widget):
    angle = NumericProperty(0)
    rotation = NumericProperty(0)
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    sensor1_x = NumericProperty(0)
    sensor1_y = NumericProperty(0)
    sensor1 = ReferenceListProperty(sensor1_x, sensor1_y)
    sensor2_x = NumericProperty(0)
    sensor2_y = NumericProperty(0)
    sensor2 = ReferenceListProperty(sensor2_x, sensor2_y)
    sensor3_x = NumericProperty(0)
    sensor3_y = NumericProperty(0)
    sensor3 = ReferenceListProperty(sensor3_x, sensor3_y)

    signal1 = NumericProperty(0)
    signal2 = NumericProperty(0)
    signal3 = NumericProperty(0)


    def sensor_value(self, sensorx, sensory, width, height):
        if sensorx > width-10 or sensorx < 10 or sensory > height-10 or sensory < 10:
            return 1.
        return 0.

    def move(self, displacement, sand, width, height):

        # Update self.pos
        # Update rotation
        # Update angle


        self.sensor1 = Vector(30, 0).rotate(self.angle) + self.pos
        self.sensor2 = Vector(30, 0).rotate((self.angle+30) % 360) + self.pos
        self.sensor3 = Vector(30, 0).rotate((self.angle-30) % 360) + self.pos

        self.signal1 = int(np.sum(sand[int(self.sensor1_x)-10:int(self.sensor1_x)+10, int(self.sensor1_y)-10:int(self.sensor1_y)+10]))/400.
        self.signal2 = int(np.sum(sand[int(self.sensor2_x)-10:int(self.sensor2_x)+10, int(self.sensor2_y)-10:int(self.sensor2_y)+10]))/400.
        self.signal3 = int(np.sum(sand[int(self.sensor3_x)-10:int(self.sensor3_x)+10, int(self.sensor3_y)-10:int(self.sensor3_y)+10]))/400.

        self.signal1 = self.sensor_value(self.sensor1_x, self.sensor1_y, width, height)
        self.signal2 = self.sensor_value(self.sensor2_x, self.sensor2_y, width, height)
        self.signal3 = self.sensor_value(self.sensor3_x, self.sensor3_y, width, height)


class Goal(Widget):
    pass


class SignalFront(Widget):
    pass


class SignalBack(Widget):
    pass
