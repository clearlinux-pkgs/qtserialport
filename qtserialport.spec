#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : qtserialport
Version  : 5.15.2
Release  : 27
URL      : https://download.qt.io/official_releases/qt/5.15/5.15.2/submodules/qtserialport-everywhere-src-5.15.2.tar.xz
Source0  : https://download.qt.io/official_releases/qt/5.15/5.15.2/submodules/qtserialport-everywhere-src-5.15.2.tar.xz
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


%package examples
Summary: examples components for the qtserialport package.
Group: Default
Requires: qtserialport-dev = %{version}-%{release}

%description examples
examples components for the qtserialport package.


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
%setup -q -n qtserialport-everywhere-src-5.15.2
cd %{_builddir}/qtserialport-everywhere-src-5.15.2

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
export SOURCE_DATE_EPOCH=1630804259
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qtserialport
cp %{_builddir}/qtserialport-everywhere-src-5.15.2/LICENSE.FDL %{buildroot}/usr/share/package-licenses/qtserialport/61907422fefcd2313a9b570c31d203a6dbebd333
cp %{_builddir}/qtserialport-everywhere-src-5.15.2/LICENSE.GPL2 %{buildroot}/usr/share/package-licenses/qtserialport/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/qtserialport-everywhere-src-5.15.2/LICENSE.GPL3 %{buildroot}/usr/share/package-licenses/qtserialport/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/qtserialport-everywhere-src-5.15.2/LICENSE.GPL3-EXCEPT %{buildroot}/usr/share/package-licenses/qtserialport/e93757aefa405f2c9a8a55e780ae9c39542dfc3a
cp %{_builddir}/qtserialport-everywhere-src-5.15.2/LICENSE.LGPL3 %{buildroot}/usr/share/package-licenses/qtserialport/f45ee1c765646813b442ca58de72e20a64a7ddba
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/qt5/QtSerialPort/5.15.2/QtSerialPort/private/qserialport_p.h
/usr/include/qt5/QtSerialPort/5.15.2/QtSerialPort/private/qserialportinfo_p.h
/usr/include/qt5/QtSerialPort/5.15.2/QtSerialPort/private/qtntdll_p.h
/usr/include/qt5/QtSerialPort/5.15.2/QtSerialPort/private/qtserialport-config_p.h
/usr/include/qt5/QtSerialPort/5.15.2/QtSerialPort/private/qtudev_p.h
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

%files examples
%defattr(-,root,root,-)
/usr/share/qt5/examples/serialport/blockingmaster/blockingmaster.pro
/usr/share/qt5/examples/serialport/blockingmaster/dialog.cpp
/usr/share/qt5/examples/serialport/blockingmaster/dialog.h
/usr/share/qt5/examples/serialport/blockingmaster/main.cpp
/usr/share/qt5/examples/serialport/blockingmaster/masterthread.cpp
/usr/share/qt5/examples/serialport/blockingmaster/masterthread.h
/usr/share/qt5/examples/serialport/blockingslave/blockingslave.pro
/usr/share/qt5/examples/serialport/blockingslave/dialog.cpp
/usr/share/qt5/examples/serialport/blockingslave/dialog.h
/usr/share/qt5/examples/serialport/blockingslave/main.cpp
/usr/share/qt5/examples/serialport/blockingslave/slavethread.cpp
/usr/share/qt5/examples/serialport/blockingslave/slavethread.h
/usr/share/qt5/examples/serialport/cenumerator/cenumerator.pro
/usr/share/qt5/examples/serialport/cenumerator/main.cpp
/usr/share/qt5/examples/serialport/creaderasync/creaderasync.pro
/usr/share/qt5/examples/serialport/creaderasync/main.cpp
/usr/share/qt5/examples/serialport/creaderasync/serialportreader.cpp
/usr/share/qt5/examples/serialport/creaderasync/serialportreader.h
/usr/share/qt5/examples/serialport/creadersync/creadersync.pro
/usr/share/qt5/examples/serialport/creadersync/main.cpp
/usr/share/qt5/examples/serialport/cwriterasync/cwriterasync.pro
/usr/share/qt5/examples/serialport/cwriterasync/main.cpp
/usr/share/qt5/examples/serialport/cwriterasync/serialportwriter.cpp
/usr/share/qt5/examples/serialport/cwriterasync/serialportwriter.h
/usr/share/qt5/examples/serialport/cwritersync/cwritersync.pro
/usr/share/qt5/examples/serialport/cwritersync/main.cpp
/usr/share/qt5/examples/serialport/enumerator/enumerator.pro
/usr/share/qt5/examples/serialport/enumerator/main.cpp
/usr/share/qt5/examples/serialport/master/dialog.cpp
/usr/share/qt5/examples/serialport/master/dialog.h
/usr/share/qt5/examples/serialport/master/main.cpp
/usr/share/qt5/examples/serialport/master/master.pro
/usr/share/qt5/examples/serialport/serialport.pro
/usr/share/qt5/examples/serialport/slave/dialog.cpp
/usr/share/qt5/examples/serialport/slave/dialog.h
/usr/share/qt5/examples/serialport/slave/main.cpp
/usr/share/qt5/examples/serialport/slave/slave.pro
/usr/share/qt5/examples/serialport/terminal/console.cpp
/usr/share/qt5/examples/serialport/terminal/console.h
/usr/share/qt5/examples/serialport/terminal/images/application-exit.png
/usr/share/qt5/examples/serialport/terminal/images/clear.png
/usr/share/qt5/examples/serialport/terminal/images/connect.png
/usr/share/qt5/examples/serialport/terminal/images/disconnect.png
/usr/share/qt5/examples/serialport/terminal/images/settings.png
/usr/share/qt5/examples/serialport/terminal/main.cpp
/usr/share/qt5/examples/serialport/terminal/mainwindow.cpp
/usr/share/qt5/examples/serialport/terminal/mainwindow.h
/usr/share/qt5/examples/serialport/terminal/mainwindow.ui
/usr/share/qt5/examples/serialport/terminal/settingsdialog.cpp
/usr/share/qt5/examples/serialport/terminal/settingsdialog.h
/usr/share/qt5/examples/serialport/terminal/settingsdialog.ui
/usr/share/qt5/examples/serialport/terminal/terminal.pro
/usr/share/qt5/examples/serialport/terminal/terminal.qrc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libQt5SerialPort.so.5
/usr/lib64/libQt5SerialPort.so.5.15
/usr/lib64/libQt5SerialPort.so.5.15.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qtserialport/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/qtserialport/61907422fefcd2313a9b570c31d203a6dbebd333
/usr/share/package-licenses/qtserialport/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/qtserialport/e93757aefa405f2c9a8a55e780ae9c39542dfc3a
/usr/share/package-licenses/qtserialport/f45ee1c765646813b442ca58de72e20a64a7ddba
