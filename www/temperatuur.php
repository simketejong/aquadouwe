<?php
$Waarde=0;
$Waarde=exec("/bin/cat /sys/class/thermal/thermal_zone0/temp");
$Waarde=$Waarde/1000;
echo $Waarde;
?>