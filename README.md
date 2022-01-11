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


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-reter">About Reter</a>
      <ul>
        <li><a href="#features">Features</a></li>
        <li><a href="#tested-terms">Tested Terminals</a></li>
      </ul>
    </li>
    <li>
      <a href="#installation">Installation</a>
      <ul>
        <li><a href="#pip">Pip</a></li>
      </ul>
    </li>
    <li><a href="#projects-using-reter">Projects Using Reter</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#thanks">Thanks</a></lu>
    <ul>
      <li><a href="#ansi-codes">Ansi Esc Codes</a></li>
      <li><a href="#stack">Stackoverflow</a></li>
      <li><a href="#lectures">Lectures</a></li>
    </ul>
  </ol>
</details>


<!--
Start of about
-->
## Retry Terminal <a name="about-reter" />
**Reter** alternatively **Terminal Retry** is a pure-python, terminal manipulation library inspired by [**crossterm**](https://github.com/crossterm-rs/crossterm#features) a terminal manipulation library for Rust. **Reter** makes it possible to write text-based interfaces (see [features](#features)). It supports all UNIX terminals *hopefully windows at some point* (not all terminals are tested, see [Tested Terminals](#tested-terminals) for more info).


<!--
Start of features
-->
### Features <a name="features" />

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
    - Clear (all lines, current line, from cursor down and up)
    - Set/get the terminal size
    - Exit current buffer
    - Alternate screen
    - Set terminal title
    - Enable/disable line wrapping
- Event
    - Input Events 
    - Terminal Resize Events
    - Advanced key events


<!--
Start of tested terminals
-->
### Tested Terminals <a name="tested-terms" />

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
  
## Installation <a name="installation" />
Want to use Reter, first let me thank you for choosing Reter! Now without further ado lets get into it,
  
### Pip <a name="pip" />
As of now pip is the only *easy* way to install Reter. 

! LET IT BE KNOWN !

This is a very early (beta) version of reter, without docs or anything!
```sh
pip install reter==1.0.6
```
 
 
<!--
Start of modules using reter
-->
## Modules using Reter
Nothing yet!
<!--
Here are some examples of Reter found in other modules

<h2 align="center">VDTGraphic</h2>
<div align="center">
  <a href="https://github.com/ZackeryRSmith/VDTGraphics/">
    <img src="https://github.com/ZackeryRSmith/Reter/blob/main/md-assets/VDTGraphic/VDTGraphic.jpg" alt="VDTGraphics logo" width="240" height="140">
  </a>
  
  **VDTGraphic** is a python library to build rich terminal user interfaces and dashboards. It is heavily inspired by the Rust library [tui-rs](https://github.com/fdehau/tui-rs)
  
  More info on this library can be found at [VDTGraphic's github](https://github.com/ZackeryRSmith/VDTGraphics/)
</div>
<h2></h2>

<h2 align="center">Bo-Boxes</h2>
<div align="center">
  <a href="https://github.com/ZackeryRSmith/Bo-Boxes/">
    <img src="https://github.com/ZackeryRSmith/Reter/blob/main/md-assets/BoBoxes/Bo-Boxes.jpg" alt="Bo-Boxes logo" width="240" height="240">
  </a>

Bo-Boxes allows the end-user to create combo boxes in the Unix Shell working on almost every terminal. Bo-Boxes has a very modular end-user theming system allowing you to customize to your needs.
  
More info on this library can be found at [BoBoxes github](https://github.com/ZackeryRSmith/Bo-Boxes/)
</div>
-->

<!--
Start of thank you,
-->
## Thank you, <a name="thanks" />

* **Zackery .R. Smith** - *Project owner & creator*
* **Timon Post** - *Author of Crossterm*

### ANSI ESC Codes <a name="ansi-codes" />
* **Christian Petersen** - *[ANSI Gist](https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797)* 
* **George Watson** - *[ANSI Table](https://www.physics.udel.edu/~watson/scen103/ascii.html)*

### Stackoverflow <a name="stack" />
*[stdin, stdout, and stderr](https://stackoverflow.com/questions/3385201/confused-about-stdin-stdout-and-stderr)*

### Lecture(s) <a name="lectures" />
* **Brian Will** - *[Unix terminals and shells](https://www.youtube.com/watch?v=07Q9oqNLXB4&list=PLFAC320731F539902)*

