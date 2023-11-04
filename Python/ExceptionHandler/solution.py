class ExceptionProxy(Exception):
    def __init__(self, name, age):
        self.msg = name
        self.function = age


def transform_exceptions(func_ls):
    tr_ls = []
    for fuction in func_ls:
        try:
            fuction()
            tr_ls.append(ExceptionProxy('ok!',fuction))
        except Exception as e:
            tr_ls.append(ExceptionProxy(str(e), fuction))
        finally:
            print('complete execute fuction')
    return tr_ls

def f():
    1/0

def g():
    pass

if __name__ == "__main__":
    tr_ls = transform_exceptions([f, g])

    for tr in tr_ls:
        print("msg: " + tr.msg + "\nfunction name: " + tr.function.__name__)