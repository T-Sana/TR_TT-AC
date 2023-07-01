import subprocess
import sys

def install(package) -> None:
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
def update(package) -> None:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", package])
def install_updated(package) -> None:
    install(package)
    update(package)