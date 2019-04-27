<?php 
require_once 'connection.php';
if (isset($_GET['term'])) 
{
$key = $_GET['term'];

	$get =  mysqli_query($connection , "SELECT * FROM sub_category WHERE category_id LIKE '%$key%'");
}

?>

<?php include 'header.php'; ?>
	<section class="banner-result">
		<div class="container">
			<div class="row">
				<div class="col-md-10 col-lg-10 col-sm-10 col-lg-offset-1 col-md-offset-1 col-sm-offset-1">
					<div class="search-bar">
						<form action="grid.php" method="GET">
							<div class="row">
								<div class="form-group col-lg-10  col-sm-10 col-md-10">
									<input type="search" name="keyword" class="new-control" placeholder="What are you searching for?">
								</div>
								<div class="form-group col-lg-2  col-sm-2 col-md-2"><br>
									<button type="submit">
									<i class="fa fa-search text-primary fa-3x" aria-hidden="true"></i>
									</button>
								</div>
							</div>
						</form>
					</div>
				</div>
			</div>
		</div>
	</section><br>
	<div class="container">
		<div class="row">

			<div class="col-md-3 col-lg-3 col-sm-3 well">
				<div class="col-md-12" id="filter">
					<h3 style="text-transform: uppercase;"><b>FILTER</b></h3>
					<hr>

					<div class="checkbox checkbox-primary">
						<input id="all" type="checkbox"  value="all" name="brand[]" class="brand">
						<label for="checkbox1">
							ALL
						</label>
					</div>
					<?php
					$getQuery = mysqli_query($connection ,"SELECT subcategory_name, subcategory_id FROM sub_category WHERE category_id LIKE '%$key%'");
					while ($result =mysqli_fetch_array($getQuery))
					{?>
						<div class="checkbox checkbox-primary">
							<input id="honda" type="checkbox" value="<?php echo$result['subcategory_id']; ?>" name="brand[]" class="brand">
							<label for="checkbox2">
								<?php echo $result['subcategory_name'] ?>
							</label>
						</div>		
					<?php }
					 ?>
					

				</div>
			</div>	

			<div class="col-md-9 col-lg-9 col-sm-9">
				<div class="row" id="res">
					<?php 
					while ($result = mysqli_fetch_array($get))
					{
						$url = "/models/image-view.php?modelid=".$result['subcategory_id'];
						?>

						<div class="col-md-4 col-lg-4 col-sm-4">
							<div class="col-md-12">
								<p class="text-center">
									<?php $image= explode('/',$result['subcategory_image']);?>
									<a href="<?php echo $url; ?>"><img src="uploadsnew/<?php echo $image['2'] ?>" class="img-responsive img-thumbnail">
										</a>
								</p>
							</div>
						</div>
					<?php }
					?>

				</div>

			</div>
		</div>
	</div>
</body>
</html>
<script type="text/javascript">
	
	$("#filter .brand").on('click',function ()
	{
		var arr = [];
$('input.brand:checkbox:checked').each(function () {
    arr.push($(this).val());
});

$.ajax({
  type: "POST",
  url: 'filterData.php',
  data:{ "keyword": arr},
  success: function (data)
  {
  	$("#res").html(data)
  },
});
	})
</script>

<script type="text/javascript">

	$(document).ready(function () 
	{	
	$("#filter .brand").on('click',function ()
	{
		var arr = [];
		$('input.brand:checkbox:checked').each(function () {
		    arr.push($(this).val());
		});

		$.ajax({
		  type: "POST",
		  url: 'filterData.php',
		  data:{ "keyword": arr},
		  success: function (data)
		  {
		  	$("#res").html(data)
		  },
		});

})
		
		$("input#all").on("click", function ()
		{
		 if($(this).prop("checked") == true){
                $("input:checkbox").prop("checked", true)

		$.ajax({
		  type: "POST",
		  url: 'filterData.php',
		  data:{ "keyword": 'all'},
		  success: function (data)
		  {
		  	$("#res").html(data)
		  },
		});
            }

		})
	})
</script>