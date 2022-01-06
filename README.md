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
**Reter** alternatively **Terminal Retry** is a pure-python, terminal manipulation library inspired by [**crossterm**](https://github.com/crossterm-rs/crossterm#features) a terminal manipulation library for Rust. **Reter** makes it possible to write text-based interfaces (see [features](#features)). It supports all UNIX terminals *hopefully windows at some point* (not all terminals are tested, see [Tested Terminals](#tested-terminals) for more info).


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
    - RGB/True color support
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
    - Advanced modifier (SHIFT | ALT | CTRL) support for both mouse and key events


<!--
Start of tested terminals
-->
### Tested Terminals

- Ubuntu Desktop Terminal
    - Ubuntu 17.10
    - Pop!_OS ( *Ubuntu* ) 20.04
- (Arch, Manjaro) KDE Konsole
- Linux Mint
- Alacritty
- Terminator
- Gnome ( *Ubuntu* )
- RXVT Color Terminal

This library supports all UNIX terminals and POSIX systems; however, not every terminal in the known universe have been tested. If you have used this library for a terminal other than the above list without issues *(or with issues)*, then feel free to contact me *(or create an issue)* It would help drastically and I would really appreciate it!

<!--
Start of modules using reter
-->
## Modules using Reter
Here are some examples of Reter found in other modules

<h2 align="center">Bo-Boxes</h2>
<div align="center">
  <a href="https://github.com/ZackeryRSmith/Bo-Boxes/">
    <img src="https://github.com/ZackeryRSmith/Reter/blob/main/md-assets/BoBoxes/Bo-Boxes.jpg" alt="Bo-Boxes logo" width="240" height="240">
  </a>

Bo-Boxes allows the end-user to create combo boxes in the Unix Shell working on almost every terminal. Bo-Boxes has a very modular end-user theming system allowing you to customize to your needs.
  
More info on this library can be found at [BoBoxes github](https://github.com/ZackeryRSmith/Bo-Boxes/)
</div>
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

<h2 align="center">VDTGraphic</h2>
<div align="center">
  <a href="https://github.com/ZackeryRSmith/VDTGraphics/">
    <img src="https://github.com/ZackeryRSmith/Reter/blob/main/md-assets/VDTGraphic/VDTGraphic.jpg" alt="VDTGraphics logo" width="240" height="140">
  </a>
  
  **VDTGraphic** is a python library to build rich terminal user interfaces and dashboards. It is heavily inspired by the Rust library [tui-rs](https://github.com/fdehau/tui-rs)
  
  More info on this library can be found at [VDTGraphic's github](https://github.com/ZackeryRSmith/VDTGraphics/)
</div>
  
<!--
Start of thank you,
-->
## Thank you,

* **Zackery .R. Smith** - *Project owner & creator*

## Resources
Reter is built with documentation created by many good souls, credited below.

### ANSI ESC Codes
* **Christian Petersen** - *[ANSI Gist](https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797)* 
* **George Watson** - *[ANSI Table](https://www.physics.udel.edu/~watson/scen103/ascii.html)*
