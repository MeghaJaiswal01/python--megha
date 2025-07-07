#taskL:-1
def local_scope_ex():
    x = 10
    print("local variable:-", x)
local_scope_ex()

#task:-2
def outer_func():
    x=10

    def inner_func():
        print("enclosing variable x from inner function:-",x)

    inner_func()

outer_func()

#task:-3
x = 10
def global_scope_ex():
    print("global variable x:",x)

global_scope_ex()
print("global variable x outside function:-", x)

#task:- 4
x = 11
def modify_global():
    global x 
    x+= 20
modify_global()
print("global variable x after modification:-",x)