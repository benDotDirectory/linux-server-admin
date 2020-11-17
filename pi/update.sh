# update.sh
# ---------
# Runs updates and removes unused packages

echo "** update.sh **"
echo "> Updating..."
sudo apt update
echo "> Done updating."
echo "> Upgrading..."
sudo apt upgrade
echo "> Done upgrading."
echo "> Removing unused packages..."
sudo apt autoremove
echo "> Done removing unused packages."
echo "upgrade.sh - terminated."
