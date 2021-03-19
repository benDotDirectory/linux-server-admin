# init_vm.sh
# Initializes a VM to my spec
# Tested on Ubuntu Server

# Update
sudo apt update && sudo apt upgrade && sudo apt full-upgrade && sudo apt autoremove && sudo apt purge

# Install software
sudo apt install git screenfetch net-tools

# Create ~/scripts and populate
mkdir ~/scripts
git clone https://github.com/benDotDirectory/linux-server-admin.git ~/scripts
cd ~/scripts
chmod +x *.sh

# @TODO: x11 forwarding

# @TODO: enable ufw
