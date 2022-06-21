import os
import typer
import subprocess
import platform
import psutil

from time import sleep
from typing import List, Optional


# Common
VERSION = '0.3.0'
OS_INFO = {
    'name': os.name,  # 'posix'
    'system': platform.system(),  # 'Linux'
    'release': platform.release(),  # '4.15.0-29-generic'
    'machine': platform.machine(),  # 'x86_64'
    'node': platform.node(),  # 'ubuntu-18'
    'python_version': platform.python_version(),  # '3.9.9'
}

app = typer.Typer()


def no_support():
    if OS_INFO.get('system') == 'Windows':
        typer.echo(typer.style("This feature is not yet supported for windows", fg=typer.colors.GREEN, bold=True))
        raise typer.Exit()

    if OS_INFO.get('system') != 'Linux':
        typer.echo(typer.style("This feature only support Linux", fg=typer.colors.GREEN, bold=True))
        raise typer.Exit()


def path_nvm():
    os.system('export NVM_DIR="$HOME/.nvm"')
    os.system('[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"')
    os.system('[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"')


def version_callback(value: bool):
    if value:
        typer.echo(f"H_devops version {VERSION}")
        raise typer.Exit()


def title(message: str):
    print('                       ')
    print(f'{message}')
    print('                       ')


@app.command()
def version():
    """
    Show the version of the installation package.
    """
    typer.echo(f"H_devops version {VERSION}")


@app.command()
def health():
    """
    System health check
    """
    print('                       ')
    typer.echo(typer.style("CPU Information summary", fg=typer.colors.WHITE, bg=typer.colors.BLUE, bold=True))
    print('                       ')

    # gives a single float value
    vcc = psutil.cpu_count()
    print('Total number of CPUs :', vcc)

    vcpu = psutil.cpu_percent()
    print('Total CPUs utilized percentage :', vcpu, '%')

    print('                       ')
    typer.echo(typer.style("RAM Information summary", fg=typer.colors.WHITE, bg=typer.colors.BLUE, bold=True))
    print('                       ')
    # you can convert that object to a dictionary
    # print(dict(psutil.virtual_memory()._asdict()))
    # gives an object with many fields
    vvm = psutil.virtual_memory()

    x = dict(psutil.virtual_memory()._asdict())

    def forloop():
        for i in x:
            print(i, "--", x[i] / 1024 / 1024 / 1024)  # Output will be printed in GBs

    forloop()
    print('                       ')
    typer.echo(typer.style("RAM Utilization summary", fg=typer.colors.WHITE, bg=typer.colors.BLUE, bold=True))
    print('                       ')
    # you can have the percentage of used RAM
    print('Percentage of used RAM :', psutil.virtual_memory().percent, '%')
    # you can calculate percentage of available memory
    print('Percentage of available RAM :', psutil.virtual_memory().available * 100 / psutil.virtual_memory().total, '%')


@app.command()
def nvm(node: int = None):
    """
    Install Nvm (Node version Manager)
    """
    no_support()
    title('Install Nvm')
    try:
        os.system('sudo apt update && sudo apt install curl -y')
        os.system('curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash')
        path_nvm()
        typer.echo(typer.style("Done Install Nvm", fg=typer.colors.WHITE, bg=typer.colors.GREEN, bold=True,))

    except:
        typer.echo("Can't Install Nvm")
        raise typer.Exit(-1)


@app.command()
def info():
    """
    View system information
    """
    print('                       ')
    typer.echo(typer.style("System information", fg=typer.colors.WHITE, bg=typer.colors.BLUE, bold=True))
    print('                       ')
    typer.echo(OS_INFO)


@app.command()
def common_service():
    """
    Install Common Service
    """
    no_support()
    title('Install Common Service')
    typer.echo(typer.style("Oh it's really necessary for you", fg=typer.colors.GREEN, bold=True))
    print('                       ')
    try:
        os.system('sudo apt update && sudo apt install -y wget curl nano git apt-transport-https vim software-properties-common neofetch screenfetch htop net-tools zip unzip tree')
    except:
        typer.echo("Can't Install Common Service")
        raise typer.Exit(-1)


@app.command()
def net_tools():
    """
    Install Net-tools
    """
    no_support()
    print('                       ')
    print('Install Net-tools')
    print('                       ')
    try:
        os.system('sudo apt update && sudo apt install net-tools -y')
    except:
        typer.echo("Can't Install Net-tools")
        raise typer.Exit(-1)


@app.command()
def get_ip():
    """
    Get public ip
    """
    no_support()
    print('                       ')
    print('Get Public IP')
    print('                       ')
    try:
        os.system('curl -4 icanhazip.com')
    except:
        typer.echo("Can't get public ip")
        typer.echo(typer.style("Maybe you don't have curl installed", fg=typer.colors.YELLOW, bold=True))
        typer.echo(typer.style("Type the following command to install curl: 'h-devops curl'", fg=typer.colors.YELLOW, bold=True))
        raise typer.Exit()


@app.callback()
def main(v: Optional[bool] = typer.Option(
    None, "--v", callback=version_callback,
    help="Show the version of the installation package.")):
    """
    Thank you very much for downloading my packages. Welcome to the world !
    Author: Võ Hoàng
    """
    typer.echo("----------- H_devops -----------")


if __name__ == "__main__":
    app()
