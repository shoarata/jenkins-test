import fire

def hello(name:str="world"):
    print( f"Hello {name}!")

def sum_list(numbers:list=[]):
    return sum(numbers)
def multiply(x, y):
    return x * y
if __name__ == "__main__":
    fire.Fire({
        "hello": hello,
        "multiply": multiply,
        "sum_list": sum_list
        })
