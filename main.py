# blake use this function instead of print
# make sure you import time and sys like this
import time, sys

# Put this at the beginning of both files
def print_out(text):
    i = 0
    while i < len(text):
        print(text[i], end="")
        # time is in seconds. This is pretty fast, feel free to adjust
        time.sleep(0.01)
        i += 1
        sys.stdout.flush()

print_out("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")