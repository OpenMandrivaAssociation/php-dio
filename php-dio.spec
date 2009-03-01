%define modname dio
%define dirname %{modname}
%define soname %{modname}.so
%define inifile 17_%{modname}.ini

Summary:	Direct I/O extension module for PHP
Name:		php-%{modname}
Version:	0.0.2
Release:	%mkrel 3
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
