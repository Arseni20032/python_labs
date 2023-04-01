import os.path


def load(self):
    if not os.path.exists(f"{self._curr_user}.txt"):
        print("No such file in dir")
        return

    with open(f"{self._curr_user}.txt", 'r') as file:
        for element in file.readline().split():
            self._cont[self._curr_user].add(element)
    print(f"Container for user {self._curr_user} loaded")
