# Simple Distributed File Indexer #

Hello! I wrote this project for an interview.

You can find the original specification in `specification.txt`.

You can find a design document I wrote to plan out this software and guide my
development in `architecture.txt`.

## Installation ##

You need Python installed in order to run this code.

To install Celery, I recommend you create a virtualenv:

```
mkdir -p ~/virtualenvs/this_project/
cd ~/virtualenvs/this_project/
virtualenv .
```

Then activate it with

```
source ~/virtualenvs/this_project/bin/activate
```

Now you can install Celery and other project requirements by changing your
working directory to the project root and running

```
pip install -r requirements.txt
```

To install Celery's task broker, RabbitMQ, on a Debian-based system, run the
command

```
# apt-get install rabbitmq-server
```

RabbitMQ is written in Erlang and will require the installation of language
packages and libraries.

## Operation ##

To run the software, first start up your Celery workers from the worker.py
module:

```
celery -A worker worker
```

Then you can run the scheduler, which will deploy tasks and collect the
results. The scheduler takes in a list of files, and will print out the top 10
words in the processed list:

```
python scheduler.py file1 file2 file3 ...
```

## Testing ##

Running all unit tests is as easy as typing the command

```
python -m unittest discover
```

You can also run tests specific to a certain part of the code base, for
instance

```
python -m unittest test_worker
```

## License ##

This code was written by Elana Hashman, (c) 2015, licensed under the GPLv2. See
LICENSE for more information.
