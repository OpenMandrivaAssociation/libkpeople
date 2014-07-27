%define major 3

Summary:	Metacontact aggregation library for KDE
Name:		libkpeople
Version:	0.2.2
Release:	1
Group:		Graphical desktop/KDE
License:	LGPLv2.1+
Url:		https://projects.kde.org/projects/playground/network/libkpeople
Source0:	ftp://ftp.kde.org/pub/kde/unstable/%{name}/%{version}/src/%{name}-%{version}.tar.bz2
BuildRequires:	kdelibs4-devel
BuildRequires:	kdepimlibs4-devel

%description
A library that provides access to all contacts and the people who hold them.

#----------------------------------------------------------------------------

%package core
Summary:	Commons files used by %{name}
Group:		Graphical desktop/KDE

%description core
Commons files used by %{name}

%files  core -f %{name}.lang
%{_kde_appsdir}/kpeople/dummy_avatar.png
%{_kde_libdir}/kde4/akonadi_kpeople_plugin.so
%{_kde_services}/akonadi_kpeople_plugin.desktop
%{_kde_servicetypes}/kpeople_data_source.desktop
%{_kde_servicetypes}/kpeople_plugin.desktop
%{_kde_servicetypes}/persondetailsplugin.desktop

#----------------------------------------------------------------------------

%define libkpeople %mklibname kpeople %{major}

%package -n %{libkpeople}
Summary:	Runtime library for %{name}
Group:		System/Libraries

%description -n %{libkpeople}
Runtime library for %{name}.

%files -n %{libkpeople}
%{_kde_libdir}/libkpeople.so.0*
%{_kde_libdir}/libkpeople.so.%{major}

#----------------------------------------------------------------------------

%define libkpeoplewidgets %mklibname kpeoplewidgets %{major}

%package -n %{libkpeoplewidgets}
Summary:	Runtime library for %{name}
Group:		System/Libraries

%description -n %{libkpeoplewidgets}
Runtime library for %{name}.

%files -n %{libkpeoplewidgets}
%{_kde_libdir}/libkpeoplewidgets.so.0*
%{_kde_libdir}/libkpeoplewidgets.so.%{major}

#----------------------------------------------------------------------------

%define devname %mklibname kpeople -d

%package -n %{devname}
Summary:	Headers files for %{name}
Group:		Development/KDE and Qt
Provides:	%{name}-devel = %{EVRD}
Provides:	kpeople-devel = %{EVRD}
Requires:	%{libkpeople} = %{EVRD}
Requires:	%{libkpeoplewidgets} = %{EVRD}

%description -n %{devname}
Headers files for %{name}.

%files -n %{devname}
%{_kde_includedir}/KPeople/
%{_kde_includedir}/kpeople/
%{_kde_libdir}/cmake/KPeople/*.cmake
%{_kde_libdir}/libkpeople.so
%{_kde_libdir}/libkpeoplewidgets.so

#----------------------------------------------------------------------------

%prep
%setup -q
%apply_patches

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%find_lang %{name}
