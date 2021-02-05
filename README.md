# WeightScale

Python script that interacts with the webpage http://ec2-54-208-152-154.compute-1.amazonaws.com/ in order to identify the fake/lightest weight.

## Requirements to run

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the following prerequisites.

```bash
pip install selenium
pip install unittest
```
Requires an environment with Google Chrome update 88 to be compatible with the chromedriver contained within the repository.
All items within the repository are required to identify the fake/lightest weight.
Chromedriver may need permissions to execute within MacOS envionrment.  Refer to
https://stackoverflow.com/questions/49787327/selenium-on-mac-message-chromedriver-executable-may-have-wrong-permissions
if running on MAC.


## Identifying the fake/lightest weight

The fake/lightest weight is determined by running the goldtestrunner.py script and may be executed via:

```
python3 goldtestrunner.py
```

or an approriate version of Python installed on the workstation.  The scripts within this repository were tested with Python 3.7 and Python 3.9.
The goldtestrunner.py is dependent on the weightscale.py and chromedriver contained within the repository and all must be in the same directory.
The WeightScale class defined within weightscale.py provides interactions with the webpage such as loading weights and reading the weighing results.
