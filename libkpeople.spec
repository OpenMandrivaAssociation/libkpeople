%define major 1
Name: libkpeople
Version: 0.1.0
Release: 7
Summary: Metacontact aggregation library
Group:   System/Libraries
License: LGPLv2
URL:     https://projects.kde.org/projects/playground/network/libkpeople
Source0: http://download.kde.org/unstable/%{name}/%{version}/src/%{name}-%{version}.tar.bz2

BuildRequires: kdelibs4-devel
BuildRequires: pkgconfig(shared-desktop-ontologies)
BuildRequires: nepomuk-core-devel


%description
A library that provides access to all contacts and the people who hold them.

#------------------------------------------------------------------------------
%package core
Summary: Commons files used by %{name}
Group:   Graphical desktop/KDE 

%description core
Commons files used by %{name}

%files  core -f %{name}.lang
%{_kde_libdir}/kde4/email_kpeople_plugin.so
%{_kde_libdir}/kde4/emaildetailswidgetplugin.so
%{_kde_libdir}/kde4/imports/org/kde/people/libkpeopledeclarative.so
%{_kde_libdir}/kde4/imports/org/kde/people/qmldir
%{_kde_libdir}/kde4/mergecontactswidgetplugin.so
%{_kde_libdir}/kde4/phonedetailswidgetplugin.so
%{_kde_appsdir}/kpeople/dummy_avatar.png
%{_kde_services}/email_kpeople_plugin.desktop
%{_kde_services}/emaildetailswidgetplugin.desktop
%{_kde_services}/mergecontactswidgetplugin.desktop
%{_kde_services}/phonedetailswidgetplugin.desktop
%{_kde_servicetypes}/kpeople_data_source.desktop
%{_kde_servicetypes}/kpeople_plugin.desktop
%{_kde_servicetypes}/persondetailsplugin.desktop
#------------------------------------------------------------------------------

%define libkpeople %mklibname kpeople %{major}

%package -n %{libkpeople}
Summary: Runtime library for %{name}
Group: System/Libraries

%description -n %{libkpeople}
Runtime library for %{name}

%files -n %{libkpeople}
%{_kde_libdir}/libkpeople.so.0*
%{_kde_libdir}/libkpeople.so.%{major}

#------------------------------------------------------------------------------

%define libkpeoplewidgets %mklibname kpeoplewidgets %{major}

%package -n %{libkpeoplewidgets}
Summary: Runtime library for %{name}
Group: System/Libraries

%description -n %{libkpeoplewidgets}
Runtime library for %{name}

%files -n %{libkpeoplewidgets}
%{_kde_libdir}/libkpeoplewidgets.so.0*
%{_kde_libdir}/libkpeoplewidgets.so.%{major}

#------------------------------------------------------------------------------

%define devel %mklibname kpeople -d

%package -n %{devel}
Summary: Headers files for %{name}
Group: Development/KDE and Qt 
Provides: %name-devel = %version-%release
Provides: kpeople-devel = %version-%release
Requires: %{libkpeople} = %version-%release
Requires: %{libkpeoplewidgets} = %version-%release

%description -n %{devel}
Headers files for %{name}

%files -n %{devel}
%{_kde_includedir}/KPeople/
%{_kde_includedir}/kpeople/
%{_kde_appsdir}/cmake/modules/FindKPeople.cmake
%{_kde_libdir}/libkpeople.so
%{_kde_libdir}/libkpeoplewidgets.so

#------------------------------------------------------------------------------

%prep
%setup -q
%apply_patches

%build
export LD=/usr/bin/ld.gold
%cmake_kde4
%make

%install
%makeinstall_std -C build
%find_lang %{name}
