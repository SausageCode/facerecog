import sys
import os
import json
from ibm_watson import VisualRecognitionV3
from PIL import Image, ImageDraw, ImageFont
import contextlib
with contextlib.redirect_stdout(None): #disable printing when importing pygame (annoying, python3 only)
	import pygame.camera
	import pygame.image

################################################################################
# Global variables
nofaces = 'NONE'
faces = 'NONE'
imagename = 'NONE'

################################################################################
# My photos:

# sample images in subfolder photos, create own 
im1 = './photos/sampleim1.jpg'
im2 = './photos/sampleim2.jpg'
im3 = './photos/sampleim3.jpg'
sim = 'sampleimage.jpg' # provided sample image in project root
cimg = './photo.jpg' #camera image

################################################################################

def getnewimage():
	#get camera iamge and save 
	pygame.camera.init()
	cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])
	cam.start()
	img = cam.get_image()
	cam.stop()
	print("Image taken!")
	pygame.image.save(img, "photo.jpg")
	# print("Webcam image saved to photo.jpg")
	pygame.camera.quit()
	return;

################################################################################
def evalimage():
	# Downsize image before sending if larger than 1M, saves upload time
	imsize = os.stat(imm).st_size	
	if(imsize > 1000000):
		im = Image.open(imm)
		im.save(imm, quality=25) #raise quality if sureness starts dropping

	# API
	visual_recognition = VisualRecognitionV3(
	    version='2018-03-19',
	    iam_apikey='{yourapikey}')#replace this with your key

	print("Sending image")
	
	# Take image and process it and get results
	with open(imm, 'rb') as image:
		faces = visual_recognition.detect_faces(image).get_result()

	print("Image sent, files received")
	
	# Save results into json file
	with open('result.json', 'w') as jsondata:
	    json.dump(faces, jsondata, indent=2)	

	return;

################################################################################
def getfaces():
	global nofaces, faces, imagename
	# Read json data
	with open('result.json') as jsondata:
		data = json.load(jsondata)

	imagename = data["images"][0]["image"]
	faces = data["images"][0]["faces"]

	if(faces == []):
		sys.exit("No face detected")

	# Get no. of faces
	nofaces = len(faces)

	print("Processed image name: %s\n" % imagename)

	return;

################################################################################
def main(num):
	# Input image
	im = Image.open(imm)
	imwidth, imheight = im.size
	# Create variable line thickness based on shorter image side
	linethicc = int(round(min(imwidth, imheight) / 100 + 1))
	
	for x in range(0, num):
		# Get faces coordinates	
		facex1 = faces[x]["face_location"]["left"]
		facey1 = faces[x]["face_location"]["top"]
		facex2 = facex1 + faces[x]["face_location"]["width"]
		facey2 = facey1 + faces[x]["face_location"]["height"]

		gender = faces[x]["gender"]["gender"]
		genderscore = 100*faces[x]["gender"]["score"]

		agemin = faces[x]["age"]["min"]
		agemax = faces[x]["age"]["max"]
		agescore = 100*faces[x]["age"]["score"]
	
		# Printing data
		# print("\nImage: Width: %d, Size: %d" % (imwidth, imheight)) #debug only
		print("Face %d is a %s, sureness is %.5f%%" % (x+1, gender, genderscore))
		print("Face %d is at least %s years old and most %s years old, with sureness %.5f%%\n" %
		(x+1, agemin, agemax, agescore))
	
		# Drawing face frame on image
		fontsizept = int(round(min(facex2-facex1, facey2-facey1)))
		fontsizepx = fontsizept*1.3333 # if needed
		
		# Get number position
		draw = ImageDraw.Draw(im)
		fnt = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', fontsizept)
		# Position of number is (center of frame) - (half of dimension of number)
		textx = (facex2-facex1)/2+facex1 - (fnt.getsize(str(x+1))[0] / 2)
		texty = (facey2-facey1)/2+facey1 - (fnt.getsize(str(x+1))[1] / 2)

		# Draw number and face box
		draw.text((textx, texty), str(x+1), font=fnt, fill=(255,0,0,255))
		draw.line((facex1,facey1, facex2, facey1), fill=500, width=linethicc)
		draw.line((facex2,facey1, facex2, facey2), fill=500, width=linethicc)
		draw.line((facex2,facey2, facex1, facey2), fill=500, width=linethicc)
		draw.line((facex1,facey2, facex1, facey1), fill=500, width=linethicc)

	# save new image with faces
	im.save('markedimage.jpg')

	return;

################################################################################
# Main
# Selfect source, camera or local
selsource = input("Do you want to use camera image? (y/n)\t")
if(selsource == "y"):
	imm = cimg #directly go for camera file
	newshot = input("Do you want to make a new image? (y/n)\t")
	if(newshot == "y"):
		getnewimage()
		evalimage()
		getfaces()
		main(nofaces)
		sys.exit()

	processim = input("Do you want to reprocess image?\t")# when testing to save time
	if(processim == "y"):
		evalimage()
	getfaces()
	main(nofaces)
	sys.exit()

# Select image from local, add or remove lines for your case
selimage = input("Which stored image do you want to use? (1, 2, 3, s)\t")
if selimage == "1":
	imm = im1
elif selimage == "2":
	imm = im2
elif selimage == "3":
	imm = im3
elif selimage == "s":
	imm = sim #use sample image on root
else:
	sys.exit("No image!") #no image
processim = input("Do you want to reprocess image? (y/n)\t")# when testing to save time
if(processim == "y"):
	evalimage()
getfaces()
main(nofaces)
sys.exit()
