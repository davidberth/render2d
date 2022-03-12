from render2d.effect import Effect
import scipy.ndimage

class Blur(Effect):
    def __init__(self, standard_deviation):
        self.standard_deviation = standard_deviation

    def apply(self, buffer):
        height, width = buffer.shape[:2]

        std_y = self.standard_deviation * height
        std_x = self.standard_deviation * width

        for i in range(3):
            buffer[:, :, i] = scipy.ndimage.gaussian_filter(buffer[:,:,i], [std_y, std_x])
        return buffer

