%define _prefix	/opt/kde3

Name:		kde3-kdelibs
Version:	20220407
Release:	1%{?dist}
Summary:	KDE3 libraries
License:	GPL

BuildRequires: gcc-c++ kde3-qt-devel cmake openssl-devel dbus-devel libxml2-devel libxslt-devel pcre-devel bzip2-devel libpng-devel libjpeg-turbo-devel libSM-devel jasper-devel libutempter-devel libart_lgpl-devel OpenEXR-devel libXrandr-devel libXcomposite-devel libidn-devel alsa-lib-devel audiofile-devel libvorbis-devel
BuildRequires: freetype-devel fontconfig-devel libXft-devel glib2-devel pulseaudio-libs-devel

Source:	kde3-kdelibs-%{version}.tar.gz
#Patch0:	kdelibs-3.5.10-ossl-1.x.patch
#Patch1:		networkstatus.diff

%description
KDE3 Libraries included: kdecore (KDE3 core library), kdeui (user interface),
kfm (file manager), khtmlw (HTML widget), kio (Input/Output, networking),
kspell (spelling checker), jscript (javascript), kab (addressbook),
kimgio (image manipulation).

%package devel
Summary:	%{name} - Development files
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	kde3-qt-devel

%description devel
This package includes the header files you will need to compile
applications for KDE.

%prep
%setup -q -n kde3-kdelibs-%{version}
#%patch0 -p1
#%patch1

%build
#%cmake -DCMAKE_VERBOSE_MAKEFILE=ON -DQT_PREFIX_DIR=/opt/kde3-qt -DQT_LIBRARY_DIR=/opt/kde3-qt/lib -DWITH_ALL_FEATURES=ON -DWITH_ARTS=OFF -DWITH_TIFF=OFF -DWITH_ASPELL=OFF -DWITH_HUNSPELL=OFF -DWITH_MAD=OFF -DWITH_OPENEXR=OFF -DWITH_LIBART=OFF
# cmake .. -DCMAKE_INSTALL_PREFIX=%{_prefix} -DSYSCONF_INSTALL_DIR=/etc -DLIB_SUFFIX=64 -DUSE_LTO=ON -DCMAKE_VERBOSE_MAKEFILE=ON -DQT_PREFIX_DIR=/opt/kde3-qt -DQT_LIBRARY_DIR=/opt/kde3-qt/lib -DWITH_ALL_FEATURES=ON -DWITH_ARTS=OFF -DWITH_TIFF=OFF -DWITH_ASPELL=OFF -DWITH_HUNSPELL=OFF -DWITH_MAD=OFF -DWITH_OPENEXR=OFF -DWITH_LIBART=OFF
#%cmake_build

%install
rm -rf %{buildroot}
#make install DESTDIR=%{buildroot} -C build
%cmake_install

mkdir -p %{buildroot}%{_sysconfdir}/profile.d
echo "export PATH=%{_bindir}:\$PATH" > %{buildroot}%{_sysconfdir}/profile.d/kde3.sh
echo "export KDEHOME=\"~/.kde3\"" >> %{buildroot}%{_sysconfdir}/profile.d/kde3.sh

mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d
echo "%{_libdir}" > %{buildroot}%{_sysconfdir}/ld.so.conf.d/kde3.conf

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc README
%doc COPYING.LIB
#%1config %{_sysconfdir}/ld.so.conf.d/kde3.conf
#%1config %{_sysconfdir}/profile.d/kde3.sh
#%1exclude %{_sysconfdir}/ld.so.conf.d/kde3.conf
#%1exclude %{_sysconfdir}/profile.d/kde3.sh
%{_bindir}/*
%{_libdir}/lib*.so.*
%{_libdir}/libkdeinit_*.so
%{_libdir}/kde3/*.so
%{_libdir}/kde3/plugins/designer/*.so
%{_libdir}/kde3/plugins/styles/*.so
%{_datadir}/*
%{_sysconfdir}/*

%files devel
%defattr(-,root,root,-)
%{_bindir}/dcopidl*
%{_bindir}/kconfig_compiler
%{_bindir}/makekdewidgets
%{_datadir}/apps/ksgmltools2/
%{_includedir}/
%{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_libdir}/lib*.a
%{_libdir}/kde3/*.la
%{_libdir}/kde3/plugins/designer/*.la
%{_libdir}/kde3/plugins/styles/*.la

#1%exclude %{_libdir}/mcop/*
%exclude %{_libdir}/libkdeinit_*.so
