%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	Common2
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}
%define		subver	RC1
%define		rel		1
Summary:	%{_pearname} - abstract base class for HTML classes (PHP5 port of HTML_Common package)
Summary(pl.UTF-8):	%{_pearname} - podstawowa klasa dla klas HTML (port pakietu HTML_Common dla PHP5)
Name:		php-pear-%{_pearname}
Version:	2.0.0
Release:	0.%{subver}.%{rel}
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}%{subver}.tgz
# Source0-md5:	4b5c216ccc365471e0235eb8d69cecbc
URL:		http://pear.php.net/package/HTML_Common2/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 3:5.0.0
Requires:	php-pear >= 3:5.0.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The HTML_Common2 package provides methods for HTML code display and
attributes handling.
- Methods to set, remove, update HTML attributes,
- Handles comments in HTML code.
- Handles global document options (encoding, linebreak and indentation
  characters),
- Handles indentation for nicer HTML code.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Pakiet HTML_Common2 zawiera metody do wyświetlania kodu HTML i obróbki
atrybutów.
- Metody do ustawiania, usuwania i aktualizacji atrybutów HTML,
- Obsługuje komentarze w kodzie HTML,
- Obsługuje opcje globalne dokumentu (kodowanie, znaki końca linii i
  wcięcia),
- Obsługuje wcięcia dla ładniejszego wyglądu kodu HTML.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}
AutoProv:	no
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
