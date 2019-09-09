# ***Dlang project template.***
----------------------------------------

Code version Orio cookie.  A project template for a new Dlang based exe 
using Meson build system and Conan package manager.

### Projects current status
--------
[![GitHub](https://img.shields.io/github/license/squidfarts/d-project.svg?color=blue)](https://github.com/squidfarts/d-project)
[![Travis](https://travis-ci.com/squidfarts/d-project.svg?branch=master)](https://travis-ci.org/squidfarts/d-project)
[![Appveyor](https://ci.appveyor.com/api/projects/status/lh6a93nw50rxq3f7/branch/master?svg=true)](https://ci.appveyor.com/project/squidfarts/d-project)
[![Codecov](https://codecov.io/gh/squidfarts/d-project/coverage.svg?branch=master)](https://codecov.io/gh/squidfarts/d-project/branch/master) 

### Table of contents
--------
> * [Project Name](#c-exe-template)
>   * [Current status bar](#current-status-bar)
>   * [Table of contents](#table-of-contents)
>   * [About this project](#about-this-project)
>   * [Features found](#features-found)
>   * [Downloading required things](#downloading-required-things)
>   * [Downloading this project](#downloading-this-project)
>   * [Building this executable](#building-this-executable)
>     * [Generating the build directory](#generating-the-build-directory)
>     * [Building from the source](#building-from-the-source)
>     * [Running test cases](#running-test-cases)
>     * [Installing the project](#installing-the-project)
>   * [Contact the developer](#contact-the-developer)


### About this project
--------

***D Project*** is a project that was designed to work out of 
the box using Meson build system and Conan package manager from 
day one.  The creation of this started at a large codebase where 
the following languages are used to build programs C, C++, Dlang,
Kotlin and Python.

The design of the project was meant for demonstrating a project
using the GitHub workflow super charged with continues integration.

However to make something that can defend agains hackers planting 
malicious software attacks or feed of data stored in your database
is mostly imposable and all that can be done is to mitigate the 
possibility of as many software attacks as posable.


### Features found
--------

- Meson as the main tool for generating ninja build files.
- Conan as the tool for managing and packaging.
- Setup with Travis-ci Linux and Mac.
- Setup with AppVeyor for Windows.
- Setup with Codecov coverage.
- Simple project structure just for you. 
- Distributed under the Apache 2.0 license.
- Works 99.95% out of the box.

### Downloading required things

This project requires the following tools:

-----------------------------------------------------------------------------
| Tool being used.                               |  Version needed          |
|------------------------------------------------|--------------------------|
| [Meson build system   ](https://mesonbuild.com)| version 0.50.0 or newer. |
| [Conan package manager](https://conan.io)      | version 1.19.x or newer. |
| [Python3 language     ](https://python.org)    | version 3.5.x or newer.  |
| [D language           ](https://dlang.org)     | version 2.087.x or newer.|


### Downloading this project.
--------

* To install this project the simplest way is to grab it off github with
this command the Github command looks something like this:

```console
git clone https://github.com/squidfarts/d-project.git
```
* You can also download it as a zip if you prefer.


### Building this executable.
--------

#### Generating the build directory

Let us assume that we have a source tree that has a Meson build
system. This means that at the topmost directory has a file
called meson.build. We run the following commands to get the
build started.

```console
meson setup <build dir name>
```

#### Building from the source

Meson uses the Ninja build system to actually build the code. To
start the build, simply type the following command.

```console
ninja -C <build dir name>
```

#### Running test cases

Meson provides native support for running tests. The command to
do that is simple.

```console
meson test -C <build dir name> --num-processes
```

#### Installing the project

Installing the built software with Meson is just as simple as.

```console
meson install -C <build dir name>
```


### Contact the developer
==========================

#### Developer and maintainer

- gmail : [squidfarts gmail](mailto:michaelbrockus@gmail.com)
- email : [squidfarts email](mailto:michaelbrockus@icloud.com)