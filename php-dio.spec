%define modname dio
%define dirname %{modname}
%define soname %{modname}.so
%define inifile 17_%{modname}.ini

Summary:	Direct I/O extension module for PHP
Name:		php-%{modname}
Version:	0.0.7
Release:	1
Group:		Development/PHP
License:	PHP License
URL:		http://pecl.php.net/package/dio
Source0:	http://pecl.php.net/get/dio-%{version}.tgz
BuildRequires:	php-devel >= 3:5.2.0
Epoch:		2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
PHP supports the direct io functions as described in the Posix Standard
(Section 6) for performing I/O functions at a lower level than the C-Language
stream I/O functions (fopen(), fread(),..). The use of the DIO functions should
be considered only when direct control of a device is needed. In all other
cases, the standard filesystem functions are more than adequate.

%prep

%setup -q -n dio-%{version}
[ "../package*.xml" != "/" ] && mv ../package*.xml .

%build
%serverbuild

phpize
%configure2_5x --with-libdir=%{_lib} \
    --with-%{modname}=shared,%{_prefix}

%make
mv modules/*.so .

%install
rm -rf %{buildroot} 

install -d %{buildroot}%{_libdir}/php/extensions
install -d %{buildroot}%{_sysconfdir}/php.d

install -m755 %{soname} %{buildroot}%{_libdir}/php/extensions/

cat > %{buildroot}%{_sysconfdir}/php.d/%{inifile} << EOF
extension = %{soname}
EOF

%post
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
	%{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc package.xml
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/php.d/%{inifile}
%attr(0755,root,root) %{_libdir}/php/extensions/%{soname}


%changelog
* Wed Jul 04 2012 Oden Eriksson <oeriksson@mandriva.com> 2:0.0.6-1mdv2012.0
+ Revision: 808114
- 0.0.6
- rebuild for php-5.4.x

* Tue Apr 10 2012 Oden Eriksson <oeriksson@mandriva.com> 2:0.0.5-1
+ Revision: 790146
- 0.0.5

* Sun Jan 15 2012 Oden Eriksson <oeriksson@mandriva.com> 2:0.0.4-0.0.RC4.9
+ Revision: 761216
- rebuild

* Wed Aug 24 2011 Oden Eriksson <oeriksson@mandriva.com> 2:0.0.4-0.0.RC4.8
+ Revision: 696409
- rebuilt for php-5.3.8

* Fri Aug 19 2011 Oden Eriksson <oeriksson@mandriva.com> 2:0.0.4-0.0.RC4.7
+ Revision: 695382
- rebuilt for php-5.3.7

* Sat Mar 19 2011 Oden Eriksson <oeriksson@mandriva.com> 2:0.0.4-0.0.RC4.6
+ Revision: 646625
- rebuilt for php-5.3.6

* Sat Jan 08 2011 Oden Eriksson <oeriksson@mandriva.com> 2:0.0.4-0.0.RC4.5mdv2011.0
+ Revision: 629780
- rebuilt for php-5.3.5

* Mon Jan 03 2011 Oden Eriksson <oeriksson@mandriva.com> 2:0.0.4-0.0.RC4.4mdv2011.0
+ Revision: 628091
- ensure it's built without automake1.7

* Wed Nov 24 2010 Oden Eriksson <oeriksson@mandriva.com> 2:0.0.4-0.0.RC4.3mdv2011.0
+ Revision: 600473
- rebuild

* Sun Oct 24 2010 Oden Eriksson <oeriksson@mandriva.com> 2:0.0.4-0.0.RC4.2mdv2011.0
+ Revision: 588756
- rebuild

* Fri Mar 05 2010 Oden Eriksson <oeriksson@mandriva.com> 2:0.0.4-0.0.RC4.1mdv2010.1
+ Revision: 514500
- 0.0.4RC4
- rebuild

* Sat Jan 02 2010 Oden Eriksson <oeriksson@mandriva.com> 2:0.0.2-8mdv2010.1
+ Revision: 485255
- rebuilt for php-5.3.2RC1

* Sat Nov 21 2009 Oden Eriksson <oeriksson@mandriva.com> 2:0.0.2-7mdv2010.1
+ Revision: 468082
- rebuilt against php-5.3.1

* Wed Sep 30 2009 Oden Eriksson <oeriksson@mandriva.com> 2:0.0.2-6mdv2010.0
+ Revision: 451212
- rebuild

* Sun Jul 19 2009 Raphaël Gertz <rapsys@mandriva.org> 2:0.0.2-5mdv2010.0
+ Revision: 397358
- Rebuild

* Wed May 13 2009 Oden Eriksson <oeriksson@mandriva.com> 2:0.0.2-4mdv2010.0
+ Revision: 375355
- rebuilt against php-5.3.0RC2

* Sun Mar 01 2009 Oden Eriksson <oeriksson@mandriva.com> 2:0.0.2-3mdv2009.1
+ Revision: 346413
- rebuilt for php-5.2.9

* Tue Feb 17 2009 Oden Eriksson <oeriksson@mandriva.com> 2:0.0.2-2mdv2009.1
+ Revision: 341502
- rebuilt against php-5.2.9RC2

* Tue Jan 06 2009 Oden Eriksson <oeriksson@mandriva.com> 2:0.0.2-1mdv2009.1
+ Revision: 325995
- 0.0.2 (newer than 0.1 :-))

* Wed Dec 31 2008 Oden Eriksson <oeriksson@mandriva.com> 1:0.1-23mdv2009.1
+ Revision: 321728
- rebuild

* Fri Dec 05 2008 Oden Eriksson <oeriksson@mandriva.com> 1:0.1-22mdv2009.1
+ Revision: 310213
- rebuilt against php-5.2.7

* Tue Jul 15 2008 Oden Eriksson <oeriksson@mandriva.com> 1:0.1-21mdv2009.0
+ Revision: 235813
- rebuild

* Fri May 02 2008 Oden Eriksson <oeriksson@mandriva.com> 1:0.1-19mdv2009.0
+ Revision: 200104
- rebuilt against php-5.2.6

* Mon Feb 04 2008 Oden Eriksson <oeriksson@mandriva.com> 1:0.1-18mdv2008.1
+ Revision: 161962
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Nov 11 2007 Oden Eriksson <oeriksson@mandriva.com> 1:0.1-17mdv2008.1
+ Revision: 107559
- restart apache if needed

* Sat Sep 01 2007 Oden Eriksson <oeriksson@mandriva.com> 1:0.1-16mdv2008.0
+ Revision: 77452
- rebuilt against php-5.2.4

* Thu Aug 16 2007 Oden Eriksson <oeriksson@mandriva.com> 1:0.1-15mdv2008.0
+ Revision: 64296
- use the new %%serverbuild macro
- use distro conditional -fstack-protector

* Fri Jun 01 2007 Oden Eriksson <oeriksson@mandriva.com> 1:0.1-14mdv2008.0
+ Revision: 33772
- rebuilt against new upstream version (5.2.3)

* Thu May 03 2007 Oden Eriksson <oeriksson@mandriva.com> 1:0.1-13mdv2008.0
+ Revision: 21021
- rebuilt against new upstream version (5.2.2)


