# Readme not created yet!
Readme will be created if this project *really* goes somewhere. Or if I just feel like doing some github work for fun I will make one.

![](http://ForTheBadge.com/images/badges/made-with-python.svg)

![](https://img.shields.io/badge/Ko--fi-F16061?style=for-the-badge&logo=ko-fi&logoColor=white)


<!-- TOP OF README ANCHOR -->
<a name="top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/ZackeryRSmith/Reter/">
    <img src="https://github.com/ZackeryRSmith/Reter/blob/main/md-assets/Reter/Reter.jpg" alt="Reter logo" width="240" height="240">
  </a>

<h3 align="center">Reter</h3>

  <p align="center">
    Reter making <b>simple</b> things simple 
    <br />
    <a href="https://github.com/ZackeryRSmith/Reter/"><strong>Explore Docs! »</strong></a>
    <br />
    <br />
    <a href="https://github.com/ZackeryRSmith/Reter/">View Examples</a>
    ·
    <a href="https://github.com/ZackeryRSmith/Reter/issues">Report Bug</a>
    ·
    <a href="https://github.com/ZackeryRSmith/Reter/issues">Request Feature</a>
  </p>
</div>

<!--
Start of about
-->
# Retry Terminal
**Retry Terminal** alternatively **Terminal Retry** is a pure-python, terminal manipulation library that makes it possible to write text-based interface. It supports all UNIX terminals *hopefully windows at some point* (not all terminals are tested, see [Tested Terminals](#tested-terminals) for more info).


<!--
Start of features
-->
## Features

- Few dependencies
- Full control over writing and flushing output buffer
- Is tty
- Cursor 
    - Move the cursor N times (up, down, left, right)
    - Move to previous / next line
    - Move to column
    - Set/get the cursor position
    - Store the cursor position and restore to it later
    - Hide/show the cursor
    - Enable/disable cursor blinking (not all terminals support this feature)
- Styled output 
    - Foreground color (16 base colors)
    - Background color (16 base colors)
    - 256 (ANSI) color support
    - RGB color support
    - Text attributes like bold, italic, underscore, crossed, etc
- Terminal 
    - Clear (all lines, current line, from cursor down and up, until new line)
    - Scroll up, down
    - Set/get the terminal size
    - Exit current process
    - Alternate screen
    - Raw screen   
    - Set terminal title
    - Enable/disable line wrapping
- Event 
    - Input Events 
    - Mouse Events (press, release, position, button, drag)
    - Terminal Resize Events
    - Advanced modifier (SHIFT | ALT | CTRL) support for both mouse and key events and


<!--
Start of tested terminals
-->
### Tested Terminals

- Ubuntu Desktop Terminal
    - Ubuntu 17.10
    - Pop!_OS ( Ubuntu ) 20.04
- (Arch, Manjaro) KDE Konsole
- Linux Mint
- Alacritty
- Terminator
- Gnome
- RXVT Color Terminal

This library supports all UNIX terminals; however, not every terminal in the known universe have been tested. If you have used this library for a terminal other than the above list without issues *(or with issues)*, then feel free to contact me *(or create an issue)* It would help drastically and I would really appreciate it!


## Modules using Reter
Here are some examples of Reter found in other modules

<h2 align="center">Bo-Boxes</h2>
<div align="center">
  <a href="https://github.com/ZackeryRSmith/Bo-Boxes/">
    <img src="https://github.com/ZackeryRSmith/Reter/blob/main/md-assets/BoBoxes/Bo-Boxes.jpg" alt="Bo-Boxes logo" width="240" height="240">
  </a>

Bo-Boxes is a python module created using Reter. Bo-Boxes allows the end-user to create combo boxes in the Unix Shell working on almost every terminal. Bo-Boxes has a end-user theming system allowing you to customize all the combo-boxes looks. The images shown below are the default theme, but it can be configured to your liking!

#### Terminator
<sub>List Box</sub>

![](https://github.com/ZackeryRSmith/Reter/blob/main/md-assets/BoBoxes/terminator-listboxes.png)

#### Xterm
<sub>List Box</sub>

![](https://github.com/ZackeryRSmith/Reter/blob/main/md-assets/BoBoxes/xterm-listboxes.png)

#### Gnome
<sub>List Box</sub>

![](https://github.com/ZackeryRSmith/Reter/blob/main/md-assets/BoBoxes/gnome-listboxes.png)

#### Konsole
<sub>List Box</sub>

![](https://github.com/ZackeryRSmith/Reter/blob/main/md-assets/BoBoxes/konsole-listboxes.png)

#### RXVT
<sub>List Box</sub>

![](https://github.com/ZackeryRSmith/Reter/blob/main/md-assets/BoBoxes/rxvt-listboxes.png)

#### Yakuake
<sub>List Box</sub>

![](https://github.com/ZackeryRSmith/Reter/blob/main/md-assets/BoBoxes/yakuake-listboxes.png)
<h2></h2>

<!-- Not too sure sure if I will make this
<h2 align="center">Cures</h2>
<div align="center">
  <a href="https://github.com/ZackeryRSmith/Cures/">
    <img src="https://github.com/ZackeryRSmith/Reter/blob/main/md-assets/Cures.jpg" alt="Cures logo" width="240" height="240">
  </a>
  
Cures is a open-source python module created using reter. Cures is the open-source equivalent to Curses, a closed-source module not quite up-to-date with newer versions of python. Cures like Curses is a python module for providing the programmer with an abstraction of a display containing multiple non-overlapping windows of text. If that sounds complex don't worry, images are shown below with what 
>providing the programmer with an abstraction of a display containing multiple non-overlapping windows of text

Really means! 
-->

<h2 align="center">VDTGraphics</h2>
<div align="center">
  <a href="https://github.com/ZackeryRSmith/VDTGraphics/">
    <img src="https://github.com/ZackeryRSmith/Reter/blob/main/md-assets/VDTGraphic/VDTGraphic.jpg" alt="VDTGraphics logo" width="240" height="140">
  </a>
  
