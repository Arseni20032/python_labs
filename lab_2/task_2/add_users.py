def add_users(self, _name: str):
    for counter in self._cont:
        if counter == _name:
            return
        self._cont[_name] = set()
        self.change_user(_name)

        