import os.path


def load(self):
    # if file not exists
    if not os.path.exists(f"{self._curr_user}.txt"):
        print("No such file in dir")
        return

    # add elements in container (current user)

    with open(f"{self._curr_user}.txt", 'r') as file:
        for element in file.readline().split():
            self._cont[self._curr_user].add(element)
    print(f"Container for user {self._curr_user} loaded")
