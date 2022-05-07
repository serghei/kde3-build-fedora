%define debug_package %{nil}
%define _prefix /opt/kde3

Name:		kde3-kdemultimedia
Version:	20220407
Release:	1%{?dist}
Summary:	-- need summary --
License:	GPL

BuildRequires:  gcc-c++ kde3-kdelibs-devel cmake libidn-devel libSM-devel libXrender-devel libX11-devel libXt-devel zlib-devel libXcomposite-devel pcre-devel libjpeg-turbo-devel freetype-devel fontconfig-devel libXext-devel alsa-lib-devel

Source0:	kde3-kdemultimedia-%{version}.tar.gz

%description
-- need description --

%prep
%setup -q -n kde3-kdemultimedia-%{version}

%build
mkdir build
cd build
cmake .. -DCMAKE_VERBOSE_MAKEFILE=OFF -DCMAKE_INSTALL_PREFIX=%{_prefix} -DQT_PREFIX_DIR=/opt/kde3-qt -DQT_LIBRARY_DIR=/opt/kde3-qt/lib -DBUILD_ALL=ON -DWITH_ALL_FEATURES=ON
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
#%doc COPYING.LIB
%{_bindir}/*
#%{_libdir}/lib*.so.*
%{_libdir}/libkdeinit_*.so
%{_libdir}/kde3/*.so
%{_datadir}/*

#%package devel
#Requires:       %{name}
#Summary:        %{summary} - Development files
#Group:          Development/Libraries

#%description devel
#Header files for developing applications using %{name}.

#%files devel
#%defattr(-,root,root,-)
#%{_includedir}/*
#%{_libdir}/lib*.so
#%{_libdir}/lib*.la
