#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v18
# autospec commit: f35655a
#
Name     : nfs-utils
Version  : 2.7.1
Release  : 52
URL      : https://sourceforge.net/projects/nfs/files/nfs-utils/2.7.1/nfs-utils-2.7.1.tar.gz
Source0  : https://sourceforge.net/projects/nfs/files/nfs-utils/2.7.1/nfs-utils-2.7.1.tar.gz
Source1  : nfs-utils.tmpfiles
Summary  : Library that handles mapping between names and ids for NFSv4.
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0
Requires: nfs-utils-bin = %{version}-%{release}
Requires: nfs-utils-config = %{version}-%{release}
Requires: nfs-utils-lib = %{version}-%{release}
Requires: nfs-utils-libexec = %{version}-%{release}
Requires: nfs-utils-license = %{version}-%{release}
Requires: nfs-utils-man = %{version}-%{release}
Requires: nfs-utils-services = %{version}-%{release}
Requires: rpcbind
BuildRequires : LVM2-dev
BuildRequires : buildreq-configure
BuildRequires : cyrus-sasl-dev
BuildRequires : e2fsprogs-dev
BuildRequires : file
BuildRequires : glibc-staticdev
BuildRequires : keyutils-dev
BuildRequires : libcap-dev
BuildRequires : libtirpc-dev
BuildRequires : libxml2-dev
BuildRequires : openldap-dev
BuildRequires : pkgconfig(libevent)
BuildRequires : pkgconfig(mount)
BuildRequires : sqlite-autoconf-dev
BuildRequires : util-linux-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Enabling-nfs-client-by-default-on-installation.patch
Patch2: 0002-Require-rpcbind-for-nfs-server.patch
Patch3: build-gcc12.patch

%description
This is nfs-utils, the Linux NFS userland utility package.
0. PROJECT RESOURCES
Home page:  http://sourceforge.net/projects/nfs/

%package bin
Summary: bin components for the nfs-utils package.
Group: Binaries
Requires: nfs-utils-libexec = %{version}-%{release}
Requires: nfs-utils-config = %{version}-%{release}
Requires: nfs-utils-license = %{version}-%{release}
Requires: nfs-utils-services = %{version}-%{release}

%description bin
bin components for the nfs-utils package.


%package config
Summary: config components for the nfs-utils package.
Group: Default

%description config
config components for the nfs-utils package.


%package dev
Summary: dev components for the nfs-utils package.
Group: Development
Requires: nfs-utils-lib = %{version}-%{release}
Requires: nfs-utils-bin = %{version}-%{release}
Provides: nfs-utils-devel = %{version}-%{release}
Requires: nfs-utils = %{version}-%{release}

%description dev
dev components for the nfs-utils package.


%package extras
Summary: extras components for the nfs-utils package.
Group: Default

%description extras
extras components for the nfs-utils package.


%package lib
Summary: lib components for the nfs-utils package.
Group: Libraries
Requires: nfs-utils-libexec = %{version}-%{release}
Requires: nfs-utils-license = %{version}-%{release}

%description lib
lib components for the nfs-utils package.


%package libexec
Summary: libexec components for the nfs-utils package.
Group: Default
Requires: nfs-utils-config = %{version}-%{release}
Requires: nfs-utils-license = %{version}-%{release}

%description libexec
libexec components for the nfs-utils package.


%package license
Summary: license components for the nfs-utils package.
Group: Default

%description license
license components for the nfs-utils package.


%package man
Summary: man components for the nfs-utils package.
Group: Default

%description man
man components for the nfs-utils package.


%package services
Summary: services components for the nfs-utils package.
Group: Systemd services
Requires: systemd

%description services
services components for the nfs-utils package.


%prep
%setup -q -n nfs-utils-2.7.1
cd %{_builddir}/nfs-utils-2.7.1
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
pushd ..
cp -a nfs-utils-2.7.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1724278897
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
export GOAMD64=v2
%reconfigure --disable-static --without-tcp-wrappers \
--disable-gss \
--disable-ipv6 \
--enable-tirpc \
--with-systemd=/usr/lib/systemd/system \
--with-statedir=/run/nfs \
--with-pluginpath=/usr/lib64/libnfsidmap/
make  %{?_smp_mflags}
unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%reconfigure --disable-static --without-tcp-wrappers \
--disable-gss \
--disable-ipv6 \
--enable-tirpc \
--with-systemd=/usr/lib/systemd/system \
--with-statedir=/run/nfs \
--with-pluginpath=/usr/lib64/libnfsidmap/
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
export SOURCE_DATE_EPOCH=1724278897
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/nfs-utils
cp %{_builddir}/nfs-utils-%{version}/COPYING %{buildroot}/usr/share/package-licenses/nfs-utils/60457201edeb887de11bf46b66fc02494d08ef4d || :
cp %{_builddir}/nfs-utils-%{version}/support/nfsidmap/COPYING %{buildroot}/usr/share/package-licenses/nfs-utils/82c1cadc8c3bb346234c740b2b77c7d607b8f9ac || :
cp %{_builddir}/nfs-utils-%{version}/utils/statd/COPYING %{buildroot}/usr/share/package-licenses/nfs-utils/74a8a6531a42e124df07ab5599aad63870fa0bd4 || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/tmpfiles.d/nfs-utils.conf
## install_append content
mkdir -p %{buildroot}/usr/lib/systemd/scripts
install -Dm755 -t %{buildroot}/usr/lib/systemd/scripts systemd/nfs-utils_env.sh
rm -rf %{buildroot}/run
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/V3/usr/lib/systemd/system-generators/nfs-server-generator
/V3/usr/lib/systemd/system-generators/rpc-pipefs-generator
/usr/lib/systemd/scripts/nfs-utils_env.sh
/usr/lib/systemd/system-generators/nfs-server-generator
/usr/lib/systemd/system-generators/rpc-pipefs-generator

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/blkmapd
/V3/usr/bin/exportfs
/V3/usr/bin/fsidd
/V3/usr/bin/nfsconf
/V3/usr/bin/nfsdcld
/V3/usr/bin/nfsdcltrack
/V3/usr/bin/nfsidmap
/V3/usr/bin/nfsref
/V3/usr/bin/nfsstat
/V3/usr/bin/rpc.idmapd
/V3/usr/bin/rpc.mountd
/V3/usr/bin/rpc.nfsd
/V3/usr/bin/rpc.statd
/V3/usr/bin/rpcdebug
/V3/usr/bin/showmount
/V3/usr/bin/sm-notify
/usr/bin/blkmapd
/usr/bin/exportfs
/usr/bin/fsidd
/usr/bin/mount.nfs
/usr/bin/mount.nfs4
/usr/bin/nfsconf
/usr/bin/nfsdcld
/usr/bin/nfsdcltrack
/usr/bin/nfsidmap
/usr/bin/nfsref
/usr/bin/nfsstat
/usr/bin/rpc.idmapd
/usr/bin/rpc.mountd
/usr/bin/rpc.nfsd
/usr/bin/rpc.statd
/usr/bin/rpcctl
/usr/bin/rpcdebug
/usr/bin/showmount
/usr/bin/sm-notify
/usr/bin/start-statd
/usr/bin/umount.nfs
/usr/bin/umount.nfs4

%files config
%defattr(-,root,root,-)
/usr/lib/tmpfiles.d/nfs-utils.conf
/usr/lib/udev/rules.d/60-nfs.rules
/usr/lib/udev/rules.d/99-nfs.rules

%files dev
%defattr(-,root,root,-)
/usr/include/nfsidmap.h
/usr/include/nfsidmap_plugin.h
/usr/lib64/libnfsidmap.so
/usr/lib64/pkgconfig/libnfsidmap.pc
/usr/share/man/man3/nfs4_uid_to_name.3

%files extras
%defattr(-,root,root,-)
/usr/bin/mountstats
/usr/bin/nfsdclddb
/usr/bin/nfsdclnts
/usr/bin/nfsiostat

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libnfsidmap.so.1.0.0
/V3/usr/lib64/libnfsidmap/nsswitch.so
/V3/usr/lib64/libnfsidmap/regex.so
/V3/usr/lib64/libnfsidmap/static.so
/V3/usr/lib64/libnfsidmap/umich_ldap.so
/usr/lib64/libnfsidmap.so.1
/usr/lib64/libnfsidmap.so.1.0.0
/usr/lib64/libnfsidmap/nsswitch.so
/usr/lib64/libnfsidmap/regex.so
/usr/lib64/libnfsidmap/static.so
/usr/lib64/libnfsidmap/umich_ldap.so

%files libexec
%defattr(-,root,root,-)
/V3/usr/libexec/nfsrahead
/usr/libexec/nfsrahead

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/nfs-utils/60457201edeb887de11bf46b66fc02494d08ef4d
/usr/share/package-licenses/nfs-utils/74a8a6531a42e124df07ab5599aad63870fa0bd4
/usr/share/package-licenses/nfs-utils/82c1cadc8c3bb346234c740b2b77c7d607b8f9ac

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man5/exports.5
/usr/share/man/man5/idmapd.conf.5
/usr/share/man/man5/nfs.5
/usr/share/man/man5/nfs.conf.5
/usr/share/man/man5/nfsmount.conf.5
/usr/share/man/man5/nfsrahead.5
/usr/share/man/man7/nfs.systemd.7
/usr/share/man/man7/nfsd.7
/usr/share/man/man8/blkmapd.8
/usr/share/man/man8/exportfs.8
/usr/share/man/man8/idmapd.8
/usr/share/man/man8/mount.nfs.8
/usr/share/man/man8/mountd.8
/usr/share/man/man8/mountstats.8
/usr/share/man/man8/nfsconf.8
/usr/share/man/man8/nfsd.8
/usr/share/man/man8/nfsdcld.8
/usr/share/man/man8/nfsdclddb.8
/usr/share/man/man8/nfsdclnts.8
/usr/share/man/man8/nfsdcltrack.8
/usr/share/man/man8/nfsidmap.8
/usr/share/man/man8/nfsiostat.8
/usr/share/man/man8/nfsref.8
/usr/share/man/man8/nfsstat.8
/usr/share/man/man8/rpc.idmapd.8
/usr/share/man/man8/rpc.mountd.8
/usr/share/man/man8/rpc.nfsd.8
/usr/share/man/man8/rpc.sm-notify.8
/usr/share/man/man8/rpc.statd.8
/usr/share/man/man8/rpcctl.8
/usr/share/man/man8/rpcdebug.8
/usr/share/man/man8/showmount.8
/usr/share/man/man8/sm-notify.8
/usr/share/man/man8/statd.8
/usr/share/man/man8/umount.nfs.8

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/fsidd.service
/usr/lib/systemd/system/nfs-blkmap.service
/usr/lib/systemd/system/nfs-client.target
/usr/lib/systemd/system/nfs-idmapd.service
/usr/lib/systemd/system/nfs-mountd.service
/usr/lib/systemd/system/nfs-server.service
/usr/lib/systemd/system/nfs-utils.service
/usr/lib/systemd/system/nfsdcld.service
/usr/lib/systemd/system/proc-fs-nfsd.mount
/usr/lib/systemd/system/rpc-statd-notify.service
/usr/lib/systemd/system/rpc-statd.service
/usr/lib/systemd/system/rpc_pipefs.target
/usr/lib/systemd/system/run-nfs-rpc_pipefs.mount
