"""
Hongjun Wu
20180208
This program will test on how to use % to format output.
"""
name = "Zemin Jiang"
print('My name is %s, nice to meet you!' % name)

age = 91
print('My age is %d, you are too young!' % age)

tankman = 1
print('The number of tankman is %06d' % tankman)

journalist = 1.0
naive = 99.0
angry = journalist + naive
print('There is %.1f journalist and her naive status is %.2f so I am %.3f percent angry.' % (journalist, naive, angry))
print('You hear me? I am %.02f%% angry!!!' % angry)

