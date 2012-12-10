Summary: A web based terminal
Name: ajaxterm
Version: 0.10
Release: %mkrel 6

# LGPL for the bundled js part 
License: GPL and LGPL
Group: System/Servers
URL: http://antony.lesuisse.org/qweb/trac/wiki/AjaxTerm
Source: http://antony.lesuisse.org/qweb/files/Ajaxterm-%{version}.tar.bz2
Source1: %{name}.init
Source2: %{name}.sysconfig
Requires(preun): rpm-helper
Requires(post):  rpm-helper
Requires: python
BuildRequires: python
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

%description
Ajaxterm is a web based terminal. It was totally inspired and works almost 
exactly like http://anyterm.org/ except it's much easier to install. 

Ajaxterm written in python (and some AJAX javascript for client side) and 
depends only on python2.3 or better.

%prep
%setup -q -n Ajaxterm-%{version}

%build
./configure --prefix=$RPM_BUILD_ROOT/%_prefix/
perl -pi -e 's/.*ajaxterm.initd.*//' Makefile
perl -pi -e 's|bin/python2.3|bin/python|' qweb.py

%install
%{__rm} -rf %{buildroot}
make install 

mkdir -p %{buildroot}/%_initrddir/
mkdir -p %{buildroot}/%_sysconfdir/sysconfig

cp %SOURCE1 %{buildroot}/%_initrddir/%{name}
cp %SOURCE2 %{buildroot}/%_sysconfdir/sysconfig/%name

chmod 755 %{buildroot}/%_initrddir/%{name}
perl -pi -e 's|%{buildroot}/||g' %{buildroot}/%{_bindir}/ajaxterm

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README.txt
%{_bindir}/*
%{_datadir}/%name/
%{_mandir}/man1/*
%config(noreplace) %{_initrddir}/%{name}
%config(noreplace) %_sysconfdir/sysconfig/%{name}

%post
%_post_service %{name}

%preun
%_preun_service %{name}




%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.10-6mdv2011.0
+ Revision: 616557
- the mass rebuild of 2010.0 packages

* Tue Sep 01 2009 Thierry Vignaud <tv@mandriva.org> 0.10-5mdv2010.0
+ Revision: 424009
- rebuild

* Tue Sep 01 2009 Thierry Vignaud <tv@mandriva.org> 0.10-4mdv2010.0
+ Revision: 423968
- rebuild

* Tue Sep 01 2009 Thierry Vignaud <tv@mandriva.org> 0.10-3mdv2010.0
+ Revision: 423937
- rebuild

* Thu Jun 19 2008 Thierry Vignaud <tv@mandriva.org> 0.10-2mdv2009.0
+ Revision: 226142
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 0.10-1mdv2008.1
+ Revision: 135819
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Sep 05 2007 Michael Scherer <misc@mandriva.org> 0.10-1mdv2008.0
+ Revision: 80049
- 0.10
- uncompress files


* Tue Oct 03 2006 Michael Scherer <misc@mandriva.org> 0.9-2mdv2007.0
+ Revision: 62824
- requires python, fix bug #24176
- Import ajaxterm

* Sat Jul 22 2006 Michael Scherer <misc@mandriva.org> 0.9-2mdv2007.0
- add missing BuildRequires, since python is no longer required for 
  rpm-build and basesystem

* Fri Jul 21 2006 Michael Scherer <misc@mandriva.org> 0.9-1mdv2007.0
- New version 0.9

* Mon Jul 10 2006 Michael Scherer <misc@mandriva.org> 0.8-1
- New release 0.8

* Fri Jun 02 2006 Michael Scherer <misc@mandriva.org> 0.7-2mdv2007.0
- fix #22855

* Thu Jun 01 2006 Michael Scherer <misc@mandriva.org> 0.7-1mdk
- New release 0.7
- removed patch0, applied upstream

* Thu May 25 2006 Michael Scherer <misc@mandriva.org> 0.6-1mdk
- First package

