# Pre-push hook for checking pep8 style convention
### First, make sure you have the Flake8 plugin installed!
### Create new empty folder and copy&paste the next commands through the terminal:
#### Getting a function to the user's local environment
 * git clone https://github.com/DimaKarpukhin/pre-push-hook.git
#### Creating a new empty file in the directory .git/hooks, which will provide a link to the pre-push hook
 * cd pre-push-hook && cat /dev/null > .git/hooks/pre-push
#### Providing symlink(symbolik link) to the hook and putting exec flag on pre-push.py file 
 * ln -s -f ../../pre-push.py .git/hooks/pre-push && chmod +x pre-push.py
