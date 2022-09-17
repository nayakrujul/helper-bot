# helper-bot
A command-line bot which can do a lot of things!

## Installation

From PyPI:

```zsh
$ pip install helper-bot
```

## randint

### Usage

To generate a random number, use the `randint` command:

```zsh
$ randint 1 100
48
```

### Arguments

It takes two arguments:

* `a` - the minimum value of the random number
* `b` - the maximum value of the random number

## output

### Usage

To evaluate a Python expression, use the `output` command:

```zsh
$ output '"abc"*3'
abcabcabc
```

Note: the expression must be in quotes, `""` or `''`

### Arguments

It takes one argument:

* `exp`: the expression to evaluate and output

### Safety

For safety reasons, the following methods are unsupported:

* `__import__`
* `eval`
* `exec`
* `open`

An error will be raised if one of these is used.

## timein

### Usage

To get the current time in [any timezone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List), use the `timein` command:

```zsh
$ timein "US/Eastern"
17/09/2022 08:08:14 EDT -0400
```

### Arguments

It takes one argument:

* `tz`: the timezone to output the time in
