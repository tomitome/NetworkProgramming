import multiprocessing

print("a")

def f(mesg):
    print("b")

print("c")

if __name__ == "__main__":
    print("d")
    p = multiprocessing.Process(target=f, args=("test"))
    p.start()

    print("e")

print("f")