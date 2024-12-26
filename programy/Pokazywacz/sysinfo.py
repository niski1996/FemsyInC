import ctypes


def main_window_position(wys, szer):
    user32 = ctypes.windll.user32
    firstscreen = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    secscreen = user32.GetSystemMetrics(78), user32.GetSystemMetrics(79)
    if secscreen != firstscreen:
        return secscreen[0] - szer, 0
    else:
        return firstscreen[0] - szer, 0
