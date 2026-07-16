# Why-Lag

<p align="center">
  A lightweight open-source system diagnostic tool made in Python.
</p>

## About

Why-Lag is a Linux system diagnostic tool that helps users understand why their computer may be running slowly.

Instead of using generic "PC cleaner" applications, Why-Lag analyzes system resources and helps identify possible causes of lag.

Currently, Why-Lag is developed and tested mainly on Linux distributions, especially Arch Linux.

## Supported Systems

Currently supported:

- ✅ Arch Linux
- ✅ Arch-based distributions

Other Linux distributions may work, but have not been fully tested yet.

Windows and macOS support are not currently available.

## Features

Current features:

- CPU usage monitoring
- RAM usage monitoring
- Disk usage information
- Simple terminal interface

More diagnostics will be added in future versions.

## Requirements

- Linux system
- Python 3.x
- psutil

Install dependency:

```bash
sudo pacman -S python-psutil
```

or using pip inside a virtual environment:

```bash
pip install psutil
```

## Installation

Clone the repository:

```bash
git clone https://github.com/SoySki/Why-Lag.git
```

Enter the folder:

```bash
cd Why-Lag
```

Run:

```bash
python main.py
```

## Roadmap

Planned features:

- [ ] Detect processes causing high CPU usage
- [ ] Detect processes consuming high RAM
- [ ] Better explanations for users
- [ ] Temperature monitoring
- [ ] Network diagnostics
- [ ] Graphical interface
- [ ] Support for more Linux distributions

## Why?

Many users experience lag but don't know what is causing it.

Why-Lag aims to make system troubleshooting easier by explaining what is happening instead of only showing raw numbers.

## License

This project is open-source under the MIT License.
