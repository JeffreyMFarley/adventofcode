#!/bin/sh

set -e

NEW_DIR="./2022/$1"

mkdir "$NEW_DIR"
touch "$NEW_DIR/input0.txt"
touch "$NEW_DIR/input1.txt"
cp ./solve_template.py "$NEW_DIR/solve1.py"
