#!/bin/bash

./00-init.sh && \
./01-build-kde3-qt.sh && \
./02-build-qca-tls.sh && \
./03-build-kde3-kdelibs.sh && \
./04-build-kde3-kdebase.sh && \
./05-build-kde3-kdenetwork.sh && \
./06-build-kde3-kdepim.sh && \
./07-build-kde3-kdewebdev.sh && \
./08-build-kde3-kdegraphics.sh && \
./09-build-kde3-kdeutils.sh && \
./10-build-kde3-kdemultimedia.sh && \
./00-upload.sh
