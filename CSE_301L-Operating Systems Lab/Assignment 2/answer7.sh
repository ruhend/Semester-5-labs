# ! /bin/bash
# @author : @ruhend (Mudigonda Himansh)
# Assignment 2

#! Question 7
read -p "Number of terms to be generated : " n
x=0
y=1
i=2
echo "Fibonacci Series up to $n terms :"
echo "$x"
echo "$y"
while [ $i -lt $n ]; do
    i=$(expr $i + 1)
    z=$(expr $x + $y)
    echo "$z"
    x=$y
    y=$z
done
