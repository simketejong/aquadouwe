 #!/bin/bash          

file="/tmp/rpm0.log"
if [ -f "$file" ]
then
poep=`tail -n 10 /tmp/rpm0.log | awk '{ sum += ; n++ } END { if (n > 0) print sum / n; }'`
echo $poep
fi
