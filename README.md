Face recognition using IBM Watson Cloud
==========================================================

This is a small project that I am working on. It is using IBM-Watson Cloud and its api for python to
recognize faces from an image. Images can be sourced local or from url. If you want more info on IBM Cloud,
check [this link](https://cloud.ibm.com/login) and for image recognition api, check [this link](https://cloud.ibm.com/apidocs/visual-recognition?code=python#detect-faces-in-an-image).

For any references, I am using Linux Mint 19.1 Cinnamon with the latest updates to all packages and software.

## Workings

This code is written in python and uses ibm_watson api to send image to the cloud for processing. Then a json
styled document is received back and saved into a json file. That data from the file is then read and from it,
number of faces, their position, gender and age can be extracted.
Then this data is used to draw frames around faces, placed numbers on them and using terminal, additional info
about each face is printed. 

This code is not in any way optimized as I am not fluent in python, but the code works well for exactly what
I want it to. Any improvements to code are welcome. All features of the code and the ones that
I might add later are described in the list below:

* Processing image from url or local with ibm_watson api using your api key
* Returned data saved into json file
* Data from json file is read and extracted to get image name, number of faces, face gender, age and position 
on the image
* For all detected faces, frames are drawn on the picture with numbers as well
* Additional info about the faces is printed in the terminal.
* Image can be also made with webcam
* A simple terminal menu is used to choose image source and option of evaluation.

## Installation

To use this script, you need python3 and pip3
(for debian/ubuntu based):
```
sudo apt install python3 pip3
```

Using pip, install all needed modules:
```
pip3 install ibm_watson pillow pygame wheel
```

If your install of `ibm_watson` fails, then you might need another package.
Error message usually indicates which.
 
## Usage

To use this script, make sure that you have everything installed. Also try the demo code
provided by IBM from the api documentation (second link on the top).

If everything works, then clone this repository and open a terminal like application in that folder and run:
```
python3 facemark.py
```
In the terminal you can navigate in a small menu asking you, if you want to use camera or image.
If you want to use camera, then click 'y', of not, then any other key.
Now it asks you which image do you want to use. I had three images in a separate folder called
'images', but if you don't want that, you can change the sources to the images in the top section of code:
```
21 im1 = './photos/sampleim1.jpg'
22 im2 = './photos/sampleim2.jpg'
23 im3 = './photos/sampleim3.jpg'
24 sim = 'sampleimage.jpg' # provided sample image in project root
25 cimg = './photo.jpg' #camera image
```
Image that I have included is in the root called 'sampleimage.jpg' and you can select it by typing 's'.

Each time after selecting source, the script will ask if you want to re-evaluate the image. That will
resize image, if too large, where you can sellect your size or remove this line if you want:
```
45 imsize = os.stat(imm).st_size	
46 if(imsize > 1000000):
47	im = Image.open(imm)
48	im.save(imm, quality=25)
```
and the second thing is sending that image to cloud. Make sure that you select the correct version and api key.
As of now, the correct version is `2018-03-19` and replace `{your_apikey}` with your key like 'youkey'.
This part exsists because when I was testing and if you are going to be using this, you won't need to re-evaluate the image every time if you are using the same image with the same evaluation resaults. Otherwise you can
remove this condition.

There are no other parts that you should modify if you like the way this script works. If you want to integrate
it into your project or build one around it, then just read the comments with code. The code is spaced and well
commented on main parts of code.

Happy coding!

##

Included image is from [rawpixel.com](rawpixel.com)
