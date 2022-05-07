%define debug_package %{nil}
%define _prefix /opt/kde3-qt
%define _syslibdir /usr/lib64
%define _libdir %{_prefix}/lib

Name:		kde3-qt
Version:	3.3.8.2
Release:	2%{?dist}
Summary:	Extended Qt3 library
License:	GPL
Provides:	kde3-qt

BuildRequires:	perl libXft-devel libXcursor-devel libXinerama-devel libXrandr-devel libXext-devel libXmu-devel glib2-devel libjpeg-turbo-devel freetype-devel

Source:		kde3-qt-%{version}.tar.gz

%description
Qt3 library which includes glib mainloop integration


%package devel
Requires:       %{name}
Summary:        %{summary} - Development files
Group:          Development/Libraries

%description devel
Header files for developing applications using %{name}.

%prep
%setup -q -n kde3-qt-%{version}

%build
export QTDIR=`/bin/pwd`
export LD_LIBRARY_PATH="$QTDIR/lib:$LD_LIBRARY_PATH"

# don't use rpath
perl -pi -e "s|-Wl,-rpath,| |" mkspecs/*/qmake.conf

echo yes | ./configure -v -prefix %{_prefix} -L %{_syslibdir} -thread -glibmainloop -no-exceptions -xinerama -xft -xrandr -xcursor -xshape -sm -xkb -qt-gif -system-zlib -system-libjpeg -system-libpng
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install INSTALL_ROOT=%{buildroot}

mkdir -p %{buildroot}%{_sysconfdir}/profile.d
echo "export PATH=%{_bindir}:\$PATH" > %{buildroot}%{_sysconfdir}/profile.d/%{name}.sh
echo "export KDE3_QTDIR=%{_prefix}" >> %{buildroot}%{_sysconfdir}/profile.d/%{name}.sh

mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d
echo "%{_libdir}" > %{buildroot}%{_sysconfdir}/ld.so.conf.d/%{name}.conf

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)

%config %{_sysconfdir}/ld.so.conf.d/%{name}.conf
%{_libdir}/libqt-mt.so.3*
%{_libdir}/libqui.so.1*
%{_prefix}/plugins/*

%files devel
%defattr(-,root,root,-)
%config %{_sysconfdir}/profile.d/%{name}.sh
%{_bindir}/*
%{_libdir}/*.prl
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/pkgconfig/*
%{_prefix}/doc/*
%{_prefix}/include/*
%{_prefix}/mkspecs/*
%{_prefix}/phrasebooks/*
%{_prefix}/templates/*
%{_prefix}/translations/*
