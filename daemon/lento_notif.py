import platform
import subprocess
from win10toast import ToastNotifier


class LentoNotif():
    def __init__(self, notif):
        super().__init__()
        self.name = notif["name"]
        self.title = notif["title"]
        self.body = notif["body"]

    def send(self):
        match platform.system():
            case "Darwin":
                return self.macos_notif()
            case "Windows":
                return self.windows_notif()

    def macos_notif(self):
        subprocess.Popen([
            "osascript",
            "-e",
            f"""display notification "{self.body}" with title "{self.title}\""""  # noqa: E501
        ])

    def windows_notif(self):
        print(
            f"==\nWIN NOTIF WITH TITLE {self.title} AND BODY {self.body}\n=="
        )
        toaster = ToastNotifier()
        toaster.show_toast(
            self.title,
            self.body,
            duration=10
        )
