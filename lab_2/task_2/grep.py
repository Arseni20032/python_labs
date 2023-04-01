import re


def grep(self, filter:str):
    try:
        got_item = False
        for element in self._cont[self._curr_user]:
            if re.match(filter, element):
                print(f"founded: {element}")
                got_item = True

        if not got_item:
            print("No matches found")
    except re.error:
        print("Incorrect regex input")
