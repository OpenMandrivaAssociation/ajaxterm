Summary: A web based terminal
Name: ajaxterm
Version: 0.10
Release: %mkrel 3

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


