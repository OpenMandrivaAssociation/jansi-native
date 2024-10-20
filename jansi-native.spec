%{?_javapackages_macros:%_javapackages_macros}
%global bits 32
%global debug_package %{nil}

%ifarch x86_64 ppc64 s390x sparc64
  %global bits 64
%endif

Name:             jansi-native
Version:          1.5
Release:          8.4
Summary:          Jansi Native implements the JNI Libraries used by the Jansi project
Group:		  Development/Java
License:          ASL 2.0
URL:              https://jansi.fusesource.org/
Source0:          https://github.com/fusesource/jansi-native/archive/jansi-native-1.5.tar.gz

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: maven-local
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-clean-plugin)
BuildRequires: mvn(org.fusesource:fusesource-pom:pom:)
BuildRequires: mvn(org.fusesource.hawtjni:hawtjni-runtime) >= 1.9
BuildRequires: mvn(org.fusesource.hawtjni:maven-hawtjni-plugin) >= 1.9

%description
Jansi is a small java library that allows you to use ANSI escape sequences
in your Java console applications. It implements ANSI support on platforms
which don't support it like Windows and provides graceful degradation for
when output is being sent to output devices which cannot support ANSI
sequences. 

%package javadoc
Summary:          Javadocs for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jansi-native-jansi-native-%{version}
%mvn_package :::linux%{bits}:

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_jnidir}/%{name}
%doc readme.md license.txt changelog.md

%files javadoc -f .mfiles-javadoc
%doc license.txt

%changelog
* Wed Sep 11 2013 Marek Goldmann <mgoldman@redhat.com> - 1.5-1
- Upstream release 1.5

* Tue Aug 06 2013 Marek Goldmann <mgoldman@redhat.com> - 1.4-7
- New guidelines

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.4-4
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Wed Dec 19 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.4-3
- revbump after jnidir change

* Wed Dec 12 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.4-2
- Move normal jar from javajnidir to javadir

* Wed Sep 19 2012 Marek Goldmann <mgoldman@redhat.com> - 1.4-1
- Upstream release 1.4
- Fixing "archiver requires 'AM_PROG_AR' in 'configure.ac'" error
- FTBFS: config.status: error: cannot find input file: `Makefile.in' RHBZ#858377

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct 26 2011 Dan Horák <dan[at]danny.cz> 1.2-2
- fix build on non-x86 64-bit arches

* Thu Jul 28 2011 Marek Goldmann <mgoldman@redhat.com> 1.2-1
- Upstream release 1.2
- Using new jnidir

* Tue May 31 2011 Marek Goldmann <mgoldman@redhat.com> 1.1-2
- Updated summary
- Removed debuginfo package
- Added license to javadoc package
- Fixed dependency on maven-hawtjni-plugin

* Fri May 27 2011 Marek Goldmann <mgoldman@redhat.com> 1.1-1
- Initial packaging

