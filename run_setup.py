import os
import subprocess

sep = os.path.sep

# Try to delete documentation files
try:
    os.remove("LICENSE")
except FileNotFoundError:
    pass

# rename project directory
while True:
    project_name = input("Name the project >> ")

    try:
        os.rename("ProjectName", project_name)
        break
    except FileExistsError:
        print("Folder already exists, please remove it and try again")
    except FileNotFoundError:
        print("Probably an invalid name. Please use a better name")

with open("README.md", "w") as f:
    f.write(f"# {project_name}")

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
