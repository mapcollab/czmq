Name:           czmq
Version:        4.0.2
Release:        1
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
%{_datarootdir}/zproject/czmq/*

%changelog
* Mon Apr 24 2017 Tomasz Rostanski <tomasz.rostanski@thalesgroup.com> 4.0.2-1
- czmq.spec: bump version to 4.0.2-1 (tomasz.rostanski@thalesgroup.com)
- Problem: #1663 modified auto-generated file (jpitc@users.noreply.github.com)
- Problem: dangling pointers are bug futures (jpitc@users.noreply.github.com)
- Problem: zsys state not reset by clean zsys_shutdown()
  (jpitc@users.noreply.github.com)
- Problem: zsys_reset changes public API side effects (luca.boccassi@gmail.com)
- Problem: zsys_init() + fork() causes undefined behaviour
  (jpitc@users.noreply.github.com)
- Problem: out of date with zproject (luca.boccassi@gmail.com)
- Problem: string leaked in zproc (luca.boccassi@gmail.com)
- Problem: out of date with zproject (luca.boccassi@gmail.com)
- fix typo (paddor@gmail.com)
- Problem: environment is not tested in zproc (michalvyskocil@eaton.com)
- Problem: zproc unit test is too complicated (michalvyskocil@eaton.com)
- problem : (bruno.bodin@cea.fr)
- problem : (bruno.bodin@cea.fr)
- Problem: build fail on CI (michalvyskocil@eaton.com)
- Problem: can "run" process without arguments (michalvyskocil@eaton.com)
- Problem: zproc_run not in API model (michalvyskocil@eaton.com)
- Problem: no way how to setup environment for a process
  (michalvyskocil@eaton.com)
- Problem: invalid declaration of zproc_run (michalvyskocil@eaton.com)
- Problem: set args not in API model (michalvyskocil@eaton.com)
- Problem: zproc mem test fails (michalvyskocil@eaton.com)
- Problem: zproc_run API is ulgy and can't be expressed as API model
  (michalvyskocil@eaton.com)
- Problem: manual <A> anchors on headers no longer work on github
  (mail@kevinsapper.de)
- Problem: trailing whitespace in zbeacon.c (luca.boccassi@gmail.com)
- Problem: static zbeacon helper function not static (luca.boccassi@gmail.com)
- Problem: no documentation for zproc pipe (michalvyskocil@eaton.com)
- Problem: zsubproc is quite long name for a class (michalvyskocil@eaton.com)
- Problem: Sending to INADDR_BROADCAST on Windows only results in a single
  packet being sent over the interface with the highest metric.
  (kaidoe@users.noreply.github.com)
- Problem: getaddrinfo in zbeacon fails on Android and FreeBSD
  (luca.boccassi@gmail.com)
- Problem: docs CI build fails (michalvyskocil@eaton.com)
- Problem: valgrind CI target fails on Travis (michalvyskocil@eaton.com)
- Problem: getline is not portable enough (michalvyskocil@eaton.com)
- Problem: memcheck still fails (michalvyskocil@eaton.com)
- Problem: zsubproc test leaks the memory (michalvyskocil@eaton.com)
- Problem: zsubproc unit test not documented enough (michalvyskocil@eaton.com)
- Problem: build of czmq broken (michalvyskocil@eaton.com)
- Problem: zsubproc_new returns NULL to express not implemented
  (michalvyskocil@eaton.com)
- Problem: windows version of zsubproc pretend to work
  (michalvyskocil@eaton.com)
- Problem: CI targets for older libzmq releases stall
  (michalvyskocil@eaton.com)
- Problem: ctest fails (michalvyskocil@eaton.com)
- Problem: Travis CI fails (michalvyskocil@eaton.com)
- Problem: zsubproc check fails on windows (michalvyskocil@eaton.com)
- Problem: zsp dont build on windows (michalvyskocil@eaton.com)
- Problem: getline does not exists on Windows (michalvyskocil@eaton.com)
- Problem: Windows build fails (michalvyskocil@eaton.com)
- Problem: zsubproc_pid declared twice (michalvyskocil@eaton.com)
- Problem: unit test can't work (michalvyskocil@eaton.com)
- Problem: process status not correctly reported after kill
  (michalvyskocil@eaton.com)
- Problem: unit test prints things (michalvyskocil@eaton.com)
- Problem: unit test runs forever (michalvyskocil@eaton.com)
- Problem: there's no portable way how to test zsubproc
  (michalvyskocil@eaton.com)
- Problem: zsubproc not portable (michalvyskocil@eaton.com)
- Problem: subprocess do not report state correcly (michalvyskocil@eaton.com)
- Problem: still dangling socket error (michalvyskocil@eaton.com)
- Problem: dangling sockets if exec fail (michalvyskocil@eaton.com)
- Problem: zsubproc don't have function declarations (michalvyskocil@eaton.com)
- Problem: can't manipulate with subprocesses from czmq
  (michalvyskocil@eaton.com)
- Problem: zloop is using reader callback after zloop_reader_end #1634
  (piskorzj@gmail.com)
- Problem: Adding/Removing network adapters in Windows can cause a null pointer
  exception (kaidoe@users.noreply.github.com)
- Problem: Travis using deprecated OBS project (luca.boccassi@gmail.com)
- Problem: about to add new draft of a class (michalvyskocil@eaton.com)
- Problem: docs ci script is not executable (mail@kevinsapper.de)
- Problem: Wikidot docs are not automatically updated (mail@kevinsapper.de)
- Problem: czmq manpage still mentions retired APIs (luca.boccassi@gmail.com)
- Problem: [travis] cannot change ulimit in containers
  (luca.boccassi@gmail.com)
- Problem: travis out of date with zproject (luca.boccassi@gmail.com)
- Problem: msvc build tools do not honor disable-drafts option
  (rodrigo.madruga@nexxtorage.com)
- fix build.bat looking for libzmq.import.props in the wrong place. Commit http
  s://github.com/zeromq/libzmq/commit/40d7a4c8962f98d2a2954d0811774e4c21ebb6bf
  removed these files. (rodrigo.madruga@nexxtorage.com)
- Problem: build error in zsys with GCC7 (luca.boccassi@gmail.com)
- Problem: build error with GCC7 in zgossip_engine.inc
  (luca.boccassi@gmail.com)
- Problem: src addr of v6 beacons is random garbage (luca.boccassi@gmail.com)
- Problem: zbeacon does not support IPv6 (luca.boccassi@gmail.com)
- Problem: zsys_udp_recv can fail to get peer addr and return garbage
  (luca.boccassi@gmail.com)
- Problem: inet_ntop sometimes fails on arm with ipv6 (luca.boccassi@gmail.com)
- Problem: zsys_udp_recv docs not compatible with IPv6
  (luca.boccassi@gmail.com)
- Problem: IPv6 addresses might be longer than INET_ADDRSTRLEN
  (luca.boccassi@gmail.com)
- Problem: missing portable if_indextoname prototype (luca.boccassi@gmail.com)
- Problem: no way to check if ziflist interface has IPv6
  (luca.boccassi@gmail.com)
- Problem: ziflist does not support IPv6 (luca.boccassi@gmail.com)
- Problem: no default zsys multicast address (luca.boccassi@gmail.com)
- Problem: incorrect indentation in zbeacon (luca.boccassi@gmail.com)
- Problem: private classes definitions out of date with zproject
  (luca.boccassi@gmail.com)
- Problem: bindings out of date with zsock options (luca.boccassi@gmail.com)
- Problem: zsock options out of date (luca.boccassi@gmail.com)
- Problem: public API/ABI changes depending on libzmq version
  (luca.boccassi@gmail.com)
- problem : assertions are disabled when running test in release mode
  (bruno.bodin@cea.fr)
- Problem: out of date with zproject (luca.boccassi@gmail.com)
- problem : zdir test behaviour depends on assert macro being enabled
  (bruno.bodin@cea.fr)
- Problem: README.md out of date with documentation (luca.boccassi@gmail.com)
- Problem: zsys_shutdown doc not very clear about DLL (luca.boccassi@gmail.com)
- Problem: Windows DLL builds can't use atexit (luca.boccassi@gmail.com)
- problem : zproxy self test fails under windows (brunobodin@gmail.com)
- ZSYS_INTERFACE variable can be a single digit (bruno.bodin@cea.fr)
- Fix win32 build (#1601) (bbdb68@users.noreply.github.com)
- handle CTRL_CLOSE_EVENT (brunobodin@gmail.com)
- Problem: zpoller_test fails without ZMQ_POLLER (luca.boccassi@gmail.com)
- Problem: helper functions symbols leaking in shared object
  (luca.boccassi@gmail.com)
- Problem: manually running private classes tests (luca.boccassi@gmail.com)
- Problem: out of date with zproject (luca.boccassi@gmail.com)
- Problem: list of readers is scanned unnecessarily (paddor@gmail.com)
- fix typo (paddor@gmail.com)
- Problem: zpoller_remove() does not always fail when removing non-existent
  reader (paddor@gmail.com)
- change PLAIN to ALLOW (chelahmy@gmail.com)
- Problem: CZMQ does not support new DRAFT handshake success/failure monitor
  events (luca.boccassi@gmail.com)
- Problem: zsys_shutdown does not call zmq_term when it closes sockets
  (luca.boccassi@gmail.com)
- Problem: uuid detection in zuuid.c breaks debian/kFreeBSD build
  (luca.boccassi@gmail.com)
- Problem: debian/kFreeBSD has its own define (luca.boccassi@gmail.com)
- Problem: README.md out of date with docs (luca.boccassi@gmail.com)
- Problem: zgossip doc is misleading (luca.boccassi@gmail.com)
- Problem: zgossip_test does not test STATUS and DELIVER commands
  (luca.boccassi@gmail.com)
- Problem: zmsg_remove updates size no matter if frame is/isn't a member
  (luca.boccassi@gmail.com)
- Problem: out of date with API (luca.boccassi@gmail.com)
- Problem: zhashx callbacks have wrong docs (luca.boccassi@gmail.com)
- Problem: typo in comment (luca.boccassi@gmail.com)
- Problem: zhash_autofree implies the value must be a string, but the
  documentation does not mention this (luca.boccassi@gmail.com)
- Problem: out of date with the version (luca.boccassi@gmail.com)
- Problem: 4.0.2 is out, time to bump version and ABI (luca.boccassi@gmail.com)
- Finalize changelog for 4.0.2 bugfix release (luca.boccassi@gmail.com)
- Problem: out of date with zproject (luca.boccassi@gmail.com)
- Problem: ABI not set in project.xml (luca.boccassi@gmail.com)
- Problem: Ruby bindings don't work on Windows (kou@clear-code.com)
- Fixed samples in examples/security to compile with API v3 (excluding zthread
  using ironhouse2.c ) (thomas.trocha@gmail.com)
- Problem: bug fixes not mentioned in NEWS file (luca.boccassi@gmail.com)
- Problem: travis CI does not use pre-built packages (luca.boccassi@gmail.com)
- Problem: out of date with zproject (luca.boccassi@gmail.com)
- Problem: out of date with zproject (luca.boccassi@gmail.com)
- Problem: Travis rebuilds libsodium every time (luca.boccassi@gmail.com)
- Problem: legacy CI jobs do not use sodium (luca.boccassi@gmail.com)
- Problem: Travis OSX workaround for libtool no longer needed
  (luca.boccassi@gmail.com)
- Problem: useless autogen.sh call in .travis.yml (luca.boccassi@gmail.com)
- Problem: out of date with zproject (luca.boccassi@gmail.com)
- Problem: code formatting problems in zhash.c (luca.boccassi@gmail.com)
- Problem: debug commented out printf left in code (luca.boccassi@gmail.com)
- Problem: out of date with zproject (luca.boccassi@gmail.com)
- Problem: Memory leak when message send fails
  (stephenprocter@users.noreply.github.com)
- Problem: Some known AUTHORS not on the file (jim@jimklimov.com)
- Problem: Auto-generated documentation files were tracked as part of the
  project (jim@jimklimov.com)
- Problem: Generated project structure was not up to date with zproject
  (jim@jimklimov.com)
- Problem: out of date with zproject (luca.boccassi@gmail.com)
- Problem: older ZMQ does not know --with-docs (luca.boccassi@gmail.com)
- Problem: Travis does not install docs build-deps (luca.boccassi@gmail.com)
- Problem: numbers in zsock_test might be trimmed to bad bitness
  (jim@jimklimov.com)
- Problem : zhash_test segfaulted with bad randof() macro (jim@jimklimov.com)
- Problem: czmq_prelude.h had a typo in macros (SRV4 => SVR4)
  (jim@jimklimov.com)
- Problem : SUNOS was not considered on par with SOLARIS for randof()
  (jim@jimklimov.com)
- Problem: randof() macro makes mistakes (jim@jimklimov.com)
- configure.ac : missed one file with redundant exec bits (jim@jimklimov.com)
- Problem : self-test in zsock.c does not clear out number4_MAX
  (jim@jimklimov.com)
- Problem: Many source and doc files were marked with executable bits
  (jim@jimklimov.com)
- Problem : self-test in zsock.c uses wrong data type (and size)
  (jim@jimklimov.com)
- zuuid.c : allow compilation on solaris/illumos (jim@jimklimov.com)
- Problem: README.md out of date (luca.boccassi@gmail.com)
- Problem: README says to run ldconfig which is wrong for OSX
  (luca.boccassi@gmail.com)
- Problem: docs out of date with API (luca.boccassi@gmail.com)
- Problem: out of date with zproject (luca.boccassi@gmail.com)
- Problem: zsock options documentation out of date (luca.boccassi@gmail.com)
- Problem: zsock options API does not document libzmq requirements
  (luca.boccassi@gmail.com)
- Problem: bindings out of date (luca.boccassi@gmail.com)
- Problem: zsock options code out of date with sockopts.xml
  (luca.boccassi@gmail.com)
- Problem: zsock options could be available at build time but not at runtime
  (luca.boccassi@gmail.com)
- Problem: DRAFT zsock_new_*_checked symbols leak (luca.boccassi@gmail.com)
- Problem: out of date with zproject (luca.boccassi@gmail.com)
- Problem: bintrayUpload fails without proper error message
  (mail@kevinsapper.de)
- Problem: python bindings fail during release build (mail@kevinsapper.de)
- Problem: out of date with project.xml (luca.boccassi@gmail.com)
- Problem: 4.0.1 is out, time to bump version for development
  (luca.boccassi@gmail.com)
- Problem: no NEWS entry for 4.0.1 (luca.boccassi@gmail.com)
- Problem: out of date with zproject and project.xml (luca.boccassi@gmail.com)
- Problem: 4.0.0 is out, time to bump version for development
  (luca.boccassi@gmail.com)
- Problem: zbeacon would not try to reconnect more than once
  (github.com@evilpaul.org)
- Problem: draft sockets _checked methods always exported
  (luca.boccassi@gmail.com)
- Problem: zgossip_msg_test not ran anymore (luca.boccassi@gmail.com)
- Problem: out of date with zproject (luca.boccassi@gmail.com)
- Problem: ruby bindings outdated wrt zproject (paddor@gmail.com)
- Finalize NEWS for 4.0.0 (luca.boccassi@gmail.com)
- Problem: README.md out of date (luca.boccassi@gmail.com)
- Problem: out of date with api/* (luca.boccassi@gmail.com)
- Problem: interrupt handling was retired, but replacement is draft
  (luca.boccassi@gmail.com)
- Problem: no NEWS entries for 4.0.0 (luca.boccassi@gmail.com)
- Problem: zlist_dup does not copy comparison function. (meleewang@gmail.com)
- Problem: docs out of date (luca.boccassi@gmail.com)
- Problem: no wrapper for new ZMQ_MAX_MSGSZ ctx option
  (luca.boccassi@gmail.com)
- Problem: docs out of date (luca.boccassi@gmail.com)
- Problem: out of date with zproject and api/*.xml (luca.boccassi@gmail.com)
- Problem: dead deprecated implementation in src (luca.boccassi@gmail.com)
- Problem: some APIs in stable classes are DEPRECATED (luca.boccassi@gmail.com)
- Problem: zhashx and zsock use deprecated v2 method (luca.boccassi@gmail.com)
- Problem: czmq is out of sync with zproject (mail@kevinsapper.de)
- Probem: version.sh is deprecated (mail@kevinsapper.de)
- Problem: Auto generated bindings are not promoted (mail@kevinsapper.de)
- Problem: out of date with src/sockopts.xml (luca.boccassi@gmail.com)
- Problem: some libzmq 4.2 socket options missing (luca.boccassi@gmail.com)
- Problem: some libzmq 4.1 socket options missing (luca.boccassi@gmail.com)
- Problem: out of date with sockopt.xml (luca.boccassi@gmail.com)
- Problem: new sockopt released in zmq 4.2 but still draft
  (luca.boccassi@gmail.com)
- Problem: irc badge does not belong to ci badges (mail@kevinsapper.de)
- Problem: There are no links to OBS packages (mail@kevinsapper.de)
- Problem: out of date with project.xml version (luca.boccassi@gmail.com)
- Problem: many API/ABI breakages for a patch version bump
  (luca.boccassi@gmail.com)
- Problem: out of date with zproject and project.xml (luca.boccassi@gmail.com)
- Problem: time to retire deprecated APIs (luca.boccassi@gmail.com)
- Problem: zsys uses deprecated zsocket APIs (luca.boccassi@gmail.com)
- Problem: zsys comment mentions deprecated zsocket API
  (luca.boccassi@gmail.com)
- Problem: zsock_option.gsl writes .xml instead of .api
  (luca.boccassi@gmail.com)
- Problem: build with libsystemd fails without zmq 4.2
  (luca.boccassi@gmail.com)
- Problem: zsock_vsend leaks zmsg_t on failure (luca.boccassi@gmail.com)
- fix typo (paddor@gmail.com)
- zproject has been updated (wes@barely3am.com)
- Problem: zlist_push doesn't return -1 (pachtchenko@gmail.com)
- Problem: A request. (taotetek@gmail.com)
- Problem: Brocade has copyright but not in AUTHORS (lboccass@brocade.com)
- Update ruby binding for referring LIBCZMQ_PATH (mrkn@mrkn.jp)
- Problem: Ruby binding outdated (zproject evolved) (paddor@gmail.com)
- Problem: Can't build Release type with "git clone"d source (kou@clear-
  code.com)
- Problem: _WIN32_WINNT version is old to use inet_pton() (kou@clear-code.com)
- Problem: LIBCZMQ_EXPORTS is still used with some builds such as CMake build
  (kou@clear-code.com)
- Problem: Hostname for any-interface broadcast non-portable
  (tom.whittock@gmail.com)
- Problem: ZBeacon does not bind to all interfaces (*) correctly.
  (tom.whittock@gmail.com)
- Problem: build failure due to missing defined() (luca.boccassi@gmail.com)
- Problem: readdir_r deprecated in glibc 2.24 (luca.boccassi@gmail.com)
- Problem: out of date with zproject (luca.boccassi@gmail.com)
- Problem: out of date with zproject (luca.boccassi@gmail.com)
- Problem: zbeacon won't reconnect on ip address change
  (tom.whittock@gmail.com)
- Problem: Some windows errors are not handled (tom.whittock@gmail.com)
- Problem: Generated README.md outdated (paddor@gmail.com)
- Problem: redhat packaging out of sync (zproject has evolved!)
  (mail@kevinsapper.de)
- Problem: out of date with zproject (luca.boccassi@gmail.com)
- Problem: out of date with zproject (luca.boccassi@gmail.com)
- Problem: czmq is out of sync (zproject has evolved!) (mail@kevinsapper.de)
- Problem: I am not in the AUTHORS file (luca.boccassi@gmail.com)
- Problem: Travis CI OSX builds are broken (luca.boccassi@gmail.com)
- Problem: No explanation how to get rid of merge commits (mail@kevinsapper.de)
- Problem: recursive merge commits cannot be fixed (luca.boccassi@gmail.com)
- Fixes typo (sappo@users.noreply.github.com)
- Problem: Contribution guidelines are easily missed (mail@kevinsapper.de)
- Use zpoller_set_nonstop argument (diorcety@users.noreply.github.com)
- Problem: README doesn't provide license and version at glance
  (mail@kevinsapper.de)
- Problem: Python bindings not executed by CI system. (tom.whittock@gmail.com)
- Problem: Python bindings test was failing. (tom.whittock@gmail.com)
- Problem: cmake configs are out of date (zproject has evolved!)
  (mail@kevinsapper.de)
- Problem: zdir.c, zmsg.c and test_zgossip.h are still LGPL3 licensed
  (luca.boccassi@gmail.com)
- Problem: invalid characters at beginning of zproxy.c breaks compilation
  (alejandro.schwoykoski@gmail.com)
- Problem: czmq is out of sync (zproject has evolved!) (mail@kevinsapper.de)
- Problem: czmq has a lot of unused shell scripts (mail@kevinsapper.de)
- Problem: zlist_dup doesn't create copy autofree list if copied list was
  autofree (pawel.weber@thaumatec.com)
- Problem: README is too vague about pkg-config (luca.boccassi@gmail.com)
- Problem: [zhashx] code does not conform with style guide
  (mail@kevinsapper.de)
- Adjust to use formatting convention (spaces, not tabs).
  (joseph_l@adventsystems.com)
- Allocate 'values' on the heap.  VC++ does not implement C99 variable length
  arrays. (joseph_l@adventsystems.com)
- Problem: [zhashx] packing items will fails if they're chained
  (mail@kevinsapper.de)
- Problem: czmq docs and mvcs are out of sync (zproject has evolved!)
  (mail@kevinsapper.de)
- Problem: bindings are out of sync (api has evolved!) (mail@kevinsapper.de)
- Problem: [zhashx] cannot (un)pack anything but string values
  (mail@kevinsapper.de)
- fixed libzmq.import.props file path. all visual studio versions now sharing
  same libzmq.import.props file located at libzmq\builds\vs2015 (ahmet.kakici
  @pro-line.com.tr)
- Problem: travis does not compile android with clang (mail@kevinsapper.de)
- Problem: czmq is out of sync (zproject has evolved!) (mail@kevinsapper.de)
- Problem: Dockerfile is not generated by zproject (mail@kevinsapper.de)
- Problem: czmq out of sync (zproject has evolved!) (mail@kevinsapper.de)
- Problem: travis + jni out of sync (zproject has evolved!)
  (mail@kevinsapper.de)
- Problem: [travis] jni layer is not automatically deployed to bintray
  (mail@kevinsapper.de)
- Problem: czmq out of sync (zproject has evolved!) (mail@kevinsapper.de)
- fixed libzmq.import.props file path. all visual studio versions now sharing
  same libzmq.import.props file located at libzmq\builds\vs2015. (ahmet.kakici
  @pro-line.com.tr)
- Problem: CZMQ out of date with zproject (luca.boccassi@gmail.com)
- Problem: no Valgrind test run on Travis CI (luca.boccassi@gmail.com)
- Problem: out of sync with zproject (luca.boccassi@gmail.com)
- Problem: ztimer tests fail under Valgrind (luca.boccassi@gmail.com)
- Problem: CURVE tests fail under Valgrind (luca.boccassi@gmail.com)
- Problem: memory leak in zauth s_authenticate_curve (luca.boccassi@gmail.com)
- Problem: memory leak in zcertstore s_disk_loader (luca.boccassi@gmail.com)
- Problem: memory leak in zcertstore_set_loader (luca.boccassi@gmail.com)
- Problem: memory leak in zarmour_decode (luca.boccassi@gmail.com)
- Problem: memory leak in zarmour self test (luca.boccassi@gmail.com)
- Problem: ~zproxy deletes zpoller after sockets (luca.boccassi@gmail.com)
- Problem: out-of-bounds read in zdir_patch_new (luca.boccassi@gmail.com)
- Fix compilation with mingw64 using autotools (diorcet.yann@gmail.com)
- Problem: [jni] gradle wrapper uses old version (mail@kevinsapper.de)
- Problem: czmq is out of sync (zproject has evolved!) (mail@kevinsapper.de)
- Problem: jni and packaging out of sync (zproject has evolved!)
  (mail@kevinsapper.de)
- Problem: autotools out of sync (zproject has evolved!) (mail@kevinsapper.de)
- Problem: out of sync with zproject (luca.boccassi@gmail.com)
- Problem: autotools out of sync (zproject has evolved!) (mail@kevinsapper.de)
- Problem: [travis] ci does not test jni binding and deploy android jar
  (mail@kevinsapper.de)
- Problem: [jni] gradle wrapper jar is missing (mail@kevinsapper.de)
- Problem: jni/travis/packaging out of sync (zproject has evolved)
  (mail@kevinsapper.de)
- Switched transport to ipc (piskorzj@gmail.com)
- Remove zpoller_add call & use when_configured function instead
  (piskorzj@gmail.com)
- Add function to add socket to poller when both are configured
  (piskorzj@gmail.com)
- Add test proving issue with hazard (piskorzj@gmail.com)
- Problem: License and URL Fields are wrong in the
  czmq/packaging/redhat/czmq.spec file (cyrille.verrier@fabriscale.com)
- Problem: zproject was not latest on prevuious commit (bkmit@maytech.net)
-     Problem: uuid library not used (bkmit@maytech.net)
- Problem: docs and README are out of date (mail@kevinsapper.de)
- Problem: bindings/builds/travis out of sync (zproject has evolved)
  (mail@kevinsapper.de)
- Problem: travis does not automatically deploy release artifacts
  (mail@kevinsapper.de)
- Problem: zproxy_test does not cleanup after itself (mail@kevinsapper.de)
- Problem: out of date wrt zproject (opedroso@gmail.com)
- Remove automatic s_logstream reset to stdout. (eric@voskuil.org)
- Gitignore windows build outputs. (eric@voskuil.org)
- Problem: tests for zfile_eof are missing Solution: add them
  (AlenaChernikava@Eaton.com)
- Problem: issue #1434 zfile_eof () doesn't work Solution: check the "eof"
  condition at the right place (AlenaChernikava@Eaton.com)
- Problem: build/bindings are out of sync (zproject has evolved). Solution:
  regenerate all! (mail@kevinsapper.de)
- Problem: There is no README documentation for ztimerset Solution: Generate
  and add it to README! (mail@kevinsapper.de)
- Generated documentation (axel.voitier@gmail.com)
- README.md: wrong order of gcc args (axel.voitier@gmail.com)
- Problem: finding the zeromq irc is too difficult (or not easy enough)
  Solution: provide a link directly in the README of zeromq project's
  (kevin.b.sapper@student.hs-rm.de)
- Problem: zframe group api already included as draft (taotetek@gmail.com)
- Problem: zframe_set_group and zframe_group not exported (taotetek@gmail.com)
- Problem: czmq fails to compile without pkg-config for autotools Solution: re-
  generate autotools config from latest zproject (mail@kevinsapper.de)
- Problem: typo in CZMQ manpage (luca.boccassi@gmail.com)
- Problem: zsys.c did not know about SCATTER / GATHER (taotetek@gmail.com)
- Problem: Comment in highlighted section is misinterpreted as header Solution:
  gitdown needs an indent for highlighted section to ignore them
  (mail@kevinsapper.de)
- Problem: CI build status images do not include platform Solution: Label the
  images for clarity (mail@kevinsapper.de)
- not running tests when zmq_timers is not available (somdoron@gmail.com)
- Problem: out of date with zproject (luca.boccassi@gmail.com)
- regenerate files following ztimerset (somdoron@gmail.com)
- add ztimerset class (somdoron@gmail.com)
- Problem: New zcertstore APIs were not marked as "draft". (pete@hayes.id.au)
- Problem: zcertstore loader doesn't allow any state to be held by the loader
  cb. (pete@hayes.id.au)
- Problem: zuuid_str case inconsistentcy (bkmit@maytech.net)
- fix wrong doc on zsock_new_scatter (somdoron@gmail.com)
- add scatter/gather (somdoron@gmail.com)
- Problem: zauth doesn't allow overriding of default zcertstore.
  (pete@hayes.id.au)
- Problem: zcertstore only works with a disk backend. (pete@hayes.id.au)
- Problem: Windows CI does not add zmakecert.exe to artefict Solution: add it
  (anonymous.maarten@gmail.com)
- Problem: artifacts of windows CI does not include czmq_selftest.exe Solution:
  Include it by pointing to the correct location (anonymous.maarten@gmail.com)
- Problem: brew install errors out with new version (luca.boccassi@gmail.com)
- Problem: czmq not using latest zproject Solution: Regenerate files
  (mail@kevinsapper.de)
- Problem: UUID not in uppercase (hitstergtd@users.noreply.github.com)
- Problem: UUID not in uppercase (hitenp@ADT.local)
- Problem: zsock_recv casts away u32/u64's last bit (luca.boccassi@gmail.com)
- Problem: Testing zauth certificate metadata breaks on ZMQ < 4.1.
  (pete@hayes.id.au)
- Problem: PR #1398 introduced an implicit conversion error for some platforms.
  (pete@hayes.id.au)
- Problem: Certificate metadata is not being returned by ZAP handler.
  (pete@hayes.id.au)
- Problem: userland needs bindings install (rgbkrk@gmail.com)
- Problem: index.js should export constants + native (rgbkrk@gmail.com)
- Problem: [nodejs] need to export constants (ph@imatix.com)
- Problem: zframe API required updating. (pete@hayes.id.au)
- Problem: zframe_meta fn disappears when using zmq < 4.1. (pete@hayes.id.au)
- Problem: zframe_meta relies on zmq_msg_gets, which isn't present in ZMQ <
  4.1.0. (pete@hayes.id.au)
- Problem: Potential for segfault in zframe_test if Socket-Type meta data not
  set. (pete@hayes.id.au)
- Added docs and unit test for zframe_meta() (pete@hayes.id.au)
- ZFrame metadata getter (pete@hayes.id.au)
- Problem: [nodejs] socket set option API was missing (ph@imatix.com)
- Problem: nodejs zsock constructor takes magic numbers (ph@imatix.com)
- Problem: NodeJS binding can't do Hello World (ph@imatix.com)
- Problem: introduced some compile errors (ph@imatix.com)
- Problem: 'src' argument is inconsistent with other classes (ph@imatix.com)
- Problem: zsock constructor is not nice for bindings (ph@imatix.com)
- Problem: API models do not identify socket arguments (ph@imatix.com)
- Problem: support for RADIO/DISH is incomplete (ph@imatix.com)
- Update README.md, missing code block start (saulthu@gmail.com)
- Problem: CZMQ not using latest ZPROJECT gsls (opedroso@gmail.com)
- Problem: CZMQ not built using lastest ZPROJECT gsls (opedroso@gmail.com)
- Problem: rebuilt packaging with old zproject (ph@imatix.com)
- Problem: packaging is out of date (zproject has evolved) (ph@imatix.com)
- Problem: title for zconfig & zdigest had redundant class name (ph@imatix.com)
- Problem: can't access CZMQ from NodeJS (ph@imatix.com)
- Problem: zdigest_update takes mutable buffer (ph@imatix.com)
- Problem: when returning buffer, need to specify size (ph@imatix.com)
- Problem: API returning mutable types for constants (ph@imatix.com)
- Problem: printf "%%d" format is pedantically wrong for pid_t getpid() return
  type (jim@jimklimov.com)
- Problem: generated script clobber my source tree (paddor@gmail.com)
- Problem: wrong namespace for constants in Ruby binding (paddor@gmail.com)
- Problem: Ruby binding outdated wrt zproject (paddor@gmail.com)
- Problem: Fixing problems in Windows build (opedroso@gmail.com)
- Renamed 'zocket' to 'socket' for legibility (ph@imatix.com)
- Minor doc fix (ph@imatix.com)
- Problem: passes null pointer on interrupt (#1374) (ph@imatix.com)
- Problem: README.txt out of date (opedroso@gmail.com)
- Problem: Build instructions in README.md out of date (opedroso@gmail.com)
- Problem: No Windows build instructions in README.txt (opedroso@gmail.com)
- Problem: zauth_v2 sometimes hangs in self test (lerwys@gmail.com)
- Problem: zlist_sort does not work according to docs (ph@imatix.com)
- Problem: libuuid dependency is fragile and unnecessary (ph@imatix.com)
- Problem: enums are over-engineered in zproject API language (ph@imatix.com)
- Problem: zmsg_encode/decode have weak API (ph@imatix.com)
- Problem: zarmour_decode returns value by reference (ph@imatix.com)
- Problem: API files still use old .xml extension (ph@imatix.com)
- Problem: packaging issues break build on OBS (luca.boccassi@gmail.com)
- Problem: stable build broken (luca.boccassi@gmail.com)
- Problem: specify NuGet target options (ph@imatix.com)
- Problem: node.js defines ssize_t as intptr_t (ph@imatix.com)
- Problem: packaging is out of date (ph@imatix.com)
- Problem: CHECK_PRINTF style doesn't work on Windows (ph@imatix.com)
- Problem: compile warnings on Windows (ph@imatix.com)
- Problem: deprecated methods not marked as such in API (ph@imatix.com)
- Problem: CI config option --without-doc is wrong (luca.boccassi@gmail.com)
- Problem: build with older libzmq is broken (luca.boccassi@gmail.com)
- Problem: CMake CI build still uses libsodium (luca.boccassi@gmail.com)
- Problem: CI build with stable ZMQ broken (luca.boccassi@gmail.com)
- Problem: CI config still mentions libsodium (luca.boccassi@gmail.com)
- Problem: various sign comparison warnings (via node-gyp) (ph@imatix.com)
- Problem: need a little doc for using GYP (ph@imatix.com)
- Problem: static/dll confusion in Windows gyp (ph@imatix.com)
- Problem: gyp link on Windows fails on UuidCreate (ph@imatix.com)
- Problem: CZMQ_EXPORTS defined in two places (ph@imatix.com)
- Problem: STATIC macros don't work with libzmq (ph@imatix.com)
- Problem: various methods cause warnings on MSVC (ph@imatix.com)
- Problem: gyp build can't find dependent includes (ph@imatix.com)
- Problem: gyp builds aren't complete (ph@imatix.com)
- Problem: CZMQ packaging out of date (ph@imatix.com)
- Problem: I should read CLASS style more carefully (luca.boccassi@gmail.com)
- Problem: use_fd needs to be used manually by apps (luca.boccassi@gmail.com)
- Problem: code out of date with project.xml (luca.boccassi@gmail.com)
- Problem: no dep on libsystemd in project.xml (luca.boccassi@gmail.com)
- Problem: out of date with zproject (luca.boccassi@gmail.com)
- Problem: static links fail due to unresolved libm (ph@imatix.com)
- Problem: sock opts out of date with sockopts.xml (luca.boccassi@gmail.com)
- Problem: ZMQ_PRE_ALLOCATED_FD renamed to USE_FD (luca.boccassi@gmail.com)
- Problem: sock opts out of date with sockopts.xml (lboccass@brocade.com)
- Problem: new pre_allocated_fd sockopt missing (lboccass@brocade.com)
- Problem: Android build uses unstable libsodium (lboccass@brocade.com)
- Problem: wrong functions names in Ruby binding (paddor@gmail.com)
- Problem: CI build uses unstable libsodium build (lboccass@brocade.com)
- Problem: git log typo breaks CI (lboccass@brocade.com)
- Problem: JNI/Android build was not working (ph@imatix.com)
- Problem: can't configure Windows builds (ph@imatix.com)
- Problem: old czmq.py module exists, but zproject now generates python
  bindings as a directory. (aaron@mustardsystems.com)
- Problem: in python binding, it's hard to compare objects to ctypes c_void_p
  (aaron@mustardsystems.com)
- Problem: gitignore is out of date with zproject (aaron@mustardsystems.com)
- Problem: czmq is out-of-sync with latest zproject (constantin@rack.li)
- add radio-dish support to czmq (somdoron@gmail.com)
- Problem: czmq_prelude.h refers to zmq_utils.h (ph@imatix.com)
- Out of sync with zproject and zproto (mail@kevinsapper.de)
- Problem: CI builds are out of date (ph@imatix.com)
- Problem: Python binding is out of date (ph@imatix.com)
- Problem: JNI binding did not build, lacking DRAFT API (ph@imatix.com)
- Problem: man pages are a little out of date (ph@imatix.com)
- Problem: czmq python bindings are a bit painful to install
  (aaron@mustardsystems.com)
- Problem: zsys_test is failing (ph@imatix.com)
- Problem: Python API broke on zlistx (ph@imatix.com)
- Problem: zhashx_values code was malformatted (ph@imatix.com)
- Problem: constructor does useless initialization (ph@imatix.com)
- Problem: zsys returns NULL if it can't create a pipe (ph@imatix.com)
- Problem: zlistx API is wrongly using czmq_destructor et. al (ph@imatix.com)
- Problem: autoconf scripts were built with out-of-date zproject
  (ph@imatix.com)
- Problem: auto-generated python cffi-bindings do not exist
  (aaron@mustardsystems.com)
- Problem: CZMQ doesn't build with MSVC without DRAFT_API definition Solution:
  Add DRAFT_API defs (granvillelintao@gmail.com)
- Problem: qt bindings won't compile against draft APIs Solution: make qmake
  read pkgconfig (mail@kevinsapper.de)
- Problem: czmq_selftest build still not conditional (ph@imatix.com)
- Problem: selftest build must be optional (ph@imatix.com)
- Problem: need a GYP build file (ph@imatix.com)
- Problem: does not build if draft API is disabled (ph@imatix.com)
- Problem: zlistx_head/tail defined as draft (ph@imatix.com)
- Problem: czmq_selftest failing on zsys (ph@imatix.com)
- Problem: Ruby binding outdated wrt zproject (paddor@gmail.com)
- Problem: unreleased methods declared as stable (paddor@gmail.com)
- Problem: socket options can't be draft (paddor@gmail.com)
- Problem: CMake find package support was broken (ph@imatix.com)
- Problem: minor fixup to comments (ph@imatix.com)
- Problem: does not support GNU/Hurd (ph@imatix.com)
- Problem: out of date wrt zproject (ph@imatix.com)
- Problem: sources still including platform.h (ph@imatix.com)
- Problem: zcert_new_from takes mutable arguments (ph@imatix.com)
- Problem: zmutex has an API model (ph@imatix.com)
- make zsock_bsend/brecv support server socket type (somdoron@gmail.com)
- Problem: out of date with zproject (lboccass@brocade.com)
- Problem: out of date with zproject (ph@imatix.com)
- Revert "I don't think class status belongs in project.xml" (ph@imatix.com)
- Problem: status attribute defined in project.xml (ph@imatix.com)
- Small change to zuuid man page (ph@imatix.com)
- Problem: legacy APIs status is not set in project.xml
  (luca.boccassi@gmail.com)
- Problem: stable APIs status is not set in project.xml
  (luca.boccassi@gmail.com)
- Problem: gsl project.xml reports unknown type clock
  (michalvyskocil@eaton.com)
- Problem: don't have zmutex model (michalvyskocil@eaton.com)
- Problem: missing API model for zlistx (michalvyskocil@eaton.com)
- Problem: zdigest.xml is missing (michalvyskocil@eaton.com)
- Problem: ZMTP 3.1 heartbeat options missing (paddor@gmail.com)
- Problem: wrong instructions in generated comment (paddor@gmail.com)
- Problem: zchunk.xml whitespace is wrong (indents) (ph@imatix.com)
- Problem: 'clock' type no longer supported in zproject (ph@imatix.com)
- Problem: warning comment left in zclass.xml (michalvyskocil@eaton.com)
- Problem: zclock does not have api model (michal.vyskocil@gmail.com)
- Problem: CMake does not discover libsodium Solution: Pass its location as an
  argument (anonymous.maarten@gmail.com)
- Problem: CMake wrongfully uses non-found optionally libraries Solution: Add
  the libraries of found optional libraries to the OPTIONAL_LIBRARIES variable
  (anonymous.maarten@gmail.com)
- Problem: Windows CI builds fail on libsodium missing symbols Solution: Use
  the stable branch of libsodium (See
  https://github.com/jedisct1/libsodium/issues/346)
  (anonymous.maarten@gmail.com)
- Re-generate configuration files and bindings from latest zproject
  (mail@kevinsapper.de)
- Problem: czmq travis build is taking too long Solution: speed up compilation
  time with `make -j4` (mail@kevinsapper.de)
- Problem: valgrind shows a couple of memory leaks Solution: fix the memory
  leaks by freeing everything correctly (mail@kevinsapper.de)
- Problem: Cannot compile czmq without libsodium Solution: Make libsodium an
  optional dependency (mail@kevinsapper.de)
- Problem: need to use zproject/mkapi.py on real world case
  (michalvyskocil@eaton.com)
- Problem: Travis CI fails due to missing Valgrind (luca.boccassi@gmail.com)
- Problem: zauth sometimes hangs in self test (ph@imatix.com)
- Problem: uuid link error on Android (ph@imatix.com)
- Problem: JNI Android build.sh out of date (ph@imatix.com)
- Problem: unconfigured zbeacon closes STDIN on destruction (paddor@gmail.com)
- Problem: Android build is too slow (ph@imatix.com)
- Problem: src/zstr.c:336: zstr_test: Assertion `server' failed.
  (ph@imatix.com)
- Problem: _ignore_interrupts is not a nice name (ph@imatix.com)
- Problem: codebase is filled with useless OOM checks (ph@imatix.com)
- Problem: unclear explanations on zpoller add/remove (ph@imatix.com)
- Problem: zpoller has lots of duplicated code (ph@imatix.com)
- Problem: zmakecert always writes to same file (ph@imatix.com)
- Problem: methods in zarmour.c are not in right order (ph@imatix.com)
- Problem: CMake test was broken (ph@imatix.com)
- Problem: zclass generator is redundant (ph@imatix.com)
- Problem: packaging is lagging behind zproject (ph@imatix.com)
- Problem: zsock_option test OK mixes with zsock's output (ph@imatix.com)
- Problem: weak/no testing for CLIENT/SERVER (ph@imatix.com)
- Problem: zstr_send on SERVER socket not working (ph@imatix.com)
- Problem: can't build JNI bindings on MSVC (ph@imatix.com)
- Fixed issue #1278 (butner.se@gmail.com)
- Fixed issue #1278 (butner.se@gmail.com)
- Problem: repetitive need to delete non-tracked files after generating
  (paddor@gmail.com)
- Problem: Python CI is broken (ph@imatix.com)
- Problem: some deprecated test cases for Python (ph@imatix.com)
- Cosmetic fix (ph@imatix.com)
- Problem: packaging has issues fixed in zproject (ph@imatix.com)
- Problem: test_gossip does not need building (ph@imatix.com)
- Problem: on MSVC, library names are not consistent (ph@imatix.com)
- Problem: missing assert in zpoller_wait() (paddor@gmail.com)
- Problem: bad readability of condition (paddor@gmail.com)
- fix typo (paddor@gmail.com)
- Problem: MSVC props files were missing (.gitignore) (ph@imatix.com)
- Problem: bindings lag behind latest API (ph@imatix.com)
- Problem: does not build on MSVC (ph@imatix.com)
- Problem: generated code is behind zproto (ph@imatix.com)
- Problem: minor warnings when compiling in MSVC (ph@imatix.com)
- Problem: ztrie uses cute Unicode box characters (ph@imatix.com)
- Problem: zbeacon_v2 does not build on Windows (ph@imatix.com)
- Problem: bindings need to know if CURVE security is available
  (paddor@gmail.com)
- Problem: git has files that shouldn't be there (ph@imatix.com)
- Problem: MSVC builds are broken (ph@imatix.com)
- android jni build.sh: ensure "gradle build jar" is run, otherwise headers
  won't be there (zoobab@gmail.com)
- Problem: libzmq master changed zmq_poller_close -> destroy (ph@imatix.com)
- Problem: check-py build fails due to syntax error (constantin@rack.li)
- Problem: Travis still tries to build qt-android (ph@imatix.com)
- Problem: MSVC builds don't match zproject output (ph@imatix.com)
- Problem: duplicate include (paddor@gmail.com)
- Problem: MSVC builds are a mess (ph@imatix.com)
- Problem: repository contains files generated by MSVC (ph@imatix.com)
- Problem: "interface" is a reserved word (ph@imatix.com)
- Problem: no access to zsys methods in generated bindings (ph@imatix.com)
- Problem: inconsistent use of class headers in sources (ph@imatix.com)
- Problem: JNI-Android scripts are out of date (ph@imatix.com)
- Problem: clumsy debugging of JNI/Android build (ph@imatix.com)
- Problem: JNI/Android configuration is all over the place (ph@imatix.com)
- Problem: Android build depends on JNI build (ph@imatix.com)
- Problem: Ruby binding lacks Zcert#unset_meta (paddor@gmail.com)
- Problem: some `assert`s do not follow CLASS style (constantin@rack.li)
- Problem: zcert_set_meta() doesn't assert enough (paddor@gmail.com)
- Problem: no way to unset zcert metadata (paddor@gmail.com)
- Problem: zcert_set_meta() doesn't assert(self) (paddor@gmail.com)
- Problem: zcert_save() ignores result of zcert_save_public()
  (paddor@gmail.com)
- Problem: have duplicate android_build_helper.sh (ph@imatix.com)
- Problem: Android build is now in android, not qt-android (ph@imatix.com)
- Problem: packaging is out of date (ph@imatix.com)
- Problem: Android needs output of qt-android build (ph@imatix.com)
- Problem: JNI/Android build fails on link (ph@imatix.com)
- Problem: need access to Android environment vars (ph@imatix.com)
- Problem: JNI C code has many warnings (ph@imatix.com)
- Problem: lack visibility on Cmake configuration (ph@imatix.com)
- Problem: need skeleton android build for JNI (ph@imatix.com)
- Problem: JNI binding is out of date (ph@imatix.com)
- Trivial indentation fix (ph@imatix.com)
- Problem: ipv6 changes conflict with boost::asio (constantin@rack.li)
- Problem: ipv6 changes conflict with boost::asio (constantin@rack.li)
- Problem: Ruby binding is outdated wrt zproject (paddor@gmail.com)
- Adding support for IPv6 (czmq issue #1236) (Sathish_Yenna@dell.com)
- Problem: JNI bindings are out of date wrt zproject (ph@imatix.com)
- Problem: czmq.h wrongly describes itself as a 'p2p framework' :)
  (ph@imatix.com)
- Problem: doc/zsock_option.{doc,txt} was deleted (constantin@rack.li)
- Problem: hand-built JNI binding is no longer needed (ph@imatix.com)
- Problem: copyright notice missing (paddor@gmail.com)
- Problem: unsafe use of format (paddor@gmail.com)
- Problem: Ruby binding lacks zcert and zcertstore (paddor@gmail.com)
- Problem: C interfaces of zcert and zcertstore are manually written
  (paddor@gmail.com)
- Problem: no API models for zcert and zcertstore (paddor@gmail.com)
- Problem: missing void in C interfaces (paddor@gmail.com)
- Problem: czmq_selftest block-local variable fails for MSVC
  (jeff.daily@pnnl.gov)
- Problem: Ruby binding outdated (paddor@gmail.com)
- Problem: JNI: not building all classes properly (ph@imatix.com)
- Problem: CZMQ classes use multiple constructors (ph@imatix.com)
- Problem: doc for zsock_brecv is inaccurate (ph@imatix.com)
- Problem: many constructors are disguised in API model (ph@imatix.com)
- Problem: bindings are out of date (ph@imatix.com)
- Problem: JNI Zframe.data returns void * not byte [] (ph@imatix.com)
- Problem: spelling mistake (ph@imatix.com)
- Problem: JNI binding cannot turn void * to String (ph@imatix.com)
- Problem: zmsg_load marked as singleton in api model
  (michalvyskocil@eaton.com)
- Problem: bindings are out of date (ph@imatix.com)
- Problem: Qt bindings don't work as qzconfig has an extra comma with method
  reload. Solution: Re-generate with latest zproject to fix it.
  (mail@kevinsapper.de)
- Problem: poor Ruby binding documentation (paddor@gmail.com)
- Problem: .self is private so we can't use it from other packages
  (ph@imatix.com)
- Problem: JNI binding was not using proper types for classes (ph@imatix.com)
- Problem: JNI API has extraneous 'self' argument (ph@imatix.com)
- Refactoring conditional directives for incomplete if conditions.
  (wesleymr.27@gmail.com)
- Refactoring conditional directives for incomplete if conditions.
  (wesleymr.27@gmail.com)
- Problem: multi-word methods did not map correctly in JNI (ph@imatix.com)
- Problem: build failed due to link error in tests (ph@imatix.com)
- Problem: Ruby binding lacks behind zproject (paddor@gmail.com)
- Problem: generated files lack zconfig fixes (paddor@gmail.com)
- Problem: zconfig API contains errors (paddor@gmail.com)
- added ability to publish to local maven repo (awynne@gmail.com)
- Regenerate gradle config from zproject (ph@imatix.com)
- Problem: generated JNI don't build (ph@imatix.com)
- Problem: unintuitive failure return value (paddor@gmail.com)
- Problem: zconfig_execute() doesn't fail early (paddor@gmail.com)
- Problem: JNI bindings are out of date (already!) (ph@imatix.com)
- Problem: JNI binding isn't building (ph@imatix.com)
- Problem: mutable and by_reference overlap (ph@imatix.com)
- Problem: by_reference has no meaning on callback arguments (ph@imatix.com)
- Problem: Latest zproject assumes that includes are relative to API Solution:
  Further zproject assues that includes are withing API directory. Thus make
  path from api/zsock.xml to api/zsock_options.xml realtive to api/zsock.xml.
  (mail@kevinsapper.de)
- Problem: zsock_option.xml is not installed Solution: use latest zproject to
  install this file as well (mail@kevinsapper.de)
- Problem: ztrie does not compile as it discards const qualifier Solution: make
  method take const char * and explicitly cast to char * (mail@kevinsapper.de)
- Problem: CMakeLists.txt was incorrect (ph@imatix.com)
- Problem: zproject is newer than generated code (ph@imatix.com)
- Problem: 'constant' attribute no longer supported (ph@imatix.com)
- Problem: path argument should be const (ph@imatix.com)
- Problem: zframe_new and zframe_refresh API broke (ph@imatix.com)
- Problem: inconsistent use of fresh/constant in APIs (ph@imatix.com)
- Problem: zframe API specifies data as 'anything' (ph@imatix.com)
- Problem: zconfig missing in generated files (paddor@gmail.com)
- Problem: Ruby bindings lack support for zconfig (paddor@gmail.com)
- Problem: bindings lag behind zproject (ph@imatix.com)
- Problem: zarmour API changes depending on libzmq version (ph@imatix.com)
- Problem: zarmour.c is a little dense to read (ph@imatix.com)
- Problem: can't build for libzmq 2.x (ph@imatix.com)
- Problem: zarmour did not build on libzmq 3.x (ph@imatix.com)
- Problem: no API XML definition for zconfig (paddor@gmail.com)
- Problem: typo (paddor@gmail.com)
- Problem: api/zdir_patch.xml does not build (ph@imatix.com)
- Problem: missing binding sources for zarmour (ph@imatix.com)
- Problem: can't build zsock_options properly (ph@imatix.com)
- Problem: Ruby bindings are wrong and outdated. (paddor@gmail.com)
- Problem: Wrong path in include (paddor@gmail.com)
- Problem: typo in zarmour enum constant (paddor@gmail.com)
- renamed ZARMOUR_MODE_BASE16_HEX to ZARMOUR_MODE_BASE16, due to
  ZARMOUR_MODE_BASE16 is used everywhere (ivan.alyakskin@gmail.com)
- Problem: zsock API has redundant code and other issues (ph@imatix.com)
- Problem: whitespace malformatting (ph@imatix.com)
- Problem: generate.sh is out of date and not needed (ph@imatix.com)
- Problem: Ruby bindings are outdated (paddor@gmail.com)
- Add zmsg_popmsg and zmsg_addstr (trevor.bernard@gmail.com)
- Problem: zarmour.h is still hand-written (paddor@gmail.com)
- Problem: wrong zarmour mode enum constant names (paddor@gmail.com)
- Problem: API lacks description of zarmour_print (paddor@gmail.com)
- Problem: enum zarmour_mode_t missing description (paddor@gmail.com)
- Problem: API excludes zarmour_print when it exists (paddor@gmail.com)
- Add new constructor that is byte[] only (trevor.bernard@gmail.com)
- Add zframe_size and zframe_data (trevor.bernard@gmail.com)
- Revert "Problem: API defines explicit enum values" (paddor@gmail.com)
- Call from the static context (trevor.bernard@gmail.com)
- Add byte constructor to zframe (trevor.bernard@gmail.com)
- zpoller server & client test will only run if zmq_poller available
  (somdoron@gmail.com)
- Fix issue with zpoller test, missing NULL parameter in zpoller ctor
  (somdoron@gmail.com)
- Fix wrong assert in zpoller test (somdoron@gmail.com)
- make zpoller work with zmq_poller when supported (somdoron@gmail.com)
- Problem: Define for server and client socket is unnecessary Solution: We can
  safely remove it as the libzmq is carefully handled in the source file.
  (mail@kevinsapper.de)
- Problem: API defines explicit enum values (paddor@gmail.com)
- Problem: Typo in paramter name in zarmour API (paddor@gmail.com)
- Problem: zarmour API: wrong return type (paddor@gmail.com)
- Problem: zarmour_test() API XML wrong (paddor@gmail.com)
- Problem: no descriptions for zarmour modes in API (paddor@gmail.com)
- Problem: self test methods missing in some APIs (paddor@gmail.com)
- Problem: enums values are not one-based (paddor@gmail.com)
- fix style (paddor@gmail.com)
- fix typo (paddor@gmail.com)
- Problem: no API XML definition for zarmour (paddor@gmail.com)
- Problem: Wrong information in comment. (paddor@gmail.com)
- Problem: bindings lack coercion of polymorphic ref (paddor@gmail.com)
- Problem: missing callback result coercion (paddor@gmail.com)
- regenerate Ruby bindings (paddor@gmail.com)
- regenerate zsock_option related things (paddor@gmail.com)
- get rid of files from wrong approach (again) (paddor@gmail.com)
- generate zsock_option functions API in its own file, include from within
  zsock.xml (paddor@gmail.com)
- fix pathnames in <include>'s (paddor@gmail.com)
- embed zsock_* option functions into zsock XML API (paddor@gmail.com)
- generate zsock_option XML API file (paddor@gmail.com)
- add GSL script to generate zsock_option XML API file (paddor@gmail.com)
- fix instructions in header comment (paddor@gmail.com)
- fix typo: zactor_r => zactor_t (paddor@gmail.com)
- generate zsock_option XML API file (paddor@gmail.com)
- add GSL script to generate zsock_option XML API file (paddor@gmail.com)
- fix instructions in header comment (paddor@gmail.com)
- Add zmsg_prepend and zmsg_append (trevor.bernard@gmail.com)
- don't use GSL's deprecated .include command anymore (paddor@gmail.com)
- added publishToMavenLocal capability (awynne@gmail.com)
- Problem: generated builds lag behind zproject (ph@imatix.com)
- Problem: need skeleton JNI files (ph@imatix.com)
- Problem: generated JNI classes are in wrong directory (ph@imatix.com)
- Cosmetic fixes to reduce line count (ph@imatix.com)
- fix typo: zock_t => zsock_t (paddor@gmail.com)
- Add zmsg_pop() (trevor.bernard@gmail.com)
- Don't throw exception on close (trevor.bernard@gmail.com)
- Add ability to create list from pointer (trevor.bernard@gmail.com)
- Add ZList support (trevor.bernard@gmail.com)
- regenerate Ruby bindings for correct handling of variadic arguments
  (paddor@gmail.com)
- Make constructor public (trevor.bernard@gmail.com)
- Expose ZMsg address (trevor.bernard@gmail.com)
- regenerate Ruby bindings (paddor@gmail.com)
- Add the ability to install packages locally (trevor.bernard@gmail.com)
- use zstr_free() instead of free() (paddor@gmail.com)
- Use 127.0.0.1 instead of localhost (trevor.bernard@gmail.com)
- First end to end (trevor.bernard@gmail.com)
- Add zmsg_pushstr (trevor.bernard@gmail.com)
- Fix build order dependencies (trevor.bernard@gmail.com)
- Issue #1152 - Create czmq-jni java native binding (trevor.bernard@gmail.com)
- Problem: Python bindings for Zpoller constructor had incorrect assert.
  (tom.whittock@gmail.com)
- Problem: Python bindings generation issue cause error
  (tom.whittock@gmail.com)

* Fri Mar 17 2017 Michal Gawlik <michal.gawlik@thalesgroup.com> 3.0.2-6
- include/czmq_prelude.h: don't include zmq_utils.h if zeromq >= 4.2.0
  (tomasz.rostanski@thalesgroup.com.pl)

* Fri Jan 13 2017 Michal Gawlik <michal.gawlik@thalesgroup.com> 3.0.2-5
- src/zcertstore.c: remove assertion on duplicated key
  (tomasz.rostanski@thalesgroup.com.pl)

* Thu Apr 21 2016 Michal Gawlik <michal.gawlik@thalesgroup.com> 3.0.2-4
- tito: use ReleaseTagger (michal.gawlik@thalesgroup.com)
- czmq.spec: remove dist name from rpm version
  (tomasz.rostanski@thalesgroup.com.pl)

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
