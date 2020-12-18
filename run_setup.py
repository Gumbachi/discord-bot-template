import os
import subprocess

sep = os.path.sep

# Try to delete documentation files
try:
    os.remove("LICENSE")
except FileNotFoundError:
    pass

# rename project directory
project_name = os.path.basename(os.getcwd())
os.rename("ProjectName", project_name)

# create README
with open("README.md", "w") as f:
    f.write(f"# {project_name}")

# create env file
token = input("Enter Token >> ")
with open(".env", 'w') as f:
    f.write(token)

# install env
subprocess.call(["env_install.bat"])
os.remove("env_install.bat")

# add gitignore
with open(".gitignore", "w") as f:
    f.write("/env\n.env\n.vscode\n__pycache__/")

print("Finished.")
print("You can delete the run_setup.py file")
print("I would recommend adding a LICENSE file to the project as well")

input("Press any key to continue...")
