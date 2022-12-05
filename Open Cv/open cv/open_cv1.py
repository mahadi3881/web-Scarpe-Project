import cv2
# image = cv2.imread('1.jpeg',cv2.IMREAD_COLOR)
#print(image.shape[0]*image.shape[1]) #height and width size
# cv2.imshow("python image",image)
# 


image = cv2.imread('1.jpeg',-1)
height = image.shape[0]*0.2
width = image.shape[1]*0.3
half = cv2.resize(image,(int(width),int(height)))
print(image.shape)
print(half.shape)
# half = cv2.resize(image,(980,980),fx=1, fy=1)
cv2.imshow("python half",half)
cv2.imshow("python original",image)
cv2.waitKey(0)
# print(image.shape)
