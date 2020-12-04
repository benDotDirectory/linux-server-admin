"""
transfer_ytdl_files.py

Transfers files from docker container 'youtubedl-material' internal storage to local host hard drive
"""

# Set the location of where you would like this script to copy the audio and video files
audioDest = "/media/raid/samba/bshare/yt-dl/"
videoDest = "/media/raid/samba/bshare/yt-dl/"

# Imports
import os

# Utility functions
def runCmd(cmd):
        stream = os.popen(cmd)
        res = stream.read()
        return res

def writeMsg(txt):
        print("[-] " + str(txt))

# -- Start script --
print("** transfer_ytdl_files **")
writeMsg("Transfers inernal docker files from 'youtubedl-material' container to local hard disk...")

# Get ID for docker container
writeMsg("Getting container id...")
containerId = runCmd("sudo docker ps -aqf 'name=youtubedl-material'").strip()
writeMsg(containerId)

# Form copy commands
copyAudioCmd = "sudo docker cp " + str(containerId)  + ":/app/audio " + audioDest
copyVideoCmd = "sudo docker cp " + str(containerId) + ":/app/video " + videoDest

# Run commands
writeMsg("Copying audio from docker image to host...")
runCmd(copyAudioCmd)
writeMsg("Done (" + audioDest + ")")

writeMsg("Copy video from docker image to host...")
runCmd(copyVideoCmd)
writeMsg("Done (" + videoDest + ")")

# Done
writeMsg("Finished!")
