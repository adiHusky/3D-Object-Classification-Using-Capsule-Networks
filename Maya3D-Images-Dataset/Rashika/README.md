


My Contribution In The Project:

 First of all we were assigned the task of learning Maya to take images of objects

![Capture1](https://user-images.githubusercontent.com/46699516/56782994-8f28c280-67b7-11e9-932a-ba486e551700.PNG)

Then I Wrote a script to get the image properties like it's shape, resolution and datatype.
 
 ![Capture2](https://user-images.githubusercontent.com/46699516/56783148-3148aa80-67b8-11e9-83ce-5a65340d7c55.PNG)
 
 ![Capture3](https://user-images.githubusercontent.com/46699516/56783177-59d0a480-67b8-11e9-83af-9bfcb8943c19.PNG)

Create a conceptual database schema along with the ERDiagram.

![Capture4](https://user-images.githubusercontent.com/46699516/56783198-75d44600-67b8-11e9-9029-bef264c26634.PNG)
 
In the website, populated the images from database provided the path of the image
 
 ![Capture5](https://user-images.githubusercontent.com/46699516/56783214-8e446080-67b8-11e9-8e39-c1c1a8d8c52b.PNG)

Created an updated Database accordingly and wrote use cases to get images from the website.

![Capture6](https://user-images.githubusercontent.com/46699516/56783232-b207a680-67b8-11e9-80d2-2102886e3914.PNG)

 ![Capture7](https://user-images.githubusercontent.com/46699516/56783269-f5621500-67b8-11e9-937f-628df6609ad2.PNG)





---SQL QUERIES---

1)search by category and display subcategories
SELECT s.subcategory_name,s.subcategory_id from sub_category s, category c where s.category_id = c.category_id and c.category_name like 'car'

2)search by subcategories and display objects
SELECT o.object_id, o.object_name from object o, sub_category s where s.subcategory_id = o.subcategory_id and s.subcategory_name like 'audi'

3)search by object and display all it's images
SELECT i.* from image i, object o, object_image_junction j where i.image_id = j.image_id and o.object_id = j.object_id and o.object_name like 'AudiA4'

4)search by angle and display images
SELECT * FROM image where x = 0 Or y = 0 or z = 100

5)search images of a particular object by it's texture
SELECT i.* from image i, object o, object_image_junction j, texture t where i.image_id = j.image_id and o.object_id = j.object_id and t.texture_id = o.texture_id and t.texture_name like 'white' and o.object_name like 'AudiA4'



Files attached:

1) Database---Contains the sql file of the CNN Database, ERDiagram and Use-Cases
2) Image Properties Scripting---Contains the jupyter Notebook for Image Properties Scripting and csv files containing Enfield,Dirtbike,R8 and RS4 Object Properties
3) Maya---Python Script to rotate objects and capture it's images
4) Website---grid.php file contains how to retrieve images stored on server by providing the path in database
5) License

