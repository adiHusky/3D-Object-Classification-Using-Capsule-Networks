<?php

require_once 'connection.php';
	if (isset($_POST['keyword']))
	{
		$keyword=  $_POST['keyword'];
		$keyCount=  count($_POST['keyword']);
		$query = "SELECT * FROM category_object WHERE ";
		for ($i=0; $i <$keyCount ; $i++) 
		{ 
			$query .= " category_id ='$keyword[$i]'";
			if ($i != $keyCount-1) 
			{
				$query .= " OR";
			}
		}
		$res = mysqli_query($connection, $query);
		if (mysqli_num_rows($res) >0) 
		{
while ($result = mysqli_fetch_array($res))
{
$url = "/models/image-view.php?modelid=".$result['object_model_id'];
?>

<div class="col-md-4 col-lg-4 col-sm-4">
<div class="col-md-12">
<p class="text-center">
<?php $image= explode('/',$result['object_image']);?>
<a href="<?php echo $url; ?>"><img src="uploads/<?php echo $image['2'] ?>" class="img-responsive img-thumbnail">
</a>
</p>
</div>
</div>
<?php
}
		}
		else
		{
			echo "<h2>NO DATA FOUND</h2>";
		}
	}
?>	