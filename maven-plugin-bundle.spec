%global site_name maven-bundle-plugin

Name:           maven-plugin-bundle
Version:        2.3.7
Release:        12%{?dist}
Summary:        Maven Bundle Plugin

Group:          Development/Tools
License:        ASL 2.0
URL:            http://felix.apache.org
Source0:        http://archive.apache.org/dist/felix/%{site_name}-%{version}-source-release.tar.gz

Patch0:         %{site_name}-dependency.patch
Patch1:         %{site_name}-unreported-exception.patch

BuildRequires: aqute-bndlib >= 1.50.0
BuildRequires: plexus-utils >= 1.4.5
BuildRequires: felix-osgi-obr
BuildRequires: kxml
BuildRequires: maven-local
BuildRequires: maven-shared-dependency-tree >= 1.1-3
BuildRequires: maven-wagon >= 1.0-0.2.b2
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-plugin-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin >= 2.3
BuildRequires: maven-surefire-provider-junit4 >= 2.3
BuildRequires: maven-doxia-sitetools
BuildRequires: maven-shared-osgi
BuildRequires: maven-archiver
BuildRequires: maven-plugin-testing-harness
BuildRequires: plexus-archiver
BuildRequires: plexus-containers-container-default
BuildRequires: felix-parent
BuildRequires: felix-bundlerepository

BuildArch: noarch


%description
Provides a maven plugin that supports creating an OSGi bundle
from the contents of the compilation classpath along with its
resources and dependencies. Plus a zillion other features.

%package javadoc
Group:          Documentation
Summary:        Javadoc for %{name}

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{site_name}-%{version}

%patch0 -p1
%patch1 -p1

# remove bundled stuff
#rm -rf src/main/java/org/apache/maven

%mvn_file : %{name}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE DEPENDENCIES

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 2.3.7-12
- Mass rebuild 2013-12-27

* Fri Aug 23 2013 Michal Srb <msrb@redhat.com> - 2.3.7-11
- Migrate away from mvn-rpmbuild (Resolves: #997487)

* Wed Jul 17 2013 Tomas Radej <tradej@redhat.com> - 2.3.7-10
- Updated source address (error 404)

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3.7-9
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Wed Apr 10 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3.7-8
- Add missing BR: maven-plugin-testing-harness

* Mon Mar 11 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3.7-7
- Re-enable tests

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 2.3.7-5
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 21 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.3.7-3
- Add kxml2 to pom as a dependency

* Mon Apr 30 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3.7-2
- Add missing BuildRequires

* Wed Feb 29 2012 Jaromir Capik <jcapik@redhat.com> 2.3.7-1
- Update to 2.3.7

* Thu Jan 19 2012 Jaromir Capik <jcapik@redhat.com> 2.3.6-3
- Bundled maven sources readded (they seem to change the behaviour)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 21 2011 Jaromir Capik <jcapik@redhat.com> 2.3.6-1
- Update to 2.3.6

* Mon Dec 19 2011 Jaromir Capik <jcapik@redhat.com> 2.3.5-3
- Minimal aqute-bndlib VR set to 1.43.0-2 (older ones are broken)

* Mon Nov 14 2011 Jaromir Capik <jcapik@redhat.com> 2.3.5-2
- OBR plugin readded (it's been merged to the bundle plugin)

* Mon Oct 24 2011 Jaromir Capik <jcapik@redhat.com> 2.3.5-1
- Update to 2.3.5

* Tue Oct 17 2011 Jaromir Capik <jcapik@redhat.com> 2.0.0-11
- aqute-bndlib renamed to aqute-bnd

* Fri Jun 17 2011 Alexander Kurtakov <akurtako@redhat.com> 2.0.0-10
- Do not depend on maven2.

* Thu Feb 10 2011 Alexander Kurtakov <akurtako@redhat.com> 2.0.0-9
- BR maven-surefire-provider-junit4.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Alexander Kurtakov <akurtako@redhat.com> 2.0.0-7
- BR/R felix-parent.

* Thu Sep 9 2010 Alexander Kurtakov <akurtako@redhat.com> 2.0.0-5
- Fix BuildRequires.

* Fri Sep 18 2009 Alexander Kurtakov <akurtako@redhat.com> 2.0.0-4
- Add missing Requires.

* Wed Sep 9 2009 Alexander Kurtakov <akurtako@redhat.com> 2.0.0-3
- BR doxia-sitetools.

* Mon Sep 7 2009 Alexander Kurtakov <akurtako@redhat.com> 2.0.0-2
- Fix BR/Rs.

* Thu Sep 3 2009 Alexander Kurtakov <akurtako@redhat.com> 2.0.0-1
- Initial import.
