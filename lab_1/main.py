import task_2
import task_1
import task_3

list_num = [i for i in range(1, 20)]

first_number = second_number = 0

task_1.fun_hello_world()

first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
operation = input("Choose operation: add, sub, mult or div ")

print("Result: ")

print(task_2.numbers_and_sign(first_number, second_number, operation))

print(task_3.list_of_even_num(list_num))
