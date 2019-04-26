Name:           darknet
Version:        %{VERSION}
Release:        %{RELEASE}%{?dist}
Summary:        Darknet Yolo v3 & v2 Neural Networks for object detection 
License:        PublicDomain
Group:          Development/Libraries/C and C++
Url:            https://github.com/hurdad/darknet
Source:         %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  cmake3
BuildRequires:	opencv-devel = 2.4.5

%description
Darknet Yolo v3 & v2 Neural Networks for object detection 

%package devel
Summary:    Development headers and library for %{name}
Group:      Development/Libraries
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the development headers and library for %{name}.

%prep
%setup -n %{name}-%{version}

%build
cmake3 -DCMAKE_BUILD_TYPE=Release .
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=%{buildroot}

mkdir -p %{buildroot}/usr/bin/
mkdir -p %{buildroot}/usr/include/darknet/
mkdir -p %{buildroot}/usr/lib64/
mkdir -p %{buildroot}/usr/share/darknet/

mv %{buildroot}/%{_builddir}/%{name}-%{version}/darknet %{buildroot}/usr/bin/
mv %{buildroot}/%{_builddir}/%{name}-%{version}/include/* %{buildroot}/usr/include/darknet/
mv %{buildroot}/%{_builddir}/%{name}-%{version}/lib/libdarklib.so %{buildroot}/usr/lib64
mv %{buildroot}/%{_builddir}/%{name}-%{version}/share/darknet/* %{buildroot}/usr/share/darknet

rm -rf %{buildroot}/%{_builddir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
ldconfig

%postun
ldconfig

%files
%defattr(-,root,root,-)
%doc LICENSE README.md
%{_bindir}/darknet
%{_libdir}/libdarklib.so
%{_datadir}/darknet/

%files devel
%defattr(-,root,root,-)
%{_includedir}/darknet/


%changelog
