
# Maya image creation

I started of with watching the videos which were provided and got a basic understanding of the Maya software and started to work around on creating the primary images such as spheres and cubes and applying different textures using lamberts on the objects.

![Octocat](https://github.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/blob/Harini/Maya3D-Images-Dataset/Harini/lambert.PNG)

Later worked with 3D image objects wchih were available online and worked around to resize the object, combine different elements in the objets and applied shaders to the images.

![Octocat](https://github.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/blob/Harini/Maya3D-Images-Dataset/Harini/lambert.PNG)
![Octocat](https://github.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/blob/Harini/Maya3D-Images-Dataset/Harini/lambert.PNG)

Once the scene was created, generated initiall images to understand the schema properties and develpoed 10 image models.


## Database creation

An initial schema was created to understand the scalibility of the dataschema and to what extent the database could be extened.

Created a script to generate the image properties to get the image properties, which were later added to the database schema.

Worked around on what is the best way to store the data in the database:
- initally file path was considered to store the data,
- Later due to the extension on the database to the website, blob images were considered to store.

Worked around on how efficiently the data could be stored and came up with a new datascheme which will reduce the redundancy of the data.

BLOB code:

``` python
def convertToBinaryData(filename):
    #Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData
  ```
    
 Created a script to convert all the images to to blob and store it in a csv which can be used to import the data into the tables directly.
    
## Further Extension

Working on creating a procedure, which accepts the image category, sub category, object name and the cvs as parameters and directly load all the data into the tables without any manual intervension.
