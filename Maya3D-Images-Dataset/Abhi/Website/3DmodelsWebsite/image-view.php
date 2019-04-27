<?php include 'header.php'; ?>
<?php 
if (isset($_GET['category_id']))
{   
    $id         = $_GET['category_id'];
    $getModel   = mysqli_query($connection,"SELECT * FROM subcategory_id WHERE category_id = '$id' ");
}
 ?>
<style type="text/css">
	.gallery
{
    display: inline-block;
    margin-top: 20px;
}
</style>
<script type="text/javascript">
	$(document).ready(function(){
    $(".fancybox").fancybox({
        openEffect: "none",
        closeEffect: "none"
    });
});
   
  
</script>
<link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/fancybox/2.1.5/jquery.fancybox.min.css" media="screen">
<script src="//cdnjs.cloudflare.com/ajax/libs/fancybox/2.1.5/jquery.fancybox.min.js"></script>

<div class="container">
	<div class="row"><br><br>
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
                    $getQuery = mysqli_query($connection ,"SELECT category_name, category_id FROM category");
                    while ($result =mysqli_fetch_array($getQuery))
                    {?>
                        <div class="checkbox checkbox-primary">
                            <input id="honda" type="checkbox" value="<?php echo$result['category_id']; ?>" name="brand[]" class="brand">
                            <label for="checkbox2">
                                <?php echo $result['category_name'] ?>
                            </label>
                        </div>      
                    <?php }
                     ?>
                    

                </div>
            </div>  
        <div class="col-md-9">
            <div class='list-group gallery'>
            <?php 
            while ($data = mysqli_fetch_array($getModel))
            {?>
            <div class='col-sm-4 col-xs-6 col-md-3 col-lg-6'>

                <a class="thumbnail fancybox" rel="ligthbox" href="uploads/<?php echo $data['2'] ?>">

                    <img src="uploads/<?php echo $data['2'] ?>" class="img-responsive ">
                </a>
            </div> <!-- col-6 / end -->
           <?php } ?>
        </div> <!-- list-group / end -->
        </div>
		
	</div> <!-- row / end -->
</div> <!-- container / end -->
</body>
</html>