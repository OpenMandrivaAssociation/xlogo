Name:		xlogo
Version:	1.0.4
Release:	1
Summary:	X Window System logo
Group:		Development/X11
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT

BuildRequires: libxext-devel >= 1.0.0
BuildRequires: libxt-devel >= 1.0.0
BuildRequires: libxaw-devel >= 1.0.1
BuildRequires: libxprintutil-devel >= 1.0.1
BuildRequires: libxrender-devel >= 0.9.0.2
BuildRequires: x11-util-macros >= 1.0.1
BuildRequires: pkgconfig(xft) >= 2.1.8.2

%description
The xlogo program displays the X Window System logo.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%{_bindir}/xlogo
%{_datadir}/X11/app-defaults/XLogo-color
%{_datadir}/X11/app-defaults/XLogo
%{_mandir}/man1/xlogo.1*
