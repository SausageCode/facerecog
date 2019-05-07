Face recognition using IBM Watson Cloud
==========================================================

This is a small project that I am working on. It is using IBM-Watson Cloud and its api for python to
recognize faces from an image. Images can be sourced local or from url. If you want more info on IBM Cloud,
check [this link](https://cloud.ibm.com/apidocs/visual-recognition?code=python#detect-faces-in-an-image).

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
(for debian/ubuntu based):''' sudo apt install python3 pip3 '''

Using pip, install all needed modules:
'''
pip3 install ibm_watson pillow pygame wheel
'''

If your install of '''ibm_watson''' fails, then you might need another package.
Error message usually indicates which.
 
##

Included image is from [rawpixel.com](rawpixel.com)
