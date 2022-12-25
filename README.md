![Build Status](https://github.com/87yh97/imperial_test/actions/workflows/python-app.yml/badge.svg?branch=main) (main)
![Build Status](https://github.com/87yh97/imperial_test/actions/workflows/python-app.yml/badge.svg?branch=dev) (develop)

# Imperial-to-Metric-units
Repository for converter to/from Imperial unit system from/to Metric unit system

Project maintained by:

<p>Никита Якубец, гр. 3530901/90101<br>
Никита Сергиенко, гр. 3530901/90101</p>

# Options
    --from TEXT          What imperial unit to convert from  [required]
    --to TEXT            What metric unit to convert to  [required]
    --precision INTEGER  How many digits of the resulting value to show
    --log                Should program log conversions  [default: False]
    --help               Show this message and exit.

# Installation
Clone repository
> git clone https://github.com/87yh97/Imperial-to-Metric-units.git

Application needs python 3.8.10 or higher to run. To install dependencies, do:
> pip install -r requirements.txt

# Usage
First, go to the cloned project directory
> cd Imperial-to-Metric-units

Then start the application
> python3 src/converter.py

Usage examples
> python3 src/converter.py --help

> python3 src/converter.py --from inch --to metre

> python3 src/converter.py --from inch --to metre --precision 5 --log

# Usage in docker
First, go to the cloned project directory
> cd Imperial-to-Metric-units

Then build the container image
> docker build -t converter .

![docker_image_build.png](resources%2Fdocker_image_build.png)

Now you can start the application inside the container!
> docker run -t -i converter

Examples
> docker run -t -i converter --from inches --to metres

![example.png](resources%2Fexample.png)

> docker run -t -i converter --from yards --to feet --precision 3

![example2.png](resources%2Fexample2.png)
