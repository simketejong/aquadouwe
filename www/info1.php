<?php
echo exec("/usr/bin/tail -n 20 /tmp/rpm0.log | awk '{ sum += $1; n++ } END { if (n > 0) print sum / n; }'");
?>