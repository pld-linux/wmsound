# %define snddevice /dev/dsp
Summary:	Window Maker sound server
Summary(fr):	Serveur de son de Window Maker
Summary(no):	Window Maker lydtjener
Summary(pl):	Serwer d�wi�ku dla WindowMakera
Summary(pt_BR):	Servidor de som do Window Maker
Name:		wmsound
Version:	0.9.5
Release:	1
License:	GPL v2+
Group:		X11/Window Managers/Tools
Source0:	ftp://shadowmere.student.utwente.nl/pub/WindowMaker/%{name}-%{version}.tar.gz
# Source0-md5:	86f9b19ca0ca1daa072d76d02943dd3e
Source1:	wmsdefault.tar.gz
# Source1-md5:	bec32117f9c7ef1f056e96bc8fefae9a
Source2:	%{name}-soundset
Patch0:		%{name}-config.patch
Patch1:		%{name}-ComplexProgramTargetNoMan.patch
# not active
URL:		http://www.frontiernet.net/~southgat/wmsound/
BuildRequires:	XFree86-devel
BuildRequires:	libPropList-devel >= 0.8.3
Requires:	WindowMaker
Provides:	wmsoundserver
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_prefix		/usr/X11R6

%description
Wmsound is the sound server for Window Maker, it currently supports 8
or 16 bit .wav files.

%description -l es
wmsound es el servidor de sonido para Window Maker, actualmente
soporta archivos .wav de 8 � 16 bits.

%description -l fr
Wmsound est le serveur de son pour Window Maker, il supporte
actuellement les fichiers son .wav 8 ou 16 bit.

%description -l no
Wmsound er en lydtjener for Window Maker, som for �yeblikket st�tter 8
og 16 bit .wav filer.

%description -l pl
Wmsound jest serwerem d�wi�ku dla WindowMaker'a. Aktualnie obs�uguje
pliki .wav w formacie 8 i 16 bitowym.

%description -l pt_BR
O wmsound � o servidor de som para o Window Maker, atualmente suporta
arquivos .wav de 8 ou 16 bits.

%package data
Summary:	Wmsound data
Summary(fr):	Donn�es de Wmsound
Summary(no):	Data til Wmsound
Summary(pl):	Pliki z danymi dla Wmsound
Group:		X11/Window Managers/Tools
Requires:	wmsoundserver
Obsoletes:	WSoundServer-data

%description data
The standard Wmsound data.

%description data -l es
Los datos predeterminados para wmsound.

%description data -l fr
Les donn�es standard de Wmsound.

%description data -l no
Standard datafiler til Wmsound.

%description data -l pl
Pliki z danymi dla Wmsound.

%description data -l pt_BR
Os dados padr�o para o wmsound.

%package devel
Summary:	Wmsound development option
Summary(no):	Utviklings bibliotek for Wmsound
Summary(pl):	Pliki nag��wkowe dla Wmsounda
Group:		X11/Development/Libraries

%description devel
The Wmsound library and header file

%description devel -l es
Bibliotecas y archivos de inclusi�n, para que puedas desarrollar
aplicaciones que usen el servidor de sonido wmsound.

%description devel -l no
Wmsound biblioteket samt �headerfilen�

%description devel -l pl
Pliki nag��wkowe i biblioteki dla Wmsounda.

%description devel -l pt_BR
Bibliotecas para construir aplica��es com wmsound.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

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
install -d $RPM_BUILD_ROOT%{_datadir}/WindowMaker/{Defaults,Sounds,SoundSets}

./Install
%{__make} install DESTDIR=$RPM_BUILD_ROOT%{_prefix}

install config/WMSound $RPM_BUILD_ROOT%{_datadir}/WindowMaker/Defaults
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
%config(noreplace) %verify(not size mtime md5) %{_datadir}/WindowMaker/Defaults/WMSound

%files data
%defattr(644,root,root,755)
%dir %{_datadir}/WindowMaker/Sounds
%dir %{_datadir}/WindowMaker/SoundSets
%{_datadir}/WindowMaker/Sounds/*.wav
%config(noreplace) %verify(not size mtime md5) %{_datadir}/WindowMaker/SoundSets/Default

%files devel
%defattr(644,root,root,755)
%{_includedir}/*.h
%{_libdir}/*.a