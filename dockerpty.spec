#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : dockerpty
Version  : 0.4.1
Release  : 19
URL      : https://github.com/d11wtq/dockerpty/archive/v0.4.1.tar.gz
Source0  : https://github.com/d11wtq/dockerpty/archive/v0.4.1.tar.gz
Summary  : Python library to use the pseudo-tty of a docker container
Group    : Development/Tools
License  : Apache-2.0
Requires: dockerpty-license = %{version}-%{release}
Requires: dockerpty-python = %{version}-%{release}
Requires: dockerpty-python3 = %{version}-%{release}
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : six
BuildRequires : tox
BuildRequires : virtualenv

%description
# Docker PTY
Provides the functionality needed to operate the pseudo-tty (PTY) allocated to
a docker container, using the Python client.

%package license
Summary: license components for the dockerpty package.
Group: Default

%description license
license components for the dockerpty package.


%package python
Summary: python components for the dockerpty package.
Group: Default
Requires: dockerpty-python3 = %{version}-%{release}

%description python
python components for the dockerpty package.


%package python3
Summary: python3 components for the dockerpty package.
Group: Default
Requires: python3-core
Provides: pypi(dockerpty)
Requires: pypi(six)

%description python3
python3 components for the dockerpty package.


%prep
%setup -q -n dockerpty-0.4.1
cd %{_builddir}/dockerpty-0.4.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603391279
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/dockerpty
cp %{_builddir}/dockerpty-0.4.1/LICENSE.txt %{buildroot}/usr/share/package-licenses/dockerpty/2b8b815229aa8a61e483fb4ba0588b8b6c491890
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/dockerpty/2b8b815229aa8a61e483fb4ba0588b8b6c491890

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
