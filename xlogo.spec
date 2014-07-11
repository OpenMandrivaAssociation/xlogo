Name:		xlogo
Version:	1.0.4
Release:	7
Summary:	X Window System logo
Group:		Development/X11
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT

BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xt)
BuildRequires: pkgconfig(xaw7)
BuildRequires: pkgconfig(xrender) >= 0.9.0.2
BuildRequires: pkgconfig(xorg-macros) >= 1.0.1
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


%changelog
* Mon Mar 26 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.0.4-1
+ Revision: 786812
- version update 10.4

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-2
+ Revision: 671336
- mass rebuild

* Tue Nov 02 2010 Thierry Vignaud <tv@mandriva.org> 1.0.3-1mdv2011.0
+ Revision: 591907
- new release

* Fri Dec 11 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0.2-1mdv2010.1
+ Revision: 476551
- New version: 1.0.2
  Applied patch removed

* Mon Apr 13 2009 Funda Wang <fwang@mandriva.org> 1.0.1-9mdv2009.1
+ Revision: 366691
- fix str fmt

  + Antoine Ginies <aginies@mandriva.com>
    - rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.0.1-8mdv2009.0
+ Revision: 226053
- rebuild

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Revert to use upstream tarball, build requires and remove non mandatory local patches.

* Thu Jan 17 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.1-7mdv2008.1
+ Revision: 154443
- Updated BuildRequires and resubmit package.
- Choose default Xaw from xaw.m4 unless configure explicitly told otherwise.

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Aug 31 2007 Adam Williamson <awilliamson@mandriva.org> 1.0.1-6mdv2008.0
+ Revision: 76539
- rebuild for 2008
- slight spec clean

  + Thierry Vignaud <tv@mandriva.org>
    - do not hardcode lzma extension!!!

