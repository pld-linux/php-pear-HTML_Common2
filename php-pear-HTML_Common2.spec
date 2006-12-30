%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	Common2
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - abstract base class for HTML classes (PHP5 port of HTML_Common package)
Summary(pl):	%{_pearname} - podstawowa klasa dla klas HTML (port pakietu HTML_Common dla PHP5)
Name:		php-pear-%{_pearname}
Version:	0.3.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	757cf3879b3a6e4750728206e4c37070
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

%description -l pl
Pakiet HTML_Common2 zawiera metody do wy¶wietlania kodu HTML i obróbki
atrybutów.
- Metody do ustawiania, usuwania i aktualizacji atrybutów HTML,
- Obs³uguje komentarze w kodzie HTML,
- Obs³uguje opcje globalne dokumentu (kodowanie, znaki koñca linii i
  wciêcia),
- Obs³uguje wciêcia dla ³adniejszego wygl±du kodu HTML.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
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
