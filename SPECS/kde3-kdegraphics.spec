%define debug_package %{nil}
%define _prefix /opt/kde3

Name:		kde3-kdegraphics
Version:	20220407
Release:	1%{?dist}
Summary:	-- need summary --
License:	GPL

#Requires:	
BuildRequires:	gcc-c++ libgphoto2-devel t1lib-devel lcms-devel fribidi-devel sane-backends-devel
BuildRequires:  kde3-kdelibs-devel cmake libidn-devel libSM-devel libXrender-devel libX11-devel libXt-devel libXft-devel zlib-devel libXcomposite-devel pcre-devel libjpeg-turbo-devel freetype-devel fontconfig-devel libXext-devel OpenEXR-devel libXmu-devel libart_lgpl-devel libpng-devel

Source0:	kde3-kdegraphics-%{version}.tar.gz

%description
-- need description --

%prep
%setup -q -n kde3-kdegraphics-%{version}

%build
mkdir build
cd build
cmake .. \
    -DCMAKE_VERBOSE_MAKEFILE=OFF \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DQT_PREFIX_DIR=/opt/kde3-qt \
    -DQT_LIBRARY_DIR=/opt/kde3-qt/lib \
    -DBUILD_ALL=ON \
    -DWITH_ALL_FEATURES=ON \
    -DWITH_PDF=OFF \
    -DBUILD_KAMERA=OFF \
    -DBUILD_KUICKSHOW=OFF \
    -DBUILD_KGAMMA=OFF

make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} -C build
rm -f %{buildroot}/%{_libdir}/kde3/*.la
rm -f %{buildroot}/%{_libdir}/libdjvu.la

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
%{_libdir}/libkdeinit_*.so
%{_libdir}/kde3/*.so
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
%exclude %{_libdir}/libkdeinit_*.*
