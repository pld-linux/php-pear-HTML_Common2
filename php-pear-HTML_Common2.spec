%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	Common2
%define		_status		devel
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - Abstract base class for HTML classes (PHP5 port of HTML_Common package)
Summary(pl):	%{_pearname} - Podstawowa klasa dla klas HTML (port pakietu HTML_Common do PHP5)
Name:		php-pear-%{_pearname}
Version:	0.1.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	f6f3df17ae2c7236b8e4d1391d2a24e3
URL:		http://pear.php.net/package/Class_Subclass/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The HTML_Common2 package provides methods for HTML code display and
attributes handling.
- Methods to set, remove, update html attributes.
- Handles comments in HTML code.
- Handles global document options (encoding, linebreak and indentation
  characters).
- Handles indentation for nicer HTML code.

In PEAR status of this package is: %{_status}.

%description -l pl
Pakiet HTML_Common2 zawiera metody do wy�wietlania kodu HTML i obr�bki
atrybut�w.
- Metdody do ustawiania, usuwania i aktualizacji atrybut�w html.
- Obs�uguje komentarze w kodzie HTML.
- Obs�uguje opcje globalne dokumentu (kodowanie, znaki ko�ca linii i
  wci�cia).
- Obs�uguje wci�cia dla �adniejszego wygl�du kodu HTML.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/tests
%{php_pear_dir}/%{_class}/*.php
