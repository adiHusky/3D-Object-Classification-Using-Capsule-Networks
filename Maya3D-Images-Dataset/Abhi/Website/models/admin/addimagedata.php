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
		<input type="text" name="objModelId" placeholder="Object Model Id" required="">
		<input type="text" name="size" placeholder="Image Size " required="">
		<input type="text" name="resolution" placeholder="Image Resolution " required="">
		<input type="text" name="type" placeholder="Image Type " required="">

		<input type="file" name="fileToUpload" id="fileToUpload" required="">

		<input type="submit" name="AddImgData" value="Add">
	</form>
</body>
</html>