#!/bin/sh

test=`cat mark.nk`
while [ $test -gt 1 ]
do
	python main.py
	test=`cat mark.nk`
done
