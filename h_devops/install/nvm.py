import os
import subprocess


def install_nvm():
    try:
        # Define the installation directory for NVM
        install_dir = os.path.expanduser("~/.nvm")

        # Clone the NVM repository
        os.system(
            'curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash')

        # Add NVM initialization to the user's shell profile file
        init_command = """
        export NVM_DIR="{install_dir}"
        [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
        [ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
        """.format(install_dir=install_dir)

        # Change this if using a different shell profile file
        shell_profile = os.path.expanduser("~/.bashrc")
        with open(shell_profile, "a") as f:
            f.write(init_command)

        # Reload the shell profile
        # subprocess.run(["source", shell_profile], shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred during NVM installation: {e}")
