# %define snddevice /dev/dsp
Summary:	Window Maker sound server
Summary(fr):	Serveur de son de Window Maker
Summary(nb):	Window Maker lydtjener
Summary(pl):	Serwer d¼wiêku dla WindowMakera
Summary(pt_BR):	Servidor de som do Window Maker
Name:		wmsound
Version:	0.9.5
Release:	3
License:	GPL v2+
Group:		X11/Window Managers/Tools
Source0:	ftp://shadowmere.student.utwente.nl/pub/WindowMaker/%{name}-%{version}.tar.gz
# Source0-md5:	86f9b19ca0ca1daa072d76d02943dd3e
Source1:	wmsdefault.tar.gz
# Source1-md5:	bec32117f9c7ef1f056e96bc8fefae9a
Source2:	%{name}-soundset
Patch0:		%{name}-config.patch
Patch1:		%{name}-ComplexProgramTargetNoMan.patch
Patch2:		%{name}-esd.patch
# not active
URL:		http://www.frontiernet.net/~southgat/wmsound/
BuildRequires:	XFree86-devel
BuildRequires:	libPropList-devel >= 0.8.3
BuildRequires:	esound-devel
Requires:	WindowMaker
Requires:	esound
Provides:	wmsoundserver
Obsoletes:	wmsoundserver
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/X11

%description
Wmsound is the sound server for Window Maker, it currently supports 8
or 16 bit .WAV files.

%description -l es
wmsound es el servidor de sonido para Window Maker, actualmente
soporta archivos .WAV de 8 ó 16 bits.

%description -l fr
Wmsound est le serveur de son pour Window Maker, il supporte
actuellement les fichiers son .WAV 8 ou 16 bit.

%description -l nb
Wmsound er en lydtjener for Window Maker, som for øyeblikket støtter 8
og 16 bit .WAV filer.

%description -l pl
Wmsound jest serwerem d¼wiêku dla WindowMaker'a. Aktualnie obs³uguje
pliki .WAV w formacie 8 i 16 bitowym.

%description -l pt_BR
O wmsound é o servidor de som para o Window Maker, atualmente suporta
arquivos .WAV de 8 ou 16 bits.

%package data
Summary:	Wmsound data
Summary(fr):	Données de Wmsound
Summary(nb):	Data til Wmsound
Summary(pl):	Pliki z danymi dla Wmsound
Group:		X11/Window Managers/Tools
Requires:	wmsoundserver
Obsoletes:	WSoundServer-data

%description data
The standard Wmsound data.

%description data -l es
Los datos predeterminados para wmsound.

%description data -l fr
Les données standard de Wmsound.

%description data -l nb
Standard datafiler til Wmsound.

%description data -l pl
Pliki z danymi dla Wmsound.

%description data -l pt_BR
Os dados padrão para o wmsound.

%package devel
Summary:	Wmsound development option
Summary(nb):	Utviklings bibliotek for Wmsound
Summary(pl):	Pliki nag³ówkowe dla Wmsounda
Group:		X11/Development/Libraries

%description devel
The Wmsound library and header file

%description devel -l es
Bibliotecas y archivos de inclusión, para que puedas desarrollar
aplicaciones que usen el servidor de sonido wmsound.

%description devel -l nb
Wmsound biblioteket samt «headerfilen»

%description devel -l pl
Pliki nag³ówkowe i biblioteki dla Wmsounda.

%description devel -l pt_BR
Bibliotecas para construir aplicações com wmsound.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p0

sed -i -e "s#LIB_INST\ =.*#LIB_INST = /%{_lib}#" lib/Imakefile
mkdir config
cd config
tar xzf %{SOURCE1}

%build
xmkmf -a

%{__make} all \
	CDEBUGFLAGS="%{rpmcflags} -ffast-math" \
	CXXDEBUGFLAGS="%{rpmcflags} -ffast-math" \
	PREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/WindowMaker/{Sounds,SoundSets} \
	$RPM_BUILD_ROOT%{_sysconfdir}/WindowMaker

./Install
%{__make} install DESTDIR=$RPM_BUILD_ROOT%{_prefix}

install config/WMSound $RPM_BUILD_ROOT%{_sysconfdir}/WindowMaker
install %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/WindowMaker/SoundSets/Default
install config/Sounds/*.wav $RPM_BUILD_ROOT%{_datadir}/WindowMaker/Sounds

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_bindir}/nmaker
%attr(755,root,root) %{_bindir}/getsounds
%attr(755,root,root) %{_bindir}/setsounds
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/WindowMaker/WMSound

%files data
%defattr(644,root,root,755)
%{_datadir}/WindowMaker/Sounds/*.wav
%config(noreplace) %verify(not size mtime md5) %{_datadir}/WindowMaker/SoundSets/Default

%files devel
%defattr(644,root,root,755)
%{_includedir}/*.h
%{_libdir}/*.a
