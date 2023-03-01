class Connect:
    def __init__(self, hostname):
        self.hostname = hostname

    def __enter__(self):
        # before main action
        print(f"Trying to connect to a server: {self.hostname}")

    def __exit__(self, exc_type, exc, traceback):
        # after main action
        print(f"Updates finished! Restarting {self.hostname} ...")
