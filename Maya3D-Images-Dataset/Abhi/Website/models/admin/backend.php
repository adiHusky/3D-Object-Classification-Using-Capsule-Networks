<?php 
	require_once 'connection.php';
	if (isset($_POST['AddCar']))
	{
	 	$carName 	=	$_POST['carName'];
		$brand 		=	$_POST['brand'];
		$color 		=	$_POST['color'];
		$image 		=	$_FILES["fileToUpload"]["tmp_name"];
		$target_dir = "/../uploads/";
		$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
		$uploadOk = 1;
		$imageFileType = strtolower(pathinfo($target_file,PATHINFO_EXTENSION));
		if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)) 
		{
        	$query 	=	mysqli_query($connection, " INSERT into cars (carName, brand , color , image) VALUES ('$carName', '$brand', '$color', '$target_file')");
        	echo "added ";
    	} 
	}
	if (isset($_POST['AddCat']))
	{
		$name 	=	$_POST['name'];
		$id 		=	$_POST['id'];
		$image 		=	$_FILES["fileToUpload"]["tmp_name"];
		$target_dir = "../uploads/";
		$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
		$uploadOk = 1;
		$imageFileType = strtolower(pathinfo($target_file,PATHINFO_EXTENSION));
		if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)) 
		{
        	$query 	=	mysqli_query($connection, " INSERT into category (category_id, category_name ,  category_image) VALUES ( '$id','$name',  '$target_file')");
        	echo "added ";
    	} 
	}

	if (isset($_POST['addObjModel']))
	{
		$catId 		=	$_POST['catId'];
		$modelId 	=	$_POST['modelId'];
		$modelname	=	$_POST['modelname'];
		$image 		=	$_FILES["fileToUpload"]["tmp_name"];
		$target_dir = "../uploads/";
		$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
		$uploadOk = 1;
		$imageFileType = strtolower(pathinfo($target_file,PATHINFO_EXTENSION));
		if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)) 
		{
        	$query 	=	mysqli_query($connection, " INSERT INTO category_object (category_id, object_model_id , object_model_name, object_image) VALUES ( '$catId','$modelId',  '$modelname', '$target_file')");
        	if (!$query) 
        	{
        		echo mysqli_error($connection);
        	}
        	else
        	{
        		echo "Added";
        	}
    	} 
	}



	if (isset($_POST['AddImgData']))
	{
		$objModelId 	=	$_POST['objModelId'];
		$size 			=	$_POST['size'];
		$resolution		=	$_POST['resolution'];
		$type			=	$_POST['type'];
		$image 			=	$_FILES["fileToUpload"]["tmp_name"];
		$target_dir = "../uploads/";
		$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
		$uploadOk = 1;
		$imageFileType = strtolower(pathinfo($target_file,PATHINFO_EXTENSION));
		if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)) 
		{
        	$query 	=	mysqli_query($connection, " INSERT INTO image_data (object_model_id, image_size , image_resolution, image_type, image) VALUES ( '$objModelId','$size',  '$resolution', '$type', '$target_file')");
        	if (!$query) 
        	{
        		echo mysqli_error($connection);
        	}
        	else
        	{
        		echo "Added";
        	}
    	} 
	}


	
?>	