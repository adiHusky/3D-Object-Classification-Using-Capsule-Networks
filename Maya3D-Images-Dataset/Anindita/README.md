# 3D-Object-Classification-Using-Capsule-Networks

When we got started with the Capsule Neural Networks (CNN) project.
We got introduced to Maya software to come up with python scripting for modelling a 3D object.
We were not sure if we had to import a 3D model or create one using python in Maya.
So to get started first we went through the videos that Professor Nik Brown shared which was quite helpful.
I started with creating objects like cubes, circles, etc.
And then I got inquisitive to learn about MEL scripting which is used in Maya.
I just did some basic touchbase and wanted to understand if scripting in MEL or Python was convenient for modelling an object.
As MEL was something new I got excited and did some basic learning on it.

Few of the examples just to know how a variable and a method is called in MEL just to understand the difference:

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
With this I got an understanding on the basics of MEL how it functions.
After which as Python was the priority using which we had to come up with the scripting part on getting snaps of a 3D model in every angle. I came across the website www.Turbosquid.com and downloaded a 3D object model and imported it in Maya.

The first model I tried capturing an angle using python script in Maya was of a TV.

![tv]()

Initial script I tried was rotating an image to a 90 degree angle.

![tv2]()

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
 
But the above script did not work as the set_attribute function was not set nor the rotate function was used.
This script just helped the 3D model to rotate once.

Later we finalized on a python script along with some environt changes in Maya that we used to capture shots of 3D image models in every angles.
I worked on 12 3D image models after understanding the final script.
<br> Below is the list of the 3D items I tried capturing in every angles using Maya:
<br>
<br> 1.) Car Tyre (Automobile Items)
<br> 2.) Wine (Drinks)
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

<br> The below google drive has the shots of 12 3D models that I captured using Maya software.
 
[https://drive.google.com/drive/u/1/folders/1FpUACGEFzOjraD5kWR0_3Elz0reb157E]()

Next, to get started with the database we had to come up with a schema to store the images.
I along with the database team tried to understand what are the attributes that can be added for the captured images with respect to the category and came up with a schema.

![Branching]()
![Octocat]()

And the initial database .dbo file is stored in the link []() that got modified later for the website integration.






