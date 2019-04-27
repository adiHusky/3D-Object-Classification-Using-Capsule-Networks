<?php 
require_once 'connection.php';
if (isset($_GET['id'])) 
{

$id = $_GET['id'];

$getimage =  mysqli_query($connection , "SELECT * FROM sub_category WHERE category_id = '$id'");

while ($row = mysql_fetch_assoc($getimage))
{

 $imagedata = $row["subcategory_image"]

}
header("content-type:image/jpeg")
echo $imagedata;


}

else {

	echo "Error"
}

?>