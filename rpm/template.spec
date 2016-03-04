Name:           ros-indigo-geometry
Version:        1.11.8
Release:        0%{?dist}
Summary:        ROS geometry package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/geometry
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-angles
Requires:       ros-indigo-eigen-conversions
Requires:       ros-indigo-kdl-conversions
Requires:       ros-indigo-tf
Requires:       ros-indigo-tf-conversions
BuildRequires:  ros-indigo-catkin

%description
Geometry Library

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Fri Mar 04 2016 Tully Foote <tfoote@osrfoundation.org> - 1.11.8-0
- Autogenerated by Bloom

* Tue Apr 21 2015 Tully Foote <tfoote@osrfoundation.org> - 1.11.7-0
- Autogenerated by Bloom

* Wed Mar 25 2015 Tully Foote <tfoote@osrfoundation.org> - 1.11.6-0
- Autogenerated by Bloom

* Tue Mar 17 2015 Tully Foote <tfoote@osrfoundation.org> - 1.11.5-0
- Autogenerated by Bloom

* Tue Dec 23 2014 Tully Foote <tfoote@osrfoundation.org> - 1.11.4-0
- Autogenerated by Bloom

