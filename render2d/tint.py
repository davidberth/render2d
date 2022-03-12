from render2d.effect import Effect
import numpy as np

class Tint(Effect):
    def __init__(self, tint_color, tint_strength):
        self.tint_color = np.array(tint_color)
        self.tint_strength = np.array(tint_strength)

    def apply(self, buffer):
        buffer[:, :, :3] = buffer[:, :, :3] * (1 - self.tint_strength) + self.tint_color * self.tint_strength
        return buffer
