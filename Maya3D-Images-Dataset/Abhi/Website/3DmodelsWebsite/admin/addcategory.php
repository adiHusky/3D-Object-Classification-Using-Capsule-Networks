<script
  src="https://code.jquery.com/jquery-3.4.0.min.js"
  integrity="sha256-BJeo0qm959uMBGb65z40ejJYGSgR7REI4+CW1fNKwOg="
  crossorigin="anonymous"></script>
  <!DOCTYPE html>
<html>
<head>
	<title>Find Your Dream Car</title>
</head>
<body>
	<form method="POST" action="backend.php" enctype="multipart/form-data">
		<input type="text" name="name" placeholder="Catagory Name" required="">
		<input type="text" name="id" placeholder="Catagory ID" required="">
		<input type="file" name="fileToUpload" id="fileToUpload" required="">
		<input type="submit" name="AddCat" value="Add">
	</form>
</body>
</html>