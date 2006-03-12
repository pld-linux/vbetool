Summary:	vbetool - run real-mode video BIOS code to alter hardware state
Summary(pl):	vbetool - modyfikacja trybu karty graficznej za pomoc± jej BIOS-u
Name:		vbetool
Version:	0.5
Release:	1
License:	GPL
Group:		Applications
Source0:	http://www.srcf.ucam.org/~mjg59/vbetool/%{name}_%{version}-1.tar.gz
# Source0-md5:	950a87f99d17bc4f4ced73cec7103859
Patch0:		%{name}-Makefile.patch
Patch1:		%{name}-opt.patch
URL:		http://freshmeat.net/projects/vbetool/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pciutils-devel
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
vbetool uses lrmi in order to run code from the video BIOS. Currently,
it is able to alter DPMS states, save/restore video card state, and
attempt to initialize the video card from scratch. It exists primarily
in order to increase the chances of successfully recovering video
state after an ACPI S3 suspend.

%description -l pl
vbetool u¿ywa lrmi do uruchamiania kodu BIOS-u karty graficznej.
Aktualnie potrafi zmieniaæ stany DPMS, zapisywaæ/odtwarzaæ stan karty
graficznej oraz próbowaæ zainicjowaæ kartê od zera. S³u¿y g³ównie
zwiêkszeniu szans w³a¶ciwego odtworzenia stanu grafiki po u¶pieniu
przez ACPI S3.

%prep
%setup -q -n %{name}-0.4
%patch0 -p1
%patch1 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
%ifnarch %{ix86}
	--with-x86emu
%endif

%{__make} \
	CC="%{__cc}" \
	OPT="%{rpmcflags}"

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
