# final_project
---
### Description
Version: *YOUR VERSION HERE*

YOUR PROJECT DESCRIPTION HERE
* Feature #1
* Feature #2
* Feature #3

### Authors
---
* [nathancmoore](https://github.com/nathancmoore/final_project)

### Dependencies
---
* s3boto
* db
* contrib
* conf
* generic
* shortcuts

### Getting Started
---
##### *Prerequisites*
* [python (3.6+)](https://www.python.org/downloads/)
* [pip](https://pip.pypa.io/en/stable/)
* [git](https://git-scm.com/)

##### *Installation*
First, clone the project repo from Github. Then, change directories into the cloned repository. To accomplish this, execute these commands:

`$ git clone https://github.com/nathancmoore/final_project.git`

`$ cd final_project`

Now now that you have cloned your repo and changed directories into the project, create a virtual environment named "ENV", and install the project requirements into your VE.

`$ python3 -m venv ENV`

`$ source ENV/bin/activate`

`$ pip install -r requirements.txt`
##### *Serving Locally*
Once you have cloned the application and installed the requirements, you can serve the project on your local machine by executing this command from your terminal, on the same level as `manage.py`.
`$ ./manage.py runserver`
Once you have executed this command, open your browser, and go to `localhost:8000/`.
### Test Suite
---
##### *Running Tests*
This application uses [unittest](https://docs.python.org/3/library/unittest.html) as a testing suite. To run tests, run:

``$ ./manage.py test``

To view test coverage, run:

``$ coverage report -m``
##### *Test Files*
The testing files for this project are:

| File Name | Description |
|:---:|:---:|
| `./ca_website/ca_events/tests.py` | Tests for our Models. |
| `./ca_website/ca_website/selenium_tests.py` | Selenium browser tests. |
| `./ca_website/ca_website/tests.py` | Tests for our views. |

### URLs
---
The URLS for this project can be found in the following modules:

| URL module | Description |
|:---:|:---:|
| ./ca_website/ca_website/urls.py | ca_website URL Configuration. |

### Django Apps
---
* ca_website
* ca_events

### Development Tools
---
* *python* - programming language
* *django* - web framework

### Contributions
---
If you wish to contribute to this project, please contact ncmoore1986@gmail.com
### License
---
This project is licensed under MIT License - see the LICENSE.md file for details.
### Acknowledgements
---
* Coffee

*This README was generated using [writeme.](https://github.com/chelseadole/write-me)*
