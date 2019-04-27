

<h1>
My Contribution In The Project:</h1>

<h2>Week1</h2>

First of all we were assigned the task of learning Maya and rotating the objects in X,Y and Z plane.Below is the script:

![Capture1](https://user-images.githubusercontent.com/46699516/56782994-8f28c280-67b7-11e9-932a-ba486e551700.PNG)

Later, I was assigned a task of creating 10 object image modelsfrom any category and below is the drive link were we uploaded our images

[Images Link](https://drive.google.com/drive/u/1/folders/14ZRx8ZiaEuuI4XEryy5VFYAyfTHbD8zk)

<h2>Week2</h2>

Then I was assigned the task pf writing a script to get the image properties like it's shape, resolution and datatype.
Initially, the script was written to get the Image properties from a single folder. But later I came up with a finalized script from where we can extract image files from all the child folders given the parent folder.
 
![Capture2](https://user-images.githubusercontent.com/46699516/56783148-3148aa80-67b8-11e9-83ce-5a65340d7c55.PNG)
 
![Capture3](https://user-images.githubusercontent.com/46699516/56783177-59d0a480-67b8-11e9-83af-9bfcb8943c19.PNG)

<h2>Week3</h2>

Create a conceptual database schema along with the following ERDiagram which was later modified according to the properties that needs to be added for the images.

![Capture4](https://user-images.githubusercontent.com/46699516/56783198-75d44600-67b8-11e9-9029-bef264c26634.PNG)
 
In the website, populated the images from database provided the path of the image for which a new column was created in the database for Image Table
 
![Capture5](https://user-images.githubusercontent.com/46699516/56783214-8e446080-67b8-11e9-8e39-c1c1a8d8c52b.PNG)


<h2>Week4</h2>

Created an updated Database from where the images are fetched in the database accordingly and wrote use cases to get images from the website.

![Capture6](https://user-images.githubusercontent.com/46699516/56783232-b207a680-67b8-11e9-80d2-2102886e3914.PNG)

Below is the updated ER Diagram which is created after finalizing the Database.

![Capture1](https://user-images.githubusercontent.com/46699516/56842697-3a905080-6866-11e9-992a-8c614bab4aa5.PNG)





<h2>
---USE CASES/SQL QUERIES---
</h2> 

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


<h2>
CONCLUSION
</h2>
This project helped me gain an insight of Capsule Networks and how 3d models can be implemented. Alo I got to learn how the database can be created to store the data of all the rotated images of a 3d objects and retrieving it to get displayed on the website.

<h2>
CITATIONS
 </h2>

1) https://www.autodesk.com
2) https://www.mkyong.com/python/python-how-to-list-all-files-in-a-directory/
3)	https://github.com/nikbearbrown/INFO_6210
4)	https://www.sqlite.org/datatype3.html
5)	https://www.w3schools.com/sql/default.asp

<h2>
MIT License
 </h2>

Copyright (c) 2019, Rashika Moza

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy,modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

