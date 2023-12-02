# Python setup

`setup.py` script provides shortcut for setting up a new challenge.

```sh
python setup.py -y <year> -d <day>
```

this might work as well

```sh
./setup.py -y $(date +%Y) -d $(date +%d)
```

and then to run

```sh
./run.py -y $(date +%Y) -d $(date +%d)
```
