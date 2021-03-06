<!-- Md file for pypi -->
![](https://img.shields.io/github/issues/ZackeryRSmith/Reter?color=red&style=flat-square)   ![](https://img.shields.io/github/issues-closed/ZackeryRSmith/Reter?color=darkgreen&style=flat-square)

## Retry Terminal
**Reter** alternatively **Terminal Retry** is a pure-python, terminal manipulation library inspired by [**crossterm**](https://github.com/crossterm-rs/crossterm#features) a terminal manipulation library for Rust. **Reter** makes it possible to write text-based interfaces. It supports all UNIX terminals _hopefully windows at some point_.

## Install
Linux/Mac
```
pip install reter
```

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

## Documentation
Sadly there is no documentation as far as the eye can see : (
As of now *reter is in a beta state*, when the full version releases so will documentation!
