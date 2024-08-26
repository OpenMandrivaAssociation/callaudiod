%define major 0
%define libname %mklibname %{name}
%define develname %mklibname -d %{name}

Name:       callaudiod
Version:    0.1.10
Release:    1
Summary:    Daemon for dealing with audio routing during phone calls

License:        GPLv3+
URL:            https://gitlab.com/mobian1/callaudiod
Source0:        https://gitlab.com/mobian1/callaudiod/-/archive/%{version}/%{name}-%{version}.tar.bz2

BuildRequires:  meson

BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)

Requires: %{libname}%{?_isa} = %{version}-%{release}


%description
callaudiod is a daemon for dealing with audio routing during phone calls.
It provides a D-Bus interface allowing other programs to:

switch audio profiles
output audio to the speaker or back to its original port
mute the microphone

%package -n %{libname}
Summary: Library for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n %{libname}
The lib%{name} package contains libraries for %{name}

%package -n %{develname}
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{libname}%{?_isa} = %{version}-%{release}

%description -n %{develname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1
%meson

%build
%meson_build

%install
%meson_install

%files
%{_bindir}/%{name}
%{_bindir}/callaudiocli
%{_datadir}/dbus-1/interfaces/org.mobian_project.CallAudio.xml
%{_datadir}/dbus-1/services/org.mobian_project.CallAudio.service

%files -n %{libname}
%{_libdir}/libcallaudio-0.1.so.%{major}

%files -n %{develname}
%{_includedir}/libcallaudio-0.1
%{_libdir}/libcallaudio-0.1.so
%{_libdir}/pkgconfig/libcallaudio-0.1.pc
%doc README.md
%license COPYING
