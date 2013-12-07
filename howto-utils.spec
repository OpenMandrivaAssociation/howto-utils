Summary:	Index generator for HTML formatted HOWTO documents from TLDP 
Name:		howto-utils
Version:	0.2.15
Release:	13
Group:		Text tools
License:	GPLv2
Url:		http://www.mandrivalinux.com
Source0:	%{name}-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	grep
Requires:	perl
Requires:	sed

%description
Linux HOWTOs are parts of the Linux Documentation Project.
They are detailed documents which describe a specific aspect of 
configuring or using Linux. Linux HOWTOs are a great source of
practical information about your system. The latest versions of these
documents are located at http://www.tldp.org/docs.html#howto

Currently, available tools are :
- makehowtoindex is an index generator for html formatted HOWTO documents
- mirror_howtos mirror howtos and mini-howtos
- untar_howtos processes a howto mirror obtained by mirror_howtos

%prep 
%setup -q

%install
mkdir -p %{buildroot}{%{_datadir}/doc/HOWTO/HTML/,%_bindir}
install -m 755 makehowtoindex {mirror,untar}_howtos %{buildroot}%_bindir
for i in *.png; do
install -m 644 $i %{buildroot}%{_datadir}/doc/HOWTO/HTML/;done

%files
%doc COPYING NEWS
%{_bindir}/*
%dir %{_datadir}/doc/HOWTO/
%dir %{_datadir}/doc/HOWTO/HTML/
%{_datadir}/doc/HOWTO/HTML/*.png

