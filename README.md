# WeightScale

Python scripts that interact with webpage http://ec2-54-208-152-154.compute-1.amazonaws.com/ to identify the fake/lightest weight.
Scripts are composed of the following:
1.  goldtestrunner.py: contains the algorithm to identify the fake/lightest weight of the collection.
2.  weightscale.py: contains interaction definitions with the webpage such as loading weights, weighing weights, and reading weighing results.
3.  config.py: defines path for ChromeDriver executable for goldtestrunner and the number of weights to search.  Default number of weights is set to 9, but can be configured to integers greater than 0.

## Requirements to run
* Download or clone repository contents onto execution environment.
* Python 3.7 must be installed on execution environment.  Python downloads can be acquired from https://www.python.org/downloads/.
* Python must be defined in the __PATH__ variable to ensure Python can be executed from any directory.
* Use the package manager [pip](https://pip.pypa.io/en/stable/) (Python must be installed) from command line/terminal to install the following:

```bash
pip install selenium
```

* Google Chrome must be installed on the execution environment.  Chrome downloads can be acquired from https://www.google.com/chrome/.
* Download compatible ChromeDriver executable from https://chromedriver.chromium.org/downloads.  Executable must match installed Chrome version (refer to Help | About Google Chrome) and the script execution environment (Windows/Mac).
* Copy ChromeDriver executable into directory containing scripts: goldtestrunner.py, weightscale.py, and config.py.  __All files must be in the same directory__.
* If scripts will be run on Mac environment, provide chromedriver executable permissions to execute.  Refer to https://stackoverflow.com/questions/60362018/macos-catalinav-10-15-3-error-chromedriver-cannot-be-opened-because-the-de
* Edit config.py __path_to_chrome__ value based on execution environment:  
    * If running on Mac, set __path_to_chrome ='./chromedriver'__
    * If running on Windows, set __path_to_chrome = '.\\\\chromedriver.exe'__
* Cd into directory containing scripts.

## Identifying the fake/lightest weight
The scripts shall identify the fake weight based on a collection of the size defined within the config.py.  Default value is 9, but may be adjusted by updating the __weights__ variable.
The fake/lightest weight is determined by navigating to the directory containing goldtestrunner.py, weighscale.py, and config.py and running the command:

```
python goldtestrunner.py
```

or an approriate version of Python installed on the execution environment.  Note that some environments call Python 2.7 via python.  If Python 2.7 is called, an error pertaining to print statements shall be displayed on console/terminal.  In case Python 2.7 is called, run command with absolute path of Python 3.7 executable.
