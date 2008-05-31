Summary:	vbetool - run real-mode video BIOS code to alter hardware state
Summary(pl.UTF-8):	vbetool - modyfikacja trybu karty graficznej za pomocą jej BIOS-u
Name:		vbetool
Version:	1.1
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://www.codon.org.uk/~mjg59/vbetool/download/%{name}-%{version}.tar.gz
# Source0-md5:	ffb03b118867a02296d7449019ad8846
URL:		http://www.codon.org.uk/~mjg59/vbetool/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libx86-devel
BuildRequires:	pciutils-devel >= 3.0.0
BuildRequires:	pkgconfig
BuildRequires:	zlib-devel
# it's supposed to be arch independant; see libx86.spec
ExclusiveArch: %{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
vbetool uses lrmi in order to run code from the video BIOS. Currently,
it is able to alter DPMS states, save/restore video card state, and
attempt to initialize the video card from scratch. It exists primarily
in order to increase the chances of successfully recovering video
state after an ACPI S3 suspend.

%description -l pl.UTF-8
vbetool używa lrmi do uruchamiania kodu BIOS-u karty graficznej.
Aktualnie potrafi zmieniać stany DPMS, zapisywać/odtwarzać stan karty
graficznej oraz próbować zainicjować kartę od zera. Służy głównie
zwiększeniu szans właściwego odtworzenia stanu grafiki po uśpieniu
przez ACPI S3.

%prep
%setup -q

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
	OPT="%{rpmcflags}" \
	vbetool_DEPENDENCIES= \
	vbetool_LDADD=$(pkg-config --libs libpci)

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	vbetool_DEPENDENCIES=

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/vbetool
%{_mandir}/man1/vbetool.1*
