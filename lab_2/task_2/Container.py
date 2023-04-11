import os
import re


class Container:
    _cont = dict()
    _curr_user = None

    # add new user in dict
    def add_users(self, _name: str):
        for i in self._cont:
            if i == _name:
                return
        self._cont[_name] = set()
        self.change_users(_name)

    def grep(self, filter: str):
        try:
            got_item = False
            for element in self._cont[self._curr_user]:
                # if you find filter in element
                if re.match(filter, element):
                    print(f"founded: {element}")
                    got_item = True

            if not got_item:
                print("No matches found")
        except re.error:
            print("Incorrect regex input")

    def change_users(self, name: str):
        # if also have user
        if self._curr_user != None:
            text = input("Save current container? Enter YES or NO: \n")
            if text == "YES":
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

        text1 = input("Load the container? Enter YES or NO:\n")
        if text1 == "YES":
            self.load()
        else:
            self._cont[name] = set()

    def save(self):
        with open(f"{self._curr_user}.txt", 'w') as file:
            for element in self._cont[self._curr_user]:
                # all elements write as str with ' '
                file.write(str(element) + ' ')
        print(f"Data saved to {self._curr_user}.txt")

    def load(self):
        # if file not exists
        if not os.path.exists(f"{self._curr_user}.txt"):
            print("No such file in directory.")
            return

        # add elements in container (current user)

        with open(f"{self._curr_user}.txt", 'r') as file:
            for element in file.readline().split():
                self._cont[self._curr_user].add(element)
        print(f"Container for user {self._curr_user} loaded")

    # add objects in container
    def add(self, *objs):
        if self._curr_user is not None:
            for counter in objs:
                self._cont[self._curr_user].add(counter)

    # find elements in container
    def find(self, *objs):
        if self._curr_user is not None:
            for obj in objs:
                if obj in self._cont[self._curr_user]:
                    print(f"founded: {obj}")
                    continue

    # delete obj from set current user
    def remove(self, obj):
        if self._curr_user is not None:
            # dict current user
            for counter in self._cont[self._curr_user]:
                if obj == counter:
                    self._cont[self._curr_user].remove(obj)
                    return
            print("No such element!")

    # write all objects in current container
    def print_fun(self):
        if self._curr_user is not None:
            print(self._cont[self._curr_user])
