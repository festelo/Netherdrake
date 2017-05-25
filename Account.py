class Account:

    def __init__(self, number, login, password, status, enabled, group, post, commentary, interval):
        self.number = number
        self.login = login
        self.password = password
        self.status = status
        self.enabled = enabled
        self.group = group
        self.post = post
        self.commentary = commentary
        self.interval = interval
        self.isWorking = False
