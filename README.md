dwnpad-codex/datenbank-für-hardware-mit-auth-erstellen
# Hardware Database

This repository contains a simple SQLite-based application for managing hardware items. It provides both a command line interface (CLI) and a minimal web UI built with Flask.
=======
# Hardware Database CLI

This repository provides a simple command line application to manage hardware items. The application uses SQLite for storage and supports basic authentication.
main

## Features

- Register and login users
- Create hardware groups and persons
- Assign hardware items to groups and persons
- List all hardware items with their assignments
 dwnpad-codex/datenbank-für-hardware-mit-auth-erstellen
- Simple web interface for managing hardware
=======
 main

## Requirements

- Python 3.7+
 dwnpad-codex/datenbank-für-hardware-mit-auth-erstellen
- Flask (for the web UI)

## Usage

### CLI

=======

## Usage

 main
Run the CLI application:

```bash
python hardware_db.py
```

Follow the on-screen options to register, login, and manage hardware items.
 dwnpad-codex/datenbank-für-hardware-mit-auth-erstellen

### Web UI

Install dependencies (Flask):

```bash
pip install Flask
```

Run the web application:

```bash
python -m webapp.app
```

Open your browser at `http://127.0.0.1:5000` to use the interface.
=======
 main
