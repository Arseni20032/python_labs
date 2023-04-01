def add(self, *objs):
    if self._curr_user is not None:
        for counter in objs:
            self._cont[self._curr_user].add(counter)
