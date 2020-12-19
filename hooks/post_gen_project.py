import os

# In the template we named it `gitignore` so it does not interfere with
# the templates `.gitignore`.
# Rename gitignore -> .gitignore
os.rename("gitignore", ".gitignore")
