#!/bin/bash

# echo "What is the name of your file ?"
# read FILE_NAME
# echo "I will create your file now"
# touch "${FILE_NAME}.txt"

# #!/bin/sh
# if [ ! -f myfile.txt ]; then
#     echo "File not found!"
#     exit 100
# fi

# check_number() {
#     if [ "$1" -gt 10 ]; then
#         echo "greater than"
#         return 0 # success
#     else
#         echo "not greater than"
#         return 1 # failure
#     fi
# }
# check_number 15
# echo "Return code was: $?"

set -x
NAME="Thomas"
echo "Hello, $NAME"
set +x


