#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : qtserialport
Version  : 5.14.0
Release  : 22
URL      : https://download.qt.io/official_releases/qt/5.14/5.14.0/submodules/qtserialport-everywhere-src-5.14.0.tar.xz
Source0  : https://download.qt.io/official_releases/qt/5.14/5.14.0/submodules/qtserialport-everywhere-src-5.14.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.3 GPL-2.0 GPL-3.0 LGPL-3.0
Requires: qtserialport-lib = %{version}-%{release}
Requires: qtserialport-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-qmake
BuildRequires : pkgconfig(Qt5Core)
BuildRequires : pkgconfig(Qt5Test)
BuildRequires : pkgconfig(Qt5Widgets)
BuildRequires : systemd-dev

%description
No detailed description available

%package dev
Summary: dev components for the qtserialport package.
Group: Development
Requires: qtserialport-lib = %{version}-%{release}
Provides: qtserialport-devel = %{version}-%{release}
Requires: qtserialport = %{version}-%{release}

%description dev
dev components for the qtserialport package.


%package lib
Summary: lib components for the qtserialport package.
Group: Libraries
Requires: qtserialport-license = %{version}-%{release}

%description lib
lib components for the qtserialport package.


%package license
Summary: license components for the qtserialport package.
Group: Default

%description license
license components for the qtserialport package.


%prep
%setup -q -n qtserialport-everywhere-src-5.14.0
cd %{_builddir}/qtserialport-everywhere-src-5.14.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export GCC_IGNORE_WERROR=1
%qmake QMAKE_CFLAGS+=-fno-lto QMAKE_CXXFLAGS+=-fno-lto
test -r config.log && cat config.log
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1576216169
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qtserialport
cp %{_builddir}/qtserialport-everywhere-src-5.14.0/LICENSE.FDL %{buildroot}/usr/share/package-licenses/qtserialport/61907422fefcd2313a9b570c31d203a6dbebd333
cp %{_builddir}/qtserialport-everywhere-src-5.14.0/LICENSE.GPL2 %{buildroot}/usr/share/package-licenses/qtserialport/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/qtserialport-everywhere-src-5.14.0/LICENSE.GPL3 %{buildroot}/usr/share/package-licenses/qtserialport/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/qtserialport-everywhere-src-5.14.0/LICENSE.GPL3-EXCEPT %{buildroot}/usr/share/package-licenses/qtserialport/e93757aefa405f2c9a8a55e780ae9c39542dfc3a
cp %{_builddir}/qtserialport-everywhere-src-5.14.0/LICENSE.LGPL3 %{buildroot}/usr/share/package-licenses/qtserialport/f45ee1c765646813b442ca58de72e20a64a7ddba
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/qt5/QtSerialPort/5.14.0/QtSerialPort/private/qserialport_p.h
/usr/include/qt5/QtSerialPort/5.14.0/QtSerialPort/private/qserialportinfo_p.h
/usr/include/qt5/QtSerialPort/5.14.0/QtSerialPort/private/qtntdll_p.h
/usr/include/qt5/QtSerialPort/5.14.0/QtSerialPort/private/qtserialport-config_p.h
/usr/include/qt5/QtSerialPort/5.14.0/QtSerialPort/private/qtudev_p.h
/usr/include/qt5/QtSerialPort/QSerialPort
/usr/include/qt5/QtSerialPort/QSerialPortInfo
/usr/include/qt5/QtSerialPort/QtSerialPort
/usr/include/qt5/QtSerialPort/QtSerialPortDepends
/usr/include/qt5/QtSerialPort/QtSerialPortVersion
/usr/include/qt5/QtSerialPort/qserialport.h
/usr/include/qt5/QtSerialPort/qserialportglobal.h
/usr/include/qt5/QtSerialPort/qserialportinfo.h
/usr/include/qt5/QtSerialPort/qtserialport-config.h
/usr/include/qt5/QtSerialPort/qtserialportversion.h
/usr/lib64/cmake/Qt5SerialPort/Qt5SerialPortConfig.cmake
/usr/lib64/cmake/Qt5SerialPort/Qt5SerialPortConfigVersion.cmake
/usr/lib64/libQt5SerialPort.prl
/usr/lib64/libQt5SerialPort.so
/usr/lib64/pkgconfig/Qt5SerialPort.pc
/usr/lib64/qt5/mkspecs/modules/qt_lib_serialport.pri
/usr/lib64/qt5/mkspecs/modules/qt_lib_serialport_private.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libQt5SerialPort.so.5
/usr/lib64/libQt5SerialPort.so.5.14
/usr/lib64/libQt5SerialPort.so.5.14.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qtserialport/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/qtserialport/61907422fefcd2313a9b570c31d203a6dbebd333
/usr/share/package-licenses/qtserialport/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/qtserialport/e93757aefa405f2c9a8a55e780ae9c39542dfc3a
/usr/share/package-licenses/qtserialport/f45ee1c765646813b442ca58de72e20a64a7ddba
