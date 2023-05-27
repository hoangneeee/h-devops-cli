import os
import subprocess


def install_nvm():
    # Define the installation directory for NVM
    install_dir = os.path.expanduser("~/.nvm")

    # Clone the NVM repository
    subprocess.run(["git", "clone", "https://github.com/nvm-sh/nvm.git", install_dir])

    # Add NVM initialization to the user's shell profile file
    init_command = """
    export NVM_DIR="{install_dir}"
    [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
    [ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
    """.format(install_dir=install_dir)

    shell_profile = os.path.expanduser("~/.bash_profile")  # Change this if using a different shell profile file
    with open(shell_profile, "a") as f:
        f.write(init_command)

    # Reload the shell profile
    subprocess.run(["source", shell_profile], shell=True)
