 #!/bin/bash          

file="/tmp/temperature.log"
if [ -f "$file" ]
then
 bestand=`ls -la /tmp | grep temperature | cut -d " " -f 10`
 if [ $bestand -gt 250000 ]
 	then
 		/usr/bin/tail -c 100KB /tmp/temperature.log > /tmp//temp 2>&1
		/bin/mv /tmp/temp /tmp/temperature.log
 		#echo $bestand
 fi
fi

file="/tmp/rpm0.log"
if [ -f "$file" ]
then
 bestand=`ls -la /tmp | grep rpm0 | cut -d " " -f 18`
 if [ $bestand -gt 250000 ]
 	then
 		/usr/bin/tail -c 100KB /tmp/rpm0.log > /tmp//temp 2>&1
		/bin/mv /tmp/temp /tmp/rpm0.log
 		#echo $bestand
 fi
fi