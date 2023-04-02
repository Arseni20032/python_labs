def change_users(self, name: str):
    # if also have user
    if self._curr_user is not None:
        text = input("Save current container? Enter YES or NO")
        if text == "YES" or "Yes" or "yes":
            self.save()
        else:
            # create new container
            self._cont[name] = set()

    # new user
    self._curr_user = name
    # if we don't find name user in dictionary
    if not self._curr_user in self._cont.keys():
        # create new set
        self._cont[self._curr_user] = set()

    print(f"Switched to {self._curr_user}")

    text1 = input("Load the container? Enter YES or NO")
    if text1 == "YES" or "Yes" or "yes":
        self.load()
    else:
        self._cont[name] = set()
