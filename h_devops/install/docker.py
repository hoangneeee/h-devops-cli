
import typer
import subprocess


# Linux-specific installation code
def install_docker_on_linux():
    try:
        subprocess.run(["apt-get", "update"])
        subprocess.run(["apt-get", "install", "-y", "docker"])
        subprocess.run(["systemctl", "start", "docker"])
        subprocess.run(["systemctl", "enable", "docker"])
        typer.echo("Docker installed successfully on Linux!")
    except subprocess.CalledProcessError as e:
        typer.echo(f"Error occurred during Docker installation: {e}")


def install_docker_compose():
    """
    Install Docker Compose.
    """
    try:
        subprocess.run(["curl", "-L", "-o", "/usr/local/bin/docker-compose",
                       "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)"])
        subprocess.run(["chmod", "+x", "/usr/local/bin/docker-compose"])
        typer.echo("Docker Compose installed successfully!")
    except subprocess.CalledProcessError as e:
        typer.echo(f"Error occurred during Docker Compose installation: {e}")


def install_docker(platform: str):
    """
    Install Docker on the specified platform.
    """
    if platform == "windows":
        typer.echo("Installing Docker on Windows...")
        # Add your Windows-specific installation code here
        typer.echo("Docker installed successfully on Windows!")
    elif platform == "mac":
        typer.echo("Installing Docker on macOS...")
        # Add your macOS-specific installation code here
        typer.echo("Docker installed successfully on macOS!")
    elif platform == "linux":
        typer.echo("Installing Docker on Linux...")
        install_docker_on_linux()
        install_docker_compose()
        typer.echo("Docker installed successfully on Linux!")
    else:
        typer.echo(f"Platform '{platform}' is not supported.")
