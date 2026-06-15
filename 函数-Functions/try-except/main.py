# try-except 语句捕获异常

try:
    num1 = int(input("please input first number here:"))
    num2 = int(input("Please input second number here:"))

    result = num1 / num2

    print(f"the result is: {result}")

except ValueError:
    print("your input is not a valid number, please re-fill again! ")

except ZeroDivisionError:
    print("the number should not be a zero! please re-fill again!")

except Exception as e:
    print("error occured:", str(e))

    