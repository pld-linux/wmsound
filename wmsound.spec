# %define snddevice /dev/dsp
Summary: 	Window Maker sound server
Summary(fr):	Serveur de son de Window Maker
Summary(no):	Window Maker lydtjener.
Summary(pl):	Serwer d�wi�ku dla WindowMaker'a
Name:		wmsound
Version:	0.9.4
Release:	1
Copyright:	GPL
Group:		X11/Window Managers/Tools
Group(pl):	X11/Zarz�dcy Okien/Narz�dzia
Source0:	http://www.frontiernet.net/~southgat/wmsound/download/%{name}-%{version}.tar.gz
Source1:	wmsdefault.tar.gz
Source2:	wmsound-soundset
Patch:      	wmsound-config.patch
Requires:   	WindowMaker
Requires:   	libjpeg
Requires:   	libpng
Buildroot:  	/tmp/%{name}-%{version}-root

%description
Wmsound is the sound server for Window Maker, it currently supports 8 or 16
bit .wav files.

%description -l fr
Wmsound est le serveur de son pour Window Maker, il supporte actuellement
les fichiers son .wav 8 ou 16 bit.

%description -l no
Wmsound er en lydtjener for Window Maker, som for �yeblikket st�tter 8 og 16
bit .wav filer.

%description -l pl
Wmsound jest serwerem d�wi�ku dla WindowMaker'a. Aktualnie obs�uguje
pliki .wav w formacie 8 i 16 bit.

%package data
Summary:	Wmsound data
Summary(fr):	Donn�es de Wmsound
Summary(no):	Data til Wmsound
Summary(pl):	Pliki z danymi dla Wmsound
Group:		X11/Window Managers/Tools
Group(pl):	X11/Zarz�dcy Okien/Narz�dzia
Requires:	%{name} = %{version}

%description data
The standard Wmsound data.

%description data -l fr
Les donn�es standard de Wmsound.

%description data -l no
Standard datafiler til Wmsound.

%description data -l pl
Pliki z danymi dla Wmsound.

%package devel
Summary:	Wmsound development option
Summary(no):	Utviklings bibliotek for Wmsound
Summary(pl):	Pliki nag��wkowe dla Wmsound'a.
Group:		X11/Development/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
The Wmsound library and header file

%description devel -l no
Wmsound biblioteket samt �headerfilen�

%description devel -l pl
Pliki nag��wkowe i biblioteki dla Wmsound'a.

%prep
%setup -q
%patch -p1

mkdir config
cd config
tar xzf $RPM_SOURCE_DIR/wmsdefault.tar.gz

%build
xmkmf -a

make all CDEBUGFLAGS="$RPM_OPT_FLAGS" \
	CXXDEBUGFLAGS="$RPM_OPT_FLAGS" \
	PREFIX=/usr/X11R6

%install
rm -rf $RPM_BUILD_ROOT

./Install
make install DESTDIR="$RPM_BUILD_ROOT/usr/X11R6"
install -d $RPM_BUILD_ROOT/usr/X11R6/share/WindowMaker/{Defaults,Sounds,SoundSets}
install config/WMSound $RPM_BUILD_ROOT/usr/X11R6/share/WindowMaker/Defaults
install $RPM_SOURCE_DIR/wmsound-soundset \
	$RPM_BUILD_ROOT/usr/X11R6/share/WindowMaker/SoundSets/Default
install config/Sounds/*.wav \
	$RPM_BUILD_ROOT/usr/X11R6/share/WindowMaker/Sounds
#strip $RPM_BUILD_ROOT/usr/X11R6/bin/*


gzip -9nf AUTHORS COPYING ChangeLog NEWS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {AUTHORS,COPYING,ChangeLog,NEWS}.gz 
%doc patches
%attr(755,root,root) /usr/X11R6/bin/wmsound
%attr(755,root,root) /usr/X11R6/bin/nmaker
%attr(755,root,root) /usr/X11R6/bin/getsounds
%attr(755,root,root) /usr/X11R6/bin/setsounds

%files data
%defattr(644,root,root,755)
%dir /usr/X11R6/share/WindowMaker/Sounds
%dir /usr/X11R6/share/WindowMaker/SoundSets
/usr/X11R6/share/WindowMaker/Sounds/*.wav
%config %verify(not size mtime md5) /usr/X11R6/share/WindowMaker/SoundSets/Default
%config %verify(not size mtime md5) /usr/X11R6/share/WindowMaker/Defaults/WMSound

%files devel
%defattr(644,root,root,755)
/usr/X11R6/include/*.h
/usr/X11R6/lib/*.a

%changelog
* Thu Apr  1 1999 Piotr Czerwi�ski <pius@pld.org.pl>
  [0.9.4-1]
- updated to 0.9.4,
- changed BuildRoot to /tmp/%{name}-%{version}-root,
- fixed passing $RPM_OPT_FLAGS,
- fixed configuration files (wmsound-config.patch, wmsound-soundset),
- added gzipping documentation,
- major changes.

* Fri Jan 22 1999 Artur Frysiak <wiget@usa.net>
  [0.9.0-1d]
- added pl translation
- rewrite spec file

* Tue Nov 10 1998 Kjetil Wiekhorst J�rgensen <jorgens+rpm@pvv.org> [0.9.0-1]
- upgraded to version 0.9.0
- minor fixes to specfile

* Sat Oct 24 1998 Kjetil Wiekhorst J�rgensen <jorgens+rpm@pvv.org> [0.8.0-1]
- upgraded to version 0.8.0

* Sun Oct 18 1998 Kjetil Wiekhorst J�rgensen <jorgens@pvv.org>
- upgraded to version 0.7.6b

* Thu Sep 10 1998 Kjetil Wiekhorst J�rgensen <jorgens@pvv.org>
- initial version
