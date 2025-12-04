from operaciones import resta as r
from operaciones import suma as s

print("__name__ principal: ", __name__)

if __name__ == "__main__":
    print("resta principal: ", r(10,5))
    print("suma:", s(5,10))