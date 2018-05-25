#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : nfs-utils
Version  : 2.3.2
Release  : 28
URL      : https://sourceforge.net/projects/nfs/files/nfs-utils/2.3.2/nfs-utils-2.3.2.tar.bz2
Source0  : https://sourceforge.net/projects/nfs/files/nfs-utils/2.3.2/nfs-utils-2.3.2.tar.bz2
Source1  : nfs-utils.tmpfiles
Summary  : Library that handles mapping between names and ids for NFSv4.
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0
Requires: nfs-utils-bin
Requires: nfs-utils-config
Requires: nfs-utils-lib
Requires: nfs-utils-man
BuildRequires : LVM2-dev
BuildRequires : e2fsprogs-dev
BuildRequires : glibc-staticdev
BuildRequires : keyutils-dev
BuildRequires : libcap-dev
BuildRequires : libtirpc-dev
BuildRequires : openldap-dev
BuildRequires : pkgconfig(libevent)
BuildRequires : sqlite-autoconf-dev
BuildRequires : util-linux-dev
Patch1: 0003-add-nfs-utils-env-script.patch
Patch2: 0004-require-rpcbind-for-nfs-server.patch
Patch3: 0005-missing-header.patch

%description
This is nfs-utils, the Linux NFS userland utility package.
0. PROJECT RESOURCES
Home page:  http://sourceforge.net/projects/nfs/

%package bin
Summary: bin components for the nfs-utils package.
Group: Binaries
Requires: nfs-utils-config
Requires: nfs-utils-man

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
Requires: nfs-utils-lib
Requires: nfs-utils-bin
Provides: nfs-utils-devel

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

%description lib
lib components for the nfs-utils package.


%package man
Summary: man components for the nfs-utils package.
Group: Default

%description man
man components for the nfs-utils package.


%prep
%setup -q -n nfs-utils-2.3.2
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1527276875
%configure --disable-static --without-tcp-wrappers --disable-gss --disable-ipv6 --disable-tirpc --with-systemd=/usr/lib/systemd/system --with-statedir=/run/nfs --with-pluginpath=/usr/lib64/libnfsidmap/
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1527276875
rm -rf %{buildroot}
%make_install
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/tmpfiles.d/nfs-utils.conf
## make_install_append content
mkdir -p %{buildroot}/usr/lib/systemd/scripts
cp systemd/nfs-utils_env.sh %{buildroot}/usr/lib/systemd/scripts
chmod 755 %{buildroot}/usr/lib/systemd/scripts/nfs-utils_env.sh
rm -rf %{buildroot}/run
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/mountstats
%exclude /usr/bin/nfsiostat
/usr/bin/blkmapd
/usr/bin/exportfs
/usr/bin/mount.nfs
/usr/bin/mount.nfs4
/usr/bin/nfsconf
/usr/bin/nfsdcltrack
/usr/bin/nfsidmap
/usr/bin/nfsstat
/usr/bin/osd_login
/usr/bin/rpc.idmapd
/usr/bin/rpc.mountd
/usr/bin/rpc.nfsd
/usr/bin/rpc.statd
/usr/bin/rpcdebug
/usr/bin/showmount
/usr/bin/sm-notify
/usr/bin/start-statd
/usr/bin/umount.nfs
/usr/bin/umount.nfs4

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/scripts/nfs-utils_env.sh
/usr/lib/systemd/system-generators/nfs-server-generator
/usr/lib/systemd/system-generators/rpc-pipefs-generator
/usr/lib/systemd/system/nfs-blkmap.service
/usr/lib/systemd/system/nfs-client.target
/usr/lib/systemd/system/nfs-idmapd.service
/usr/lib/systemd/system/nfs-mountd.service
/usr/lib/systemd/system/nfs-server.service
/usr/lib/systemd/system/nfs-utils.service
/usr/lib/systemd/system/proc-fs-nfsd.mount
/usr/lib/systemd/system/rpc-statd-notify.service
/usr/lib/systemd/system/rpc-statd.service
/usr/lib/systemd/system/rpc_pipefs.target
/usr/lib/systemd/system/var-lib-nfs-rpc_pipefs.mount
/usr/lib/tmpfiles.d/nfs-utils.conf

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/libnfsidmap.so
/usr/lib64/pkgconfig/libnfsidmap.pc

%files extras
%defattr(-,root,root,-)
/usr/bin/mountstats
/usr/bin/nfsiostat

%files lib
%defattr(-,root,root,-)
/usr/lib64/libnfsidmap.so.1
/usr/lib64/libnfsidmap.so.1.0.0
/usr/lib64/libnfsidmap/nsswitch.so
/usr/lib64/libnfsidmap/static.so
/usr/lib64/libnfsidmap/umich_ldap.so

%files man
%defattr(-,root,root,-)
/usr/share/man/man3/nfs4_uid_to_name.3
/usr/share/man/man5/exports.5
/usr/share/man/man5/idmapd.conf.5
/usr/share/man/man5/nfs.5
/usr/share/man/man5/nfs.conf.5
/usr/share/man/man5/nfsmount.conf.5
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
/usr/share/man/man8/nfsdcltrack.8
/usr/share/man/man8/nfsidmap.8
/usr/share/man/man8/nfsiostat.8
/usr/share/man/man8/nfsstat.8
/usr/share/man/man8/rpc.idmapd.8
/usr/share/man/man8/rpc.mountd.8
/usr/share/man/man8/rpc.nfsd.8
/usr/share/man/man8/rpc.sm-notify.8
/usr/share/man/man8/rpc.statd.8
/usr/share/man/man8/rpcdebug.8
/usr/share/man/man8/showmount.8
/usr/share/man/man8/sm-notify.8
/usr/share/man/man8/statd.8
/usr/share/man/man8/umount.nfs.8
