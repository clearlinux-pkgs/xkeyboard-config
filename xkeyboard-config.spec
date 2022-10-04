#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x0661D98FC933A145 (sergey.udaltsov@gmail.com)
#
Name     : xkeyboard-config
Version  : 2.37
Release  : 34
URL      : https://www.x.org/releases/individual/data/xkeyboard-config/xkeyboard-config-2.37.tar.xz
Source0  : https://www.x.org/releases/individual/data/xkeyboard-config/xkeyboard-config-2.37.tar.xz
Source1  : https://www.x.org/releases/individual/data/xkeyboard-config/xkeyboard-config-2.37.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : ICU
Requires: xkeyboard-config-data = %{version}-%{release}
Requires: xkeyboard-config-license = %{version}-%{release}
Requires: xkeyboard-config-locales = %{version}-%{release}
Requires: xkeyboard-config-man = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : libxslt-bin
BuildRequires : pkgconfig(fontsproto)
BuildRequires : pkgconfig(inputproto)
BuildRequires : pkgconfig(xcb)
BuildRequires : pkgconfig(xextproto)
BuildRequires : pkgconfig(xkbcomp)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xorg-server)
BuildRequires : pkgconfig(xproto)
BuildRequires : pkgconfig(xtrans)

%description
X Keyboard Extension
--------------------
The X Keyboard (XKB) Extension essentially replaces the core protocol
definition of a keyboard. The extension makes it possible to specify
clearly and explicitly most aspects of keyboard behaviour on a per-key
basis, and to track more closely the logical and physical state of a
keyboard. It also includes a number of keyboard controls designed to
make keyboards more accessible to people with physical impairments.

%package data
Summary: data components for the xkeyboard-config package.
Group: Data

%description data
data components for the xkeyboard-config package.


%package dev
Summary: dev components for the xkeyboard-config package.
Group: Development
Requires: xkeyboard-config-data = %{version}-%{release}
Provides: xkeyboard-config-devel = %{version}-%{release}
Requires: xkeyboard-config = %{version}-%{release}

%description dev
dev components for the xkeyboard-config package.


%package license
Summary: license components for the xkeyboard-config package.
Group: Default

%description license
license components for the xkeyboard-config package.


%package locales
Summary: locales components for the xkeyboard-config package.
Group: Default

%description locales
locales components for the xkeyboard-config package.


%package man
Summary: man components for the xkeyboard-config package.
Group: Default

%description man
man components for the xkeyboard-config package.


%prep
%setup -q -n xkeyboard-config-2.37
cd %{_builddir}/xkeyboard-config-2.37

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1664927852
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/xkeyboard-config
cp %{_builddir}/xkeyboard-config-%{version}/COPYING %{buildroot}/usr/share/package-licenses/xkeyboard-config/40f6d7c0dba74ddd10663dfa50c2659cbe251423
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang xkeyboard-config

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/X11/xkb/compat/README
/usr/share/X11/xkb/compat/accessx
/usr/share/X11/xkb/compat/basic
/usr/share/X11/xkb/compat/caps
/usr/share/X11/xkb/compat/complete
/usr/share/X11/xkb/compat/iso9995
/usr/share/X11/xkb/compat/japan
/usr/share/X11/xkb/compat/ledcaps
/usr/share/X11/xkb/compat/ledcompose
/usr/share/X11/xkb/compat/lednum
/usr/share/X11/xkb/compat/ledscroll
/usr/share/X11/xkb/compat/level5
/usr/share/X11/xkb/compat/misc
/usr/share/X11/xkb/compat/mousekeys
/usr/share/X11/xkb/compat/olpc
/usr/share/X11/xkb/compat/pc
/usr/share/X11/xkb/compat/pc98
/usr/share/X11/xkb/compat/xfree86
/usr/share/X11/xkb/compat/xtest
/usr/share/X11/xkb/geometry/README
/usr/share/X11/xkb/geometry/amiga
/usr/share/X11/xkb/geometry/ataritt
/usr/share/X11/xkb/geometry/chicony
/usr/share/X11/xkb/geometry/dell
/usr/share/X11/xkb/geometry/digital_vndr/lk
/usr/share/X11/xkb/geometry/digital_vndr/pc
/usr/share/X11/xkb/geometry/digital_vndr/unix
/usr/share/X11/xkb/geometry/everex
/usr/share/X11/xkb/geometry/fujitsu
/usr/share/X11/xkb/geometry/hhk
/usr/share/X11/xkb/geometry/hp
/usr/share/X11/xkb/geometry/keytronic
/usr/share/X11/xkb/geometry/kinesis
/usr/share/X11/xkb/geometry/macintosh
/usr/share/X11/xkb/geometry/microsoft
/usr/share/X11/xkb/geometry/nec
/usr/share/X11/xkb/geometry/nokia
/usr/share/X11/xkb/geometry/northgate
/usr/share/X11/xkb/geometry/pc
/usr/share/X11/xkb/geometry/sanwa
/usr/share/X11/xkb/geometry/sgi_vndr/O2
/usr/share/X11/xkb/geometry/sgi_vndr/indigo
/usr/share/X11/xkb/geometry/sgi_vndr/indy
/usr/share/X11/xkb/geometry/sony
/usr/share/X11/xkb/geometry/steelseries
/usr/share/X11/xkb/geometry/sun
/usr/share/X11/xkb/geometry/teck
/usr/share/X11/xkb/geometry/thinkpad
/usr/share/X11/xkb/geometry/typematrix
/usr/share/X11/xkb/geometry/winbook
/usr/share/X11/xkb/keycodes/README
/usr/share/X11/xkb/keycodes/aliases
/usr/share/X11/xkb/keycodes/amiga
/usr/share/X11/xkb/keycodes/ataritt
/usr/share/X11/xkb/keycodes/digital_vndr/lk
/usr/share/X11/xkb/keycodes/digital_vndr/pc
/usr/share/X11/xkb/keycodes/empty
/usr/share/X11/xkb/keycodes/evdev
/usr/share/X11/xkb/keycodes/fujitsu
/usr/share/X11/xkb/keycodes/hp
/usr/share/X11/xkb/keycodes/ibm
/usr/share/X11/xkb/keycodes/jolla
/usr/share/X11/xkb/keycodes/macintosh
/usr/share/X11/xkb/keycodes/olpc
/usr/share/X11/xkb/keycodes/sgi_vndr/indigo
/usr/share/X11/xkb/keycodes/sgi_vndr/indy
/usr/share/X11/xkb/keycodes/sgi_vndr/iris
/usr/share/X11/xkb/keycodes/sony
/usr/share/X11/xkb/keycodes/sun
/usr/share/X11/xkb/keycodes/xfree86
/usr/share/X11/xkb/keycodes/xfree98
/usr/share/X11/xkb/rules/README
/usr/share/X11/xkb/rules/base
/usr/share/X11/xkb/rules/base.extras.xml
/usr/share/X11/xkb/rules/base.lst
/usr/share/X11/xkb/rules/base.xml
/usr/share/X11/xkb/rules/evdev
/usr/share/X11/xkb/rules/evdev.extras.xml
/usr/share/X11/xkb/rules/evdev.lst
/usr/share/X11/xkb/rules/evdev.xml
/usr/share/X11/xkb/rules/xfree98
/usr/share/X11/xkb/rules/xkb.dtd
/usr/share/X11/xkb/symbols/af
/usr/share/X11/xkb/symbols/al
/usr/share/X11/xkb/symbols/altwin
/usr/share/X11/xkb/symbols/am
/usr/share/X11/xkb/symbols/apl
/usr/share/X11/xkb/symbols/ara
/usr/share/X11/xkb/symbols/at
/usr/share/X11/xkb/symbols/au
/usr/share/X11/xkb/symbols/az
/usr/share/X11/xkb/symbols/ba
/usr/share/X11/xkb/symbols/bd
/usr/share/X11/xkb/symbols/be
/usr/share/X11/xkb/symbols/bg
/usr/share/X11/xkb/symbols/bqn
/usr/share/X11/xkb/symbols/br
/usr/share/X11/xkb/symbols/brai
/usr/share/X11/xkb/symbols/bt
/usr/share/X11/xkb/symbols/bw
/usr/share/X11/xkb/symbols/by
/usr/share/X11/xkb/symbols/ca
/usr/share/X11/xkb/symbols/capslock
/usr/share/X11/xkb/symbols/cd
/usr/share/X11/xkb/symbols/ch
/usr/share/X11/xkb/symbols/cm
/usr/share/X11/xkb/symbols/cn
/usr/share/X11/xkb/symbols/compose
/usr/share/X11/xkb/symbols/ctrl
/usr/share/X11/xkb/symbols/cz
/usr/share/X11/xkb/symbols/de
/usr/share/X11/xkb/symbols/digital_vndr/lk
/usr/share/X11/xkb/symbols/digital_vndr/pc
/usr/share/X11/xkb/symbols/digital_vndr/us
/usr/share/X11/xkb/symbols/digital_vndr/vt
/usr/share/X11/xkb/symbols/dk
/usr/share/X11/xkb/symbols/dz
/usr/share/X11/xkb/symbols/ee
/usr/share/X11/xkb/symbols/eg
/usr/share/X11/xkb/symbols/empty
/usr/share/X11/xkb/symbols/epo
/usr/share/X11/xkb/symbols/es
/usr/share/X11/xkb/symbols/et
/usr/share/X11/xkb/symbols/eu
/usr/share/X11/xkb/symbols/eurosign
/usr/share/X11/xkb/symbols/fi
/usr/share/X11/xkb/symbols/fo
/usr/share/X11/xkb/symbols/fr
/usr/share/X11/xkb/symbols/fujitsu_vndr/jp
/usr/share/X11/xkb/symbols/fujitsu_vndr/us
/usr/share/X11/xkb/symbols/gb
/usr/share/X11/xkb/symbols/ge
/usr/share/X11/xkb/symbols/gh
/usr/share/X11/xkb/symbols/gn
/usr/share/X11/xkb/symbols/gr
/usr/share/X11/xkb/symbols/group
/usr/share/X11/xkb/symbols/hp_vndr/us
/usr/share/X11/xkb/symbols/hr
/usr/share/X11/xkb/symbols/hu
/usr/share/X11/xkb/symbols/id
/usr/share/X11/xkb/symbols/ie
/usr/share/X11/xkb/symbols/il
/usr/share/X11/xkb/symbols/in
/usr/share/X11/xkb/symbols/inet
/usr/share/X11/xkb/symbols/iq
/usr/share/X11/xkb/symbols/ir
/usr/share/X11/xkb/symbols/is
/usr/share/X11/xkb/symbols/it
/usr/share/X11/xkb/symbols/jolla_vndr/sbj
/usr/share/X11/xkb/symbols/jp
/usr/share/X11/xkb/symbols/ke
/usr/share/X11/xkb/symbols/keypad
/usr/share/X11/xkb/symbols/kg
/usr/share/X11/xkb/symbols/kh
/usr/share/X11/xkb/symbols/kpdl
/usr/share/X11/xkb/symbols/kr
/usr/share/X11/xkb/symbols/kz
/usr/share/X11/xkb/symbols/la
/usr/share/X11/xkb/symbols/latam
/usr/share/X11/xkb/symbols/latin
/usr/share/X11/xkb/symbols/level2
/usr/share/X11/xkb/symbols/level3
/usr/share/X11/xkb/symbols/level5
/usr/share/X11/xkb/symbols/lk
/usr/share/X11/xkb/symbols/lt
/usr/share/X11/xkb/symbols/lv
/usr/share/X11/xkb/symbols/ma
/usr/share/X11/xkb/symbols/macintosh_vndr/apple
/usr/share/X11/xkb/symbols/macintosh_vndr/ch
/usr/share/X11/xkb/symbols/macintosh_vndr/de
/usr/share/X11/xkb/symbols/macintosh_vndr/dk
/usr/share/X11/xkb/symbols/macintosh_vndr/fi
/usr/share/X11/xkb/symbols/macintosh_vndr/fr
/usr/share/X11/xkb/symbols/macintosh_vndr/gb
/usr/share/X11/xkb/symbols/macintosh_vndr/is
/usr/share/X11/xkb/symbols/macintosh_vndr/it
/usr/share/X11/xkb/symbols/macintosh_vndr/jp
/usr/share/X11/xkb/symbols/macintosh_vndr/latam
/usr/share/X11/xkb/symbols/macintosh_vndr/nl
/usr/share/X11/xkb/symbols/macintosh_vndr/no
/usr/share/X11/xkb/symbols/macintosh_vndr/pt
/usr/share/X11/xkb/symbols/macintosh_vndr/se
/usr/share/X11/xkb/symbols/macintosh_vndr/us
/usr/share/X11/xkb/symbols/mao
/usr/share/X11/xkb/symbols/md
/usr/share/X11/xkb/symbols/me
/usr/share/X11/xkb/symbols/mk
/usr/share/X11/xkb/symbols/ml
/usr/share/X11/xkb/symbols/mm
/usr/share/X11/xkb/symbols/mn
/usr/share/X11/xkb/symbols/mt
/usr/share/X11/xkb/symbols/mv
/usr/share/X11/xkb/symbols/my
/usr/share/X11/xkb/symbols/nbsp
/usr/share/X11/xkb/symbols/nec_vndr/jp
/usr/share/X11/xkb/symbols/ng
/usr/share/X11/xkb/symbols/nl
/usr/share/X11/xkb/symbols/no
/usr/share/X11/xkb/symbols/nokia_vndr/rx-44
/usr/share/X11/xkb/symbols/nokia_vndr/rx-51
/usr/share/X11/xkb/symbols/nokia_vndr/su-8w
/usr/share/X11/xkb/symbols/np
/usr/share/X11/xkb/symbols/olpc
/usr/share/X11/xkb/symbols/parens
/usr/share/X11/xkb/symbols/pc
/usr/share/X11/xkb/symbols/ph
/usr/share/X11/xkb/symbols/pk
/usr/share/X11/xkb/symbols/pl
/usr/share/X11/xkb/symbols/pt
/usr/share/X11/xkb/symbols/ro
/usr/share/X11/xkb/symbols/rs
/usr/share/X11/xkb/symbols/ru
/usr/share/X11/xkb/symbols/rupeesign
/usr/share/X11/xkb/symbols/se
/usr/share/X11/xkb/symbols/sgi_vndr/jp
/usr/share/X11/xkb/symbols/sharp_vndr/sl-c3x00
/usr/share/X11/xkb/symbols/sharp_vndr/ws003sh
/usr/share/X11/xkb/symbols/sharp_vndr/ws007sh
/usr/share/X11/xkb/symbols/sharp_vndr/ws011sh
/usr/share/X11/xkb/symbols/sharp_vndr/ws020sh
/usr/share/X11/xkb/symbols/shift
/usr/share/X11/xkb/symbols/si
/usr/share/X11/xkb/symbols/sk
/usr/share/X11/xkb/symbols/sn
/usr/share/X11/xkb/symbols/sony_vndr/us
/usr/share/X11/xkb/symbols/srvr_ctrl
/usr/share/X11/xkb/symbols/sun_vndr/ara
/usr/share/X11/xkb/symbols/sun_vndr/be
/usr/share/X11/xkb/symbols/sun_vndr/br
/usr/share/X11/xkb/symbols/sun_vndr/ca
/usr/share/X11/xkb/symbols/sun_vndr/ch
/usr/share/X11/xkb/symbols/sun_vndr/cz
/usr/share/X11/xkb/symbols/sun_vndr/de
/usr/share/X11/xkb/symbols/sun_vndr/dk
/usr/share/X11/xkb/symbols/sun_vndr/ee
/usr/share/X11/xkb/symbols/sun_vndr/es
/usr/share/X11/xkb/symbols/sun_vndr/fi
/usr/share/X11/xkb/symbols/sun_vndr/fr
/usr/share/X11/xkb/symbols/sun_vndr/gb
/usr/share/X11/xkb/symbols/sun_vndr/gr
/usr/share/X11/xkb/symbols/sun_vndr/it
/usr/share/X11/xkb/symbols/sun_vndr/jp
/usr/share/X11/xkb/symbols/sun_vndr/kr
/usr/share/X11/xkb/symbols/sun_vndr/lt
/usr/share/X11/xkb/symbols/sun_vndr/lv
/usr/share/X11/xkb/symbols/sun_vndr/nl
/usr/share/X11/xkb/symbols/sun_vndr/no
/usr/share/X11/xkb/symbols/sun_vndr/pl
/usr/share/X11/xkb/symbols/sun_vndr/pt
/usr/share/X11/xkb/symbols/sun_vndr/ro
/usr/share/X11/xkb/symbols/sun_vndr/ru
/usr/share/X11/xkb/symbols/sun_vndr/se
/usr/share/X11/xkb/symbols/sun_vndr/sk
/usr/share/X11/xkb/symbols/sun_vndr/solaris
/usr/share/X11/xkb/symbols/sun_vndr/tr
/usr/share/X11/xkb/symbols/sun_vndr/tw
/usr/share/X11/xkb/symbols/sun_vndr/ua
/usr/share/X11/xkb/symbols/sun_vndr/us
/usr/share/X11/xkb/symbols/sy
/usr/share/X11/xkb/symbols/terminate
/usr/share/X11/xkb/symbols/tg
/usr/share/X11/xkb/symbols/th
/usr/share/X11/xkb/symbols/tj
/usr/share/X11/xkb/symbols/tm
/usr/share/X11/xkb/symbols/tr
/usr/share/X11/xkb/symbols/trans
/usr/share/X11/xkb/symbols/tw
/usr/share/X11/xkb/symbols/typo
/usr/share/X11/xkb/symbols/tz
/usr/share/X11/xkb/symbols/ua
/usr/share/X11/xkb/symbols/us
/usr/share/X11/xkb/symbols/uz
/usr/share/X11/xkb/symbols/vn
/usr/share/X11/xkb/symbols/xfree68_vndr/amiga
/usr/share/X11/xkb/symbols/xfree68_vndr/ataritt
/usr/share/X11/xkb/symbols/za
/usr/share/X11/xkb/types/README
/usr/share/X11/xkb/types/basic
/usr/share/X11/xkb/types/cancel
/usr/share/X11/xkb/types/caps
/usr/share/X11/xkb/types/complete
/usr/share/X11/xkb/types/default
/usr/share/X11/xkb/types/extra
/usr/share/X11/xkb/types/iso9995
/usr/share/X11/xkb/types/level5
/usr/share/X11/xkb/types/mousekeys
/usr/share/X11/xkb/types/nokia
/usr/share/X11/xkb/types/numpad
/usr/share/X11/xkb/types/pc

%files dev
%defattr(-,root,root,-)
/usr/share/pkgconfig/xkeyboard-config.pc

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xkeyboard-config/40f6d7c0dba74ddd10663dfa50c2659cbe251423

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man7/xkeyboard-config.7

%files locales -f xkeyboard-config.lang
%defattr(-,root,root,-)

