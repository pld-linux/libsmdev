#
# Conditional build:
%bcond_without	python	# Python (3) bindings
%bcond_without	python3	# CPython 3.x bindings
#
%if %{without python}
%undefine	with_python3
%endif
# see m4/${libname}.m4 />= for required version of particular library
%define		libcdata_ver	20230108
%define		libcerror_ver	20120425
%define		libcfile_ver	20160409
%define		libclocale_ver	20120425
%define		libcnotify_ver	20120425
%define		libcthreads_ver	20160404
%define		libuna_ver	20230702
Summary:	Library to access and read storage media (SM) devices
Summary(pl.UTF-8):	Biblioteka służąca do dostępu i odczytu urządzeń nośników pamięci (SM)
Name:		libsmdev
Version:	20240505
Release:	2
License:	LGPL v3+
Group:		Libraries
#Source0Download: https://github.com/libyal/libsmdev/releases
Source0:	https://github.com/libyal/libsmdev/releases/download/%{version}/%{name}-alpha-%{version}.tar.gz
# Source0-md5:	befafd92fbc8571b38ac0d583d39182e
URL:		https://github.com/libyal/libsmdev/
BuildRequires:	autoconf >= 2.71
BuildRequires:	automake >= 1.6
BuildRequires:	gettext-tools >= 0.21
BuildRequires:	libcdata-devel >= %{libcdata_ver}
BuildRequires:	libcerror-devel >= %{libcerror_ver}
BuildRequires:	libcfile-devel >= %{libcfile_ver}
BuildRequires:	libclocale-devel >= %{libclocale_ver}
BuildRequires:	libcnotify-devel >= %{libcnotify_ver}
BuildRequires:	libcthreads-devel >= %{libcthreads_ver}
BuildRequires:	libuna-devel >= %{libuna_ver}
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig
%{?with_python3:BuildRequires:	python3-devel >= 1:3.7}
Requires:	libcdata >= %{libcdata_ver}
Requires:	libcerror >= %{libcerror_ver}
Requires:	libcfile >= %{libcfile_ver}
Requires:	libclocale >= %{libclocale_ver}
Requires:	libcnotify >= %{libcnotify_ver}
Requires:	libcthreads >= %{libcthreads_ver}
Requires:	libuna >= %{libuna_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libsmdev is a library to access and read storage media (SM) devices.

%description -l pl.UTF-8
libsmdev to biblioteka służąca do dostępu i odczytu urządzeń nośników
pamięci (SM - Storage Media)

%package devel
Summary:	Header files for libsmdev library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libsmdev
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libcdata-devel >= %{libcdata_ver}
Requires:	libcerror-devel >= %{libcerror_ver}
Requires:	libcfile-devel >= %{libcfile_ver}
Requires:	libclocale-devel >= %{libclocale_ver}
Requires:	libcnotify-devel >= %{libcnotify_ver}
Requires:	libcthreads-devel >= %{libcthreads_ver}
Requires:	libuna-devel >= %{libuna_ver}

%description devel
Header files for libsmdev library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libsmdev.

%package static
Summary:	Static libsmdev library
Summary(pl.UTF-8):	Statyczna biblioteka libsmdev
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libsmdev library.

%description static -l pl.UTF-8
Statyczna biblioteka libsmdev.

%package -n python3-pysmdev
Summary:	Python 3 bindings for libsmdev library
Summary(pl.UTF-8):	Wiązania Pythona 3 do biblioteki libsmdev
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description -n python3-pysmdev
Python 3 bindings for libsmdev library.

%description -n python3-pysmdev -l pl.UTF-8
Wiązania Pythona 3 do biblioteki libsmdev.

%prep
%setup -q

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	PYTHON_VERSION=3 \
	%{?with_python3:--enable-python}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libsmdev.la

%if %{with python3}
%{__rm} $RPM_BUILD_ROOT%{py3_sitedir}/pysmdev.{la,a}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/smdevinfo
%attr(755,root,root) %{_libdir}/libsmdev.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsmdev.so.1
%{_mandir}/man1/smdevinfo.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsmdev.so
%{_includedir}/libsmdev
%{_includedir}/libsmdev.h
%{_pkgconfigdir}/libsmdev.pc
%{_mandir}/man3/libsmdev.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libsmdev.a

%if %{with python3}
%files -n python3-pysmdev
%defattr(644,root,root,755)
%attr(755,root,root) %{py3_sitedir}/pysmdev.so
%endif
