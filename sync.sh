#!/usr/bin/env bash

SRC="/home/krelus/AdventOfCode2023"
DEST="pi@192.168.0.7:/mnt/ext_drive/AdventOfCode2023"
DEST_GDRIVE="/mnt/chromeos/GoogleDrive/MyDrive/AdventOfCode2023"


echo "Backing up to pi"
rsync -Pcauv $SRC/ $DEST/
rsync -Pcauv $DEST/ $SRC/
# echo "Backing up to Google Drive"
# cp  -r $SRC/ $DEST_GDRIVE

echo "Data is backed up"
