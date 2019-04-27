<?php 
	require_once 'connection.php';
	if (isset($_POST['AddCar']))
	{
	 	$carName 	=	$_POST['carName'];
		$brand 		=	$_POST['brand'];
		$color 		=	$_POST['color'];
		$image 		=	$_FILES["fileToUpload"]["tmp_name"];
		$target_dir = "uploads/";
		$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
		$uploadOk = 1;
		$imageFileType = strtolower(pathinfo($target_file,PATHINFO_EXTENSION));
		if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)) 
		{
        	$query 	=	mysqli_query($connection, " INSERT into cars (carName, brand , color , image) VALUES ('$carName', '$brand', '$color', '$target_file')");
        	echo "added ";
    	} 
	}
?>	