#!/bin/bash

source ./fedora-version

test -f /usr/bin/mock || sudo dnf install mock
mock -r ./mock-fedora-kde3.cfg init
