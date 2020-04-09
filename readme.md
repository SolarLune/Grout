# Grout

A manual window tiling script for Linux written in Python, heavily inspired by [gtile](https://github.com/grocid/gtile).

## What is Grout?

Grout is a Python script to manually tile windows for Linux. The goal is to allow you to have the fun of tiling window managers like [bspwm](https://wiki.archlinux.org/index.php/Bspwm) or [i3](https://i3wm.org/), while also allowing you to use whatever window manager and Linux distro you normally use. It's not perfect, but it works fairly well nonetheless, I think.

Ideally, at some point I'd like to make it a daemon so it could, say, monitor your computer for new windows and automatically slot them into dynamic tiling layouts, but for now, this is fine. 

## WHY is Grout?

Existential!

I wanted some of the efficiency (and cool factor) of a tiling window manager. However, I didn't want to install another window manager, as I like the way my distro (Solus) looks and the general usability of it - it's just tiling that's really missing. 

So, I looked around to see if I could find a tool that did tiling _within_ an existing windowing manager, and found GTile. While it was a great start, there were some things that were lacking. So, Grout is an attempt to improve on that in a distribution-agnostic way.

## No, WHY is Grout named the way it is?

Oh.

Well, y'know. 

It's... for tiles.

So...

## WHICH is Gro- uh, I mean, Features?

- Works nicely with one desktop spread across multiple screens
- Each screen can have its own tiling layout
- Easy to extend with your own custom tiling layouts
- At least _tries_ to work with GTK apps
- ... That's it, haha.

## GIFs?

![Grout](https://thumbs.gfycat.com/DirectLazyHedgehog-small.gif)

You can also check out the same video in higher quality on YouTube [here](https://www.youtube.com/watch?v=zPT98n3sKC4&feature=youtu.be).
______

## Requirements?

Grout has a few requirements:

- Python 3
- xrandr
- xprop
- xdotool

For Solus, you can just run:

```
sudo eopkg it xrandr xprop xdotool
```

From there, just clone or download this repo and stick it somewhere, then run `grout` from there. You can also put `grout` and `config.py` somewhere in your PATH and launch it from wherever. You would probably also do well to copy `config.py` as a backup.

## What do?

To use Grout, just run:

```
grout [number]
```

The number corresponds to one of the tiles in a tiling layout. A variety of tiling layouts are provided in the config file, but you can make your own and slot it into the layout library in `config.py` very easily. 

Here's an example of a tiling layout:

```
"squares":[
		[1, 2, 2],
		[1, 2, 2],
		[4, 3, 3],
		],
```

The layout's name is "squares", and it's selected by setting `currentLayout` in `config.py` to contain "squares". With the above layout selected, `grout 1` will set the currently selected window to the top-left corner of the screen, with 33% width and 66% height - in other words, where the `1`'s are in the layout. `grout 2` will set it to 66% width and 66% height, hugging the top-right corner, which is where the `2`s are, and so on. 

Once you've got that down, you just map keyboard shortcuts to call Grout with each number in your OS's global keyboard shortcuts section. Each provided tiling layout uses a maximum of 5 tiles (numbered 1 - 5). Then you just press the key combos to tile windows as you like.

## Thanks!

You're welcome! 

If you want to thank me, throw me a bone by buying a copy of my indie dev project planning software, MasterPlan, [here](https://solarlune.itch.io/masterplan), hyuk hyuk hyuk. Note that the source for MasterPlan is also available [here](https://github.com/SolarLune/masterplan) on GitHub.

Thanks to grocid for making GTile, as well~!