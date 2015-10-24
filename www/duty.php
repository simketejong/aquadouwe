<!DOCTYPE html>
<html>
<body>

<form method="post" action="<?php echo $_SERVER['PHP_SELF'];?>">
   Temperature raspberry: <input type="text" name="fname">
   <input type="submit">
</form>

<?php
$myfile = fopen("/tmp/temperatuur", "w") or die("Unable to open file!");
if ($_SERVER["REQUEST_METHOD"] == "POST") {
     // collect value of input field
     $name = $_POST['fname']; 
     echo $name;
     fwrite($myfile, $name);
	 fclose($myfile);
}
?>

</body>
</html>