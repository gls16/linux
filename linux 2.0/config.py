
from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from os import path
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()

color_base = "#101010" 


def sep(color):
    return widget.Sep(     
        background = color,
        foreground = color,
        padding = 4,
    )

def triangle(background,foreground):
    return widget.TextBox(
        text = " ",
        fontsize = 50,
        padding = -1,
        background = background,
        foreground = foreground
    )

def triangle_2(background,foreground):
    return widget.TextBox(
        text = "  ",
        fontsize = 28,
        padding = -1,
        background = background,
        foreground = foreground
    )
def icon(icono,background):
    return widget.TextBox(
    text = icono,
    background = background,
    fontsize = 20,
    padding = 12
    )

keys = [
    # Switch between windows
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(),desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(),desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(),desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "Left", lazy.layout.grow_left(),desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(),desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(),desc="Grow window down"),
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

    #Audio
    Key([], "XF86AudioLowerVolume", lazy.spawn("pamixer --decrease 5")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pamixer --increase 5")),
    Key([], "XF86AudioMute", lazy.spawn("pamixer --toggle-mute")),

    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),

    # spawn_apps
    Key([mod],"c", lazy.spawn("google-chrome-stable")),
    Key([mod],"d", lazy.spawn("rofi -show drun -theme materia")),

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
                sep(["#FFA500","#ed1717"]),
                widget.GroupBox(
                    background = ["#FFA500","#ed1717"],
                    foreground = "#101010",
                    borderwidth = 0.3,
                    fontsize = 17,
                    active = "#101010",
                    inactive = "#F4F3EF"
                ),
                triangle_2("#101010",["#FFA500","#ed1717"]),
               
                widget.WindowName(
                    background = "#101010",
                    max_chars = 40,
                    padding = 12,
                    font = 'sans',
                    fontsize = 13,
                ),
                triangle_2(["#7f00ff","#20165b"],'#101010'),

                icon("龍",["#7f00ff","#20165b"]),

                sep(["#7f00ff","#20165b"]),

                widget.Net(
                    background = ["#7f00ff","#20165b"],
                    format = '{down} {up}',
                    interface = 'wlp3s0',
                    use_bits= 'true'
                ),
                triangle(["#7f00ff","#20165b"],["#52b2bf","#1338be"]),

                widget.CurrentLayout(
                    background = ["#52b2bf","#1338be"],
                    foreground = "#101010",
                    fontsize = 16
                ),
                
                sep(["#52b2bf","#1338be"]),

                widget.CurrentLayoutIcon(
                    background = ["#52b2bf","#1338be"],
                    foreground = "#5b0a91",
                    scale = 0.70,
                    
                ),

                triangle(["#52b2bf","#1338be"],["#59788e", "#52b2bf"]),
               
                widget.Clock(
                    format=' %I:%M ',
                    background = ["#59788e", "#52b2bf"],
                    foreground = "#000000"  
                ),
                widget.Systray(
                    background = "#101010",
                    padding = 8,
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

