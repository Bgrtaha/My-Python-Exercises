def my_func(x,y):
    result_string = "00"
    try:
        print(int(x/y),end="")
        result_string += "1"
    except ZeroDivisionError:
        result_string += "2"
    except:
        result_string += "3"
    finally:
        result_string = result_string[:1] + "4" + result_string[1:]
    print(result_string)

my_func("6","0")
