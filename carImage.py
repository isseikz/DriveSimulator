import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage
from scipy import misc

class CarImage(object):
    """docstring for CarImage."""
    def __init__(self, filename='./topview_car_wagon.png'):
        super(CarImage, self).__init__()
        # TODO: 画像表示・更新方法の作成

        # originalImage =  misc.imread(filename)
        # imshow(originalImage)
        # oiShape = np.shape(originalImage)
        # rate = oiShape[1] // 80
        # image = originalImage // rate
        # print(np.shape(image))
        self.fig = plt.figure()

        plt.rcParams['keymap.fullscreen'] = ''
        plt.rcParams['keymap.home'] = ''
        plt.rcParams['keymap.back'] = ''
        plt.rcParams['keymap.forward'] = ''
        plt.rcParams['keymap.pan'] = ''
        plt.rcParams['keymap.zoom'] = ''
        plt.rcParams['keymap.save'] = ''
        plt.rcParams['keymap.quit'] = ''
        plt.rcParams['keymap.grid'] = ''
        plt.rcParams['keymap.yscale'] = ''
        plt.rcParams['keymap.xscale'] = ''
        plt.rcParams['keymap.all_axes'] = ''
        plt.rcParams['keymap.yscale'] = ''


    def updateFrom(self, state):
        print(state)
        # 車の回転
        # 座標の移動(x)(常に車道に対する前後方向位置が座標の中心にある)
        # 座標の移動(y)
        # 画像の更新
        plt.scatter(state[0],state[1])
        plt.ylim([-10,10])
        plt.pause(.01)
        pass

if __name__ == '__main__':
    # car = CarImage()

    # plt.imshow(car.image)
    # plt.show()
    pass
