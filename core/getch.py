import time
class _Getch:
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()
class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        key = msvcrt.getch()
        rus_sym = {'b\'\\xa2\'':"d",'b\'\\x82\'':"d",'b\'\\xeb\'':'s','b\'\\x9b\'':'s',
        'b\'\\xe4\'':'a', 'b\'\\x94\'':'a', 'b\'\\xe6\'':'w', 'b\'\\x96\'':'w',
        'b\'\\xe0\'':'h','b\'\\x90\'':'h','b\'\\xef\'':'z', 'b\'\\x9f\'':'z',
        'b\'\\xaf\'':'g','b\'\\x8f\'':'g','b\'\\xa4\'':'l', 'b\'\\x84\'':'l'}
        if str(key) in rus_sym.keys():
            key = rus_sym[str(key)]
        else:
            key = key.decode('utf-8')
        key = key.upper()
        return key

getch = _Getch()

def getch_():
	return getch()
