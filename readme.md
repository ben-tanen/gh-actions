# GitHub Actions

This is a repo for me to play around with automated [GitHub actions](https://docs.github.com/en/actions/learn-github-actions/introduction-to-github-actions).

Currently this repo contains a few sample workflows:

1. `simple-CLI-workflow`: pipes date of latest run in a file
2. `simple-Python-workflow`: queries a website with some packages and output some results
3. `simple-R-workflow`: uses the tidyverse to save a sample of `mtcars`

In order to perform these actions, I've also set up some helper actions:

1. `commit`: given a commit message (`message`) and an indication of what to add (`what`), commits and pushes any new files to the repo
2. `build_py_env`: given the path to a pip requirement file (`requirements`), creates a pipenv environment that can be used by later steps

Many thanks to the LA Times folks who put together [this repo](https://github.com/datadesk/california-coronavirus-scrapers) that served as a great guide.