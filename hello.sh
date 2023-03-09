#!/bin/bash

count=0
number=2

while [ $count -lt 100 ]
do
  prime=1
  for ((i=2;i<=$number/2;i++))
  do
    if [ $(($number%i)) -eq 0 ]
    then
      prime=0
      break
    fi
  done
  if [ $prime -eq 1 ]
  then
    echo $number
    count=$((count+1))
  fi
  number=$((number+1))
done

