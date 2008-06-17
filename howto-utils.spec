Summary:	Index generator for HTML formatted HOWTO documents from TLDP 
Name:		howto-utils
Version:	0.2.15
Release:	%mkrel 5
Group:		Text tools
Source:		%name-%version.tar.bz2
Url: http://www.mandrivalinux.com
License:	GPL
BuildRoot:	%_tmppath/%name-%version-root
BuildArchitectures: noarch
Requires:	sed perl
# sed and coreutils're already required by basesystem:
BuildRequires: grep

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
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT{%_datadir/doc/HOWTO/HTML/,%_bindir}
install -m 755 makehowtoindex {mirror,untar}_howtos $RPM_BUILD_ROOT%_bindir
for i in *.png; do
install -m 644 $i $RPM_BUILD_ROOT%_datadir/doc/HOWTO/HTML/;done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING NEWS
%{_bindir}/*
%dir %{_datadir}/doc/HOWTO/
%dir %{_datadir}/doc/HOWTO/HTML/
%{_datadir}/doc/HOWTO/HTML/*.png
