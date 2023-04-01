def save(self):
    with open (f"{self._curr_user}.txt", 'w') as file:
        for element in self._cont[self._curr_user]:
            file.write(str(element) + ' ')
    print(f"Data saved to {self._curr_user}.txt")
    