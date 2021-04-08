# Pre-push hook for checking pep8 style convention
Be sure you have Flake8 plugin installed
### Installing throug command line(copy & paste):
 * git clone https://github.com/DimaKarpukhin/pre-push-hook.git
 * cd pre-push-hook && cat /dev/null > .git/hooks/pre-push
 * ln -s -f ../../pre-push.py .git/hooks/pre-push && chmod +x pre-push.py
