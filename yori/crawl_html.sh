#! /bin/sh
#
# crwal.sh
# Copyright (C) 2015 becxer <becxer87@gmail.com>
#
# Distributed under terms of the MIT license.
#

url='http://www.yorirecipe.com/bbs/board.php?bo_table=recipe&wr_id='

number=300
for i in `seq 1 $number`
do
    wget -O $i.html "$url""$i"
    echo "$i.html crawled"
done
echo "done.."

