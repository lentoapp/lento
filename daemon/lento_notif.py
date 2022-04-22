import platform
import subprocess


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
        print(
            f"==\nMACOS NOTIF WITH TITLE {self.title} AND BODY {self.body}\n=="
        )
        subprocess.Popen([
            "osascript",
            "-e",
            f"""display notification "{self.body}" with title "{self.title}\""""  # noqa: E501
        ])

    def windows_notif(self):
        print(
            f"==\nWIN NOTIF WITH TITLE {self.title} AND BODY {self.body}\n=="
        )