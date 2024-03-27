#	__     __    _              _
#	\ \   / /__ (_) ___ ___  __| |_ __ _____      __
#	 \ \ / / _ \| |/ __/ _ \/ _` | '__/ _ \ \ /\ / /
#	  \ V / (_) | | (_|  __/ (_| | | |  __/\ V  V /
#	   \_/ \___/|_|\___\___|\__,_|_|  \___| \_/\_/

import os
import subprocess
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()
browser = "firefox"
file_manager = "thunar"
barsize = 32 
opct = 0.90

colors_gruvbox = {
    'dark0_hard': '#1d2021',
    'dark0': '#282828',
    'dark0_soft': '#32302f',
    'dark1': '#3c3836',
    'dark2': '#504945',
    'dark3': '#665c54',
    'dark4': '#7c6f64',
    'dark4_256': '#7c6f64',

    'gray_245': '#928374',
    'gray_244': '#928374',

    'light0_hard': '#f9f5d7',
    'light0': '#fbf1c7',
    'light0_soft': '#f2e5bc',
    'light1': '#ebdbb2',
    'light2': '#d5c4a1',
    'light3': '#bdae93',
    'light4': '#a89984',
    'light4_256': '#a89984',

    'bright_red': '#fb4934',
    'bright_green': '#b8bb26',
    'bright_yellow': '#fabd2f',
    'bright_blue': '#83a598',
    'bright_purple': '#d3869b',
    'bright_aqua': '#8ec07c',
    'bright_orange': '#fe8019',

    'neutral_red': '#cc241d',
    'neutral_green': '#98971a',
    'neutral_yellow': '#d79921',
    'neutral_blue': '#458588',
    'neutral_purple': '#b16286',
    'neutral_aqua': '#689d6a',
    'neutral_orange': '#d65d0e',

    'faded_red': '#9d0006',
    'faded_green': '#79740e',
    'faded_yellow': '#b57614',
    'faded_blue': '#076678',
    'faded_purple': '#8f3f71',
    'faded_aqua': '#427b58',
    'faded_orange': '#af3a03',
}

colors = {
    'fg':       colors_gruvbox['light2'],
    'bg':       colors_gruvbox['dark0'],
    'h':        colors_gruvbox['bright_green'],
    'o':        colors_gruvbox['bright_orange'],
    'b':        colors_gruvbox['bright_aqua'],
    'sep':      colors_gruvbox['dark4'],
}

widget_defaults = dict(
font="mono",
fontsize=14,
padding=10,
foreground=colors['h'],
background=colors['bg'],
size_percent=50
)

extension_defaults = widget_defaults.copy()
def init_widgets():
    widgets_list = [
        widget.GroupBox(
            highlight_method='line',
            highlight_color=[colors['bg']],
            this_current_screen_border=colors['h'],
            this_screen_border=colors['h']
            ),
        widget.Sep(foreground=colors['sep']),
        widget.WindowName(),
        widget.Spacer(),
        widget.Cmus(noplay_color=colors['o'],play_color=colors['h']),
        widget.Spacer(),
        widget.DF(format="󰗮 {r:.0f}%",visible_on_warn=False),
        widget.Sep(foreground=colors['sep']),
        widget.Volume(fmt='󰕾 {}'),
        widget.Sep(foreground=colors['sep']),
        widget.CPU(format="  {load_percent}%"),
        widget.Sep(foreground=colors['sep']),
        widget.Memory(measure_mem='M',format=" {MemUsed: .0f}{mm}"),
        widget.Sep(foreground=colors['sep']),
        widget.Clock(format="  %H:%M "),
    ]
    return widgets_list

@hook.subscribe.startup
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key([mod], "f", lazy.window.toggle_floating(), desc="Tile an untiled window"),
    Key([mod, "shift"], "f", lazy.window.toggle_fullscreen(), desc="Toggle Fullscreen"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),

    #### QUICKLAUNCHES ####

    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "b", lazy.spawn(browser), desc="Launch browser"),
    Key([mod], "i", lazy.spawn(file_manager), desc="file manager"),
    Key([mod], "p", lazy.spawn("alacritty -e newsboat"), desc="test"),
    Key([mod], "o", lazy.spawn("alacritty -e irssi --config ~/.config/irssi/config"), desc="test"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), lazy.spawn("rofi -show drun"), desc="dmenu"),
]

    #### MULTI MONITOR GROUPS ####

groups = [
    # Screen affinity here is used to make
    # sure the groups startup on the right screens
    Group(name="1", screen_affinity=0),
    Group(name="2", screen_affinity=0),
    Group(name="3", screen_affinity=0),
    Group(name="m", screen_affinity=1), # Second Monitor Group
]

def go_to_group(name: str):
    def _inner(qtile):
        if len(qtile.screens) == 1:
            qtile.groups_map[name].toscreen()
            return

        if name in '123':
            qtile.focus_screen(0)
            qtile.groups_map[name].toscreen()
        else:
            qtile.focus_screen(1)
            qtile.groups_map[name].toscreen()

    return _inner

for i in groups:
    keys.append(Key([mod], i.name, lazy.function(go_to_group(i.name))))
    keys.append(Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True)))

layouts = [
    layout.Columns(border_focus=colors['h'],border_width=4, margin=15),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    #layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
    layout.Floating(),
]



screens = [
    Screen(
        wallpaper='~/.config/qtile/wallpapers/ghibli-japanese-walled-garden.png',
        wallpaper_mode='fill',
        top=bar.Bar(
            widgets=init_widgets(),
            size=barsize,
            background=colors['bg'],
            opacity=opct
        )
    )
]
    

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = False 
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = False 

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.

wmname = "LG3D"
