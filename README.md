# glennscli

Package a Python application using the [Packaging Python Projects guidance](https://packaging.python.org/tutorials/packaging-projects/), build it with the [Knack CLI framework](https://github.com/microsoft/knack), and run it as a local CLI with [pipx](https://pypi.org/project/pipx/)

## running the CLI

If you build the [container in this repository as a Remote Development Environment in VS Code](#devcontainer) (which includes all the dependencies you need) the CLI will install itself.

Otherwise, using `pipx` to install the latest release:

```bash
> pipx install https://github.com/glennmusa/glennscli/releases/download/v0.0.5/glennscli-0.0.5.tar.gz
    installed package glennscli 0.0.5, Python 3.6.13
    These apps are now globally available
      - glennscli
  done! ✨ 🌟 ✨
```

Then run `tellmeajoke` to get the funny:

```bash
> glennscli tellmeajoke cat
[SPOILERS REDACTED]
```

Or pass in an argument to get multiple funnies:
```bash
> glennscli tellmeajoke dog --numjokes 3
[SPOILERS REDACTED]
```

## running tests

Use `tox` to run the tests at `/tests`:

```bash
> tox
tests/command_line/test_command_line.py::TestJokeScenarios::test_tellmeajoke_cat PASSED
tests/command_line/test_command_line.py::TestJokeScenarios::test_tellmeajoke_cat_with_numjokes PASSED
tests/command_line/test_command_line.py::TestJokeScenarios::test_tellmeajoke_dog PASSED
tests/command_line/test_command_line.py::TestJokeScenarios::test_tellmeajoke_dog_with_numjokes PASSED
tests/funnies/test_cat_jokes.py::TestCatJokes::test_returns_a_joke PASSED
tests/funnies/test_dog_jokes.py::TestDogJokes::test_returns_a_joke PASSED
6 passed in 0.41s
```

Or, [debug and run the tests with Visual Studio Code](https://code.visualstudio.com/docs/python/testing#_run-tests).

### devcontainer

I like Visual Studio Code's Remote - Containers extension because I don't have to worry about what tools are available on my machine.

Instead, when I clone the repo, I get with it all the tools the authors used to create the repo.

For more information see <https://code.visualstudio.com/docs/remote/containers/>

In their words:

> The Visual Studio Code Remote - Containers extension lets you use a Docker container as a full-featured development environment. It allows you to open any folder or repository inside a container and take advantage of Visual Studio Code's full feature set. A devcontainer.json file in your project tells VS Code how to access (or create) a development container with a well-defined tool and runtime stack. This container can be used to run an application or to sandbox tools, libraries, or runtimes needed for working with a codebase.
