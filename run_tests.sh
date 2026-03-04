#!/bin/bash
# compile project and tests, then execute JUnit runner
./compilation.sh

# path to jars
JUNIT=lib/junit-4.13.2.jar
HAMCREST=lib/hamcrest-core-1.3.jar
MG2D=/home/pi/git/MG2D

if [ ! -f "$JUNIT" ] || [ ! -f "$HAMCREST" ]; then
    echo "Veuillez placer junit-4.13.2.jar et hamcrest-core-1.3.jar dans lib/"
    exit 1
fi

# run all tests under tests/ (names must end with Test)
java -cp .:$MG2D:$JUNIT:$HAMCREST org.junit.runner.JUnitCore \
    $(ls tests/*Test.java | sed 's#.*/##; s/\.java$//')
