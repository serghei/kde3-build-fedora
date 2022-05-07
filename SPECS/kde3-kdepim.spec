%define debug_package %{nil}
%define _prefix /opt/kde3

Name:		kde3-kdepim
Version:	20220407
Release:	1%{?dist}
Summary:	KDE pim
License:	GPL

BuildRequires: gcc-c++ kde3-kdelibs-devel cmake gpgme-devel libical-devel boost-devel cyrus-sasl-devel
#BuildRequires: libSM-devel libXrender-devel libX11-devel zlib-devel libidn-devel libXcomposite-devel libICE-devel freetype-devel fontconfig-devel libXext-devel pcre-devel libjpeg-turbo-devel dbus-devel alsa-lib-devel audiofile-devel libvorbis-devel glib2-devel
BuildRequires: libSM-devel libXrender-devel libX11-devel zlib-devel libidn-devel libXcomposite-devel libICE-devel freetype-devel fontconfig-devel libXext-devel pcre-devel libjpeg-turbo-devel dbus-devel glib2-devel perl-Getopt-Long

Source:	kde3-kdepim-%{version}.tar.gz

%description
KDE3 pim

%prep
%setup -q -n kde3-kdepim-%{version}

%build
mkdir build
cd build
cmake .. -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DSYSCONF_INSTALL_DIR=/etc \
    -DLIB_SUFFIX=64 \
    -DUSE_LTO=ON \
    -DCMAKE_VERBOSE_MAKEFILE=ON \
    -DQT_PREFIX_DIR=/opt/kde3-qt \
    -DQT_LIBRARY_DIR=/opt/kde3-qt/lib \
    -DBUILD_ALL=ON \
    -DWITH_ALL_FEATURES=ON \
    -DBUILD_WIZARDS=OFF \
    -DWITH_GROUPWISE=OFF

make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} -C build
rm -f %{buildroot}/%{_libdir}/kde3/*.la
rm -f %{buildroot}/%{_libdir}/libkmailprivate.la
rm -rf %{buildroot}/%{_datadir}/icons/default.kde

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README
%{_bindir}/*
%{_libdir}/lib*.so.*
%{_libdir}/libkmailprivate.so
%{_libdir}/kde3/*.so
%{_libdir}/kconf_update_bin/*
%{_datadir}/*

%package devel
Requires:       %{name}
Summary:        %{summary} - Development files
Group:          Development/Libraries

%description devel
Header files for developing applications using %{name}.

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/lib*.la
%exclude %{_libdir}/libkmailprivate.so
%{_libdir}/kde3/plugins/*
