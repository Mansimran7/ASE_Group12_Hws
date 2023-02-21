"""
Help
-------------------------
It is a header string showing help, from which we build our 'the' settings object

"""
the = {
    'dump': False,
    'go': None,
    'seed': 937162211,
}
help="\n\
bins: multi-objective semi-supervised discetization\n\
(c) 2023 Tim Menzies <timm@ieee.org> BSD-2\n\
USAGE: lua bins.lua [OPTIONS] [-g ACTIONS]\n\
OPTIONS:\n\
  -b  --bins    initial number of bins       = 16\n\
  -c  --cliffs  cliff\'s delta threshold      = .147\n\
  -f  --file    data file                    = ../../etc/data/auto93.csv\n\
  -F  --Far     distance to distant          = .95\n\
  -g  --go      start-up action              = nothing\n\
  -h  --help    show help                    = false\n\
  -H  --Halves  search space for clustering  = 512\n\
  -m  --min     size of smallest cluster     = .5\n\
  -M  --Max     numbers                      = 512\n\
  -p  --p       dist coefficient             = 2\n\
  -r  --rest    how many of rest to sample   = 4\n\
  -R  --Reuse   child splits reuse a parent pole = true\n\
  -s  --seed    random number seed           = 937162211\n\
"
Seed = 937162211

egs={}

n = 0

b4 =[]
