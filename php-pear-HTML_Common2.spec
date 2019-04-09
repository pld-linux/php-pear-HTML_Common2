%include	/usr/lib/rpm/macros.php
%define		_status		stable
%define		_pearname	HTML_Common2
Summary:	%{_pearname} - abstract base class for HTML classes (PHP5 port of HTML_Common package)
Summary(pl.UTF-8):	%{_pearname} - podstawowa klasa dla klas HTML (port pakietu HTML_Common dla PHP5)
Name:		php-pear-%{_pearname}
Version:	2.1.2
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	0676ea550115e595568d19ef4c773670
URL:		http://pear.php.net/package/HTML_Common2/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(core) >= 5.0.0
Requires:	php-pear >= 3:5.0.0
Obsoletes:	php-pear-HTML_Common2-tests
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
%{php_pear_dir}/HTML/*.php
