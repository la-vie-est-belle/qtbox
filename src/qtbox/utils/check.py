from urllib.request import urlopen
from threading import Thread
import ssl


def compare_version():
    try:
        context = ssl._create_unverified_context()
        r = urlopen("https://la-vie-est-belle.github.io/qtbox/CHANGELOG", context=context, timeout=1)
        remote_version = r.readline().decode().strip()
    except Exception as e:
        return

    current_version = "v1.1.4"
    if remote_version != current_version:
        print(f"Qt Box {remote_version} is available. Upgrade it with command `pip install --upgrade qtbox`")


def check_update():
    Thread(target=compare_version).start()