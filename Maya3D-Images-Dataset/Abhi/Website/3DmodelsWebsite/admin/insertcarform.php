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
	<input type="text" name="subCategoryId" placeholder="Sub Category Id">
	<input type="text" name="subCategoryName" placeholder=" Sub Category Name">
	<input type="text" name="CategoryId" placeholder=" Category Id">
	<input type="file" name="fileToUpload" id="fileToUpload">
	<input type="submit" name="AddCar" value="Add Car">
</form>
</body>
</html>