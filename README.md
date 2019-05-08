# pytest-hue
Control your Phillips Hue by PyTest. 

The following parameters are used:

- Brightness is controlled by the number of run tests against total number of tests
- Green hue is controlled by the number of passed tests against total number of tests
- Red hue is controlled by the number of failed tests against total number of tests
- Blue hue is controlled by the number of passed tests against total number of tests

## Configuration
You'll need to supply the following values:

- `--hue-ip`: Hue Bridge IP Address
- `--hue-username`: Username to connect to Hue Bridge with ([follow instructions here to get a new one](https://developers.meethue.com/develop/get-started-2/))
- `--hue-rooms`: Rooms to control the lights within

## Installing and Running
To install

`pip install pytest-hue`

or clone this repo and run `python setup.py install`

To run, make sure:

 - Your Phillips Hue Bridge and lights are turned on

Then run with following command (substituting the appropriate values)

`pytest --hue-ip XXX.XXX.XXX.XXX --hue-username XXXXXXXXXX --hue-rooms Office`