# ambisleep

by elliott watson

## raspberry pi based sleep machine, forked from wolfgang by brad arnett
## https://github.com/daed/wolfgang

- the current version of ambisleep leverages mpc/mpd under the hood, much like wolfgang.
however the current implementation is geared around looping mp3 files rather than streaming.

- tracks are currently added via `mpc add file:///filepath`
which worked after enabling unix socket comm in the config file mpd.conf

- the code is currently written in python3

- the GUI elements are currently tkinter based. Subject to change

## usage
`python3 ambisleep.py`

click or touch the gui elements/pics to trigger a looping ambient track

click/touch the stop button to stop

## todo

- build a list of grid elements dynamically based on mpc playlist items
- get screen dimming working on the pi
- icorporate motion sensor for tighter control of when and for how long the screen stays on
- modularize code
- try a React UI version?

## current hardware (cat /proc/cpuinfo):
Hardware        : BCM2835
Revision        : a02082
Serial          : 0000000067bcd520
Model           : Raspberry Pi 3 Model B Rev 1.2

## os (cat /etc/os-release)
PRETTY_NAME="Raspbian GNU/Linux 11 (bullseye)"
NAME="Raspbian GNU/Linux"
VERSION_ID="11"
VERSION="11 (bullseye)"
VERSION_CODENAME=bullseye
ID=raspbian
ID_LIKE=debian
HOME_URL="http://www.raspbian.org/"
SUPPORT_URL="http://www.raspbian.org/RaspbianForums"
BUG_REPORT_URL="http://www.raspbian.org/RaspbianBugs"
