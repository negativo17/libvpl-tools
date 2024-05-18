Name:           libvpl-tools
Version:        1.0.0
Release:        3%{?dist}
Summary:        Intel Video Processing Library (Intel VPL) Tools
License:        MIT
URL:            https://intel.github.io/libvpl/latest/index.html
ExclusiveArch:  x86_64

Source0:        https://github.com/intel/libvpl-tools/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         libvpl-tools-fedora.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gtest-devel
BuildRequires:  libvpl-devel >= 2.11.0
BuildRequires:  pkgconfig(libdrm) >= 2.4.91
BuildRequires:  pkgconfig(libva) >= 1.2
BuildRequires:  pkgconfig(libva-drm) >= 1.2
BuildRequires:  pkgconfig(libva-x11) >= 1.10.0
BuildRequires:  pkgconfig(pciaccess)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.15
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-dri3)
BuildRequires:  pkgconfig(xcb-present)

%description
Intel Video Processing Library (Intel VPL) tools provide access to hardware
accelerated video decode, encode, and frame processing capabilities on Intel
GPUs from the command line.

The tools require the Intel VPL base library and a runtime library installed.
Current runtime implementations:

- Intel VPL GPU Runtime for use on Intel Iris Xe graphics and newer
- Intel Media SDK for use on legacy Intel graphics

%prep
%autosetup -p1

# delete bundled googletest
rm -rf ext/*

%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_TESTS=ON \
    -DTOOLS_ENABLE_OPENCL=ON
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE
%doc README.md CONTRIBUTING.md third-party-programs.txt
%{_bindir}/system_analyzer
%{_bindir}/val-surface-sharing
%{_bindir}/vpl-import-export
%{_bindir}/vpl-inspect
%{_bindir}/sample_decode
%{_bindir}/sample_vpp
%{_bindir}/sample_encode
%{_bindir}/sample_multi_transcode
%{_bindir}/metrics_monitor
%dir %{_libdir}/vpl-tools
%{_libdir}/vpl-tools/libvpl_wayland.so
%{_libdir}/libcttmetrics.so

%changelog
* Fri May 17 2024 Ali Erdinc Koroglu <aekoroglu@fedoraproject.org> - 1.0.0-3
- Bundled googletest removed

* Sat May 04 2024 Simone Caronni <negativo17@gmail.com> - 1.0.0-2
- Require libvpl 2.11.0 for building.

* Sat May 04 2024 Simone Caronni <negativo17@gmail.com> - 1.0.0-1
- First build.
