#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : librtlsdr
Version  : 0.5.4
Release  : 5
URL      : https://github.com/osmocom/rtl-sdr/archive/v0.5.4.tar.gz
Source0  : https://github.com/osmocom/rtl-sdr/archive/v0.5.4.tar.gz
Summary  : C Utility Library
Group    : Development/Tools
License  : GPL-2.0
Requires: librtlsdr-bin
Requires: librtlsdr-lib
Requires: librtlsdr-license
BuildRequires : cmake
BuildRequires : pkgconfig(libusb-1.0)

%description
rtl-sdr
turns your Realtek RTL2832 based DVB dongle into a SDR receiver
======================================================================

%package bin
Summary: bin components for the librtlsdr package.
Group: Binaries
Requires: librtlsdr-license

%description bin
bin components for the librtlsdr package.


%package dev
Summary: dev components for the librtlsdr package.
Group: Development
Requires: librtlsdr-lib
Requires: librtlsdr-bin
Provides: librtlsdr-devel

%description dev
dev components for the librtlsdr package.


%package lib
Summary: lib components for the librtlsdr package.
Group: Libraries
Requires: librtlsdr-license

%description lib
lib components for the librtlsdr package.


%package license
Summary: license components for the librtlsdr package.
Group: Default

%description license
license components for the librtlsdr package.


%prep
%setup -q -n rtl-sdr-0.5.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1529454302
%reconfigure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1529454302
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/librtlsdr
cp COPYING %{buildroot}/usr/share/doc/librtlsdr/COPYING
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/rtl_adsb
/usr/bin/rtl_eeprom
/usr/bin/rtl_fm
/usr/bin/rtl_power
/usr/bin/rtl_sdr
/usr/bin/rtl_tcp
/usr/bin/rtl_test

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/librtlsdr.so
/usr/lib64/pkgconfig/librtlsdr.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/librtlsdr.so.0
/usr/lib64/librtlsdr.so.0.0.5

%files license
%defattr(-,root,root,-)
/usr/share/doc/librtlsdr/COPYING
