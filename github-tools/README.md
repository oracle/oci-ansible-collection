# Tools for the SDK GitHub Repos

Requires python 3.5.  Works with 2.7 for now, but that's not guaranteed forever :)


### Installation

In a new virtualenv:

```
make install
```

### Usage

```
$ github --help
Usage: github [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  copy
```

### TODO

* Add global exclude patterns to reduce noise (.git/* especially)
* Flag to clean dst directory before installing (remove stale files)