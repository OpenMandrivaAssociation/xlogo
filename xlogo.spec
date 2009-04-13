Name:		xlogo
Version:	1.0.1
Release:	%mkrel 9
Summary:	X Window System logo
Group:		Development/X11
Source:		http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
Patch0:		xlogo-1.0.1-fix-str-fmt.patch
License:	MIT
BuildRoot:	%{_tmppath}/%{name}-root

BuildRequires: libxext-devel >= 1.0.0
BuildRequires: libxt-devel >= 1.0.0
BuildRequires: libxaw-devel >= 1.0.1
BuildRequires: libxprintutil-devel >= 1.0.1
BuildRequires: libxrender-devel >= 0.9.0.2
BuildRequires: x11-util-macros >= 1.0.1
BuildRequires: xft2-devel >= 2.1.8.2

%description
The xlogo program displays the X Window System logo.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p0

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xlogo
%{_datadir}/X11/app-defaults/XLogo-color
%{_datadir}/X11/app-defaults/XLogo
%{_mandir}/man1/xlogo.1*
