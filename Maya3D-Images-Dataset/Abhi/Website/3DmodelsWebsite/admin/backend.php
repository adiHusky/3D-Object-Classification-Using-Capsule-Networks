<?php 
	require_once 'connection.php';
	if (isset($_POST['AddCar']))
	{
	 	$subCategoryId 	=	$_POST['subCategoryId'];
		$subCategoryName 		=	$_POST['subCategoryName'];
		$CategoryId 		=	$_POST['CategoryId'];
		$image 		=	$_FILES["fileToUpload"]["tmp_name"];
		$target_dir = "/../uploadsnew/";
		$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
		$uploadOk = 1;
		$imageFileType = strtolower(pathinfo($target_file,PATHINFO_EXTENSION));
		if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)) 
		{
        	$query 	=	mysqli_query($connection, " INSERT into sub_category (subcategory_id, subcategory_name , category_id , subcategory_image) VALUES ('$subCategoryId', '$subCategoryName', '$CategoryId', '$target_file')");

        	if (!$query) 
        	{
        		echo mysqli_error($connection);
        	}
        	else

        	{
        	echo "added ";
    	}
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
	
	if(isset($_POST['importSubmit']))
	{
	    
	    // Allowed mime types
	    $csvMimes = array('text/x-comma-separated-values', 'text/comma-separated-values', 'application/octet-stream', 'application/vnd.ms-excel', 'application/x-csv', 'text/x-csv', 'text/csv', 'application/csv', 'application/excel', 'application/vnd.msexcel', 'text/plain');
	    
	    // Validate whether selected file is a CSV file
	    if(!empty($_FILES['file']['name']) && in_array($_FILES['file']['type'], $csvMimes)){
	        
	        // If the file is uploaded
	        if(is_uploaded_file($_FILES['file']['tmp_name'])){
	            
	            // Open uploaded CSV file with read-only mode
	            $csvFile = fopen($_FILES['file']['tmp_name'], 'r');
	           
	            
	            // Skip the first line
	            fgetcsv($csvFile);
	            // Parse data from CSV file line by line
	            while(($line = fgetcsv($csvFile)) !== FALSE){
				/*$image 		=	$_FILES["fileToUpload"]["tmp_name"];*/
				$target_url = "/../uploads";
				
                	$imgName 	= $line[0];
                	$shape  	= $line[1];
                 	/* dirname("$csvFile");*/
					$size  		= $line[2];
					$Datatype 	= $line[3];
					$Category 	= $line[4];
					$SubCategory= $line[5];
					$ObjectName = $line[6];
					$x 			= $line[7];
					$y 			= $line[8];
					$z 			= $line[9];
					$Shadow 	= $line[10];
					$path 		=	"uploads/".$imgName;
					print_r($line);
					$origin =file_get_contents("toupload/".$imgName);
					if (file_put_contents("../uploads/$imgName",$origin))
					{
						print_r($origin);
					}
					else
					{
						echo("no");
					}

					//QUERY HERE
					$q =mysqli_query($connection,"INSERT INTO cars(carName , brand ,image) VALUES('$shape','$Category' ,'$path') ");

	            }
	            
	            // Close opened CSV file
	            fclose($csvFile);
	            
	            $qstring = '?status=succ';
	        }else{
	            $qstring = '?status=err';
	        }
	    }else{
	        $qstring = '?status=invalid_file';
	    }
	}


	if(isset($_POST['importSubmitNew']))
	{
	    
	    // Allowed mime types
	    $csvMimes = array('text/x-comma-separated-values', 'text/comma-separated-values', 'application/octet-stream', 'application/vnd.ms-excel', 'application/x-csv', 'text/x-csv', 'text/csv', 'application/csv', 'application/excel', 'application/vnd.msexcel', 'text/plain');
	    
	    // Validate whether selected file is a CSV file
	    if(!empty($_FILES['file']['name']) && in_array($_FILES['file']['type'], $csvMimes)){
	        
	        // If the file is uploaded
	        if(is_uploaded_file($_FILES['file']['tmp_name'])){
	            
	            // Open uploaded CSV file with read-only mode
	            $csvFile = fopen($_FILES['file']['tmp_name'], 'r');
	           
	            
	            // Skip the first line
	            fgetcsv($csvFile);
	            // Parse data from CSV file line by line
	            while(($line = fgetcsv($csvFile)) !== FALSE){
				/*$image 		=	$_FILES["fileToUpload"]["tmp_name"];*/
				$target_url = "/../uploads";
				
                	$imgName 	= $line[0];
                	$shape  	= $line[1];
                 	/* dirname("$csvFile");*/
					$size  		= $line[2];
					$Datatype 	= $line[3];
					$Category 	= $line[4];
					$SubCategory= $line[5];
					$ObjectName = $line[6];
					$x 			= $line[7];
					$y 			= $line[8];
					$z 			= $line[9];
					$Shadow 	= $line[10];
					$path 		=	"uploads/".$imgName;
					print_r($line);
					$origin =file_get_contents("toupload/".$imgName);
					if (file_put_contents("../uploads/$imgName",$origin))
					{
						print_r($origin);
					}
					else
					{
						echo("no");
					}

					//QUERY HERE
					$q =mysqli_query($connection,"INSERT INTO cars(carName , brand ,image) VALUES('$shape','$Category' ,'$path') ");

	            }
	            
	            // Close opened CSV file
	            fclose($csvFile);
	            
	            $qstring = '?status=succ';
	        }else{
	            $qstring = '?status=err';
	        }
	    }else{
	        $qstring = '?status=invalid_file';
	    }
	}

	
?>	