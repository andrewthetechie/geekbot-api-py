# geekbot-api-py
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

A Geekbot (<https://geekbot.com/>) API client in python supporting async and sync operations.

Implements the Geekbot API per <https://geekbot.com/developers/>

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

- [Python +3.7](https://www.python.org)
- [pydantic](https://github.com/samuelcolvin/pydantic/)
- [httpx](https://www.python-httpx.org/)
- [requests](https://docs.python-requests.org/en/master/)

## Getting Started

### Installation

Install the package

    pip install geekbot-api

### Usage

Follow the directions on <https://geekbot.com/developers/> to get an API Token

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

- Clone the repo and enter its root folder

  ```{.sourceCode .bash}
  git clone https://github.com/andrewthetechie/geekbot-api-py.git && cd geekbot-api-py
  ```

- Create a python 3.11 virtual environment and activate it. We suggest
  using [pyenv](https://github.com/pyenv/pyenv) to easily setup
  multiple python environments on multiple versions.

- Install the dependencies

  ```{.sourceCode .bash}
  make setup
  ```

### How to Run Tests

- Run the test command to run tests on only python 3.9

  ```{.sourceCode .bash}
  pytest
  ```

- Run Nox to run all python version tests

  ```{.sourceCode .bash}
  nox -s tests
  ```

### Test Requirements

Prs should always have tests to cover the change being made. Code
coverage goals for this project are 100% coverage.

### Code Linting

Code is linted with ruff

You can run the linting manually with make

```{.sourceCode .bash}
make lint
```

## CI

CI is run via Github Actions on all PRs and pushes to the main branch.

Releases are automatically released by Github Actions to Pypi.

## License

Licensed under the [MIT License](./LICENSE)

### Contributors

Thanks go to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/andrewthetechie"><img src="https://avatars.githubusercontent.com/u/1377314?v=4?s=100" width="100px;" alt="Andrew"/><br /><sub><b>Andrew</b></sub></a><br /><a href="https://github.com/andrewthetechie/geekbot-api-py/commits?author=andrewthetechie" title="Code">💻</a> <a href="https://github.com/andrewthetechie/geekbot-api-py/commits?author=andrewthetechie" title="Documentation">📖</a> <a href="https://github.com/andrewthetechie/geekbot-api-py/commits?author=andrewthetechie" title="Tests">⚠️</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->


## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!