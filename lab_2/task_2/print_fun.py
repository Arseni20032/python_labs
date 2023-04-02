# write all objects in current container
def print_fun(self):
    if self._curr_user is not None:
        print(self._cont[self._curr_user])
