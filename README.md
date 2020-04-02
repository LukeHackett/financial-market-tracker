# Financial Market Tracker

A python script to track the financial market to be run as an [AWS Lambda](https://aws.amazon.com/lambda/) function.

## Getting Started

You'll need to be using python 3.6 or higher to run this project. While the project may run with older versions of python, this project is actively supporting development with python 3.6 or higher.

See deployment for notes on how to deploy the project on a live system.

### Prerequisites

All dependencies are managed with pip, and thus installing the project's dependencies is as simple as:

```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

## Built With

* [Python 3](https://www.python.org/) - The programming language used
* [yfinance](https://github.com/ranaroussi/yfinance) - Yahoo! Finance market data downloader library

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/LukeHackett/financial-market-tracker/tags). 

## Authors

* **Luke Hackett** - *Initial work* - [LukeHackett](https://github.com/LukeHackett)

See also the list of [contributors](https://github.com/LukeHackett/financial-market-tracker/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.c](LICENSE.md) file for details
