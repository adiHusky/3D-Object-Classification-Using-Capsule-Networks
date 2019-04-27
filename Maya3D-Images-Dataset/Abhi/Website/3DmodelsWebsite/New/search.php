<?php 
	require_once 'connection.php';
	$key = $_GET['keyword'];
	$get =  mysqli_query($connection , "SELECT * FROM cars WHERE carName LIKE '%$key%'");
	
	while ($result = mysqli_fetch_array($get))
	{
		echo "<pre>";
		print_r($result);
	}
 ?>