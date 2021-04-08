# Pre-push hook for checking pep8 style convention
### First, make sure you have the Flake8 plugin installed!
### Create new empty folder and copy&paste the next commands through the terminal:
### Getting a feature to the user's local environment
 * _git clone https://github.com/DimaKarpukhin/pre-push-hook.git_
### Creating a new empty file in the directory .git/hooks, which will provide a link to the pre-push hook
 * _cd pre-push-hook && cat /dev/null > .git/hooks/pre-push_
### Providing symlink(symbolik link) to the hook and putting exec flag on the pre-push.py file 
 * _ln -s -f ../../pre-push.py .git/hooks/pre-push && chmod +x pre-push.py_
