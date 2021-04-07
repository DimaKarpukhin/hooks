#!/usr/local/bin/python3

import subprocess
import color
import sys

"""
Installing pre-push Flake8 hook throug command line:
 1. cd hooks && cat /dev/null > .git/hooks/pre-push
 2. ln -s -f ../../pre-push.py .git/hooks/pre-push && chmod +x pre-push.py
"""


def main():
    flake8_path = '/usr/local/bin/flake8'
    result = subprocess.run([flake8_path], stdout=subprocess.PIPE)
    is_failed = result.stdout.decode('utf-8')
    if is_failed:
        print(color.BLUE + 'Flake8'
              + color.BLUE + ' ------------------------> '
              + color.FAILED + 'Failed!')
        print(
            f'{color.RED}Please correct following linting errors:')
        print(f'{color.FAILED}{result.stdout.decode("utf-8")}{color.RESET}')
        sys.exit(1)
    else:
        print(color.BLUE + 'Flake8'
              + color.BLUE + ' ------------------------> '
              + color.PASSED + 'Passed!')
        print(f"{color.GREEN}'git push' succeeded!{color.RESET}")
        sys.exit(0)


if __name__ == "__main__":
    main()
