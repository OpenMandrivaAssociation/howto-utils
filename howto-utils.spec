Summary:	Index generator for HTML formatted HOWTO documents from TLDP 
Name:		howto-utils
Version:	0.2.15
Release:	%mkrel 9
Group:		Text tools
Source:		%name-%version.tar.bz2
Url: http://www.mandrivalinux.com
License:	GPL
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
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


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.2.15-9mdv2011.0
+ Revision: 665434
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2.15-8mdv2011.0
+ Revision: 605877
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2.15-7mdv2010.1
+ Revision: 520719
- rebuilt for 2010.1

* Fri Jul 04 2008 Oden Eriksson <oeriksson@mandriva.com> 0.2.15-6mdv2009.0
+ Revision: 231705
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 0.2.15-4mdv2008.1
+ Revision: 150275
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- upgrade comment

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Jul 05 2007 Adam Williamson <awilliamson@mandriva.org> 0.2.15-3mdv2008.0
+ Revision: 48500
- rebuild for 2008
- Import howto-utils



* Fri Jun 30 2006 Pablo Saratxaga <pablo@mandriva.com> 0.2.15-2mdv
- i18n: made strings for title and headers of the howto index
  translatable (translations got from "menu-messages" domain)

* Mon Jul 18 2005 Thierry Vignaud <tvignaud@mandriva.com> 0.2.15-1mdk
- switch from mandrakesoft to mandriva

* Fri Aug 13 2004 Thierry Vignaud <tvignaud@mandruva.com> 0.2.14-1mdk
- makehowtoindex:
  o blacklist deprecated and obsoleted howtos: ipchains, ...
  o fix usage message: only mirror_howtos takes a format parameter
- mirror_howtos:
  o fix mini howtos mirroring
  o adatp to new lftp
- untar_howtos: remove broken links mirrored from FTP (#9706)

* Mon May 31 2004 Thierry Vignaud <tvignaud@mandriva.com> 0.2.13-4mdk
- makehowtoindex:
  o blacklist deprecated and obsoleted howtos: ipchains, ...
  o fix usage message: only mirror_howtos takes a format parameter
- untar_howtos: remove broken links mirrored from FTP (#)

* Mon Mar  1 2004 Thierry Vignaud <tvignaud@mandriva.com> 0.2.13-3mdk
- update list
- fix sort

* Wed Jul 16 2003 Thierry Vignaud <tvignaud@mandriva.com> 0.2.13-2mdk
- distriblint fixes

* Tue Jul  1 2003 Thierry Vignaud <tvignaud@mandriva.com> 0.2.13-1mdk
- makehowtoindex: sort more howtos
- mirror_howtos: fr url has been altered

* Tue Feb 18 2003 Thierry Vignaud <tvignaud@mandriva.com> 0.2.12-2mdk
- new color scheme
- fix sv howtos
- merge both howtos and mini howtos since we class them

* Fri Feb 14 2003 Thierry Vignaud <tvignaud@mandriva.com> 0.2.12-1mdk
- handle non splited mini howtos 
- a lot faster menu generation
- handle broken howtos (aka those who have "><TITLE\n>blabla\n></TITLE"
- handle howtos whose title include html tags
- sort howto entries by title

* Thu Feb 13 2003 Thierry Vignaud <tvignaud@mandriva.com> 0.2.11-1mdk
- switch scripts to perl:
  o better error handling
  o don't forget some howtos
  o incremental updates when making snapshots
  o fix links

* Mon Jan 20 2003 Thierry Vignaud <tvignaud@mandriva.com> 0.2.10-1mdk
- support specifying a optional format than html (eg sgml, text)
- ensure we've 1 or 2 arguments or else print usage help
- fix program name in help

* Fri Aug 02 2002 Thierry Vignaud <tvignaud@mandriva.com> 0.2.9-1mdk
- requires perl
- mirror_howtos:
	o add execption for id and en locales (there're already fr and de ones)
	o warn that we cannot handle hu for now
	o new data structure
- untar_howtos:
	o force decompression of gzipped files
	o handle zip files too
	o display broken gzipped files


* Thu Aug 01 2002 Thierry Vignaud <tvignaud@mandriva.com> 0.2.8-1mdk
- add mirror_howtos
- untar => untar_howtos

* Thu Aug 01 2002 Thierry Vignaud <tvignaud@mandriva.com> 0.2.7-1mdk
- add untar 

* Tue Apr 09 2002 Thierry Vignaud <tvignaud@mandriva.com> 0.2.6-1mdk
- handle howtos using "...-html" naming
- handle howtos using "...-HOWTO" naming
- add a few comments in the makehowtoindex script
- BuildRequires: grep (sed and fileutils're already required by basesystem)
- get rid of howto that only redirect to another howto
- faster tests
- final code factorisation between mini howtos and howtos
- display bad links
- fix wrong permissions if needed

* Tue Apr 09 2002 Thierry Vignaud <tvignaud@mandriva.com> 0.2.5-1mdk
- handle howtos in subdirectories

* Fri Feb 01 2002 Thierry Vignaud <tvignaud@mandriva.com> 0.2.4-1mdk
- typo fix from adrien
- remove bogus files
- add cleaner prototype from adrien

* Tue Oct 30 2001 Thierry Vignaud <tvignaud@mandriva.com> 0.2.3-3mdk
- add %%url

* Tue Jun 19 2001 Thierry Vignaud <tvignaud@mandriva.com> 0.2.3-2mdk
- minor spec cleaning
- truncate summary for rpm tools
- enhence description

* Tue Mar 13 2001 Thierry Vignaud <tvignaud@mandriva.com> 0.2.2-1mdk
- new version. From Ivan Zakharyaschev <imz@linux.ru.net>
	- include some meta-information really needed for Russian
	  HTML-documents, otherwise some strict HTML-renderers like StarOffice
	  or Midnight Commander assume it to be the standard ISO-..., but not
	  the actually used koi8-r);

	- some HOWTOs are split into several parts (files having names
	  <name>-HOWTO-[0-9]*.html); and then the real overall title is placed
	  into a correspondig ".dsc"-file, the TITLE-elements in each part
	  relate usually only to that part's contents, but not the whole document
	  (that's the situation one can observe in Russian howtos);

	- one has to invoke the script in a subshell, otherwise the environment
	  is spoilt after exec 1> index.html;

	- <TITLE>the title</title> elemnts are not recognised for title
	  extraction;

	- and the bug I described in the previous message: in some cases, we
	  get duplicate names for subsequent items (with different links) --
	  in English howtos.

* Mon Mar 05 2001 Thierry Vignaud <tvignaud@mandriva.com> 0.2.2-1mdk
- Merge Etienne Faure patch (Little fix to handle english howto that do
  not have pretty html 
  [Last time someone patch an old version and upload it, i'll kill him)

* Thu Mar 01 2001 Thierry Vignaud <tvignaud@mandriva.com> 0.2.1-1mdk
- let makehowtoindex fix howto location

* Fri Aug 11 2000 Thierry Vignaud <tvignaud@mandriva.com> 0.2-1mdk
- add LN touch

* Fri Aug 11 2000 Thierry Vignaud <tvignaud@mandriva.com> 0.1.1-1mdk
- little fix to handle greek howto that don't follow LDP naming rules

* Fri Aug 11 2000 Thierry Vignaud <tvignaud@mandriva.com> 0.1-1mdk
- initial release
