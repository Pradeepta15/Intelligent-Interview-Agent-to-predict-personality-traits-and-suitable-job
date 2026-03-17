import cv2

# Capture a video

video = cv2.VideoCapture(0)
if (video.isOpened() == False):
	print("Error reading video file")
frame_width = int(video.get(3))
frame_height = int(video.get(4))
size = (frame_width, frame_height)
result = cv2.VideoWriter('abc.mp4',0x7634706d,10, size)	
while(True):
	ret, frame = video.read()
	if ret == True:
		result.write(frame)
		cv2.imshow('Frame', frame)
		if cv2.waitKey(1) & 0xFF == ord('s'):
			break
	else:
		break
video.release()
result.release()
cv2.destroyAllWindows()
print("The video was successfully saved")




# Convert the video to Frames

vidcap = cv2.VideoCapture('abc.mp4')
success,image = vidcap.read()
count = 0
while success:
  vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*1000))
  cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1




# convert to gray scale and detect face

img = cv2.imread('frame3.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
for (x, y, w, h) in faces:
    cv2.rectangle(gray, (x, y), (x+w, y+h), (0, 0, 255), 2)
    faces = gray[y:y + h, x:x + w]
    cv2.imshow("face",faces)
    cv2.imwrite('face1.jpg', faces)
cv2.imwrite('detected1.jpg', gray)
cv2.imshow('img', gray)
cv2.waitKey(200)

img = cv2.imread('frame7.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
for (x, y, w, h) in faces:
    cv2.rectangle(gray, (x, y), (x+w, y+h), (0, 0, 255), 2)
    faces = gray[y:y + h, x:x + w]
    cv2.imshow("face",faces)
    cv2.imwrite('face2.jpg', faces)
cv2.imwrite('detected2.jpg', gray)
cv2.imshow('img', gray)
cv2.waitKey(200)

img = cv2.imread('frame11.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
for (x, y, w, h) in faces:
    cv2.rectangle(gray, (x, y), (x+w, y+h), (0, 0, 255), 2)
    faces = gray[y:y + h, x:x + w]
    cv2.imshow("face",faces)
    cv2.imwrite('face3.jpg', faces)
cv2.imwrite('detected3.jpg', gray)
cv2.imshow('img', gray)
cv2.waitKey(200)

img = cv2.imread('frame15.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
for (x, y, w, h) in faces:
    cv2.rectangle(gray, (x, y), (x+w, y+h), (0, 0, 255), 2)
    faces = gray[y:y + h, x:x + w]
    cv2.imshow("face",faces)
    cv2.imwrite('face4.jpg', faces)
cv2.imwrite('detected4.jpg', gray)
cv2.imshow('img', gray)
cv2.waitKey(200)