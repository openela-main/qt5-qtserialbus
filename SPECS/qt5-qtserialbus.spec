%global qt_module qtserialbus

%global build_tests 1

Summary: Qt5 - SerialBus component
Name:    qt5-%{qt_module}
Version: 5.15.3
Release: 1%{?dist}

# See LGPL_EXCEPTIONS.txt, LICENSE.GPL3, respectively, for exception details
License: LGPLv2 with exceptions or GPLv3 with exceptions
Url:     http://www.qt.io
%global majmin %(echo %{version} | cut -d. -f1-2)
Source0: https://download.qt.io/official_releases/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-opensource-src-%{version}.tar.xz

## upstreamable patches
# workaround FTBFS against kernel-header-5.2.0+
Patch100: qtserialbus-everywhere-src-5.12.3-SIOCGSTAMP.patch

BuildRequires: make
BuildRequires: qt5-qtbase-devel >= %{version}
BuildRequires: qt5-qtbase-private-devel
#libQt5Core.so.5(Qt_5_PRIVATE_API)(64bit)
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
BuildRequires: qt5-qtserialport-devel >= %{version}

%description
Qt Serial Bus (API) provides classes and functions to access the various
industrial serial buses and protocols, such as CAN, ModBus, and others.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt5-qtbase-devel%{?_isa}
%description devel
%{summary}.

%package examples
Summary: Programming examples for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description examples
%{summary}.

%if 0%{?build_tests}
%package tests
Summary: Unit tests for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description tests
%{summary}.
%endif

%prep
%autosetup -n %{qt_module}-everywhere-src-%{version} -p1


%build
%{qmake_qt5} \
  %{?_qt5_examplesdir:CONFIG+=qt_example_installs}

%make_build

%if 0%{?build_tests}
%qt5_build_tests
%endif

%install
make install INSTALL_ROOT=%{buildroot}

%if 0%{?build_tests}
%qt5_install_tests
%endif

%ldconfig_scriptlets

%files
%license LICENSE.*
%{_qt5_libdir}/libQt5SerialBus.so.5*
%{_qt5_bindir}/canbusutil
%{_qt5_plugindir}/canbus

%files devel
%{_qt5_headerdir}/QtSerialBus/
%{_qt5_libdir}/libQt5SerialBus.so
%{_qt5_libdir}/libQt5SerialBus.prl
%dir %{_qt5_libdir}/cmake/Qt5SerialBus/
%{_qt5_libdir}/cmake/Qt5SerialBus
%{_qt5_libdir}/pkgconfig/Qt5SerialBus.pc
%{_qt5_archdatadir}/mkspecs/modules/*
%exclude %{_qt5_libdir}/libQt5SerialBus.la

# no examples, yet
%if 0%{?_qt5_examplesdir:1}
%files examples
%{_qt5_examplesdir}/
%endif

%if 0%{?build_tests}
%files tests
%{_qt5_libdir}/qt5/tests
%endif

%changelog
* Mon Mar 28 2022 Jan Grulich <jgrulich@redhat.com> - 5.15.3-1
- 5.15.3
  Resolves: bz#2061367

* Fri Dec 17 2021 Jan Grulich <jgrulich@redhat.com> - 5.15.2-8
- Rebuild to include -devel subpkg in AppStream
  Resolves: bz#2028567

* Tue Aug 10 2021 Mohan Boddu <mboddu@redhat.com> - 5.15.2-7
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Sat Jun 19 2021 Jan Grulich <jgrulich@redhat.com> - 5.15.2-6
- Properly build unit tests
  Resolves: bz#1968472

* Wed Jun 09 2021 Jan Grulich <jgrulich@redhat.com> - 5.15.2-5
- Add gating tests
  Resolves: bz#1968472

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 5.15.2-4
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 24 07:54:15 CET 2020 Jan Grulich <jgrulich@redhat.com> - 5.15.2-2
- Rebuild for qtbase with -no-reduce-relocations option

* Fri Nov 20 09:30:47 CET 2020 Jan Grulich <jgrulich@redhat.com> - 5.15.2-1
- 5.15.2

* Thu Sep 10 2020 Jan Grulich <jgrulich@redhat.com> - 5.15.1-1
- 5.15.1

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.14.2-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.14.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Apr 04 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.14.2-1
- 5.14.2

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.13.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 09 2019 Jan Grulich <jgrulich@redhat.com> - 5.13.2-1
- 5.13.2

* Tue Sep 24 2019 Jan Grulich <jgrulich@redhat.com> - 5.12.5-1
- 5.12.5

* Sat Aug 17 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.12.4-3
- update %%summary %%description (#1667670)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.12.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 14 2019 Jan Grulich <jgrulich@redhat.com> - 5.12.4-1
- 5.12.4

* Tue Jun 04 2019 Jan Grulich <jgrulich@redhat.com> - 5.12.3-1
- 5.12.3

* Fri Feb 15 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.12.1-1
- 5.12.1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.11.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 07 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.11.3-1
- 5.11.3

* Fri Sep 21 2018 Jan Grulich <jgrulich@redhat.com> - 5.11.2-1
- 5.11.2

* Sun Jul 15 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.11.1-3
- use %%{_qt5_archdatadir}/mkspecs/

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.11.1-1
- 5.11.1

* Sun May 27 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.11.0-1
- 5.11.0
- use %%make_build %%ldconfig_scriptlets

* Wed Feb 14 2018 Jan Grulich <jgrulich@redhat.com> - 5.10.1-1
- 5.10.1

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 03 2018 Rex Dieter <rdieter@fedoraproject.org> 5.10.0-1
- 5.10.0

* Thu Nov 23 2017 Jan Grulich <jgrulich@redhat.com> - 5.9.3-1
- 5.9.3

* Tue Oct 17 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.9.2-2
- BR: qt5-qtbase-private-devel, cosmetics

* Mon Oct 09 2017 Jan Grulich <jgrulich@redhat.com> - 5.9.2-1
- 5.9.2

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 31 2017 Helio Chissini de Castro <helio@kde.org> - 5.9.0-1
- Upstream official release

* Fri May 26 2017 Helio Chissini de Castro <helio@kde.org> - 5.9.0-0.1.rc
- Upstream Release Candidate retagged

* Wed May 24 2017 Helio Chissini de Castro <helio@kde.org> - 5.9.0-0.rc.1
- Upstream Release Candidate 1

* Fri May 05 2017 Helio Chissini de Castro <helio@kde.org> - 5.9.0-0.beta.3
- New upstream beta3 release

* Sun Apr 16 2017 Helio Chissini de Castro <helio@kde.org> - 5.9.0-0.beta.1
- New upstream beta release

* Wed Feb 01 2017 Helio Chissini de Castro <helio@kde.org> - 5.8.0-1
- New upstream version

* Sat Dec 17 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.7.1-2
- updated sources, drop pkgconfig-style deps (for now)

* Thu Nov 10 2016 Helio Chissini de Castro <helio@kde.org> - 5.7.1-1
- New upstream version

* Tue Jul 05 2016 Helio Chissini de Castro <helio@kde.org> - 5.7.0-1
- New Qt 5.7.0 package
