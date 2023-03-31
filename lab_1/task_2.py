def numbers_and_sign(first_number: float, second_number: float, operation: str):
    match operation:
        case "add":
            return first_number + second_number
        case "sub":
            return first_number - second_number
        case "mult":
            return first_number * second_number
        case "div":
            if second_number == 0:
                return "Can't divide by zero"
            else:
                return first_number / second_number
        case _:
            return "incorrect input"




