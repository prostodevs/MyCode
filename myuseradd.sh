#! /bin/bash
prompt(){
echo "What is the user's name?"
read USER
echo "What is the new user group?"
echo "(if no group exists, it will be created)"
read GROUP
}

createuser(){
    sudo useradd $USER
    sudo usermod -aG $GROUP $USER
    echo "The new user, $USER, has been added to group '$GROUP'"
}

quit(){
    echo "Would you like to quit? (type 'exit')"
    echo "(if not, another user will be added)"
    read QUIT
}

echo "This is myuseradd application!"
echo "Please enjoy your stay"

while [ "$QUIT" != "exit" ]
do
    prompt
    quit
    createuser
done

echo "This has been myuseradd, thanks for using!"
