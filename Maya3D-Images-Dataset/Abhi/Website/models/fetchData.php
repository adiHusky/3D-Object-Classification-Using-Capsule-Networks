<?php

require_once 'connection.php';

if(isset($_POST['search'])){
 $search = $_POST['search'];

 $query = "SELECT * FROM category WHERE category_name like'%".$search."%'";
 $result = mysqli_query($connection,$query);

 $response = array();
 while($row = mysqli_fetch_array($result) ){
   $response[] = array("catId"=>$row['category_id'],"label"=>$row['category_name'], "category_image"=> $row['category_image'] );
 }

 echo json_encode($response);
}
?>	