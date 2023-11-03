#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure_ac
# autospec version: v2
# autospec commit: 250a666
#
Name     : librtlsdr
Version  : 2.0.1
Release  : 10
URL      : https://github.com/steve-m/librtlsdr/archive/v2.0.1/librtlsdr-2.0.1.tar.gz
Source0  : https://github.com/steve-m/librtlsdr/archive/v2.0.1/librtlsdr-2.0.1.tar.gz
Summary  : C Utility Library
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: librtlsdr-bin = %{version}-%{release}
Requires: librtlsdr-lib = %{version}-%{release}
Requires: librtlsdr-license = %{version}-%{release}
BuildRequires : pkgconfig(libusb-1.0)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
rtl-sdr
turns your Realtek RTL2832 based DVB dongle into a SDR receiver
======================================================================

%package bin
Summary: bin components for the librtlsdr package.
Group: Binaries
Requires: librtlsdr-license = %{version}-%{release}

%description bin
bin components for the librtlsdr package.


%package dev
Summary: dev components for the librtlsdr package.
Group: Development
Requires: librtlsdr-lib = %{version}-%{release}
Requires: librtlsdr-bin = %{version}-%{release}
Provides: librtlsdr-devel = %{version}-%{release}
Requires: librtlsdr = %{version}-%{release}

%description dev
dev components for the librtlsdr package.


%package lib
Summary: lib components for the librtlsdr package.
Group: Libraries
Requires: librtlsdr-license = %{version}-%{release}

%description lib
lib components for the librtlsdr package.


%package license
Summary: license components for the librtlsdr package.
Group: Default

%description license
license components for the librtlsdr package.


%prep
%setup -q -n librtlsdr-2.0.1
cd %{_builddir}/librtlsdr-2.0.1
pushd ..
cp -a librtlsdr-2.0.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1699020979
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%reconfigure --disable-static
make  %{?_smp_mflags}
unset PKG_CONFIG_PATH
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -m64 -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -m64 -march=x86-64-v3 "
%reconfigure --disable-static
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1699020979
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/librtlsdr
cp %{_builddir}/librtlsdr-%{version}/COPYING %{buildroot}/usr/share/package-licenses/librtlsdr/06877624ea5c77efe3b7e39b0f909eda6e25a4ec || :
cp %{_builddir}/librtlsdr-%{version}/debian/copyright %{buildroot}/usr/share/package-licenses/librtlsdr/78479bcc66c8173ca136c98e779b8f63563a5b94 || :
pushd ../buildavx2/
%make_install_v3
popd
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/rtl_adsb
/V3/usr/bin/rtl_eeprom
/V3/usr/bin/rtl_fm
/V3/usr/bin/rtl_power
/V3/usr/bin/rtl_sdr
/V3/usr/bin/rtl_tcp
/V3/usr/bin/rtl_test
/usr/bin/rtl_adsb
/usr/bin/rtl_eeprom
/usr/bin/rtl_fm
/usr/bin/rtl_power
/usr/bin/rtl_sdr
/usr/bin/rtl_tcp
/usr/bin/rtl_test

%files dev
%defattr(-,root,root,-)
/usr/include/rtl-sdr.h
/usr/include/rtl-sdr_export.h
/usr/lib64/librtlsdr.so
/usr/lib64/pkgconfig/librtlsdr.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/librtlsdr.so.0.0.5
/usr/lib64/librtlsdr.so.0
/usr/lib64/librtlsdr.so.0.0.5

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/librtlsdr/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
/usr/share/package-licenses/librtlsdr/78479bcc66c8173ca136c98e779b8f63563a5b94
