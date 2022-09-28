#! /bin/bash
prompt(){
echo "What is the user's name?"
read USER
echo "What is the new user group?"
echo "(if no group exists, it will be created)"
read GROUP
}

createuser(){
    sudo useradd $user
    sudo usermod -aG $group $user
    echo "The new user, $user, has been added to group $group"
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
