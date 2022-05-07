%define debug_package %{nil}
%define _prefix /opt/kde3

Name:		kde3-kdebase
Version:	20220407
Release:	1%{?dist}
Summary:	KDE libraries
License:	GPL

Requires:	kde3-kdelibs udisks2 upower polkit xorg-x11-apps xorg-x11-server-utils xorg-x11-xdm cyrus-sasl-plain xprop
BuildRequires:	gcc-c++ rpcgen libtirpc-devel glib2-devel bdftopcf libXt-devel libxkbfile-devel pam-devel libXtst-devel libXrender-devel libXcursor-devel libXcomposite-devel libXdamage-devel freetype-devel fontconfig-devel libXft-devel libXrandr-devel libraw1394-devel cyrus-sasl-devel OpenEXR-devel openldap-devel libXdmcp-devel libXinerama-devel pcre-devel polkit-devel upower-devel perl-Digest-MD5 libidn-devel libjpeg-turbo-devel alsa-lib-devel audiofile-devel libvorbis-devel
BuildRequires:	kde3-kdelibs-devel cmake libsmbclient-devel openssl-devel dbus-devel

Source0:	kde3-kdebase-%{version}.tar.gz
Source1:	pamd.kde3-kdm
Source2:	pamd.kde3-kcheckpass
Source3:	pamd.kde3-kscreensaver
Source4:	kde3-kdm.service

#Patch0:		kdebase-kpolkitagent.patch

#Patch1:		arts-start-on-demand-cmake.diff
#Patch2:		kpamgreeter.diff
#Patch3:		kdebase-svn-merge-diff.patch
#Patch4:		kdebase_networkstatus_branch.diff

%description
Core applications for the KDE3. Included are: kdm
(replacement for xdm), kwin (window manager), konqueror (filemanager,
web browser, ftp client, ...), konsole (xterm replacement), kpanel
(application starter and desktop pager), kaudio (audio server),
kdehelp (viewer for kde help files, info and man pages), kthememgr
(system for managing alternate theme packages) plus other KDE
components (kcheckpass, kikbd, kscreensaver, kcontrol, kfind,
kfontmanager, kmenuedit).

%package devel
Requires:	%{name}
Requires:	kde3-kdelibs-devel >= %{version}
Summary:	%{summary} - Development files
Group:		Development/Libraries

%description devel
Header files for developing applications using %{name}.

%prep
%setup -q -n kde3-kdebase-%{version}
#%patch0 -p1
#%patch1 -p1
#%patch2 -p1
#%patch3 -p1
#%patch4 -p0

%build
mkdir build
cd build
cmake .. \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DCMAKE_VERBOSE_MAKEFILE=ON \
    -DLIB_SUFFIX=64 \
    -DSYSCONF_INSTALL_DIR=/etc \
    -DUSE_LTO=ON \
    -DQT_PREFIX_DIR=/opt/kde3-qt \
    -DQT_LIBRARY_DIR=/opt/kde3-qt/lib \
    -DKDM_PAM_SERVICE=kde3-kdm \
    -DKCHECKPASS_PAM_SERVICE=kde3-kcheckpass \
    -DKSCREENSAVER_PAM_SERVICE=kde3-kscreensaver \
    -DBUILD_ALL=ON \
    -DWITH_ALL_FEATURES=ON \
    -DWITH_SAMBA=ON \
    -DWITH_NFS=OFF \
    -DWITH_ARTS=OFF \
    -DBUILD_DOC=OFF \
    -DWITH_OPENEXR=OFF

make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} -C build
%__install -D -m 644 "%{SOURCE1}" "%{?buildroot}%{_sysconfdir}/pam.d/kde3-kdm"
%__install -D -m 644 "%{SOURCE2}" "%{?buildroot}%{_sysconfdir}/pam.d/kde3-kcheckpass"
%__install -D -m 644 "%{SOURCE3}" "%{?buildroot}%{_sysconfdir}/pam.d/kde3-kscreensaver"
%__install -D -m 644 "%{SOURCE4}" "%{?buildroot}/usr/lib/systemd/system/kde3-kdm.service"
%__sed -i "%{?buildroot}%{_datadir}/config/kdm/kdmrc" -e "s/^#*MinShowUID=.*/MinShowUID=1000/"
%__sed -i "%{?buildroot}%{_datadir}/config/kdm/kdmrc" -e "s/^#AntiAliasing=.*/AntiAliasing=true/"
rm -f %{buildroot}/%{_libdir}/kde3/*.la

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc README
#%doc COPYING.LIB
%{_bindir}/*
%{_libdir}/lib*.so.*
%{_libdir}/kconf_update_bin/*
%{_libdir}/libkdeinit_*.so
%{_libdir}/kde3/*.so
%{_datadir}/*
/etc/*
/usr/lib/systemd/system/kde3-kdm.service

%files devel
%defattr(-,root,root,-)
%{_includedir}/*.h
%dir %{_includedir}/kate
%{_includedir}/kate/*
%dir %{_includedir}/kwin
%{_includedir}/kwin/*
%dir %{_includedir}/ksgrd
%{_includedir}/ksgrd/*
%dir %{_includedir}/ksplash
%{_includedir}/ksplash/*
%{_libdir}/lib*.so
%{_libdir}/lib*.la
%exclude %{_libdir}/libkdeinit_*.*
%{_datadir}/cmake/*.cmake
