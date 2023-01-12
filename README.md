# **Pytest API Test Automation Framework**

A test automation framework using Pytest and the requests library for testing RESTful APIs.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing
purposes.

### Prerequisites

Python 3.8 or later

### Installing

To install the dependencies run **setup.sh** script

`sh setup.sh`

### Test Structure

The framework consists of the following components:

**Test suite**: A collection of test cases, grouped by functionality.

**Test case**: A single test scenario that verifies the functionality of the API.

**Test data**: The input data for the test cases.

**Assertions**: The expected outcome of the test cases.

The tests are located in the _tests_ directory, and are organized by functionality. Each test case has its own file, and
test data is read from a separate file.

### Adding tests

To add new test cases, create a new file with a descriptive name in the tests directory and add a test function. The
test function should make an API call using the requests library and assert the response using Pytest's built-in assert
statement. You can also include test data in a separate file and read it in your test function.

### Reports

You can generate the report by pytest-html

### Running the tests

You can run the tests by executing pytest on the root directory.

`pytest --html report.html`