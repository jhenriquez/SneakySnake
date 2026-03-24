import atexit
import os

if os.name == "nt":
    import msvcrt
else:
    import sys
    import tty
    import termios
    import select

_old_settings = None


def setup_keyboard():
    """Put terminal in character-by-character mode for non-blocking input."""
    global _old_settings

    if os.name == "nt":
        return

    _old_settings = termios.tcgetattr(sys.stdin)
    tty.setcbreak(sys.stdin.fileno())
    atexit.register(restore_keyboard)


def restore_keyboard():
    """Restore terminal to normal mode."""
    global _old_settings

    if os.name == "nt":
        return

    if _old_settings is not None:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, _old_settings)
        _old_settings = None


def get_key_pressed():
    """Return "UP", "DOWN", "LEFT", "RIGHT", or None.

    Drains the input buffer and returns the *last* arrow key pressed,
    so the game loop always acts on the most recent input.
    """
    if os.name == "nt":
        return _read_key_windows()
    else:
        return _read_key_unix()


# -- Windows ------------------------------------------------------------------

def _read_key_windows():
    last_key = None
    while msvcrt.kbhit():
        ch = msvcrt.getch()
        if ch in (b"\xe0", b"\x00"):
            if msvcrt.kbhit():
                code = msvcrt.getch()
                if code == b"H":
                    last_key = "UP"
                elif code == b"P":
                    last_key = "DOWN"
                elif code == b"K":
                    last_key = "LEFT"
                elif code == b"M":
                    last_key = "RIGHT"
    return last_key


# -- macOS / Linux ------------------------------------------------------------

def _read_key_unix():
    last_key = None
    fd = sys.stdin.fileno()
    while select.select([fd], [], [], 0)[0]:
        ch = os.read(fd, 1)
        if ch == b"\x1b":
            if select.select([fd], [], [], 0)[0]:
                ch2 = os.read(fd, 1)
                if ch2 == b"[" and select.select([fd], [], [], 0)[0]:
                    ch3 = os.read(fd, 1)
                    if ch3 == b"A":
                        last_key = "UP"
                    elif ch3 == b"B":
                        last_key = "DOWN"
                    elif ch3 == b"D":
                        last_key = "LEFT"
                    elif ch3 == b"C":
                        last_key = "RIGHT"
    return last_key
