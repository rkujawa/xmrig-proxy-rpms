Name:		xmrig-proxy
Version:	2.6.0	
Release:	1%{?dist}
Summary:	Monero (XMR) Stratum protocol proxy.

Group:		System Environment/Base	
License:	GPLv3
URL:		https://github.com/xmrig/xmrig-proxy
Source0:	xmrig-proxy-2.6.0.tar.gz

# note this requires source scl_source enable devtoolset-7 before running rpmbuild
BuildRequires:	cmake libuv-devel libmicrohttpd-devel devtoolset-7-gcc-c++ devtoolset-7-libstdc++-devel libuuid-devel
Requires:	libuv libmicrohttpd libuuid

%description
Monero (XMR) Stratum protocol proxy.

%prep
%setup -q

%build
cmake .
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}/usr/bin/
install -m 755 xmrig-proxy %{buildroot}/usr/bin/xmrig-proxy

%files
/usr/bin/xmrig-proxy

%changelog

