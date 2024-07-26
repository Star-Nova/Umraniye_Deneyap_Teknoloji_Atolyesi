import cv2
filter = cv2.imread("png-clipart-snapchat-filters-filtros-o-efectos-de-snapchat-sliced-bread-illustration-thumbnail.png",cv2.IMREAD_UNCHANGED)
ml=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
cap=cv2.VideoCapture(0)

def put_filter(filter, fc, x, y, w, h):
    face_width = w
    face_height = h

    filter = cv2.resize(filter, (int(face_width * 1.5), int(face_height * 1.95)))
    for i in range(int(face_height * 1.75)):
        for j in range(int(face_width * 1.5)):
            for k in range(3):
                if filter[i][j][k] < 235:
                    fc[y + i - int(0.375 * h) - 1][x + j - int(0.35 * w)][k] = filter[i][j][k]
    return fc

while True:
    _, frame = cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces= ml.detectMultiScale(frame)
    try:
        for (x,y,w,h) in faces:
            put_filter(filter,frame,x,y,w,h)

        cv2.imshow("Face Detect",frame)
        cv2.waitKey(1)
    except:
        pass


