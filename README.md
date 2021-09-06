# geekbot-api-py
A Geekbot (https://geekbot.com/) API client in python supporting async and sync operations.

Implements the Geekbot API per https://geekbot.com/developers/
<p align="center">
    <a href="https://github.com/andrewthetechie/geekbot-api-py" target="_blank">
        <img src="https://img.shields.io/github/last-commit/andrewthetechie/geekbot-api-py" alt="Latest Commit">
    </a>
        <img src="https://github.com/andrewthetechie/geekbot-api-py/actions/workflows/run_tests_with_tox.yaml/badge.svg?branch=main">
        <img src="https://codecov.io/gh/andrewthetechie/geekbot-api-py/branch/main/graph/badge.svg?token=7BK6JL2VL4"/>
    <br />
    <a href="https://pypi.org/project/geekbot-api" target="_blank">
        <img src="https://img.shields.io/pypi/v/geekbot-api" alt="Package version">
    </a>
    <img src="https://img.shields.io/pypi/pyversions/geekbot-api">
    <img src="https://img.shields.io/badge/license-MIT-green">
</p>

## Main Dependencies


-   [Python +3.6](https://www.python.org)
-   [aioredis 2.0](https://aioredis.readthedocs.io/en/latest/)
-   [pydantic](https://github.com/samuelcolvin/pydantic/)
-   [httpx](https://www.python-httpx.org/)
-   [requests](https://docs.python-requests.org/en/master/)

## Getting Started

### Installation
Install the package

    
    pip install geekbot-api

### Usage

Follow the directions on https://geekbot.com/developers/ to get an API Token

#### Example
    from geekbot_api.config import GeekbotAPIConfig
    from geekbot_api.client import GeekbotAPIClient

    config = GeekbotAPIConfig(api_key="api_YOURKEYGOESHERE")

    client = GeekbotAPIClient(config=config)

    for standup in client.standups.list():
        standups.append(standup)
        
        print(standups)

#### Async Example
    import asyncio
    from geekbot_api.config import GeekbotAPIConfig
    from geekbot_api.client import GeekbotAPIClient

    config = GeekbotAPIConfig(api_key="api_YOURKEYGOESHERE")

    client = GeekbotAPIClient(config=config)

    async def print_standups():
        standups = list()
        async for standup in client.async_standups.list():
            standups.append(standup)
        
        print(standups)
    
    if __name__ == "__main__":
        loop = asyncio.get_event_loop()
        loop.run_until_complete(print_standups())

#### Reporting to a standup using schemas

    import asyncio
    from geekbot_api.config import GeekbotAPIConfig
    from geekbot_api.client import GeekbotAPIClient
    from geekbot_api.schemas import ReportIn

    config = GeekbotAPIConfig(api_key="api_YOURKEYGOESHERE")

    client = GeekbotAPIClient(config=config)
    standup_id = "12345" # Your standup id
    answers = dict() # keys are question ids, values are a dict responding to the question
    answers['123'] = {'text': "My first answer"}
    answers['234'] = {'text': "My second answer"}

    report_in = ReportIn(standup_id=standup_id, answers=answers) # pydantic will validate your inputs
    report = client.reports.create(report_in)
    print(report)

    

## Development

The [Makefile](./makefile) has useful targets to help setup your
development encironment. We suggest using pyenv to have access to
multiple python versions easily.

### Environment Setup

-   Clone the repo and enter its root folder

    ``` {.sourceCode .bash}
    git clone https://github.com/andrewthetechie/geekbot-api-py.git && cd geekbot-api-py
    ```

-   Create a python 3.9 virtual environment and activate it. We suggest
    using [pyenv](https://github.com/pyenv/pyenv) to easily setup
    multiple python environments on multiple versions.

    ``` {.sourceCode .bash}
    # We use the extra python version (3.6, 3.7, 3.8) for tox testing
    pyenv install 3.9.6 3.6.9 3.7.11 3.8.11
    pyenv virtualenv 3.9.6 geekbot-api
    pyenv local geekbot-api 3.6.9 3.7.11 3.8.11
    ```

-   Install the dependencies

    ``` {.sourceCode .bash}
    make setup
    ```

### How to Run Tests

-   Run the test command to run tests on only python 3.9

    ``` {.sourceCode .bash}
    make test
    ```

    or

    ``` {.sourceCode .bash}
    pytest
    ```

-   Run the tox command to run all python version tests

    ``` {.sourceCode .bash}
    make tox
    ```

    or

    ``` {.sourceCode .base}
    tox
    ```

### Test Requirements

Prs should always have tests to cover the change being made. Code
coverage goals for this project are 100% coverage.

### Code Linting

All code should pass Flake8 and be blackened. If you install and setup
pre-commit (done automatically by environment setup), pre-commit will
lint your code for you.

You can run the linting manually with make

``` {.sourceCode .bash}
make lint
```

## CI

CI is run via Github Actions on all PRs and pushes to the main branch. 

Releases are automatically released by Github Actions to Pypi.

License
-------

Licensed under the [MIT License](./LICENSE)
