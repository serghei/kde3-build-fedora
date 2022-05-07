%define debug_package %{nil}

Name:		kde3-qca-tls
Version:	1.0
Release:	1%{?dist}

Summary:	TLS plugin for the Qt Cryptographic Architecture
License:	LGPLv2+
Group:		Applications/Internet
URL:		http://delta.affinix.com/qca/
Source0:	kde3-qca-tls-1.0.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Provides:	kde3-qca-tls
Obsoletes:	qca1-tls

BuildRequires:	kde3-qt-devel libXext-devel libX11-devel
BuildRequires:	gcc-c++ openssl-devel >= 0.9.8


%description
This is a plugin to provide SSL/TLS capability to programs that use the Qt
Cryptographic Architecture (QCA).  QCA is a library providing an easy API
for several cryptographic algorithms to Qt programs.  This package only
contains the TLS plugin.

%prep
%setup -q -n kde3-qca-tls-%{version}

%build
[ -n "$KDE3_QTDIR" ] && . %{_sysconfdir}/profile.d/kde3-qt.sh

./configure --qtdir=$KDE3_QTDIR
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT

export INSTALL_ROOT=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT$KDE3_QTDIR/plugins/crypto
make install


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0644,root,root,0755)
%doc README.md COPYING
%attr(755,root,root) /opt/kde3-qt/plugins/crypto
#/opt/kde3-qt/plugins/crypto/*

%changelog
* Sun Aug 26 2007 Aurelien Bompard <abompard@fedoraproject.org> 1.0-11
- fix license tag
- rebuild for BuildID

* Wed Aug 30 2006 Aurelien Bompard <abompard@fedoraproject.org> 1.0-10
- rebuild

* Tue Feb 21 2006 Aurelien Bompard <gauret[AT]free.fr> 1.0-9
- rebuild for FC5

* Sun Nov 13 2005 Aurelien Bompard <gauret[AT]free.fr> 1.0-8
- fix patch1

* Sun Nov 13 2005 Aurelien Bompard <gauret[AT]free.fr> 1.0-7
- build for openssl 0.9.8

* Sun Nov 13 2005 Aurelien Bompard <gauret[AT]free.fr> 1.0-6
- fix BRs

* Sun Nov 13 2005 Aurelien Bompard <gauret[AT]free.fr> 1.0-5
- rebuild for new openssl

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 1.0-4
- rebuild on all arches

* Thu Apr 7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Thu Jun 24 2004 Aurelien Bompard <gauret[AT]free.fr> 0:1.0-0.fdr.2
- License is LGPL
- BR: XFree86-devel
- own the crypto dir (see bug 1738)

* Fri Jun 11 2004 Aurelien Bompard <gauret[AT]free.fr> 0:1.0-0.fdr.1
- Initial RPM, split from psi
