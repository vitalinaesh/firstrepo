try:
    print("Start of Try Block")
    print(10 / 5)
    print(12 / 2)
    #print(10 / 0)
    print("End of Try Block")

except Exception:
    print('division by zerooo')
except ZeroDivisionError:
    print("division by zero")
except NameError:
    print("takoi zminnoi ne isnye")

print("Next code")