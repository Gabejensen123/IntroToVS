import matplotlib.pyplot as plt #allows you to create graphs in python from a thirdparty database. 
import numpy as np #numpy is apart of the matplotlib.pyplot library 

x = np.linspace(0, 20,100)
plt.plot(x, np.sin(x))
plt.show()

#pythong is an open source language, you can use anyones code in the world. Upsidem you dont pay for anything. 
#it has a an extenseive set of libraries
# there is no governance, when you intall these libraries they can have overlap and errors. They interfere with memory and CPU space. 
# best practices, install a Virtual environment - creates a folder and makes a copy of your python interpreter. 
# quiz 1 how to create a virtual environment, install a virtual environment. 

#Step 1 - creating a virtual environment - folder that makes a copy of your python files. #naming convention py -3 -m venv introvenv#names of the new environment
#That way this has access to the python interpreter and subsequent libraries.It made a copy of the python.exe, the things that runs pything
# 
# 
# Step 2 - activate the virtual environment - put in command line that follows the path  
#the way you know you VE has been activated if the very beginning is green (for PCS)

#Step 3 - Intsall 3rd party library, make sure you VE interpreter is in the bottom right
# installed matplotlib using,  pip3 install is the command and then you put what you want to install after pip3 install

# version control = could be anything outside of the code that we need to control 
#helps us versionUp the different iterations of our project. THey pull requests of the different iterations. So people can go back to previous versions 
# Repository is in GitHub, source our version control, source control talking about a code
#in the terminal section we are naming the source path 
