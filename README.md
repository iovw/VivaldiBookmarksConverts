# Vivaldi bookmarks converter

Convert vivaldi browser bookmakets to firefox bookmarkets format.

## Prerequirements

- python3.6+
- pipenv

### Install requirements

```shell
pipenv install
```

## How to Run

usage: vivaldi_bookmarks_converter.py [-h] -f FILE [-o OUT]


optional arguments:

- -h, --help            show this help message and exit

- -o OUT, --out OUT     the path of output

required arguments:

- -f FILE, --file FILE  the path of vivaldi   bookmarkets

## TODO

- the vivaldi bookmarks format has a `date_added` attribute such as: `"date_added": "13227507398411997"`, but in html format, it have `ADD_DATE="1583314735" LAST_MODIFIED="1583322178"`, I don't know how to convert, so lost it.
