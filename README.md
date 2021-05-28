# mypypackage

Package a Python application using the [Packaging Python Projects guidance](https://packaging.python.org/tutorials/packaging-projects/) and run it as a local CLI using [pipx](https://pypi.org/project/pipx/)

## running the CLI

If you build the [container in this repository](#devcontainer) (which includes all the tools and Python you need) the CLI will install itself. 

Otherwise, using `pipx` install the latest release:

```bash
> pipx https://github.com/glennmusa/mypypackage/releases/download/0.0.3/mypypackage-glennmusa-0.0.3.tar.gz
    installed package mypypackage-glennmusa 0.0.3, Python 3.6.13
    These apps are now globally available
      - tellmeajoke
  done! ✨ 🌟 ✨
```

Then run `tellmeajoke` to get the funny:

```bash
> tellmeajoke
[SPOILERS REDACTED]
```

## running tests

Use `tox` to run the tests at `/tests`:

```bash
> tox
tests/command_line/test_command_line.py . [ 33%]
tests/funnies/test_cat_jokes.py . [ 66%]
tests/funnies/test_dog_jokes.py . [100%]
3 passed in 0.08s
```

### devcontainer

I like Visual Studio Code's Remote - Containers extension because I don't have to worry about what tools are available on my machine.

Instead, when I clone the repo, I get with it all the tools the authors used to create the repo.

For more information see <https://code.visualstudio.com/docs/remote/containers/>

In their words:

> The Visual Studio Code Remote - Containers extension lets you use a Docker container as a full-featured development environment. It allows you to open any folder or repository inside a container and take advantage of Visual Studio Code's full feature set. A devcontainer.json file in your project tells VS Code how to access (or create) a development container with a well-defined tool and runtime stack. This container can be used to run an application or to sandbox tools, libraries, or runtimes needed for working with a codebase.
