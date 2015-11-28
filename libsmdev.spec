#
# Conditional build:
%bcond_without	python	# Python bindings
#
Summary:	Library to access and read storage media (SM) devices
Summary(pl.UTF-8):	Biblioteka służąca do dostępu i odczytu urządzeń nośników pamięci (SM)
Name:		libsmdev
Version:	20150105
Release:	3
License:	LGPL v3+
Group:		Libraries
Source0:	https://github.com/libyal/libsmdev/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	872758d8c516785966cab26de58d7f1b
Patch0:		%{name}-system-libs.patch
URL:		https://github.com/libyal/libsmdev/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1.6
BuildRequires:	gettext-tools >= 0.18.1
BuildRequires:	libcdata-devel >= 20150102
BuildRequires:	libcerror-devel >= 20120425
BuildRequires:	libcfile-devel >= 20140503
BuildRequires:	libclocale-devel >= 20120425
BuildRequires:	libcnotify-devel >= 20120425
BuildRequires:	libcstring-devel >= 20120425
BuildRequires:	libcsystem-devel >= 20141018
BuildRequires:	libcthreads-devel >= 20130509
BuildRequires:	libuna-devel >= 20120425
BuildRequires:	libtool
BuildRequires:	pkgconfig
%{?with_python:BuildRequires:	python-devel >= 1:2.5}
BuildRequires:	sed >= 4.0
Requires:	libcdata >= 20150102
Requires:	libcerror >= 20120425
Requires:	libcfile >= 20140503
Requires:	libclocale >= 20120425
Requires:	libcnotify >= 20120425
Requires:	libcstring >= 20120425
Requires:	libcsystem >= 20141018
Requires:	libcthreads >= 20130509
Requires:	libuna >= 20120425
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
Requires:	libcdata-devel >= 20150102
Requires:	libcerror-devel >= 20120425
Requires:	libcfile-devel >= 20140503
Requires:	libclocale-devel >= 20120425
Requires:	libcnotify-devel >= 20120425
Requires:	libcstring-devel >= 20120425
Requires:	libcthreads-devel >= 20130509
Requires:	libuna-devel >= 20120425

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

%package -n python-pysmdev
Summary:	Python bindings for libsmdev library
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki libsmdev
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description -n python-pysmdev
Python bindings for libsmdev library.

%description -n python-pysmdev -l pl.UTF-8
Wiązania Pythona do biblioteki libsmdev.

%prep
%setup -q
%patch0 -p1

%build
%{__gettextize}
%{__sed} -i -e 's/ po\/Makefile.in//' configure.ac
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?with_python:--enable-python}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libsmdev.la

%if %{with python}
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/pysmdev.{la,a}
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

%if %{with python}
%files -n python-pysmdev
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/pysmdev.so
%endif
