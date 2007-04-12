%define modname dio
%define dirname %{modname}
%define soname %{modname}.so
%define inifile 17_%{modname}.ini

Summary:	Direct I/O extension module for PHP
Name:		php-%{modname}
Version:	0.1
Release:	%mkrel 12
Group:		Development/PHP
URL:		http://pecl.php.net/package/dio
License:	PHP License
Source0:	dio.tar.bz2
BuildRequires:	php-devel >= 3:5.2.0
Provides:	php5-dio
Obsoletes:	php5-dio
Epoch:		1
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
PHP supports the direct io functions as described in the Posix Standard
(Section 6) for performing I/O functions at a lower level than the C-Language
stream I/O functions (fopen(), fread(),..). The use of the DIO functions should
be considered only when direct control of a device is needed. In all other
cases, the standard filesystem functions are more than adequate.

%prep

%setup -q -n dio

%build

phpize
%configure2_5x --with-libdir=%{_lib} \
    --with-%{modname}=shared,%{_prefix}

%make
mv modules/*.so .

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot} 

install -d %{buildroot}%{_libdir}/php/extensions
install -d %{buildroot}%{_sysconfdir}/php.d

install -m755 %{soname} %{buildroot}%{_libdir}/php/extensions/

cat > %{buildroot}%{_sysconfdir}/php.d/%{inifile} << EOF
extension = %{soname}
EOF

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc package.xml
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/php.d/%{inifile}
%attr(0755,root,root) %{_libdir}/php/extensions/%{soname}


