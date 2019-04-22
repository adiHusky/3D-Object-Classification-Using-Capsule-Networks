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
	<input type="text" name="carName" placeholder="Car Name">
	<input type="text" name="brand" placeholder=" Brand">
	<select name="color">
		<option value=""> SELECT A COLOR</option>
		<option value="red" > Red 	</option>
		<option value="blue"> Blue 	</option>
		<option value="red" > Black </option>
		<option value="orange" > Orange </option>
		<option value="Yellow" > Yellow </option>
		<option value="red" > White </option>
	</select>
	<input type="file" name="fileToUpload" id="fileToUpload">
	<input type="submit" name="AddCar" value="Add Car">
</form>
</body>
</html>