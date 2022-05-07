#!/bin/bash
source ./fedora-version

NAME=kde3-kdebase

VERSION=$( grep 'Version:' SPECS/${NAME}.spec | awk '{print $2}' )

tar cfzP SOURCES/${NAME}-${VERSION}.tar.gz -C ../.. --exclude .git --transform="s,^${NAME},${NAME}-${VERSION},S" ${NAME} && \
rpmbuild -bs --define "_topdir ." SPECS/${NAME}.spec && \
mock -r ./mock-fedora-kde3.cfg --clean --rebuild $(ls SRPMS/${NAME}-${VERSION}-* | tail -n1) && \
cp /var/lib/mock/fedora-${FEDORA_VERSION}-x86_64/result/${NAME}-{devel,debuginfo,${VERSION}}-* ./RPMS/${FEDORA_VERSION}
createrepo ./RPMS/${FEDORA_VERSION}
