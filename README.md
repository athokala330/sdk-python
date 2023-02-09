[![CloudGenix Logo](https://raw.githubusercontent.com/CloudGenix/sdk-python/master/docs/CloudGenix_Logo.png)](https://www.cloudgenix.com)

[![image](https://img.shields.io/pypi/v/cloudgenix.svg)](https://pypi.org/project/cloudgenix/)
[![image](https://img.shields.io/pypi/pyversions/cloudgenix.svg)](https://pypi.org/project/cloudgenix/)
[![Downloads](https://pepy.tech/badge/cloudgenix)](https://pepy.tech/project/cloudgenix)
[![License: MIT](https://img.shields.io/pypi/l/cloudgenix.svg?color=brightgreen)](https://pypi.org/project/cloudgenix/)
[![GitHub issues open](https://img.shields.io/github/issues/CloudGenix/sdk-python.svg)](https://github.com/CloudGenix/sdk-python/issues)
# CloudGenix Python SDK v6.1.2b1
Python2 and Python3 SDK for the CloudGenix AppFabric

#### Synopsis
Intended to be a small, lightweight SDK wrapper around the CloudGenix API for easy use. 
Initial version requires knowledge of JSON/Dict objects for POST/PUT/PATCH operations.

#### Requirements
* Active CloudGenix Account
* Python >=3.7
* Python modules:
    * Requests + Security Extras >= 2.22.0 - <http://docs.python-requests.org/en/master/>
    * Websockets >= 8.1 - <https://websockets.readthedocs.io/en/stable/index.html>
    * urllib3 >= 1.26.12 - <https://urllib3.readthedocs.io/en/stable/>

#### Code Example
Comes with `example.py` that shows usage to get a JSON list of sites.

Super-simplified example code (rewrite of example.py in ~4 lines of code):
```python
# Import the CloudGenix SDK API constructor and JSON response pretty printer
from cloudgenix import API, jd

# Instantiate the CloudGenix API constructor
sdk = API()

# Call CloudGenix API login using the Interactive helpers (Handle SAML2.0 login and MSP functions too!).
sdk.interactive.login()

# Print a dump of the list of sites for your selected account
jd(sdk.get.sites())
```

#### License
MIT

#### Version
| Version | Build | Changes                                                                                                   |
| ------- | ----- |-----------------------------------------------------------------------------------------------------------|
| **6.1.2** | **b1** | Deprecation of Python 2.x and 3.6 to enable SSL re-work for cleaner support and TLSv1.3 improvements.     |
| **6.1.2** | **b1** | Support for January 2023 Controller release.                                                              |
| **6.1.1** | **b1** | Support for November 2022 Controller release.                                                             |
| **6.0.2** | **b1** | Support for August 2022 Controller release.                                                               |
| **6.0.1** | **b1** | Support for June 2022 Controller release.                                                                 |
| **5.6.1** | **b2** | Minor bugfix.                                                                                             |
|           | **b1** | Support for Sept 2021 Controller release.                                                                 |
| **5.5.3** | **b1** | Support for June 2021 Controller release.                                                                 |
| **5.5.1** | **b3** | Fix for issue #25.                                                                                        |
|           | **b2** | Minor bugfixes.                                                                                           |
|           | **b1** | Support for April 2021 Controller release.                                                                |
| **5.4.3** | **b1** | Support for October 2020 Controller release.                                                              |
| **5.4.1** | **b1** | Support for July 2020 Controller release.                                                                 |
| **5.3.1** | **b1** | Support for April 2020 Controller release.                                                                |
| **5.2.3** | **b1** | Support for March 2020 Controller release.                                                                |
| **5.2.1** | **b1** | Support for January 2020 Controller release.                                                              |
| **5.1.5** | **b1** | Support for June 2019 Controller release.                                                                 |
| **5.1.1** | **b1** | Support for November 2018 Controller release.                                                             |
| **5.0.3** | **b2** | Enhanced REST API retry handling and options.                                                             |
|           | **b1** | Support for September 2018 Controller release.                                                            |
| **5.0.1** | **b1** | Support for July 2018 Controller release, New version notifications, Depreciate legacy _single functions. |
| **4.7.1** | **b1** | Support for May 2018 Controller release.                                                                  |
| **4.6.1** | **b1** | Support for Mar 2018 Controller release.                                                                  |
| **4.5.7** | **b1** | Support for Feb 2018 Controller release, Bugfix for issue #4                                              |
| **4.5.5** | **b4** | Bugfix for certain POST APIs, other minor fixes.                                                          |
|           | **b3** | CA Pinning update, *_single function deprecation, add missed 'security' extras requirement.               |
|           | **b2** | Various fixes and cleanup for public release.                                                             |
|           | **b1** | Update for 15/12/2017 API additions.                                                                      |
| **4.5.3** | **b2** | Initial Internal Release.                                                                                 |

## For more info
 * Get help and additional CloudGenix Documentation at <http://support.cloudgenix.com>
 * View the autogenerated documentation in the `docs/` directory, or at <https://cloudgenix.github.io/sdk-python/>.
 * View in-python help using `help()` functions. (example: `help(sdk.get.login)`)
