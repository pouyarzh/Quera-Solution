import numpy as np
def main():
    _number = input()
    print(np.prod(list(range(1,int(_number)+1))))
if __name__ == "__main__":
    main()