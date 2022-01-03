#!/bin/sh

mkdir "$1"
cd "$1"
touch input0.txt
touch input1.txt
cp ../solve_template.py solve1.py
