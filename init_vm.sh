# init_vm.sh
# Initializes a VM to my spec
# Tested on Ubuntu Server

# Update
echo "Updating..."
sudo apt update && sudo apt upgrade && sudo apt full-upgrade && sudo apt autoremove && sudo apt purge

# Create ~/scripts and populate
mkdir ~/scripts

# @todo dl update.sh etc

chmod +x *.sh

# Downloads
sudo apt install screenfetch net-tools cowsay fortune
