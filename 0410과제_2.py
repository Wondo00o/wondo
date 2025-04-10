#5-13
import math

#5-13-1
def v_cube(s):
    return s ** 3
s = 12
print(f"부피는 {v_cube(s)}입니다.")

#5-13-2
def v_cube(s):
    return s ** 3
s = 20
print(f"부피는 {v_cube(s)}입니다.")

#5-13-3
def v_rectangular(w, h, l):
    return w * h * l
w,h,l= 3,5,6
print(f"부피는 {v_rectangular(w,h,l)}입니다.")

#5-13-4
def v_cone(r, h):
    return (1/3) * math.pi * r**2 * h
r,h= 20,10
print(f"부피는 {v_cone(r,h)}입니다.")

#5-13-5
def v_sphere(r):
    return (4/3) * math.pi * r**3
r=15
print(f"부피는 {v_sphere(r)}입니다.")

#5-13-6
def v_cylinder(r, h):
    return math.pi * r**2 * h
r,h= 20,10
print(f"부피는 {v_cylinder(r,h)}입니다.")
