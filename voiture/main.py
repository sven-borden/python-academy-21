import random
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from kivy.app import App
from kivy.clock import Clock
from kivy.config import Config
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.vector import Vector

from controller_widgets import SignalBack, SignalFront, Robot, Goal
from dqn import Dqn

# Adding this line if we don't want the right click to put a red point
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
Window.size = (1280, 720)

n_points = 0
length = 0
goal_reached_nb = 0
last_reward = 0
last_action = 0
last_distance = 0
last_orientation = 0
last_nb_steps = 1e5
cum_rewards = 0
scores = []
steps_memory = []
seq_change_memory = []
first_update = True


def init():
    global goal_x
    global goal_y
    global first_update
    global scorelabel
    goal_x = 150
    goal_y = height - 150
    first_update = False


list_actions = [
    [6, 0, 0],
    [6, 0, 10],
    [6, 0, -10]
]
print(f'Number of actions : {len(list_actions)}')
model = Dqn(5, len(list_actions), 0.9)


class Game(Widget):
    robot = Robot()
    signal1 = SignalFront()
    signal2 = SignalFront()
    signal3 = SignalFront()
    goal = Goal()

    def serve_robot(self):
        self.robot.center = self.center
        self.robot.angle = 0
        self.robot.velocity = Vector(1, 0)

    def update(self, time_interval):

        global model
        global last_reward
        global cum_rewards
        global scores
        global last_distance
        global last_orientation
        global goal_x
        global goal_y
        global width
        global height

        width = self.width
        height = self.height
        if first_update:
            self.steps = 0
            self.last_steps = 0
            self.seq_change = 0
            init()

        xx = goal_x - self.robot.x
        yy = goal_y - self.robot.y
        orientation = Vector(*self.robot.velocity).angle((xx, yy))/180.

        last_signal = [
            self.robot.signal1, self.robot.signal2, self.robot.signal3,
            orientation, -orientation
        ]

        action = model.update(last_reward, last_signal)
        scores.append(model.score())
        displacement = list_actions[action]
        self.robot.move(displacement, width, height)
        distance = np.sqrt((self.robot.x - goal_x)**2 + (self.robot.y - goal_y)**2)
        self.signal1.pos = self.robot.sensor1
        self.signal2.pos = self.robot.sensor2
        self.signal3.pos = self.robot.sensor3
        self.goal.pos = Vector(goal_x, goal_y)

        self.steps += 1

        self.robot.velocity = Vector(1, 0).rotate(self.robot.angle)
        last_reward = (last_distance - distance) / 6

        # score based also on orientation
        #  last_reward += (1-abs(orientation)) * 0.9
        if abs(last_orientation) < abs(orientation):
            last_reward -= 0.2
        elif abs(last_orientation) == abs(orientation):
            last_reward += 0.
        else:
            last_reward += 0.2
        # Score also based on sequence change
        # global last_action
        # if list_actions[last_action][0] == list_actions[action][0]:
        #     last_reward += 0.02
        # else:
        #     self.seq_change += 1

        # last_action = action

        if self.robot.x < 10:
            self.robot.x = 10
            last_reward = -50  # too close to edges of the wall reward
        if self.robot.x > self.width - 10:
            self.robot.x = self.width - 10
            last_reward = -50
        if self.robot.y < 10:
            self.robot.y = 10
            last_reward = -50
        if self.robot.y > self.height - 10:
            self.robot.y = self.height - 10
            last_reward = -50

        if distance < 50:
            global goal_reached_nb
            global steps_memory
            global seq_change_memory
            global last_nb_steps
            goal_reached_nb += 1
            if goal_reached_nb <= 50000:
                goal_x = self.width-goal_x
                goal_y = self.height-goal_y
                steps_memory.append(self.steps)
                seq_change_memory.append(self.seq_change)
                last_reward = self.last_steps - self.steps  # reward for reaching the objective faster than last round
                if len(steps_memory) % 5 == 0:
                    _, axs = plt.subplots(1, 1)
                    i = range(len(steps_memory))
                    axs.plot(i, steps_memory, 'r-', label='steps')
                    axs.plot(i, seq_change_memory, 'b-', label='sequence change')
                    axs.set_title('# steps and # sequence change to reach goal')
                    axs.set_xlabel('iteration')
                    axs.set_ylabel('#')
                    axs.legend()
                    plt.savefig(f'{Path(__file__).resolve().parent}/perf.png')
                    merged_list = [i, steps_memory, seq_change_memory]
                    df = pd.DataFrame(np.array(merged_list).T, columns=['iteration', 'steps', 'sequence switch'])
                    df.to_csv(f'{Path(__file__).resolve().parent}/perf.csv')
            else:
                goal_x = random.randint(10, width-10)
                goal_y = random.randint(10, height-10)

            self.last_steps = self.steps
            last_nb_steps = self.steps
            self.steps = 0
            self.seq_change = 0
            cum_rewards = 0

        cum_rewards += last_reward
        last_distance = distance
        global scorelabel
        scorelabel.text = 'Last run steps : {:.0f}\nReward : {:.1f}\nSequence : {}\nGoals completed : {}'.format(
            last_nb_steps,
            cum_rewards,
            list_actions[action][0],
            goal_reached_nb
        )


class RobotApp(App):

    def build(self):
        parent = Game()
        parent.serve_robot()
        Clock.schedule_interval(parent.update, 1.0/120.0)
        savebtn = Button(text='save', pos=(0, 0))
        loadbtn = Button(text='load', pos=(parent.width, 0))
        savebtn.bind(on_release=self.save)
        loadbtn.bind(on_release=self.load)

        global scorelabel
        scorelabel = Label(
            text="Score",
            pos=(0.3 * parent.width, 2 * parent.height),
            halign="left",
            size_hint=(1.0, 1.0)
        )
        scorelabel.bind(size=scorelabel.setter('text_size'))
        parent.add_widget(scorelabel)
        parent.add_widget(savebtn)
        parent.add_widget(loadbtn)
        return parent

    def save(self, obj):
        model.save()
        print("Saved model")
        plt.plot(scores)
        plt.show()

    def load(self, obj):
        model.load()
        print("Loaded model")


# Running the whole thing
if __name__ == '__main__':
    RobotApp().run()
