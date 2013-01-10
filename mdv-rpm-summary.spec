Summary:	Localization files for packages summaries
Name:		mdv-rpm-summary
Version:	0.9.4
Release:	6
Source0:	%{name}-%{version}.tar.bz2
License:	GPL
Group:		System/Internationalization
BuildRequires:	gettext
BuildArch:	noarch

%description
This package includes translations of summaries the Mandriva Linux packages.
They are used by rpmdrake.

%prep
%setup -q

%build
make

%install
%makeinstall_std PREFIX=%{buildroot}/

%find_lang rpm-summary-contrib rpm-summary-devel rpm-summary-main rpm-summary-non-free %{name}.lang

%files -f %{name}.lang 
%defattr(-,root,root,0755)


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.9.4-3mdv2011.0
+ Revision: 666409
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.4-2mdv2011.0
+ Revision: 606634
- rebuild

* Tue May 25 2010 Pascal Terjan <pterjan@mandriva.org> 0.9.4-1mdv2010.1
+ Revision: 545861
- update for 2010.1

* Tue May 25 2010 Antoine Ginies <aginies@mandriva.com> 0.9.3-3mdv2010.1
+ Revision: 545844
+ rebuild (emptylog)

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.3-2mdv2010.1
+ Revision: 523302
- rebuilt for 2010.1

* Thu Oct 29 2009 Funda Wang <fwang@mandriva.org> 0.9.3-1mdv2010.0
+ Revision: 459937
- final version for 2010

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.9.2-2mdv2010.0
+ Revision: 426082
- rebuild

* Fri Apr 17 2009 Thierry Vignaud <tv@mandriva.org> 0.9.2-1mdv2009.1
+ Revision: 367914
- translation updates

* Mon Mar 30 2009 Funda Wang <fwang@mandriva.org> 0.9.1-1mdv2009.1
+ Revision: 362424
- New version 0.9.1

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.9-4mdv2009.1
+ Revision: 351591
- rebuild

* Wed Oct 01 2008 Funda Wang <fwang@mandriva.org> 0.9-3mdv2009.0
+ Revision: 290278
- New snapshot of translation

* Mon Sep 29 2008 Funda Wang <fwang@mandriva.org> 0.9-2mdv2009.0
+ Revision: 289778
- New translation snapshot

* Sat Sep 13 2008 Funda Wang <fwang@mandriva.org> 0.9-1mdv2009.0
+ Revision: 284498
- New version 0.9 for 2009

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.8-2mdv2009.0
+ Revision: 223227
- rebuild

  + Funda Wang <fwang@mandriva.org>
    - New snapshot of translation

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.7-2mdv2008.1
+ Revision: 153056
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Sep 18 2007 Thierry Vignaud <tv@mandriva.org> 0.7-1mdv2008.0
+ Revision: 89644
- translation snapshot

* Thu Sep 13 2007 Thierry Vignaud <tv@mandriva.org> 0.6-1mdv2008.0
+ Revision: 85234
- translation snapshot

* Thu Sep 13 2007 Thierry Vignaud <tv@mandriva.org> 0.5-1mdv2008.0
+ Revision: 85162
- translation snapshort

* Tue Jul 31 2007 Thierry Vignaud <tv@mandriva.org> 0.4-1mdv2008.0
+ Revision: 56817
- new release


* Tue Mar 13 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.3-1mdv2007.1
+ Revision: 142454
- updated translations

* Wed Mar 07 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.2-1mdv2007.1
+ Revision: 134504
- updated translations

* Wed Feb 28 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.1-1mdv2007.1
+ Revision: 129323
- Import mdv-rpm-summary

* Wed Feb 28 2007 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.1-1mdv2007.1
- initial release

