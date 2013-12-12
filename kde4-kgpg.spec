#
%define		_state		stable
%define		orgname		kgpg
%define		qtver		4.8.3
%define		kdeworkspacever	4.11.0

Summary:	K Desktop Environment - interface for GnuPG
Name:		kde4-kgpg
Version:	4.12.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	a9ef6a85892a5305072b761c911e68c0
URL:		http://www.kde.org/
BuildRequires:	kde4-kdebase-devel >= %{version}
Requires:	kde4-kdebase-workspace >= %{kdeworkspacever}
Obsoletes:	kde4-kdeutils-kgpg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
kgpg is a simple, free, open source KDE frontend for gpg. It features
- editor mode enables you to type/paste a text and
  encrypt/decrypt/sign/verify it
- key manager: import, export, delete, sign, generate and edit keys.
- integration with konqueror: left click on a file to decrypt/verify
  it, right click on a file to encrypt/sign it.
- encryption: support for symetric encryption. Multiple keys & default
  key encryption. Optional shredding of source files
- signatures: creation & verification of detached & cleartext
  signatures
- drag & drop encryption + clipboard en/decryption

%description -l pl.UTF-8
kgpg jest prostą, darmową, z otwartymi źródłami, graficzną nakładką na
gpg przeznaczoną dla KDE. Ma następujące możliwości:
- tryb edytora umożliwiający napisanie/wklejenie tekstu oraz
  zaszyfrowanie/odszyfrowanie/podpisanie/sprawdzenie go,
- zarządzanie kluczami: import, eksport, usuwanie, podpisywanie,
  generowanie oraz edycję,
- integrację z Konquerorem: kliknięcie lewym przyciskiem na pliku w
  celu odszyfrowania/sprawdzenia go, kliknięcie prawym przyciskiem na
  pliku w celu zaszyfrowania/podpisania go,
- szyfrowanie: obsługa szyfrów symetrycznych; wiele kluczy i domyślne
  szyfrowanie kluczem; opcjonalnie niszczenie plików źródłowych,
- sygnatury: tworzenie i sprawdzanie oddzielonych i czysto tekstowych
  sygnatur,
- szyfrowanie metodą przeciągnij-i-upuść oraz szyfrowanie i
  odszyfrowywanie schowka.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%find_lang %{orgname} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{orgname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kgpg
%{_desktopdir}/kde4/kgpg.desktop
%{_datadir}/apps/kgpg
%{_datadir}/autostart/kgpg.desktop
%{_datadir}/config.kcfg/kgpg.kcfg
%{_datadir}/dbus-1/interfaces/org.kde.kgpg.Key.xml
%{_iconsdir}/hicolor/*/apps/kgpg.png
%{_datadir}/kde4/services/ServiceMenus/encryptfile.desktop
%{_datadir}/kde4/services/ServiceMenus/encryptfolder.desktop
%{_datadir}/kde4/services/ServiceMenus/viewdecrypted.desktop
