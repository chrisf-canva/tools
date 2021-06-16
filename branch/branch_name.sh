#!/bin/bash

if [ $# = 0 ]
then
    echo "Usage: $0 [-b <new branch name>] [-r <based remote branch. be current branch if blank (not empty). 'origin/master' is default> ]" 1>&2
    exit 1
fi

while getopts ":b:r:" opt; do
    case ${opt} in
        b)
        	b=${OPTARG}
        	;;
        r)
            br=${OPTARG}
            br_trimmed="${br## }"
            br_trimmed="${br_trimmed%% }"
            ;;
        ?)
	        echo "unknown argument"
        	exit 1
            ;;
    esac
done

# echo "branch name is $b"
# echo "based branch is ${br}"

if [ -z "$b" ]
then echo "branch name is invalid: $b"
exit 1
fi

if [ -z "${br}" ] # null or empty
then
    echo "checkout branch from origin/master"
    python3 $(dirname $0)/branch_name.py -b "$b"
elif [ "${br_trimmed}" = "" ] # empty or blank string
then
    echo "checkout branch from current branch"
    python3 $(dirname $0)/branch_name.py -b "$b" -br "${br}"
else
    echo "checkout branch from ${br}"
    python3 $(dirname $0)/branch_name.py -b "$b" -br "${br}"
fi
