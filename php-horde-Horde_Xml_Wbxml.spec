%define		status		stable
%define		pearname	Horde_Xml_Wbxml
Summary:	%{pearname} - Horde_Xml_Wbxml provides an API for encoding and decoding WBXML documents used in SyncML and other wireless applications
Name:		php-horde-Horde_Xml_Wbxml
Version:	1.0.3
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.horde.org/get/%{pearname}-%{version}.tgz
# Source0-md5:	c804d294a154a96740c27b0fcec9bfbd
URL:		https://github.com/horde/horde/tree/master/framework/Xml_Wbxml/
BuildRequires:	php-channel(pear.horde.org)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR >= 1:1.7.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php-channel(pear.horde.org)
Requires:	php-horde-Horde_Util < 2.0.0
Requires:	php-pear >= 4:1.3.6-2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides encoding and decoding of WBXML (Wireless Binary
XML) documents. WBXML is used in SyncML for transferring smaller
amounts of data with wireless devices.

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

mv docs/Horde_Xml_Wbxml/examples .

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%{php_pear_dir}/.registry/.channel.*/*.reg
%dir %{php_pear_dir}/Horde/Xml
%{php_pear_dir}/Horde/Xml/Wbxml
%{php_pear_dir}/Horde/Xml/Wbxml.php
%{_examplesdir}/%{name}-%{version}
