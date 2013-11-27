Hamster Export
=============

hamster-export is a command line tool to export logged time from Hamster
time-tracking application.

Following formats are now supported:
* ActiveCollab. ActiveCollab is web based project management application.

Installtion
----
Clone repository and enter to hamster-export directory
* python setup.py install
* pip install .

Usage
----

    usage: hamster-export [-h] [--short] [--round ROUND] profile date [till]

    Hamster exporter.

    positional arguments:
      profile        specify profile
      date           export time entries from this date
      till           export time entries till this date

    optional arguments:
      -h, --help     show this help message and exit
      --short        merge similar time entries
      --round ROUND  round up the duration of time entries

* date - support 'today' or month name from 3 letter and day conjuction e.g. jun10, may1, dec40
* round - todo

Configuration file
----
~/.hamster-export sample file

    [profile "profile_name"]
    format = activecollab
    short = False # merge similar time entries
    url = http://activecollab.com
    api_key =
    editor = vim

    [activity "development@activity_category"]
    profile = profile_name
    project = 10 # project id or slug

    [activity "support@activity_category"]
    profile = profile_name
    project = my_new_project # project id or slug

    [activity "lunch@activity_category"]
    skip = True # Dont include activity to export
