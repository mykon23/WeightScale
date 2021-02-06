# WeightScale

Python script that interacts with the webpage http://ec2-54-208-152-154.compute-1.amazonaws.com/ in order to identify the fake/lightest weight.

## Requirements to run

Must have Python3.7 installed on the environment intended to execute the scripts.
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the following:

```bash
pip install selenium
```

All Python files within the repository are required to be within the same directory in order to execute the scripts. 

Google Chrome is required along with a compatible ChromeDriver executable.  ChromeDriver executables can be downloaded from
https://chromedriver.chromium.org/downloads.  Download an executable compatible with the Chrome version installed (refer to Help | About Google Chrome) and the script execution environment (Windows/Mac).
It is recommended that the chromedriver executable be placed within the directory containing Python files: goldtestrunner.py, weighscale.py, and config.py.  If the chromedriver executable is placed elsewhere, update the 'path_to_chrome" value within config.py with the executable's location and executable name.  Note that path must be formatted correctly as in having '/' for Mac and '\\' for Windows.  Note that Windows executable have the .exe extension.
Chromedriver may need permissions to executed within Mac environment.  Refer to
https://stackoverflow.com/questions/49787327/selenium-on-mac-message-chromedriver-executable-may-have-wrong-permissions
if running on Mac.

## Identifying the fake/lightest weight

The fake/lightest weight is determined by running the goldtestrunner.py script and may be executed via:

```
python goldtestrunner.py
```

or an approriate version of Python installed on the execution environment.  Note that some environments cally Python2.7 via python command.  Python scripts were developed with Python3.7 which cannot be exectuted with Python2.7 (which is end of life).
The goldtestrunner.py script contains the algorithm and interactions with the webpage to identify the fake web.  The behavior of the webpage such as loading weighs and reading weighing results is captured within the WeightScale class defined within weighscale.py.  The config.py file contains configurations required for the script execution.
