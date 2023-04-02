# find elements in container
def find(self, *objs):
    if self._curr_user is not None:
        for obj in objs:
            if obj in self._cont[self._curr_user]:
                print(f"founded: {obj}")
                continue
