%define _prefix	/opt/kde3

Name:		kde3-mpv
Version:	0
Release:	1%{?dist}
Summary:	-
License:	GPL

#BuildRequires: nasm

Source:		https://github.com/mpv-player/mpv/archive/v0.28.2.tar.gz

%description
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
