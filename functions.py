# Functions

def fn1():
    print("hello")
fn1()
fn1()
fn1()

#PARAMETERS

#default parameters

def say_hello(name='Bincy',age=24):
    print(f'Hello {name}{age}')

#positional arguments

say_hello('biju',53)
say_hello('jayanthi',46)

#keyword arguments

say_hello(name="Jincy",age=22)
say_hello()
say_hello(age=24)