#! /usr/bin/python2.7

# tiling.py
# Simple tiling for GTK
#
# `tiling.py width height x y -d 1`
# All dimensions and coordinates are given as percentages of the screen,
# so `tiling.py 50 50 25 25 -d 1` would give you a window that's 50% of your
# screen's height and width, and positioned in the center of your screen.
# The `-d` argument indicates the presence (1) or absence (0) of window
# decorations. Remember to give the script executing right with
# `chmod +x tiling`.
#
# Examples:
#
# Size Position       Hotkey              Command
# ---------------------------------------------------------------
# 70 % TOP            <Super>Up           tiling.py 100 70 0 0 -d 0
# 30 % BOTTOM         <Super>Down         tiling.py 100 30 0 70 -d 0
# 60 % LEFT           <Super>Left         tiling.py 60 100 0 0 -d 0
# 40 % RIGHT          <Super>Right        tiling.py 40 100 60 0 -d 0
#
# 28 % TOP LEFT       <Super><Alt>Page_Up tiling.py 28 50 0 0 -d 0
# 28 % BOTTOM LEFT    <Super><Alt>Left    tiling.py 28 50 0 50 -d 0
# 28 % LEFT           <Super>Page_Up      tiling.py 28 100 0 0 -d 0
# 72 % RIGHT          <Super>Page_Down    tiling.py 72 100 28 0 -d 0
#
# 74 % CENTER         <Super><Alt>Up      tiling.py 74 74 13 13 -d 1
# 100 % CENTER        <Super><Alt>Down    tiling.py 100 100 0 0 -d 1
#
# By Sjaak van den Berg
# @svdb

from gtk.gdk import *
import argparse

TITLE_BAR = 22  # Put the height of your title bar here

# Parse the command line arguments

parser = argparse.ArgumentParser(description="Simple tiling for GTK")
parser.add_argument("w", type=int, help="Frame width (in screen %)")
parser.add_argument("h", type=int, help="Frame height (in screen %)")
parser.add_argument("x", type=int, help="Frame x coordinate (in screen %)")
parser.add_argument("y", type=int, help="Frame y coordinate (in screen %)")
parser.add_argument("-d", type=int, choices=[0, 1], default=1,
                    help="1 for window decorations, 0 for none")
args = parser.parse_args()

win = window_foreign_new((get_default_root_window()
                          .property_get('_NET_ACTIVE_WINDOW')[2][0]))
state = win.property_get('_NET_WM_STATE')[2]

# Get the screen's width and height

screen_width = screen_width()
screen_height = screen_height()

# Calculate the frame dimensions and location in pixels

w = int(round(args.w / 100.0 * screen_width))
h = int(round(args.h / 100.0 * screen_height))
x = int(round(args.x / 100.0 * screen_width))
y = int(round(args.y / 100.0 * screen_height))

# Check whether decorations are desired

if args.d == 1:
    win.set_decorations(DECOR_TITLE)  # or DECOR_ALL for all decorations
    win.move_resize(x, y, w, (h - TITLE_BAR))
if args.d == 0:
    win.set_decorations(0)
    win.move_resize(x, y, w, h)

# Apply changes to window

window_process_all_updates()
flush()
