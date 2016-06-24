Summary:	C++11 threading classes implementation for MinGW
Summary(pl.UTF-8):	Implementacja klas C++11 związanych z wątkami dla MinGW
Name:		crossmingw32-std-threads
Version:	0
%define	gitref	b7e670d91d33b7ce5836c6255d37e69f17eb3687
%define	snap	20160317
Release:	0.%{snap}.1
License:	BSD
Group:		Development/Libraries
Source0:	https://github.com/meganz/mingw-std-threads/archive/%{gitref}/mingw-std-threads-%{snap}.tar.gz
# Source0-md5:	e5f0fcdb69d99ab493f45e65767f9346
URL:		https://github.com/meganz/mingw-std-threads
Requires:	crossmingw32-gcc-c++ >= 1:4.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		no_install_post_strip	1

%define		target			i386-mingw32
%define		target_platform 	i386-pc-mingw32

%define		_sysprefix		/usr
%define		_prefix			%{_sysprefix}/%{target}

%description
Standard C++11 threading classes (std::condition_variable, std::mutex,
std::thread) implementation, which are currently still missing on
MinGW GCC.

%description -l pl.UTF-8
Implementacja klas związanych z wątkami ze standardu C++11
(std::condition_variable, std::mutex, std::thread), obecnie
brakujących w GCC dla MinGW.

%prep
%setup -q -n mingw-std-threads-%{gitref}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}/std-threads

cp -p *.h $RPM_BUILD_ROOT%{_includedir}/std-threads

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{_includedir}/std-threads
