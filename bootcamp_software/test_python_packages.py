import subprocess

# test for Anaconda
pypath = subprocess.check_output(["which", "python"])
if pypath.split("/")[-3] != "anaconda":
    print "WARNING: You are not running the anaconda distribution of Python!"
    print "\t If this is intentional, ignore this message."
    print "\t If you attempted to install anaconda, check your PATH..."
    print "\t you may need to prepend the ~/anaconda/bin/ directory."

# test for necessary libraries

# NumPy
try:
    import numpy
    numpy_version = numpy.__version__
    if numpy_version[0:3] != '1.9':
        print "minor warning: you are running a version of numpy < 1.9"
        print "\t to update in anaconda, use the command line:"
        print "\t $> conda update numpy"
except ImportError:
    print "WARNING: You do not have the numpy package installed"
    print "\t your Python is bare bones, please install anaconda"

# astropy
try:
    import astropy
    astropy_version = astropy.__version__
    if astropy_version[0] != '1':
        print "minor warning: you are running a version of astropy < 1.0"
        print "\t to update in anaconda, use the command line:"
        print "\t $> conda update astropy"
except ImportError:
    print "WARNING: You do not have the astropy package installed"
    print "\t to install in anaconda, use the command line:"
    print "\t $> conda install astropy"
    print "\t if you aren't using anaconda consider using pip"

# glob
try:
    import glob
except ImportError:
    print "WARNING: You do not have the glob package installed"
    print "\t your Python is bare bones, please install anaconda"

# matplotlib
try:
    import matplotlib
    matplotlib_version = matplotlib.__version__
    if matplotlib_version[0:3] != '1.4':
        print "minor warning: you are running a version of matplotlib < 1.4"
        print "\t to update in anaconda, use the command line:"
        print "\t $> conda update matplotlib"
except ImportError:
    print "WARNING: You do not have the matplotlib package installed"
    print "\t your Python is bare bones, please install anaconda"

# shelve
try:
    import shelve
except ImportError:
    print "WARNING: You do not have the shelve package installed"
    print "\t your Python is bare bones, please install anaconda"

# pickle
try:
    import pickle
except ImportError:
    print "WARNING: You do not have the pickle package installed"
    print "\t your Python is bare bones, please install anaconda"

# time
try:
    import time
except ImportError:
    print "WARNING: You do not have the time package installed"
    print "\t your Python is bare bones, please install anaconda"

# astroML
try:
    import astroML
    astroml_version = astroML.__version__
    if astroml_version[0:3] != '0.3':
        print "minor warning: you are running a version of astroML < 0.3"
        print "\t consider upgrading"
except ImportError:
    print "WARNING: You do not have the astroML package installed"
    print "\t to install in anaconda, use the command line:"
    print "\t $> conda install --channel https://conda.binstar.org/astropy astroML"
    print "\t if you aren't using anaconda consider using pip:"
    print "\t $> pip install astroML"
    print "\t ALSO! Speed up your code, by running this (all Python):"
    print "\t $> pip install astroML_addons"

# gatspy
try:
    import gatspy
    gatspy_version = gatspy.__version__
    if gatspy_version[0:3] != '0.2':
        print "minor warning: you are running a version of gatspy < 0.2"
        print "\t consider upgrading"
except ImportError:
    print "WARNING: You do not have the gatspy package installed"
    print "\t to install in anaconda, use the command line:"
    print "\t $> conda install --channel https://conda.binstar.org/srwalker101 gatspy"
    print "\t if you aren't using anaconda consider using pip:"
    print "\t $> pip install gatspy"

# astroquery
try:
    import astroquery
    astroquery_version = astroquery.__version__
    if astroquery_version[0:3] != '0.2':
        print "minor warning: you are running a version of astroquery < 0.2"
        print "\t consider upgrading"
except ImportError:
    print "WARNING: You do not have the astroquery package installed"
    print "\t to install astroquery use pip on the command line:"
    print "\t $> pip install astroquery"

# sklearn

try:
    import sklearn
    sklearn_version = sklearn.__version__
    if sklearn_version[0:4] != '0.16':
        print "minor warning: you are running a version of scikit-learn < 0.16"
        print "\t to update in anaconda, use the command line:"
        print "\t $> conda update scikit-learn"
except ImportError:
    print "WARNING: You do not have the scikit-learn package installed"
    print "\t to install in anaconda, use the command line:"
    print "\t $> conda install scikit-learn"
    print "\t if you aren't using anaconda consider using pip:"
    print "\t $> pip install scikit-learn"

# FATS 
try:
    import FATS
except ImportError:
    print "WARNING: You do not have the FATS package installed"
    print "\t to install FATS use the pip on the command line:"
    print "\t $> pip install FATS"

# IPython
try:
    import IPython
    ipy_version = IPython.__version__
    if ipy_version[0] != '3':
        print "minor warning: you are running a version of ipython < 3.0.0"
        print "\t to update in anaconda, use the command line:"
        print "\t $> conda update ipython"
except ImportError:
    print "WARNING: You do not have IPython installed"
    print "\t your Python is bare bones, please install anaconda"
    