#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : qtserialport
Version  : 5.10.1
Release  : 5
URL      : http://download.qt.io/official_releases/qt/5.10/5.10.1/submodules/qtserialport-everywhere-src-5.10.1.tar.xz
Source0  : http://download.qt.io/official_releases/qt/5.10/5.10.1/submodules/qtserialport-everywhere-src-5.10.1.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.3 GPL-2.0 GPL-3.0 LGPL-3.0
Requires: qtserialport-lib
BuildRequires : cmake
BuildRequires : pkgconfig(Qt5Core)
BuildRequires : pkgconfig(Qt5Test)
BuildRequires : pkgconfig(Qt5Widgets)
BuildRequires : qtbase-dev
BuildRequires : qtbase-extras
BuildRequires : systemd-dev

%description
No detailed description available

%package dev
Summary: dev components for the qtserialport package.
Group: Development
Requires: qtserialport-lib
Provides: qtserialport-devel

%description dev
dev components for the qtserialport package.


%package lib
Summary: lib components for the qtserialport package.
Group: Libraries

%description lib
lib components for the qtserialport package.


%prep
%setup -q -n qtserialport-everywhere-src-5.10.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
qmake QMAKE_CFLAGS="$CFLAGS" QMAKE_CXXFLAGS="$CXXFLAGS" QMAKE_LFLAGS="$LDFLAGS" \
    QMAKE_CFLAGS_RELEASE= QMAKE_CXXFLAGS_RELEASE=
test -r config.log && cat config.log
make  %{?_smp_mflags}

%install
make INSTALL_ROOT=%{buildroot} install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/qt5/QtSerialPort/5.10.1/QtSerialPort/private/qserialport_p.h
/usr/include/qt5/QtSerialPort/5.10.1/QtSerialPort/private/qserialportinfo_p.h
/usr/include/qt5/QtSerialPort/5.10.1/QtSerialPort/private/qtudev_p.h
/usr/include/qt5/QtSerialPort/5.10.1/QtSerialPort/private/qwinoverlappedionotifier_p.h
/usr/include/qt5/QtSerialPort/QSerialPort
/usr/include/qt5/QtSerialPort/QSerialPortInfo
/usr/include/qt5/QtSerialPort/QtSerialPort
/usr/include/qt5/QtSerialPort/QtSerialPortDepends
/usr/include/qt5/QtSerialPort/QtSerialPortVersion
/usr/include/qt5/QtSerialPort/qserialport.h
/usr/include/qt5/QtSerialPort/qserialportglobal.h
/usr/include/qt5/QtSerialPort/qserialportinfo.h
/usr/include/qt5/QtSerialPort/qtserialportversion.h
/usr/lib64/cmake/Qt5SerialPort/Qt5SerialPortConfig.cmake
/usr/lib64/cmake/Qt5SerialPort/Qt5SerialPortConfigVersion.cmake
/usr/lib64/libQt5SerialPort.la
/usr/lib64/libQt5SerialPort.prl
/usr/lib64/libQt5SerialPort.so
/usr/lib64/pkgconfig/Qt5SerialPort.pc
/usr/lib64/qt5/mkspecs/modules/qt_lib_serialport.pri
/usr/lib64/qt5/mkspecs/modules/qt_lib_serialport_private.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libQt5SerialPort.so.5
/usr/lib64/libQt5SerialPort.so.5.10
/usr/lib64/libQt5SerialPort.so.5.10.1
