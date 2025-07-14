#
# Conditional build:
%bcond_without	tests	# perform test build
#
Summary:	C++11 threading classes implementation for MinGW
Summary(pl.UTF-8):	Implementacja klas C++11 związanych z wątkami dla MinGW
Name:		crossmingw32-std-threads
Version:	0
%define	gitref	ee67ef384470e998c8e0b7301f7a79b5019251a2
%define	snap	20180912
%define	rel	2
Release:	0.%{snap}.%{rel}
License:	BSD
Group:		Development/Libraries
Source0:	https://github.com/meganz/mingw-std-threads/archive/%{gitref}/mingw-std-threads-%{snap}.tar.gz
# Source0-md5:	c55d7a463149d803535b71c6bb1346cb
Patch0:		mingw-std-threads-include.patch
Patch1:		mingw-std-threads-errors.patch
URL:		https://github.com/meganz/mingw-std-threads
%if %{with tests}
BuildRequires:	crossmingw32-gcc-c++ >= 1:4.7
%endif
Requires:	crossmingw32-gcc-c++ >= 1:4.7
Requires:	crossmingw32-runtime
Requires:	crossmingw32-w32api
ExcludeArch:	i386
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		no_install_post_strip	1

%define		target			i386-mingw32
%define		target_platform 	i386-pc-mingw32

%define		__cc			%{target}-gcc
%define		__cxx			%{target}-g++

%define		_sysprefix		/usr
%define		_prefix			%{_sysprefix}/%{target}

%ifnarch %{ix86}
# arch-specific flags (like alpha's -mieee) are not valid for i386 gcc.
# now at least i486 is required for atomic operations
%define		optflags	-O2 -march=i486
%endif
# -z options are invalid for mingw linker, most of -f options are Linux-specific
%define		filterout_ld	-Wl,-z,.*
%define		filterout_c	-f[-a-z0-9=]*
%define		filterout_cxx	-f[-a-z0-9=]*

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
%patch -P0 -p1
%patch -P1 -p1

%build
%if %{with tests}
install -d tests/build
cd tests/build
CC="%{__cc}" \
CXX="%{__cxx}" \
cmake .. \
	-DCMAKE_BUILD_TYPE=PLD \
	-DCMAKE_CXX_FLAGS_PLD="%{rpmcxxflags} -DWINVER=0x0501" \
	-DCMAKE_SYSTEM_NAME=Windows \
	-DCMAKE_SYSTEM_PROCESSOR=i386 \
	-DCMAKE_VERBOSE_MAKEFILE=ON

%{__make}
%endif

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
