n = 0
s = 0
m = float('inf')  # set initial minimum to positive infinity
a = -1
x = int(input("Enter a number (-1 to terminate): "))
while x != -1:
n += 1
s += x
m = min(m, x)
x = int(input("Enter a number (-1 to terminate): ")
if n != 0:
 a = s / n
print(f"Count (n): {n}")
print(f"Sum (s): {s}")
print(f"Minimum (m): {m}")
print(f"Mean (a): {a}")
# it looks like I learned how to use git today 
