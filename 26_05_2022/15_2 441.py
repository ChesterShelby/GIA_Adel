a = int(input())

maxx = 0
minn = 301
speed = []
k = 0
"""1 решение"""
# for s in range(a):
#     d = round(float(input()))
#     speed.append(d)
#
# for i in range(a):
#     if speed[i] > maxx:
#         maxx = speed[i]
#
# for i in range(a):
#     if speed[i] < minn:
#         minn = speed[i]
#
# for i in range(a):
#     if speed[i] < 30:
#         k += 1
#
# print(maxx - minn, k)


"""2 решение"""
# for i in range(a):
#     d = round(float(input()))
#     if d > maxx:
#         maxx = d
#     if d < minn:
#         minn = d
#     if d < 30:
#         k += 1
#
# print(maxx - minn, k)

"""3 решение"""
# for s in range(a):
#     d = round(float(input()))
#     speed.append(d)
#     if d < 30:
#         k += 1
#
# print(max(speed) - min(speed), k)