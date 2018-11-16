#!/bin/sh
rt -M \
 -o box.pix\
 $*\
 '/Users/Zitar/project/brlcad/tmp/box.g'\
 'cube' \
 2>> box.log\
 <<EOF
viewsize 2.00000000000000e+03;
orientation 2.48097349045873e-01 4.76590573266048e-01 7.48097349045873e-01 3.89434830518390e-01;
eye_pt 5.14352493537865e+03 3.60153493272174e+03 2.92798520616534e+03;
start 0; clean;
end;

EOF
