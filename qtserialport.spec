#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : qtserialport
Version  : 5.12.3
Release  : 18
URL      : https://download.qt.io/official_releases/qt/5.12/5.12.3/submodules/qtserialport-everywhere-src-5.12.3.tar.xz
Source0  : https://download.qt.io/official_releases/qt/5.12/5.12.3/submodules/qtserialport-everywhere-src-5.12.3.tar.xz
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
%setup -q -n qtserialport-everywhere-src-5.12.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
%qmake
test -r config.log && cat config.log
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1556914415
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qtserialport
cp LICENSE.FDL %{buildroot}/usr/share/package-licenses/qtserialport/LICENSE.FDL
cp LICENSE.GPL2 %{buildroot}/usr/share/package-licenses/qtserialport/LICENSE.GPL2
cp LICENSE.GPL3 %{buildroot}/usr/share/package-licenses/qtserialport/LICENSE.GPL3
cp LICENSE.GPL3-EXCEPT %{buildroot}/usr/share/package-licenses/qtserialport/LICENSE.GPL3-EXCEPT
cp LICENSE.LGPL3 %{buildroot}/usr/share/package-licenses/qtserialport/LICENSE.LGPL3
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/qt5/QtSerialPort/5.12.3/QtSerialPort/private/qserialport_p.h
/usr/include/qt5/QtSerialPort/5.12.3/QtSerialPort/private/qserialportinfo_p.h
/usr/include/qt5/QtSerialPort/5.12.3/QtSerialPort/private/qtudev_p.h
/usr/include/qt5/QtSerialPort/5.12.3/QtSerialPort/private/qwinoverlappedionotifier_p.h
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
/usr/lib64/libQt5SerialPort.prl
/usr/lib64/libQt5SerialPort.so
/usr/lib64/pkgconfig/Qt5SerialPort.pc
/usr/lib64/qt5/mkspecs/modules/qt_lib_serialport.pri
/usr/lib64/qt5/mkspecs/modules/qt_lib_serialport_private.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libQt5SerialPort.so.5
/usr/lib64/libQt5SerialPort.so.5.12
/usr/lib64/libQt5SerialPort.so.5.12.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qtserialport/LICENSE.FDL
/usr/share/package-licenses/qtserialport/LICENSE.GPL2
/usr/share/package-licenses/qtserialport/LICENSE.GPL3
/usr/share/package-licenses/qtserialport/LICENSE.GPL3-EXCEPT
/usr/share/package-licenses/qtserialport/LICENSE.LGPL3
