def f(x):
    return x**2 -4 

def df(x):
    return 2*x
from newton import Newton
# x = 10 
# f_x = f(x)
# df_x = df(x)
# print(f'f({x}) = {f_x}')
# print(f'df({x}) = {df_x}')

# print(f'') #f คือ format

# def display(x):
#     print(f'f({x}) = {f(x)}')
#     print(f'df({x}) = {df(x)}')

# class Newton:
#     def __init__(self, f, df):
#         self.f = f
#         self.df = df
    
#     def display(self, x):
#         print(f'f({x}) = {self.f(x)}')
#         print(f'df({x}) = {self.df(x)}')

#     def solve(self, x, tol, max_iter):
#         for i in range(max_iter):
#             if self.df(x) == 0:
#                 print('df(x) is zero')
#                 break
#             x = x - self.f(x)/self.df(x)
#             self.display(x)
#             if abs(self.f(x)) < tol:
#                 break
#         return x



# def display(x):
#     print(f'f({x}) = {f(x)}')
#     print(f'df({x}) = {df(x)}')

# for i in range(10):
#     x=10
#     if df(x) == 0 :
#         print("df(x) is zero")
#         break
#     x = x - f(x)/df(x)
#     display(x)
#     # print(f' at i={i}, x = {x} , f({x}) = {f(x)}')

# print(f' final x = {x} ')
# print(f' final f({x}) = {f(x)} ')

x = 10 
f_x = f(x)
df_x = df(x)

aaa = Newton(f,df)
aaa.solve(x, 1e-10, 100)