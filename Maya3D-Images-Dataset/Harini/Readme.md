
# Maya image creation

I started of with watching the videos which were provided and got a basic understanding of the Maya software and started to work around on creating the primary images such as spheres and cubes and applying different textures using lamberts on the objects.

![Octocat](https://github.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/blob/Harini/Maya3D-Images-Dataset/Harini/lambert.PNG)

Later I worked with 3D image objects wchih were available online and worked around on resizing the object.Few images had different layers which had to be combined to get a final object and pivots were to be centered as it affected the was shadows were generated in the final images.

![Octocat](https://github.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/blob/Harini/Maya3D-Images-Dataset/Harini/resizing.PNG)
![Octocat](https://github.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/blob/Harini/Maya3D-Images-Dataset/Harini/meshcombine.PNG)

Once the scene was created, generated initiall images to understand the schema properties and develpoed image models. As the object size was large I had to work on resizing the objecrts optimally so that the clarity of the image was not comporomised and also considering the size of the image not to go out of the image.

I have created the following objects using the Maya 

[Drive Link](https://drive.google.com/drive/u/1/folders/16t5UjjPavOiRu6UeHQIKFy53stng-Hw3)


## Database creation

An initial conceptual schema was created to understand the scalibility of the dataschema and to what extent the database could be extened and what more attributes could be added to the schema which would help the user get all the required properties of each image.

![Octocat](https://github.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/blob/Harini/Maya3D-Images-Dataset/Harini/conceptual_schema.jpeg)

The database would be incomplete without the properties of the images for which a I created a script to fetch all the image properties. The image is read using CV2 library which will fetch all the properties of the image.

```python
photos = []
for filename in os.listdir('.../Desktop/photos'):
    photos.append(filename)
    
file_name = []
shape = []
size =[]
img_type = []

for i in range(0,len(photos)):
    fn = '.../Desktop/photos/{}'.format(photos[i])
    file_name.append(fn)
    
for i in file_name:
    img = cv2.imread(i)
    shape.append(img.shape)
    size.append(img.size)
    img_type.append(img.dtype)
    
image_df = pd.DataFrame(np.column_stack([photos,shape,size,img_type]), 
                             s  columns=['file_name','shape_1','shape_2','shape_3','size','type'])
```
The above code creates a dataframe with all the image properties in a given directory.

Later I worked on what is the best way to store the data in the database:
- initally file path was considered to store the data,
- Later due to the extension on the database to the website, blob images were considered to store.
    
Created a script to convert all the images to to blob and store it in a csv which can be used to import the data into the tables directly.


BLOB code:

``` python
def convertToBinaryData(filename):
    #Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData
  ```
Which reads the image file as a binary file and store the binary string in a dataframe.

Later worked around on how efficiently the data could be stored and came up with a new datascheme which will reduce the redundancy of the data and came up with the following schema.

![Octocat](https://github.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/blob/Harini/Maya3D-Images-Dataset/Harini/Final_DB_Schema.png)

Also woked on updating the blob directly into the database. As the id's used in the varchar and not integer type Autoincrement would not work on for which increment was done in the loop. Also as the object table was separately created, I created a different data frame by which we can eliminate all the duplicate records which will be similar of all the 540 object images. This dataframe can directly be pushed into the table without any duplicates.

References:
Maya
[1](https://knowledge.autodesk.com/support/maya-lt/learn-explore/caas/CloudHelp/cloudhelp/2017/ENU/MayaLT/files/GUID-F9B3EE68-94F8-4C25-88C6-712F9C9D2B50-htm.html)
[2](https://knowledge.autodesk.com/support/maya/learn-explore/caas/CloudHelp/cloudhelp/2016/ENU/Maya/files/GUID-9656522D-ED3B-4FAA-AA95-5167A7AC3482-htm.html)
[3](https://knowledge.autodesk.com/support/maya/learn-explore/caas/CloudHelp/cloudhelp/2018/ENU/Maya-Basics/files/GUID-150B390E-840B-4FE3-B8E9-8DEBCE7CEC97-htm.html)
Data Base
[1](https://teamtreehouse.com/community/what-is-considered-the-best-practice-for-storing-images-in-a-database-how-do-twitter-and-instagram-store-images)
[2](https://dev.mysql.com/doc/workbench/en/)
[3](https://stackoverflow.com/questions/51751242/transfer-binary-data-image-etc-in-a-csv-file)
