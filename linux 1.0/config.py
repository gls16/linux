# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from os import path
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()

keys = [
    # Switch between windows
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "Left", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(),desc="Spawn a command using a prompt widget"),
    
    # spawn_apps
    Key([mod],"c", lazy.spawn("google-chrome-stable")),
    Key([mod],"d", lazy.spawn("rofi -show drun ")),

    #Audio
    Key([], "XF86AudioLowerVolume", lazy.spawn("pamixer --decrease 5")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pamixer --increase 5")),
    Key([], "XF86AudioMute", lazy.spawn("pamixer --toggle-mute")),

    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),

    # screamshot
    Key([mod], "p", lazy.spawn("scrot")),

    # filemanager
    Key([mod], "s", lazy.spawn("spotify")),
    
]

groups = [Group(i) for i in ["   ","   ","    "," 阮  ","   "]]

for i,group in enumerate(groups):
    actual_key=str(i+1)
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], actual_key, lazy.group[group.name].toscreen()),

        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])       

layouts = [
    layout.Columns(
        border_width=6, 
        border_focus='#00bb2d'
        ),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall( border_width = 3,border_focus = "#00ff00", margin = 6),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font='UbuntuMono Nerd Font',
    fontsize=14,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(
                    padding= 10,
                    background = ["#FFA500","#ed1717"],
                    foreground = ["#FFA500","#ed1717"]
                ),
                widget.GroupBox(
                    background = ["#FFA500","#ed1717"],
                    foreground = "#101010",
                    borderwidth = 0.3,
                    fontsize = 17,
                    active = "#101010",
                    inactive = "#F4F3EF"
                ),
                widget.TextBox(
                    text = "  ",
                    fontsize = 60,
                    padding = -3,
                    foreground = ["#FFA500","#ed1717"],
                    background = "#101010"
                    
                ),
                widget.WindowName(
                    background = "#101010",
                    max_chars = 40,
                    padding = 12

                ),
                
                widget.Systray(
                    background = "#101010",
                    padding = 8,

                ),
                widget.TextBox(
                    text = " ",
                    fontsize = 43,
                    padding = -1,
                    foreground = ["#7f00ff","#20165b"],
                    background = "#101010",
                ),
                widget.TextBox(
                    text = ",",
                    fontsize = 15,
                    foreground = "#efebd8",
                    background = ["#7f00ff","#20165b"],
                ),
                widget.CheckUpdates(
                    custom_command = "checkupdates",
                    background = ["#7f00ff","#20165b"],
                    update_interval = 100,
                    colour_have_updates = "#f4f3ef",
                    colour_no_updates = "#ff5500",
                    display_format="act:{updates}",
                    padding = 10,
                    fontsize = 15
                    
                ),
                widget.TextBox(
                    text = " ",
                    fontsize = 43,
                    padding = -1,
                    foreground = ["#52b2bf","#1338be"],
                    background = ["#7f00ff","#20165b"]
                ),
                widget.CurrentLayout(
                    background = ["#52b2bf","#1338be"],
                    foreground = "#101010",
                    fontsize = 16
                ),
                widget.Sep(
                    background = ["#52b2bf","#1338be"],
                    foreground = ["#52b2bf","#1338be"],
                    padding = 3,
                ),
                widget.CurrentLayoutIcon(
                    background = ["#52b2bf","#1338be"],
                    foreground = "#5b0a91",
                    scale = 0.70,
                    
                ),
                widget.TextBox(
                    text = " ",
                    fontsize = 43,
                    padding = -1,
                    foreground = ["#59788e", "#52b2bf"],
                    background = ["#52b2bf","#1338be"],
                ),
                #["#59788e", "#52b2bf"],
                widget.Clock(
                    format=' %I:%M ',
                    background = ["#59788e", "#52b2bf"],
                    foreground = "#000000"  
                ),
                
            ],
            25,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"

wmname = "LG3D"
