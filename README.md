# hashcode
Hackathon tool, initially intended for Hash Code 2020.

## Execution
To make `main.py` executable, run :
```bash
$ chmod +x main.py
```

Make sure to have python3.8 installed.

### System arguments
* service name as `--name` (will default to `solve`)
* source package name
* instance aliases

### Examples
```bash
$ ./main.py --solve greedy/ a b
$ python main.py greedy quite_big
```

## Architecture
### model
The model consists of simple `Instance` and `Solution` data classes.
`score` will compute the score of a solution for a given instance.

### service
`Service` is a generic tool used on an `Instance`, such as `solve` or `view`.
A service package contains several modules, each implementing a function
named like the service, and a class inheriting from `Service` which provides
an interface for the user (e.g. output handling).

Services can be accessed by name through `Service.load`,
or by imports such as `from solve import Solve`.

A service is instanciated with a module name, and called on an instance alias.

### data
Data is separated in `input/` and `output/` files.

`Driver` loads and writes `model` objects for an instance based on its `alias`.
It will usually be instanciated by a `Service`.

`Driver` can `load` a `Parser` for given file type (`in` or `out`)
and parsing mode. This parser implements `next` which behaves accordingly :

* in write mode ("w"), write passed arguments to a new line
* in read mode ("r"), cast new line to list with usual types (int, float, str)

### control
`control` implements generic actions such as parsing system arguments
and preparing the `upload` package, which contains the solver code
in a single file (source or zip), and the files for new best solutions.

### tools
The `chrono` decorator in `timer` offers function timing, with records
restitution through `Clock.report()`.

`report` presents data with a custom message for each entry.

## Services
### solve
`Solve` computes a solution for each alias it is given, compute the gain
and save them if no better solution was previously found.
On `close`, the `upload` package will be prepared, along with a Gains report.

### view
`View` offers visualization of instance data.

## Workflow
### Problem setup
* Define `Instance`, `Solution` and `score` in `model`
* Adapt `Driver` methods to fit file conventions
* Adapt aliasing in `driver.aliases` to fit instance naming
* Download input files to `data/input/` and clean up `data/output/`

### Solution finding
* Create a new package and make sure to provide `solve` in the `__init__.py`
* set default solver as `Solver` attribute
* Run `main` using a solver package and hope for the best

### Testing
Run `test.sh` for overall testing (arguments will be passed to `main.py`):
* All instances should have a positive gain
* All solutions should appear in `upload`, along with the source code.
* After validation, check the pylint report
