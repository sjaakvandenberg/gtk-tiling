#! /usr/bin/env python3

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

import gi
gi.require_version('Gdk', '3.0')
from gi.repository import Gdk
import argparse

TITLE_BAR = 22  # Put the height of your title bar here

# Parse the command line arguments

parser = argparse.ArgumentParser(description="Simple tiling for GTK")
parser.add_argument("w", type=int,
                    help="Frame width (in percentage of screen width)")
parser.add_argument("h", type=int,
                    help="Frame height (in percentage of screen height)")
parser.add_argument("x", type=int,
                    help="Frame x coordinate (in percentage of screen width)")
parser.add_argument("y", type=int,
                    help="Frame y coordinate (in percentage of screen height)")
parser.add_argument("-d", type=int, choices=[0, 1], default=1,
                    help="1 for window decorations, 0 for none")
args = parser.parse_args()

display = Gdk.Display.get_default()
num_monitors = display.get_n_monitors()
monitors = {}

def active_window():
    screen = Gdk.Screen.get_default()
    window = scree.get_active_window()

    if no_window(screen, window):
        return None

    return (window, screen)

def no_window(screen, window):
    return (
        not screen.supports_net_wm_hint(
            Gdk.atom_intern('_NET_ACTIVE_WINDOW', True)
        ) or
        not screen.supports_net_wm_hint(
            Gdk.atom_intern('NET_WM_WINDOW_TYPE', True)
        ) or
        window.get_type_hint().value_name == 'GDK_WINDOW_TYPE_HINT_DESKTOP'
    )

def offsets(window):
    origin = window.get_origin()
    root = window.get_root_origin()

    return (origin.x - root.x, origin.y - root.y)

def get_multi_screen_offset(screen, window):
    monitor = screen.get_monitor_at_window(window)
    monitor_geometry = screen.get_monitor_geometry(monitor)

    return monitor_geometry.x

# for m in list(range(0, num_monitors)):
#     monitors[m] = [
#         display.get_monitor(m).get_geometry().width,
#         display.get_monitor(m).get_geometry().height
#     ]
#     # monitors.append([
#     #     display.get_monitor(m).get_geometry().width,
#     #     display.get_monitor(m).get_geometry().height
#     # ])

# # print(monitors)
# print()

# screen = display.get_default_screen()
# window = Gdk.Screen.get_default().get_active_window()

# root_window = Gdk.get_default_root_window()

# win = window_foreign_new((get_default_root_window()
#                           .property_get('_NET_ACTIVE_WINDOW')[2][0]))
# state = win.property_get('_NET_WM_STATE')[2]

# Get the screen's width and height

# screen_width = screen_width()
# screen_height = screen_height()

# Calculate the frame dimensions and location in pixels

# w = int(round(args.w / 100.0 * screen_width))
# h = int(round(args.h / 100.0 * screen_height))
# x = int(round(args.x / 100.0 * screen_width))
# y = int(round(args.y / 100.0 * screen_height))

# # Check whether decorations are desired

# if args.d == 1:
#     win.set_decorations(DECOR_TITLE)  # or DECOR_ALL for all decorations
#     win.move_resize(x, y, w, (h - TITLE_BAR))
# if args.d == 0:
#     win.set_decorations(0)
#     win.move_resize(x, y, w, h)

# # Apply changes to window

# win.window_process_all_updates()
# win.flush()
