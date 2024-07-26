import cv2

face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
filename='image.jpg'
img=cv2.imread(filename)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
fl=face.detectMultiScale(gray,1.09,7)
filter=cv2.imread('png-clipart-snapchat-filters-filtros-o-efectos-de-snapchat-sliced-bread-illustration-thumbnail.png')



def put_dog_filter(filter, fc, x, y, w, h):
    face_width = w
    face_height = h

    filter = cv2.resize(filter, (int(face_width * 1.5), int(face_height * 1.95)))
    for i in range(int(face_height * 1.75)):
        for j in range(int(face_width * 1.5)):
            for k in range(3):
                if filter[i][j][k] < 235:
                    fc[y + i - int(0.375 * h) - 1][x + j - int(0.35 * w)][k] = filter[i][j][k]
    return fc

for (x, y, w, h) in fl:
    frame = put_dog_filter(filter, img, x, y, w, h)

cv2.imshow('image',frame)
cv2.waitKey(20000)& 0xff
cv2.destroyAllWindows()