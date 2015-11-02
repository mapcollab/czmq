Name:           czmq
Version:        3.0.2
Release:        3%{?dist}
Summary:        High-level C binding for 0MQ (ZeroMQ)

Group:          Development/Libraries
License:        MPLv2.0
URL:            http://czmq.zeromq.org/
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  libuuid-devel
BuildRequires:  zeromq4-devel
BuildRequires:  autoconf automake libtool

%description
CZMQ has the following goals:
  i) To wrap the ØMQ core API in semantics that are natural and lead to
     shorter, more readable applications.
 ii) To hide the differences between versions of ØMQ.
iii) To provide a space for development of more sophisticated API semantics.


%package devel
Summary:        Development files for the czmq package
Group:          Development/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       zeromq4-devel
Requires:       pkgconfig

%description devel
This package contains files needed to develop applications using czmq.


%prep
%setup -q

%build
./autogen.sh
%configure

# remove rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}

rm -f %{buildroot}%{_libdir}/libczmq.{a,la}


%check
# LD_LIBRARY_PATH=%{buildroot}/%{_libdir} make check


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc AUTHORS NEWS LICENSE
%{_libdir}/*.so.*

%files devel
%doc CONTRIBUTING.md README.md
%{_bindir}/zmakecert
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_mandir}/man1/*.1*
%{_mandir}/man3/*.3*
%{_mandir}/man7/*.7*
%{_datarootdir}/zproject/czmq/*.xml


%changelog
* Mon Nov 02 2015 Tomasz Rostanski <tomasz.rostanski@thalesgroup.com.pl> 3.0.2-3
- initial version for mps

* Mon Nov 02 2015 Tomasz Rostanski <tomasz.rostanski@thalesgroup.com.pl>
- initial version for mps

* Sat Jun 27 2015 Jose Pedro Oliveira <jose.p.oliveira.oss at gmail.com> - 3.0.2-2
- Disable the test suite for the moment (requires network access)

* Sat Jun 27 2015 Jose Pedro Oliveira <jose.p.oliveira.oss at gmail.com> - 3.0.2-1
- Update to 3.0.2.
- License: MPLv2.0 (Mozilla Public License Version 2.0).
- Man pages installation patch (0001-Problem-does-not-install-man-pages-if-BUILD_DOC-is-o.patch)

* Tue Jun 23 2015 Thomas Spura <tomspur@fedoraproject.org> - 2.2.0-7
- rebuilt for new zeromq 4.1.2

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar  2 2015 Jose Pedro Oliveira <jose.p.oliveira.oss at gmail.com> - 2.2.0-5
- Patch to fix sha1 on bigendian machines (#1196994)

* Fri Feb 27 2015 Jose Pedro Oliveira <jose.p.oliveira.oss at gmail.com> - 2.2.0-4
- Renamed /usr/bin/makecert to avoid a file conflict (#1196483)

* Fri Feb 20 2015 Jose Pedro Oliveira <jose.p.oliveira.oss at gmail.com> - 2.2.0-3
- Build against ZeroMQ v4

* Fri Feb 20 2015 Jose Pedro Oliveira <jose.p.oliveira.oss at gmail.com> - 2.2.0-2
- Add upstream patch eebf66a (0001-Use-_DEFAULT_SOURCE-instead-of-_BSD_SOURCE.patch)

* Tue Feb 17 2015 Jose Pedro Oliveira <jose.p.oliveira.oss at gmail.com> - 2.2.0-1
- Update to 2.2.0.

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed May  1 2013 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.4.1-1
- Update to 1.4.1.

* Tue Apr 30 2013 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.4.0-1
- Update to 1.4.0.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 20 2012 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.3.2-1
- Improve the description.

* Wed Dec 12 2012 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.3.2-0
- Update to 1.3.2.

* Sun Oct 28 2012 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.3.1-1
- Update to 1.3.1.

* Thu Oct 25 2012 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.3.0-0
- Rename to libczmq.
- Update to v1.3.0 git snapshot.

* Tue Oct 23 2012 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.2.0-3
- Make czmq-devel require zeromq3-devel.

* Sat Oct 20 2012 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.2.0-2
- Build against limzmq v3.x (BR zeromq3-devel instead of zeromq-devel).

* Sat Oct 20 2012 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.2.0-1
- First Fedora build.

# vim:set ai ts=4 sw=4 sts=4 et:
