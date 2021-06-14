import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)

    def draw(self, num):
        drawn = []
        if num >= len(self.contents):
            return self.contents
        else:
            for i in range(num):
                drawn.append(self.contents.pop(self.contents.index(random.choice(self.contents))))
        return drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    hits = 0
    for _ in range(num_experiments):
        is_hit = True
        experiment_hat = copy.deepcopy(hat)
        experiment_list = experiment_hat.draw(num_balls_drawn)
        for key, value in expected_balls.items():
            if key not in experiment_list:
                is_hit = False
                break
            count = 0
            for ball in experiment_list:
                if ball == key: count+= 1
            if count < value:
                is_hit = False
                break
        if is_hit: hits += 1
    return hits / num_experiments
