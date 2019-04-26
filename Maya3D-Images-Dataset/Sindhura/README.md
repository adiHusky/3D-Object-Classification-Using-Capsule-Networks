# 3D Image dataset generation

## MAYA

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

### Images modeled using the MAYA script

https://drive.google.com/drive/u/0/folders/1FbC_pVgVmi8HFHlb8RtDvbqfBIH7PS2y

## Database

In database part, we came up with the initial conceptual database schema as below.

![Branching](https://raw.githubusercontent.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/sindhura/Maya3D-Images-Dataset/Sindhura/Images_ERDiagram.png)

Later, we tried establishing connection with MYSQL workbench using python script where i faced challenge in authenticating the root password. After referring to the official MYSQL site i came up with a solution to establish the connection and tried inserting values using the below code.

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
            sql_insert_query = """ INSERT INTO `category` (`category_id`, `category_name`) VALUES (1,'Animals')"""
            cursor = cnx.cursor()
            result  = cursor.execute(sql_insert_query)
            cnx.commit()
            print ("Record inserted successfully into python_users table")
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

I also worked on script to extract the image properties from the local folder. 


```python
import numpy as np
import pandas as pd
import cv2
import os
import os.path
pics = []
for files in os.listdir('/Users/../Desktop/test'):
    pics.append(files)
print(pics)
    file_name = []
size = []
shape = []
image_type = []

for i in range(0,len(pics)):
    filename = '/Users/../Desktop/test/{}'.format(pics[i])
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



Later there are few more attributes are added to the schema based on the website requirement. Created new physical database based on the changes.

![Branching](https://raw.githubusercontent.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/sindhura/Maya3D-Images-Dataset/Sindhura/Final_schema.png)

The above schema can be explained with an example below:


<br> category - table 
<br> category_id: C01 (PK) 
<br> category_name: Animals 


<br> sub_category - table
<br> sub_category_id: C01_01 (PK)
<br> category_id: C01(FK)
<br> sub_category_name: Dog


<br> object - table
<br> object_id: O1_01 (PK)
<br> object_name: labrador
<br> sub_category_id: C01_01 (FK)
<br> texture_id : tx_01
<br> background_id : bk_01
<br> shadow_id : sh_01


<br> texture - table
<br> texture_id : tx_01 (PK)
<br> texture_name : black


<br> background - table
<br> background_id : bk_01 (PK)
<br> background_name : white


<br> shadow - table
<br> shadow_id : sh_01 (PK)
<br> shadow_presence : yes


<br> object_image_junction - table
<br> image_id : I01
<br> object_id : O1_01


<br> image_data - TABLE
<br> image_id: I01 (PK)
<br> image_name : (FK)
<br> image_size: in KB
<br> image_resolution: 960X540
<br> image_type: .png
<br> image: BLOB image
<br> X: angle in degree
<br> Y: angle in degree
<br> Z: angle in degree


## Portfolio

Created portfolio to show the details of overall project.

https://sindhurakolli.github.io/DMDD_portfolio/

Added all the files related to work in git hub : 

https://github.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/tree/sindhura/Maya3D-Images-Dataset/Sindhura 


## Contributions

In the entire project, i have contributed my work towards generations of images for 10 object models in MAYA, creating database conceptual schema and physical database, connection of database using python to MYSQL workbench and inserting data to tables. Created portfolio for the project.

## Citations and References

https://dev.mysql.com/doc/connector-python/en/connector-python-installation.html 

https://dev.mysql.com/doc/refman/8.0/en/upgrading-from-previous-series.html#upgrade-caching-sha2-password-root-account 

https://www.w3schools.com/sql/

https://www.geeksforgeeks.org/working-images-python/


## Licence

MIT License

Copyright (c) 2019 Sindhura Kolli

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
