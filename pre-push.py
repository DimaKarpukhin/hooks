#!/usr/local/bin/python3

import subprocess
import colors
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
        print(
            f'{colors.BLUE}Flake8 -------------> {colors.FAILED}Failed!')
        print(f'{colors.RED}Please correct following linting errors:')
        print(f'{colors.FAILED}{result.stdout.decode("utf-8")}{colors.RESET}')
        sys.exit(1)
    else:
        print(
            f'{colors.BLUE}Flake8 -------------> {colors.PASSED}Passed!')
        print(f"{colors.GREEN}'git push' succeeded!{colors.RESET}")
        sys.exit(0)


if __name__ == "__main__":
    main()
