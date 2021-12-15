a = """
def f():
    global a, b
    b = 'a = ' + '"'*3 + a
    b += '"'*3
    b += a
    print(b)
b = ""
f()
"""
def f():
    global a, b
    b = 'a = ' + '"'*3 + a
    b += '"'*3
    b += a
    print(b)
b = ""
f()

