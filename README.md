# JIRA Agile Metrics dev base 

This project serves as a base to setup a contribution environment for the project
[jira-agile-metrics](https://github.com/DeloitteDigitalUK/jira-agile-metrics).

# Preparing the development environment

## TL;DR;

Requirements:
* git
* python 3
* virtualenv

```sh
git clone jira-agile-metrics-dev-base
cd jira-agile-metrics-dev-base
git clone git@github.com:DeloitteDigitalUK/jira-agile-metrics.git
if [ "$(command -v virtualenv)" != "" ]; then
   virtualenv venv
   source venv/bin/activate
   pip install -r jira-agile-metrics/requirements.txt
fi
```

## Step-by-step

### 1. Clone this repo

```sh
git clone jira-agile-metrics-dev-base
```

### 2. Clone jira-agile-metrics

```sh
cd jira-agile-metrics-dev-base
git clone git@github.com:DeloitteDigitalUK/jira-agile-metrics.git
```

### 3. Create and activate a virtual environment called `venv`

You need to have `virtualenv` installed globally in your machine.

Run this from the root folder `jira-agile-metrics-dev-base`.

```sh
virtualenv venv
source venv/bin/activate
# after this you should see (venv) preceding your terminal prompt
```

### 4. Install required packages

Install jira-agile-metrics required python packages in the virtual environment.

```sh
pip install -r jira-agile-metrics/requirements.txt
```

# Setting up JIRA credentials

Duplicate `config/auth.yml.template` as `config/auth.yml` and edit it with the
authentication details. Don't use quotes to write values.
* `Domain`: the url domain of your JIRA instance (everything before the first `\`).
* `Useraname`: the email you use to login.
* `Password`: **This is not your login password.** Go to your
[Atlassian API tokens](https://id.atlassian.com/manage-profile/security/api-tokens)
page, where you can create (and revoke) tokens at eny time you like, and use the token
code as password.

# Running and debugging

Make sure the virtualenv is activated before running the project
```sh
source ./venv/bin/activate
```

Some examples of how you can run the project from the terminal:

```sh
./run.py --help
./run.py config/test.yml -o output
```

This project contains a `.vscode` folder with launch and project settings, which means
that if you use vscode and installed `venv` properly, you can place breakpoints, launch
the session **Run config/test.yml** and start debugging right away.

For the first time debugging, these interesting locations for a breakpoint, to help
understanding the main flow of the application:
* *jira-agile-metrics/jira_agile_metrics/cli.py* - function `main`
* *jira-agile-metrics/jira_agile_metrics/calculator.py* - function `run_calculators`
* For any calculator of your interest inside *jira-agile-metrics/jira_agile_metrics/calculators* - functions `run` and `write`

