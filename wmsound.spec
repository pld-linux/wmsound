# %define snddevice /dev/dsp
Summary:	Window Maker sound server
Summary(fr):	Serveur de son de Window Maker
Summary(no):	Window Maker lydtjener
Summary(pl):	Serwer d¼wiêku dla WindowMaker'a
Name:		wmsound
Version:	0.9.4
Release:	3
License:	GPL
Group:		X11/Window Managers/Tools
Group(de):	X11/Fenstermanager/Werkzeuge
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Source0:	ftp://shadowmere.student.utwente.nl/pub/WindowMaker/%{name}-%{version}.tar.gz
Source1:	wmsdefault.tar.gz
Source2:	%{name}-soundset
Patch0:		%{name}-config.patch
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
Wmsound er en lydtjener for Window Maker, som for øyeblikket støtter 8
og 16 bit .wav filer.

%description -l pl
Wmsound jest serwerem d¼wiêku dla WindowMaker'a. Aktualnie obs³uguje
pliki .wav w formacie 8 i 16 bitowym.

%package data
Summary:	Wmsound data
Summary(fr):	Données de Wmsound
Summary(no):	Data til Wmsound
Summary(pl):	Pliki z danymi dla Wmsound
Group:		X11/Window Managers/Tools
Group(de):	X11/Fenstermanager/Werkzeuge
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Requires:	%{name} = %{version}

%description data
The standard Wmsound data.

%description data -l fr
Les données standard de Wmsound.

%description data -l no
Standard datafiler til Wmsound.

%description data -l pl
Pliki z danymi dla Wmsound.

%package devel
Summary:	Wmsound development option
Summary(no):	Utviklings bibliotek for Wmsound
Summary(pl):	Pliki nag³ówkowe dla Wmsounda
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
The Wmsound library and header file

%description devel -l no
Wmsound biblioteket samt «headerfilen»

%description devel -l pl
Pliki nag³ówkowe i biblioteki dla Wmsounda.

%prep
%setup -q
%patch -p1

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
