"""
Env 2D
@author: huiming zhou
"""


class Env:
    def __init__(self):
        self.x_range = 41  # size of background
        self.y_range = 61
        self.motions = [(-1, 0), (-1, 1), (0, 1), (1, 1),
                        (1, 0), (1, -1), (0, -1), (-1, -1)]
        self.obs = self.obs_map()

    def update_obs(self, obs):
        self.obs = obs

    def obs_map(self):
        """
        Initialize obstacles' positions
        :return: map of obstacles
        """

        x = self.x_range
        y = self.y_range
        obs = set()

        for i in range(18, x):
            obs.add((i, 0))
            
        for i in range(19):
            obs.add((i, y - 1))
            
        for i in range(41):
            obs.add((18, i))
            
        for i in range(19):
            obs.add((i, 41))
            
        for i in range(41, y):
            obs.add((0, i))
            
        for i in range(55, y):
            obs.add((18, i))
            
        for i in range(18, 30):
            obs.add((i, 55))
            
        for i in range(32):
            obs.add((x - 1, i))
            
        for i in range(32, 55):
            obs.add((29, i))
            
        for i in range(29, x):
            obs.add((i, 32))

        return obs

