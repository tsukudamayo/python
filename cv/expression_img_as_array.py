from PIL import Image
import numpy as np

im = np.array(Image.open('empire.jpg'))
print("normal",im.shape, im.dtype)

im = np.array(Image.open('empire.jpg').convert('L'),'f')
print("convert L ",im.shape, im.dtype)

#FIXME
im = np.array(Image.open('empire.jpg'))
value = []
value = im
print("i=x_position", value[0])
print("j=y_positon", value[1])
print("k=channel", value[2])


# subsutitue the value of the first line into the second line
print("before subsutitue the value of the line1 into the line2 (line1):", im[1])
print("before subsutitue the value of the line1 into the line2 (line2):", im[2])
im[1,:] = im[2,:]
print("after subsutitue the value of the line1 into the line2 :", im[1])
print("after subsutitue the value of the line1 into the line2 :", im[2])


# do sbsutitution the value of the line 1 is 100
print("before :", im[:,1])
im[:,1] = 100
print(im[:,1])

# sum line100, row50
print("sum line100, row50", im[:100, :50].sum())

# access line50~100, row50~100
print("access line50~100, row50~100", im[50:100, 50:100])

# mean
print("line1 mean", im[1].mean())

# access last row
print("access last row", im[:,-1])

# access second last row
print("access second last row", im[-2.:])

