Summary:	vbetool - run real-mode video BIOS code to alter hardware state
Summary(pl):	vbetool - modyfikacja trybu karty video za pomoc± jej BIOS-u
Name:		vbetool
Version:	0.4
Release:	1
License:	GPL
Group:		Applications
Source0:	http://www.srcf.ucam.org/~mjg59/vbetool/%{name}_%{version}-1.tar.gz
# Source0-md5:	f8b52980603f458c125026fd9c97b7b0
Patch0:		%{name}-Makefile.patch
URL:		http://freshmeat.net/projects/vbetool/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pciutils-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
vbetool uses lrmi in order to run code from the video BIOS. Currently,
it is able to alter DPMS states, save/restore video card state, and 
attempt to initialize the video card from scratch. It exists primarily
in order to increase the chances of successfully recovering video 
state after an ACPI S3 suspend.

%description -l pl
vbetool s³u¿y do modyfikacji trybu karty graficznej za pomoc± 
BIOS-u karty video.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make} \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man1/*
