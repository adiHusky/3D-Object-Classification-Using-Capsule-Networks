# 3D-Object-Classification-Using-Capsule-Networks

When we got started with the Capsule Neural Networks (CNN) project.
We got introduced to Maya software to model a 3D image using python scripting.
We were not sure if we had to import a 3D model or create one using python in Maya.
So to get started first we went through the videos that was shared by Professor Nik Brown which was very helpful to begin with.
I started with creating objects like cubes, circles, etc.
And then I learnt about MEL scripting which is used in Maya.
I just did some basic touchbase and wanted to understand if scripting in MEL or Python was convenient for modelling an object.
As MEL was something new I did some basic learning on it to get a fair understanding.

Few of the examples just to know how a variable and a method is called in MEL inorder to understand the difference:

```mel
 proc hellotellme(string $name, int $abb)
{
    if ($abb == true)
    {
    print ("Your name is hmmm" + "\n");
    }
       else
    {
    print ("your name is " +$name +"\n");
    }
}
hellotellme("Cat",true);
hellotellme("Dog", false);
hellotellme("puppy", false);
```
Then I tried playing with some objects using MEL scripting :

```mel
{
    int $a=1;
    float $h = 1.8;
    string $y = "cat";
    
    int $yaay = true;
    
    string $objects[] = {"square \n","rectangle"};
    
    for ($i in $objects)
    {
        print $i;
    }
   }
```
And then tried coloring it to get started with creating objects initially:

```mel
string $abc[] = {"lambert1", "lambert2"};
for ($i in $abc)
{
    setAttr ($i+ ".colorR") 8;
    setAttr ($i+ ".colorG") 4;
    setAttr ($i+ ".colorB") 3;
}
```
With this I got an understanding on the basics of MEL on how it functions.
After which as Python was the priority using which we had to come up with the scripting part on getting snaps of a 3D model in every angle. I came across the website www.Turbosquid.com and downloaded a 3D object model and imported it in Maya.

The first model I tried capturing an angle using python script in Maya was of a TV.

![Branching](https://raw.githubusercontent.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/anindita/Maya3D-Images-Dataset/Anindita/3D%20Images%20-%20Maya/TV%20Image_TV_MA.PNG)

Initial script I tried was rotating an image to a 90 degree angle using the below script.
```python
import maya.cmds as cmds

ax=0
ay=0
az=0

for i in range(1,5):
        cmds.rotate( 0, '90deg', 0, 'Retro_TV:Retro_TV')
        for a in range(1,10):
            cmds.rotate('90deg',0,0,'Retro_TV:Retro_TV')
            for b in range(1,10):
                cmds.rotate(0,0,'90deg', 'Retro_TV:Retro_TV')
                 x=x+90
                 y=y+90
                 z=z+90
 ```
![Branching](https://raw.githubusercontent.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/anindita/Maya3D-Images-Dataset/Anindita/3D%20Images%20-%20Maya/TV_Image_Rotate_MA.PNG)
 
But the above script did not work as the set_attribute function was not set nor the rotate function was used.
This script just helped the 3D model to rotate once.

Later we finalized on a python script along with some environt changes in Maya that we eventually used to capture shots of 3D image models in every angles.
I worked on 12 3D image models after understanding the final script.
<br> Below is the list of the 3D items I tried capturing in every angles using Maya:
<br>
<br> 1.) Car Tyre (Automobile Items)
<br>For eg:
![Branching](https://raw.githubusercontent.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/anindita/Maya3D-Images-Dataset/Anindita/3D%20Images%20-%20Maya/Car_Tyre.PNG)
<br> 2.) WineBottle (Drinks)
<br> 3.) Antenna TV (Electronics)
<br> 4.) Light Bulb (Electronics)
<br> 5.) Capsicum (Food)
<br> 6.) Chicken (Food)
<br> 7.) Cupcake (Food)
<br> 8.) Coffee Mug (Household Items)
<br> 9.) Lantern (Household Items)
<br> 10.) Scissors (Household Items)
<br> 11.) Wineglass (Household Items)
<br> 12.) Taj Mahal (Monuments)
<br>For eg:
![Branching](https://raw.githubusercontent.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/anindita/Maya3D-Images-Dataset/Anindita/3D%20Images%20-%20Maya/Taj_Mahal.PNG)

<br> The below google drive also has the shots of 12 3D models that I captured using Maya software.
 
[https://drive.google.com/drive/u/1/folders/1FpUACGEFzOjraD5kWR0_3Elz0reb157E]()

Next, to get started with the database work we had to plan on the conceptual schema.
I along with the database team tried to understand what are the attributes that can be added for the captured images with respect to the category and we came up with a schema.

Now to store the data of an image we had to import the properties.
Manually checking for every image was not possible so we decided on creating a script that will read an image and give us the properties.
As a python beginner, I came up with a script on how to read an image using python and got its properties.
Below is the script:

```python
import numpy as np
import cv2

img = cv2.imread('.../Desktop/Capture.png')
print('Image shape is \n', img.shape)
print('Image shape is \n', img.size)
print('Image datatype is \n', img.dtype)

```
But our main motive was to import the properties of thousands of images and store it into a csv that we can use it in our database.
Later one final script got created that gets the properties while it iterates through various folders and its images and gets the property data exported to a CSV file.

Then I along with my team mates came up with the initial database schema (shown in the below ER diagram) and created a database in MySQL Workbench where we created the Images.dbo file that is stored in the link [Database File](https://github.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/blob/anindita/Maya3D-Images-Dataset/Anindita/3D%20Images%20-%20Maya/Dump20190415.sql) and which got modified later for the website integration.

![Branching](https://raw.githubusercontent.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/anindita/Maya3D-Images-Dataset/Anindita/3D%20Images%20-%20Maya/Initial%20DB_ERDiagram.png)

The final database that we came up with is:

![Octocat](https://raw.githubusercontent.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/develop-db/Maya3D-Images-Dataset/Anindita/3D%20Images%20-%20Maya/final%20db.PNG)

Next I got involved with the Cloud team to understand its scalability and implementation.
And got started with how to connect a database in GCP.
Initially we did a dry run to create a database in Google Cloud Platform by running queries to check if building a database was possible in GCP and how.

**1.) Query to Create a Database:**
```
CREATE DATABASE Images;
```
**2.) Query to Insert data into a Database**
```
USE Images;
CREATE TABLE entries (ImageName VARCHAR(255), Properties VARCHAR(255),
    ImageID INT NOT NULL, PRIMARY KEY(ImageID));
    INSERT INTO entries (ImageName, Properties) values ("Dog", "12.3MB");
    INSERT INTO entries (ImageName, Properties) values ("Cat", "16.8MB");  
```
So we can see from the above two examples that it is quite the same as we do in MySQL for creating a databse in GCP.

Then later it was decided that we will be importing the same database used by the website and hence we moved on with the cloud integration part and worked on creating cloud instances for integrating a sql database and storage bucket.
I moved on with learning on Setting up / (Linking) own domain to google cloud Storage and hosting it for free on GCP.
The steps that I researched through various videos combines to the ones stated below:

```
- Network Services > Cloud DNS > Zone
- Go to the Domain > Manage DNS
- Nameservers (Edit the name) -- add the servers that are already given by google
- Go to Cloud Storage
- Create a bucket
- Click on edit website config > main page opens up > set it with the name
- Cloud & Domain linked (For eg: from GoDaddy) or if other Domain site then go to manage DNS (server names given by google)

```
Similarly to import MySQL to cloud SQL Instance, I researched and concluded with the below steps:

```
- Under GCP> Click on SQL
- Create Instance> Choose first generation
- Choose same region> Instance ID> Click on create
- Go to Console or MAMP
- Open Webstart page > Click on the DB > Export> Custom > SQL > Go> Uncheck enclose table & column names> Go
- Copy the code & save it as DB.sql file
- Click to the DB Instance> Import (SQL or CSV) 
- In the meanwhile save the DB(exported one) into the storage> Select the DB
- And the MySQL DB gets imported to SQL instance

```
And lastly for hosting a website I came across few videos that helped me to come up with the below commands:

```
1.) Go to console.cloud.google.com
2.) Go to Compute Engine> New VM Instance> Create> Boot disk(change)> Ubuntu 18.04 LTS> Size = 30> Machine Type(US-Central 1)
3.) Allow HTTP or HTTPs traffic> Check two options> Name (Website name) -- created the instance
4.) Under instance = Connect (view gcloud command)
5.) Copy the gcloud command line
6.) Paste it in the terminal
7.) sudo apt update && sudo apt upgrade
8.) htop sudo fallocate -l 1g/swapfile
9.) sudo dd if=/dev/zero of=/swapfile bs=1024 count = 1048576
10.) sudo chmod 600/swapfile (for security concern)
11.) sudo mkswap/swapfile
12.) sudo swapon/swapfile
13.) sudo nano/etc/fstab
14.) sudo mount -a
15.) htop (to verify the space)
16.) sudo apt install tasksel
17.) sudo tasksel install lamp server
18.) sudo apt install php-curl php-gd php-mbstring php-xml php-xmlrpc
19.) curl ipconfig.me
20.) setup dns
21.) sudo nano/etc/hosts
22.) cd/etc/apache2/sites-available$ll
23.) cp 000-default.config* ... (domain).com.conf
24.) sudo cp 000-default.config* ... (domain).com.conf
25.) sudo sin
26.) clear
27.) edit the server name <Directory /var/new>
28.) a2 dissite 00.default.conf
29.) a2 ensite server.com
30.) system ctl reload apache2
31.) run the website in the link
32.) mysql -uroot
33.) create database abc (for eg.)
34.) grant ALL on abc.*To 'abc user' identified by 'Secure123' (for eg. password)
35.) quit
36.) mysql_secure_installation(mysql is secured)
37.) New password
38.) All 'Y'
39.) cd /etc/php/7.2/apache2
40.) nano php.ini 
41.) max_input_time=30 (set to 30 from 60)
42.) Set to upload_max_filesize = 20M
43.) Set to post_max_size = 21M
44.) id~
45.) id/var/www/html/
46.) /var/www/html#ll
47.) /var/www/html#mvindex.html 
48.) /var/www/html#tar_xvf.latest
49.) mv.wp-config-sample.php wp-config.php
50.) verify the database names
51.) visit the website/wp-admin/install.php
52.) nano/etc/apache2/mods-enabled/mpm-prefork.com
53.)  Start server 1
      Minimum      2
      Maximun      5
      MaxRes       10
      MaxConn      1000
54.) cd2
55.) wget

```
Later, I tried to get the properties of images converted to a Blob and store it into MySQL TABLE in an attempt to do the same for images stored in the GCP cloud storage for displaying its properties in the website. 
Although it was discarded later as our plans got changed.
Below is an attempted python code script that I created by establishing connection with MYSQL server that reads images from the local and convert it to Blob type for storing it. 
But the below script had some issues and in the meanwhile we came up with a more optimized script to get the expected output and converted to Blob.
Now we are still working to get the blob images converted to the database.

```python
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
def convertToBinaryData(filename):
    #Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData
def insertBLOB(photo):
    print("Inserting BLOB into image_properties table")
    try:
        connection = mysql.connector.connect(host='127.0.0.1:3306',
                             database='images',
                             user='root',
                             password='Anin@123')
        cursor = connection.cursor(prepared=True)
        #sql_insert_blob_query = ""INSERT INTO TABLE 'image_properties'
                          #('image_id', 'image_name', 'image_link', 'image') VALUES (%s,%s,%s,%s)""
        imagePicture = convertToBinaryData(image)
        # Convert data into tuple format
        insert_blob = (image_id, image_name, image_link, image)
        result  = cursor.execute(sql_insert_blob_query, insert_blob)
        connection.commit()
        print ("Image and file inserted successfully as a BLOB into python_employee table", result)
    except mysql.connector.Error as error :
        connection.rollback()
        print ("Failed inserting BLOB data into MySQL table {}".format(error))
    finally:
        #closing database connection
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
insertBLOB("...\Images\capture.png")
insertBLOB("...\capture1.png")
```
The above written brief piece of work is an excerpt of the tasks I have done so far towards the project Capsule Neural Networks project.

**Things I learnt:**
<br> 1.) Basics of Maya on exporting/importing and running python scripts on objects
<br> 2.) Learnt about MEL (basics)
<br> 3.) Learnt how an object can be viewed from every angle using python script and MEL library
<br> 4.) Learnt about Google Cloud Platform on setting up instances for storage bucket and SQL database
<br> 5.) Learnt to create a Database in GCP

**CONCLUSION** 

The exposure I gained from this project has helped me understand that viewing a 3D model can be implemented in the real time from every angle and also information on the viewed image's properties can be demonstrated for a user to know.

**CITATIONS**

<br>https://stackoverflow.com (referred Python scripts)
<br>https://cloud.google.com/gcp (cloud related information)
<br>https://turbosquid.com & http://free3dmodels.com (used 3D models)
<br>https://w3schools.com/sql (for database related)
<br>https://www.geeksforgeeks.org/ (for python scripts)

# MIT License
Copyright (c) 2019, Anindita Baishya

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy,modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
