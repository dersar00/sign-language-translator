# Program To Read video 
# and Extract Frames 
import cv2 
import numpy as np
from win32api import GetSystemMetrics
from PIL import ImageFont, ImageDraw, Image  

# Function to extract frames 
def FrameCapture(path): 
	width= GetSystemMetrics(0)
	height= GetSystemMetrics(1)
	#screen = screeninfo.get_monitors()[screen_id]

	# Path to video file 
	#cap = cv2.VideoCapture(path) 
	cap = cv2.VideoCapture(0)
	#cap.set(3,1920)
	#cap.set(4,1080)
	# Used as counter variable 
	count = 0

	#cv2.namedWindow("ASL Translator", cv2.WINDOW_FULLSCREEN)
	#cv2.moveWindow("ASL Translator",0,0)
	#cv2.setWindowProperty("window",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
	# checks whether frames were extracted 
	success = 1
	#cap.set(3,1920)
	#cap.set(4,1080# Write some Text

	font                   = cv2.FONT_HERSHEY_DUPLEX
	bottomLeftCornerOfText = (10,400)
	fontScale              = 1
	fontColor              = (255,255,255)
	lineType               = 2
	window_name = 'ASL Translator'

	img = cv2.imread('letterD.png',0)
	while success: 
		# Capture frame-by-frame
		ret, frame = cap.read()
		#frame=cv2.resize(frame,(1000,500),interpolation =cv2.INTER_AREA)
		
		# Our operations on the frame come here
		mat = cv2.cvtColor(frame, 0)
		#resize = cv2.resize(mat, (width, height)) 
		'''cv2.putText(frame,'Hello World!', 
			bottomLeftCornerOfText, 
			font, 
			fontScale,
			fontColor,
			lineType)'''
		latoFont=ImageFont.truetype("LATO-REGULAR.TTF",20)
		matRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
		forPIL=Image.fromarray(matRGB)
		
		draw=ImageDraw.Draw(forPIL)
		draw.text((10, 10), window_name, font=latoFont)  
		cv2_im_processed = cv2.cvtColor(np.array(forPIL), cv2.COLOR_RGB2BGR)  
   
 		
		'''cv2.namedWindow(.lkl"ASL Translator", cv2.WINDOW_FULLSCREEN)
		cv2.setWindowProperty("ASL Translator",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
		'''
		cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
		cv2.moveWindow(window_name, width - 1, height - 1)
		#cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
		#cv2.moveWindow('frame',1000,0)
		#cv2.setWindowProperty('frame',cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
		# checks whether frames were extracted 
		#cap.set(3,1920)
		#cap.set(4,1080)
		# Display the resulting frame
		#cv2.imshow(window_name,frame)
		#cv2.imshow('frame',img)

		cv2.imshow('Fonts', cv2_im_processed)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

		# cap object calls read 
		# function extract frames 
		#success, image = cap.read() 

		# Saves the frames with frame-count 
		#cv2.imwrite("frame%d.jpg" % count, image) 

		count += 1

# Driver Code 
if __name__ == '__main__': 

	# Calling the function 
	FrameCapture("sample.mp4") 
