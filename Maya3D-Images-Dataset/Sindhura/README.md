# 3D Image dataset generation using Maya

#MAYA

Firstly, i went through the videos and references provided by professor to get basic knowledge on how to get started with Maya. I have tried creating some basic scripts to take screen shots of images in MAYA to get familiar with the environment.

```python

import maya.cmds as cmds 

selection = cmds.ls(sl=True)
ws = cmds.workspace(q = True, fullName = True)
wsp = ws + "/" + "images"
cmds.sysFile(wsp, makeDir=True)


for i in range(0,50):
    cmds.xform('Lamborginhi_Aventador',  ws =True,  relative=True, rotation=(45, 45, 45) )
    cmds.saveImage( currentView=True )
    imageSnapshot = wsp + "/" + "image" + str(i) +".jpg"
    cmds.refresh(cv=True, fe = "jpg", fn = imageSnapshot)

```


After that, i have modeled 10 objects of "Character" category end to end using the script that was created  with shadows. Below is the link with the images generated with shadow. 

https://drive.google.com/drive/u/0/folders/1FbC_pVgVmi8HFHlb8RtDvbqfBIH7PS2y

#Database

In database part, we came up with the conceptual database schema.

![Branching](https://raw.githubusercontent.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/sindhura/Maya3D-Images-Dataset/Sindhura/Images_ERDiagram.png)

Later, we tried establishing connection with MYSQL workbench using python script where i face challenge in authenticating the root password. After referring to the official MYSQL site i came up with a solution to establish the connection using the below code.

```sql
ALTER USER 'root'@'localhost'
 IDENTIFIED WITH mysql_native_password
 BY 'password';
```

```python
import mysql.connector
from mysql.connector import errorcode
try:
  cnx = mysql.connector.connect(host= 'localhost',
                                user='root',
                                password='password',
                                auth_plugin='mysql_native_password',
                                database='images')
  if cnx.is_connected():
            print('Connected to MySQL database')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cnx.close()

```
and created a physical database on mysql workbench. 

We also worked on script to extract the image properties from the local folder. 

```python
import numpy as np
import pandas as pd
import cv2
import os
import os.path
pics = []
for files in os.listdir('/Users/sindhurareddy/Desktop/test'):
    pics.append(files)
print(pics)
    file_name = []
size = []
shape = []
image_type = []

for i in range(0,len(pics)):
    filename = '/Users/sindhurareddy/Desktop/test/{}'.format(pics[i])
    file_name.append(filename)
for j in file_name:
    image = cv2.imread(j)
    size.append(image.size)
    shape.append(image.shape)
    image_type.append(image.dtype)
image = pd.DataFrame(np.column_stack([pics,shape,size,image_type]),
                             columns=['File Name','Shape 1','Shape 2','Shape 3','Size','Type'])
image
```



Later there are few more attributes are added to the schema based on the website requirement. Created new physical database based on the changes and inserted the sample data to configure it with cloud.

![Branching](https://raw.githubusercontent.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/sindhura/Maya3D-Images-Dataset/Sindhura/latestdbschema.PNG)



#Portfolio

Created portfolio to show the details of overall project.

https://sindhurakolli.github.io/DMDD_portfolio/

Added all the files related to work in git hub