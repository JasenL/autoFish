import math
import random
from ctypes import windll  # 获取屏幕上某个坐标的颜色
from time import sleep

import keyboard
import pyautogui


def get_color(x, y):
    gdi32 = windll.gdi32
    user32 = windll.user32
    hdc = user32.GetDC(None)  # 获取颜色值
    pixel = gdi32.GetPixel(hdc, x, y)  # 提取RGB值
    r = pixel & 0x0000ff
    g = (pixel & 0x00ff00) >> 8
    b = pixel >> 16
    return [r, g, b]


def run(pos):
    pyautogui.FAILSAFE = True  # 鼠标移动左上角终止程序
    sleep(10)
    previous_color = get_color(pos.x, pos.y)
    while judge != 0:
        k = 1
        keyboard.press_and_release('1')
        while judge != 0 and k == 1:
            color = get_color(pos.x, pos.y)  # 获取指定位置的色值
            sim = ColourDistance(previous_color, color)
            if sim > 200:
                k = 0
                print('tuple(np.array(' + '{}'.format(color) + ')/255)-' + '{}'.format(pos))
                sleep(random.randint(1, 2) + random.random())
                keyboard.press_and_release('2')

            sleep(0.1)
        sleep(random.randint(1, 4) + random.random())


def ColourDistance(rgb_1, rgb_2):
    R_1, G_1, B_1 = rgb_1
    R_2, G_2, B_2 = rgb_2
    rmean = (R_1 + R_2) / 2
    R = R_1 - R_2
    G = G_1 - G_2
    B = B_1 - B_2
    return math.sqrt((2 + rmean / 256) * (R ** 2) + 4 * (G ** 2) + (2 + (255 - rmean) / 256) * (B ** 2))


def out():
    global judge
    judge = 0


def getPos():
    pos = pyautogui.position()  # 获取鼠标当前的位置
    return pos


def clear():
    pass


if __name__ == '__main__':
    judge = 1
    keyboard.add_hotkey('esc', out)
    # recorded = keyboard.record(until='esc')
    # keyboard._hotkeys = {}
    sleep(0.5)

    # if not 'pos' in locals():
    print("请先按alt选颜色点,然后按ctrl 10s后开始")
    keyboard.wait('alt')
    pos = getPos()
    print("获取点位为：" + '{}'.format(pos))
    keyboard.wait('ctrl')

    run(pos)
