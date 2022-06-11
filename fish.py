import cv2
import numpy as np

print("Running fish")
window_name = 'image'
def draw_circle(event,x,y,flags,param,cb_args=0,img=cv2.imread('/home/jhsrobo/Pictures/fishLength.png', cv2.IMREAD_COLOR)):
    window_name = 'image'
    if event == cv2.EVENT_LBUTTONDOWN:
	clicks.append((x, y))
	img = cv2.circle(img,(x,y),20,(0,255,0),-1)
	img = cv2.imread('/home/jhsrobo/Pictures/fishLength.png', cv2.IMREAD_COLOR)
	cv2.imshow(window_name, img)
clicks = []
vid_capture = cv2.VideoCapture('http://192.168.1.111:5000') # CHANGE DEPENDING ON IP OF CAMERAS

count = 0
q = 0

while True: 

    if count < 1:
        ret, frame = vid_capture.read()
        cv2.imshow('video', frame)
        k = cv2.waitKey(1)
	if k == ord('p'):
	    cv2.imwrite('/home/jhsrobo/Pictures/fishLength.png', frame)
	    count = 1
            vid_capture.release()
	    

    if count >= 1:
	cv2.destroyAllWindows()
	img = cv2.imread('/home/jhsrobo/Pictures/fishLength.png', cv2.IMREAD_COLOR)
	window_open = False
	while not window_open:
	    try:
		cv2.namedWindow(window_name)
		cv2.setMouseCallback(window_name, draw_circle)
		window_open = True
	    except:
		cv2.destroyAllWindows()
	status = True
	while status:
	    cv2.imshow(window_name, img)
	    cv2.waitKey(1)
            for click in clicks:
                img = cv2.circle(img,(click[0],click[1]),10,(255,0,0),-1)
	    if len(clicks) == 4:
		reference = abs(clicks[0][0] - clicks[1][0])
		ratio = 20. / reference
		total = ((((abs(clicks[2][0] - clicks[3][0]) ** 2) + (abs(clicks[2][1] - clicks[3][1])) ** 2)) ** 0.5) * ratio
		status = False
	displayImg = np.zeros((512,1024,3), dtype=np.uint8)
	cv2.putText(displayImg, "{:.2f} cm".format(total), (50,325), cv2.FONT_HERSHEY_SIMPLEX, 6, (50, 255, 50), 3)
	cv2.destroyWindow(window_name)
	finalDisplay = True
	while finalDisplay:
	    cv2.imshow('displayImage', displayImg)
	    q = cv2.waitKey(1)
	    if q == ord('q'):
		cv2.destroyAllWindows()
		break
	if q == ord('q'):
		cv2.destroyAllWindows()
		break

