import os
import typer
import subprocess
import platform
import psutil
import json

from time import sleep
from tabulate import tabulate
from typing import List, Optional
from h_devops import __version__


# Common
VERSION = __version__
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
        # Kiểm tra xem đã có curl hay chưa và nếu chưa có tiến hành cài đặt
        res = subprocess.run(["curl", "-V"]).__dict__

        if (res.get('returncode') == 0):
            subprocess.run(["curl", "-4", "icanhazip.com"])
        else:
            os.system("sudo apt install curl")
            subprocess.run(["curl", "-4", "icanhazip.com"])
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
    if (status):
        subprocess.run(["systemctl", "status", status])
    elif (start):
        subprocess.run(["systemctl", "status", start])
    elif (stop):
        subprocess.run(["systemctl", "status", stop])
    elif (restart):
        subprocess.run(["systemctl", "status", restart])
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


@app.command()
def docker():
    """
    Install Docker and Docker-compose
    """
    no_support()
    title('Install Docker and Docker-compose')
    #TODO: Install Docker and Docker-compose, kiểm tra OS tương ứng để cài đặt

    datas = subprocess.run(["dpkg", "--print-architecture"], stdout=subprocess.PIPE).stdout.decode("utf-8").split("\n")
    if (datas[0] == "amd64"):
        title('Install Docker AMD64')
        try:
            os.system("sudo apt update")
            os.system("sudo apt install apt-transport-https ca-certificates curl software-properties-common")
            os.system("curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -")
            os.system(
                'sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"')
            os.system("sudo apt update")
            os.system("apt-cache policy docker-ce")
            os.system("sudo apt install docker-ce -y")
            os.system(
                'sudo curl -L "https://github.com/docker/compose/releases/download/1.27.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose')
            os.system('sudo chmod +x /usr/local/bin/docker-compose')

            headers = [style("ID", 'header'), style("Name", 'header'), style("Value", 'header')]
            table = [[0, "Docker", "Successful Installation"], [1, "Docker-compose", "Successful Installation"]]
            typer.echo(tabulate(table, headers, tablefmt="fancy_grid"))
        except:
            headers = [style("ID", 'header'), style("Name", 'header'), style("Value", 'header')]
            table = [[0, "Docker", "Install Fail"], [1, "Docker-compose", "Install Fail"]]
            typer.echo(tabulate(table, headers, tablefmt="fancy_grid"))
    else:
        headers = [style("ID", 'header'), style("Name", 'header'), style("Value", 'header')]
        table = [[0, "Docker", "Install Fail"], [1, "Docker-compose", "Install Fail"]]
        typer.echo(tabulate(table, headers, tablefmt="fancy_grid"))


@app.command()
def jenkins():
    """
    Install Jenkins
    """
    no_support()
    title('Install Jenkins')

    try:
        os.system("sudo apt install openjdk-11-jdk -y")
        os.system("java --version")
        os.system("wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -")
        os.system("sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'")
        os.system("sudo apt update")
        os.system("sudo apt install jenkins -y")
        os.system("sudo ufw allow 8080")
        os.system("sudo systemctl enable jenkins")
        os.system("sudo systemctl start jenkins")
        os.system("sudo systemctl status jenkins")

    except:
        typer.echo(style("Can't install jenkins", "error"))


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
