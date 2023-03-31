Name:		xlogo
Version:	1.0.6
Release:	2
Summary:	X Window System logo
Group:		Development/X11
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz
License:	MIT
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xt)
BuildRequires:	pkgconfig(xaw7)
BuildRequires:	pkgconfig(xrender) >= 0.9.0.2
BuildRequires:	pkgconfig(xorg-macros) >= 1.0.1
BuildRequires:	pkgconfig(xft) >= 2.1.8.2

%description
The xlogo program displays the X Window System logo.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%files
%{_bindir}/xlogo
%{_datadir}/X11/app-defaults/XLogo-color
%{_datadir}/X11/app-defaults/XLogo
%doc %{_mandir}/man1/xlogo.1*
