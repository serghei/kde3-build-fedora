%define _prefix	/opt/kde3

Name:		kde3-ffmpeg
Version:	0
Release:	1%{?dist}
Summary:	-
License:	GPL

BuildRequires: nasm

Source:	https://www.ffmpeg.org/releases/ffmpeg-snapshot.tar.bz2

%description
-

%package devel
Summary:	%{name} - Development files
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	kde3-ffmpeg

%description devel
-

%prep
%setup -q -n ffmpeg

%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README
%doc COPYING.LIB
%{_bindir}/*
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/
