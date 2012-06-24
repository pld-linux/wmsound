# %define snddevice /dev/dsp
Summary:	Window Maker sound server
Summary(fr):	Serveur de son de Window Maker
Summary(no):	Window Maker lydtjener
Summary(pl):	Serwer d�wi�ku dla WindowMaker'a
Summary(pt_BR):	Servidor de som do Window Maker
Summary(es):	Serveur de son de WindowMaker
Name:		wmsound
Version:	0.9.4
Release:	4
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	ftp://shadowmere.student.utwente.nl/pub/WindowMaker/%{name}-%{version}.tar.gz
Source1:	wmsdefault.tar.gz
Source2:	%{name}-soundset
Patch0:		%{name}-config.patch
Patch1:		%{name}-ComplexProgramTargetNoMan.patch
# not active
URL:		http://www.frontiernet.net/~southgat/wmsound/
BuildRequires:	libPropList-devel >= 0.8.3
BuildRequires:	XFree86-devel
Requires:	WindowMaker
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_prefix		/usr/X11R6

%description
Wmsound is the sound server for Window Maker, it currently supports 8
or 16 bit .wav files.

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

%description -l es
wmsound es el servidor de sonido para Window Maker, actualmente
soporta archivos .wav de 8 � 16 bits.

%package data
Summary:	Wmsound data
Summary(fr):	Donn�es de Wmsound
Summary(no):	Data til Wmsound
Summary(pl):	Pliki z danymi dla Wmsound
Group:		X11/Window Managers/Tools
Requires:	%{name} = %{version}

%description data
The standard Wmsound data.

%description data -l fr
Les donn�es standard de Wmsound.

%description data -l no
Standard datafiler til Wmsound.

%description data -l pl
Pliki z danymi dla Wmsound.

%description data -l pt_BR
Os dados padr�o para o wmsound.

%description data -l es
Los datos predeterminados para wmsound.

%package devel
Summary:	Wmsound development option
Summary(no):	Utviklings bibliotek for Wmsound
Summary(pl):	Pliki nag��wkowe dla Wmsounda
Group:		X11/Development/Libraries
Requires:	X11/%{name} = %{version}

%description devel
The Wmsound library and header file

%description devel -l no
Wmsound biblioteket samt �headerfilen�

%description devel -l pl
Pliki nag��wkowe i biblioteki dla Wmsounda.

%description devel -l pt_BR
Bibliotecas para construir aplica��es com wmsound.

%description devel -l es
Bibliotecas y archivos de inclusi�n, para que puedas desarrollar
aplicaciones que usen el servidor de sonido wmsound.

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

gzip -9nf AUTHORS COPYING ChangeLog NEWS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_bindir}/nmaker
%attr(755,root,root) %{_bindir}/getsounds
%attr(755,root,root) %{_bindir}/setsounds

%files data
%defattr(644,root,root,755)
%dir %{_datadir}/WindowMaker/Sounds
%dir %{_datadir}/WindowMaker/SoundSets
%{_datadir}/WindowMaker/Sounds/*.wav
%config %verify(not size mtime md5) %{_datadir}/WindowMaker/SoundSets/Default
%config %verify(not size mtime md5) %{_datadir}/WindowMaker/Defaults/WMSound

%files devel
%defattr(644,root,root,755)
%{_includedir}/*.h
%{_libdir}/*.a
