def change_users(self, name: str):
    if self._current_user is not None:
        text = input("Save current container? Enter YES or NO")
        if text == "YES" or "Yes" or "yes":
            self.save()
        else:
            self._cont[name] = set()

    self._current_user = name

    if not self._current_user in self._cont.keys():
        self._cont[self._current_user] = set()

    print(f"Switched to {self._current_user}")

    text1 = input("Load the container? Enter YES or NO")
    if text == "YES" or "Yes" or "yes":
        self.load()
    else:
        self._cont[name] = set()
