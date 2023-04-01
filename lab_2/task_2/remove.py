def remove(self, obj):
    if self._curr_user is not None:
        for counter in self._cont[self._curr_user]:
            if obj == counter:
                self._cont[self._curr_user].remove(obj)
                return
        print("No such element!")
        