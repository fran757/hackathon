#!/bin/bash

# overall code test

# if first argument is 'dev', enable dev mode
dev=false
if [ "$1" == "dev" ] ; then
    dev=true
    shift
fi

printf "*** cleaning up output directory\n"
if [[ $(ls data/output) ]]
then
    rm data/output/*
else
    printf "No output files\n\n"
fi

# if no input, make one up
input=$(ls data/input)
if ! [[ $input ]] ; then
    touch data/input/test.in
fi

# if main fails, clean up and quit
printf "*** running solver\n"
./main.py $@

if ! [[ $input ]] ; then
    rm data/input/test.in || true
    rm data/output/test.out || true
fi

printf "\n*** upload package contents :\n"
ls upload
rm -r upload

printf "\n"
read -n 1 -p "Everything ok ? (y|.)" answer
if [ "$answer" != y ]; then
    printf "\n"
    exit 1
fi
printf "\n\n"

if $dev ; then
cat > .pylintrc <<-EOF
[MESSAGES CONTROL]
disable=W0511, W0612, W0613
EOF
fi

find . -path ./.venv -prune -o -name "*py" -print |xargs pylint

if $dev ; then
    rm .pylintrc
fi
