#!/bin/bash
# compile project and tests, then execute JUnit runner
./compilation.sh

# path to jars
JUNIT=lib/junit-4.13.2.jar
HAMCREST=lib/hamcrest-core-1.3.jar
MG2D=/home/pi/git/MG2D

# download jars if they don't exist
if [ ! -f "$JUNIT" ] || [ ! -f "$HAMCREST" ]; then
    echo "JUnit/Hamcrest non trouvés ; tentative de téléchargement..."
    mkdir -p lib
    if [ ! -f "$JUNIT" ]; then
        curl -L -o "$JUNIT" \
            https://search.maven.org/remotecontent?filepath=junit/junit/4.13.2/junit-4.13.2.jar || \
            wget -O "$JUNIT" "https://search.maven.org/remotecontent?filepath=junit/junit/4.13.2/junit-4.13.2.jar"
    fi
    if [ ! -f "$HAMCREST" ]; then
        curl -L -o "$HAMCREST" \
            https://search.maven.org/remotecontent?filepath=org/hamcrest/hamcrest-core/1.3/hamcrest-core-1.3.jar || \
            wget -O "$HAMCREST" "https://search.maven.org/remotecontent?filepath=org/hamcrest/hamcrest-core/1.3/hamcrest-core-1.3.jar"
    fi
    if [ ! -f "$JUNIT" ] || [ ! -f "$HAMCREST" ]; then
        echo "Échec du téléchargement. Placez manuellement les jars dans lib/."
        exit 1
    fi
fi

# run all tests under tests/ (names must end with Test)
java -cp .:$MG2D:$JUNIT:$HAMCREST org.junit.runner.JUnitCore \
    $(ls tests/*Test.java | sed 's#.*/##; s/\.java$//')
