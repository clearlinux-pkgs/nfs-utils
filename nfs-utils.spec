#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : nfs-utils
Version  : 1.3.3
Release  : 13
URL      : http://downloads.sourceforge.net/project/nfs/nfs-utils/1.3.3/nfs-utils-1.3.3.tar.bz2
Source0  : http://downloads.sourceforge.net/project/nfs/nfs-utils/1.3.3/nfs-utils-1.3.3.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: nfs-utils-bin
Requires: nfs-utils-config
Requires: nfs-utils-doc
BuildRequires : LVM2-dev
BuildRequires : e2fsprogs-dev
BuildRequires : keyutils-dev
BuildRequires : libcap-dev
BuildRequires : libevent-dev
BuildRequires : libnfsidmap-dev
BuildRequires : libtirpc-dev
BuildRequires : sqlite-autoconf-dev
BuildRequires : util-linux-dev
Patch1: 0002-fix-rpc-statd-start.patch
Patch2: 0003-add-nfs-utils-env-script.patch

%description
This is nfs-utils, the Linux NFS userland utility package.
0. PROJECT RESOURCES
Home page:  http://sourceforge.net/projects/nfs/

%package bin
Summary: bin components for the nfs-utils package.
Group: Binaries
Requires: nfs-utils-config

%description bin
bin components for the nfs-utils package.


%package config
Summary: config components for the nfs-utils package.
Group: Default

%description config
config components for the nfs-utils package.


%package doc
Summary: doc components for the nfs-utils package.
Group: Documentation

%description doc
doc components for the nfs-utils package.


%package extras
Summary: extras components for the nfs-utils package.
Group: Default

%description extras
extras components for the nfs-utils package.


%prep
%setup -q -n nfs-utils-1.3.3
%patch1 -p1
%patch2 -p1

%build
%configure --disable-static --without-tcp-wrappers --disable-gss --disable-ipv6 --disable-tirpc --with-systemd=/usr/lib/systemd/system
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install
## make_install_append content
mkdir -p %{buildroot}/usr/lib/systemd/scripts
mkdir -p %{buildroot}/usr/lib/systemd/system/sockets.target.wants
mkdir -p %{buildroot}/usr/lib/systemd/system/multi-user.target.wants
ln -s /usr/lib/systemd/system/rpcbind.socket %{buildroot}/usr/lib/systemd/system/sockets.target.wants/rpcbind.socket
ln -s /usr/lib/systemd/system/rpcbind.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/rpcbind.service
cp systemd/nfs-utils_env.sh %{buildroot}/usr/lib/systemd/scripts
chmod 755 %{buildroot}/usr/lib/systemd/scripts/nfs-utils_env.sh
## make_install_append end

%files
%defattr(-,root,root,-)
/var/lib/nfs/etab
/var/lib/nfs/rmtab
/var/lib/nfs/state
/var/lib/nfs/xtab

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/mountstats
%exclude /usr/bin/nfsiostat
/usr/bin/blkmapd
/usr/bin/exportfs
/usr/bin/mount.nfs
/usr/bin/mount.nfs4
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
/usr/lib/systemd/system/multi-user.target.wants/rpcbind.service
/usr/lib/systemd/system/nfs-blkmap.service
/usr/lib/systemd/system/nfs-client.target
/usr/lib/systemd/system/nfs-config.service
/usr/lib/systemd/system/nfs-idmapd.service
/usr/lib/systemd/system/nfs-mountd.service
/usr/lib/systemd/system/nfs-server.service
/usr/lib/systemd/system/nfs-utils.service
/usr/lib/systemd/system/proc-fs-nfsd.mount
/usr/lib/systemd/system/rpc-statd-notify.service
/usr/lib/systemd/system/rpc-statd.service
/usr/lib/systemd/system/sockets.target.wants/rpcbind.socket
/usr/lib/systemd/system/var-lib-nfs-rpc_pipefs.mount

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man5/*
%doc /usr/share/man/man7/*
%doc /usr/share/man/man8/*

%files extras
%defattr(-,root,root,-)
/usr/bin/mountstats
/usr/bin/nfsiostat
