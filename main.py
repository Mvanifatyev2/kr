'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
def newset(num):
    new_set = set()
    for i in range(num):
        new_set.add(int(input("Введите число для множества: ")))
    return new_set

n = int(input("Введите кол-во элементов первого множества: "))
n_set = newset(n)

m = int(input("Введите кол-во элементов второго множества: "))
m_set = newset(m)

print(*n_set)
print(*m_set)

s_set = sorted(n_set.intersection(m_set))
print(*s_set)