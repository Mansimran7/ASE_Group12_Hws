## Introduction
LUA is an ultra lightweight scripting language comprising less than two dozen keywords: and, break, do, else, elseif, end, false, for, function, if, in, local, nil, not, or, repeat, return, then, true, until, while.

LUA has a considerably smaller footprint than other programming languages (with its complete source code and documentation taking a mere 1.3 MB).

This repository contains the source code cnversion from lua to python scripting language.

|Recommended files | Notes |
|------------------:|:------|
| /.gitignore | lists of files never to commit (e.g. compiler intermediaries). To find the right ignores for your tools, see the [Github ignore repo](https://github.com/github/gitignore/) |
| [/.github/workflows/tests.yaml](.github/workflows/tests.yml) | on each commit, runs the /src/lua files with `lua file.lua -g all` and reports a crash if any produce a non-zero error code|
| /CITATION.cff | for bibliography information<br>To make your own file, use [this generator](https://citation-file-format.github.io/cff-initializer-javascript/#/) |
| /LICENSE.md  | open source license<br>To browse different licenses, go to [choose a license](https://choosealicense.com/licenses/)| 
| /Makefile| for any tricky scripting stuff: pretty tricky stuff (not for everyone)<br>For notes on cool Makefile tricks, see [Automation and Make](https://swcarpentry.github.io/make-novice/08-self-doc/index.html)|
| /README.md| top-level doco file|
| /docs | for markdown files<br> Anything starting with `on*` is a lecture file. All other files are generated from the comments in the files in `/src/*.lua`.|
| /etc | for local config files|
| /etc/img | for images|
| /etc/out | cache for experimental output logs|
| /src | for code|