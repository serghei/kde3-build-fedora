%define _prefix /opt/kde3

Name:		kde3-kdenetwork
Version:	20220407
Release:	1%{?dist}
Summary:	KDE network
License:	GPL

Requires:	kde3-qca-tls
BuildRequires:	gcc-c++ libv4l-devel
BuildRequires:	kde3-kdelibs-devel cmake libidn-devel libSM-devel libXrender-devel libX11-devel libXt-devel zlib-devel libXcomposite-devel pcre-devel libjpeg-turbo-devel freetype-devel fontconfig-devel libXext-devel

Source:	kde3-kdenetwork-%{version}.tar.gz

%description
KDE3 network

%prep
%setup -q -n kde3-kdenetwork-%{version}

%build
mkdir build
cd build
cmake .. \
    -DCMAKE_VERBOSE_MAKEFILE=OFF \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DQT_PREFIX_DIR=/opt/kde3-qt \
    -DQT_LIBRARY_DIR=/opt/kde3-qt/lib \
    -DBUILD_KOPETE=ON \
    -DBUILD_KOPETE_PROTOCOL_JABBER=ON \
    -DBUILD_KOPETE_PLUGIN_HISTORY=ON \
    -DBUILD_KOPETE_PLUGIN_CONNECTIONSTATUS=ON \
    -DWITH_ARTS=OFF

make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} -C build
rm -f %{buildroot}/%{_libdir}/kde3/*.la
rm -f %{buildroot}/%{_libdir}/libkdeinit_*.la

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc README
%{_bindir}/*
%{_libdir}/lib*.so.*
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
