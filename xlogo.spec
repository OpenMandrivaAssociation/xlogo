Name:		xlogo
Version:	1.0.1
Release:	%mkrel 7
Summary:	X Window System logo
Group:		Development/X11
Source:		http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT
BuildRoot:	%{_tmppath}/%{name}-root

BuildRequires:	x11-util-macros		>= 1.1.5
BuildRequires:	libxaw-devel		>= 1.0.4
BuildRequires:	libxprintutil-devel	>= 1.0.1
BuildRequires:	libxrender-devel	>= 0.9.4
BuildRequires:	xft2-devel		>= 2.1.12

%description
The xlogo program displays the X Window System logo.

%prep
%setup -q -n %{name}-%{version}

%build
autoreconf -ifs
%configure	--x-includes=%{_includedir} \
		--x-libraries=%{_libdir}

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
