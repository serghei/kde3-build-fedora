#!/bin/bash

if [ ! -f upload.conf ]; then
    echo Missing upload.conf!
    exit 1
fi

source ./fedora-version
source ./upload.conf

cd RPMS/${FEDORA_VERSION}
#rpm --addsign *.rpm
createrepo .
rsync -avR --progress --delete . ${UPLOAD_PATH}/${FEDORA_VERSION}
