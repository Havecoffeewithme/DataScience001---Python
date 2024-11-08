import numpy as np


a = np.array([10, 20, 30, 33])

b = np.array([1,77,2,3])

print(a[1])
print(b[0])

c = np.array([
    [1, 4, 6, 7, 77],
    [3, 6, 9, 12, 15],
    [2, 4, 6, 8, 10]
])

for k in c:
    print(k)

print()

print(c[2][4])

d = np.array([
    [
        [1 , 3, 5, 7, 9], [2, 4, 6, 8, 10], [12, 14, 16, 18, 20]
    ],

    [
        [2, 4, 8, 8, 8], [9, 4, 7, 9, 0], [0, 1, 1, 5, 10]
    ],

    [
        [12, 44, 58, 8, 8], [59, 4, 47, 9, 50], [10, 1, 11, 55, 10]
    ]

], dtype=float )

e = np.full((3, 5, 4), 7)

aa = np.zeros((3, 3))
bb = np.ones((2, 3, 4, 2))

print()

j = np.arange(100, 1000, 100)
print(j)

cc = np.array([
    [11, 4, 6, 7, 33],
    [47, 34, 41, 38, 35],
    [8, 6, 4, 2, 90]
])

print(c + cc)
print()
print( a + b)
print()
print(b * 0)
print()

z = np.array([10, 20, 30, 0])

print("taking cosine of every value ")
zz =np.cos(z)
print(zz)

print("The minimum value is : ", z.min())

cd = np.array([10, 20, 30])
dd = np.array([5, 5, 5])

print()
print("here we are concatenating ")
print(np.concatenate((cd, dd)))
print('here we are stacking: ')
print(np.stack((cd, dd)))

a1 = np.array([
[ 10 , 20 , 30 ],
[ 40 , 50 , 60 ],
[ 70 , 80 , 90 ],
[ 100 , 110 , 120 ]
])

print()
np.save('filea1', a1)

np 