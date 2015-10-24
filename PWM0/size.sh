 #!/bin/bash          
file="/tmp/temperature.log"
if [ -f "$file" ]
then
 bestand=`/usr/bin.du -k /tmp/temperature.log | /usr/bin/cut -f1`
 if [ $bestand -gt 250 ]
 	then
 		/usr/bin/tail -c 100KB /tmp/temperature.log > /tmp//temp 2>&1
		/bin/mv /tmp/temp /tmp/temperature.log
 		#echo $bestand
 fi
fi

file="/tmp/rpm0.log"
if [ -f "$file" ]
then
 bestand=`/usr/bin/du -k /tmp/rpm0.log | /usr/bin/cut -f1`
 if [ $bestand -gt 250 ]
 	then
 		/usr/bin/tail -c 100KB /tmp/rpm0.log > /tmp//temp 2>&1
		/bin/mv /tmp/temp /tmp/rpm0.log
 		#echo $bestand
 fi
fi