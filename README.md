# Hardware Database

This repository contains a simple SQLite-based application for managing hardware items. It provides both a command line interface (CLI) and a minimal web UI built with Flask.

## Features

- Register and login users
- Create hardware groups and persons
- Assign hardware items to groups and persons
- List all hardware items with their assignments
- Simple web interface for managing hardware

## Requirements

- Python 3.7+
- Flask (for the web UI)

## Usage

### CLI

Run the CLI application:

```bash
python hardware_db.py
```

Follow the on-screen options to register, login, and manage hardware items.

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
