# Flask-RabbitMQ

A simple API for passing messages to RabbitMQ via HTTP requests.

This is the proof of concept for another project that I decided to keep as it
serves as a useful base to work from.

## Mirror

This is a public mirror the master branch of a private repo.

## Requirements

 * Python 3
 * RabbitMQ

## Installation

Install Vagrant and Virtualbox, then go into the directory and run `vagrant up`.

## Usage

* log in via `vagrant ssh`
* activate the env via `source env/bin/activate`
* cd into `flask-rabbitmq/src/`
* run `python worker.py`

Now, send JSON to the API, eg:

`curl -X POST -d '{"message": "Hello world"}' http://192.168.33.100 --header "Content-Type:application/json"`

The worker should then print out the message.
