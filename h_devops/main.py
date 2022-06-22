import os
import typer
import subprocess
import platform
import psutil

from time import sleep
from tabulate import tabulate
from typing import List, Optional

# Common
VERSION = '0.3.1'
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


def style(message: str, type: str):
    if (type == 'green'):
        return typer.style(f"{message}", fg=typer.colors.GREEN, bold=True)
    if (type == 'header'):
        return typer.style(f"{message}", fg=typer.colors.BLUE, bold=True)
    if (type == 'error'):
        return typer.style(f"{message}", fg=typer.colors.RED, bold=True)


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
    vcpu = psutil.cpu_percent()
    # Table
    headers1 = [style("ID", 'header'), style("Name", 'header'), style("Value", 'header')]
    table1 = [[0, "Total number of CPUs ", vcc], [1, "Total CPUs utilized percentage ", f"{vcpu} %"]]
    typer.echo(tabulate(table1, headers1, tablefmt="fancy_grid"))

    print('                       ')
    typer.echo(typer.style("RAM Information summary", fg=typer.colors.WHITE, bg=typer.colors.BLUE, bold=True))
    print('                       ')
    # you can convert that object to a dictionary
    # print(dict(psutil.virtual_memory()._asdict()))
    # gives an object with many fields
    vvm = psutil.virtual_memory()

    # Table
    headers2 = [style("ID", 'header'), style("Name", 'header'), style("Value", 'header')]
    table2 = []
    x = dict(psutil.virtual_memory()._asdict())

    def forloop():
        index = 0
        for i in x:
            col = [index, i, f"{x[i] / 1024 / 1024 / 1024} GBs"]  # Output will be printed in GBs
            table2.append(col)
            index += 1

    forloop()
    typer.echo(tabulate(table2, headers2, tablefmt="fancy_grid"))

    print('                       ')
    typer.echo(typer.style("RAM Utilization summary", fg=typer.colors.WHITE, bg=typer.colors.BLUE, bold=True))
    print('                       ')
    # you can have the percentage of used RAM
    used_RAM = psutil.virtual_memory().percent
    # you can calculate percentage of available memory
    available_memory = psutil.virtual_memory().available * 100 / psutil.virtual_memory().total
    # Table
    headers3 = [style("ID", 'header'), style("Name", 'header'), style("Value", 'header')]
    table3 = [[0, "Percentage of used RAM ", f"{used_RAM} %"],
              [1, "Percentage of available RAM ", f"{available_memory} %"]]
    typer.echo(tabulate(table3, headers3, tablefmt="fancy_grid"))


@app.command()
def nvm():
    """
    Install Nvm (Node version Manager)
    """
    no_support()
    title('Install Nvm')
    try:
        os.system('sudo apt update && sudo apt install curl -y')
        os.system('curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash')
        path_nvm()
        typer.echo(typer.style("Done Install Nvm", fg=typer.colors.WHITE, bg=typer.colors.GREEN, bold=True, ))

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
        #TODO: Kiểm tra xem các dịch vụ đã cài thành công hay chưa và đổi trạng thái trong bảng
        headers = [style("Service", 'header'), style("Status", 'header')]
        table = [["wget", style("Installed", 'green')], ["curl", style("Installed", 'green')],
                 ["nano", style("Installed", 'green')], ["git", style("Installed", 'green')],
                 ["vim", style("Installed", 'green')], ["software-properties-common", style("Installed", 'green')],
                 ["neofetch", style("Installed", 'green')], ["screenfetch", style("Installed", 'green')],
                 ["htop", style("Installed", 'green')], ["net-tools", style("Installed", 'green')],
                 ["zip", style("Installed", 'green')], ["unzip", style("Installed", 'green')],
                 ["tree", style("Installed", 'green')], ["apt-transport-https", style("Installed", 'green')]]
        typer.echo(tabulate(table, headers, tablefmt="fancy_grid"))
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
        # TODO: Kiểm tra curl đã có hay chưa nếu chưa có tiến hành cài đặt
        os.system('curl -4 icanhazip.com')
    except:
        typer.echo("Can't get public ip")
        typer.echo(typer.style("Maybe you don't have curl installed", fg=typer.colors.YELLOW, bold=True))
        typer.echo(typer.style("Type the following command to install curl: 'h-devops curl'", fg=typer.colors.YELLOW,
                               bold=True))
        raise typer.Exit()


@app.command()
def service(status: str = typer.Option(None, "-ss", help="Check the status of the service. < all | service name >", metavar="status"),
        start: str = typer.Option(None, "-st", help="Start the <service name> service", metavar="start"),
        stop: str = typer.Option(None, "-s", help="Stop the <service name> service", metavar="stop"),
        restart: str = typer.Option(None, "-r", help="Restart the <service name> service", metavar="restart")):
    """
    Manipulate services on the system
    """
    no_support()
    #TODO: Thực hiện cmd ứng với các trạng thái của dịch vụ
    if (status):
        typer.echo(status)
    elif (start):
        typer.echo(start)
    elif (stop):
        typer.echo(stop)
    elif (restart):
        typer.echo(restart)
    else:
        try:
            subprocess.run(["service", "--status-all"])
        except:
            typer.echo(style("Can't check status all service", "error"))


@app.command()
def update():
    """
    Update your H-devops package to the latest version
    """
    title('Update H-Devops package latest version')
    try:
        subprocess.run(["pip", "install", "--upgrade", "h-devops"])
    except:
        typer.echo("Can't update H-Devops package latest version")
        raise typer.Exit()


@app.callback()
def main(v: Optional[bool] = typer.Option(
    None, "-v", callback=version_callback,
    help="Show the version of the installation package.")):
    """
    Thank you very much for downloading my packages. Welcome to the world !
    Author: Võ Hoàng
    """
    typer.echo("----------- H_devops -----------")


if __name__ == "__main__":
    app()
