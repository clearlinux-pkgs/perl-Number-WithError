#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v13
# autospec commit: dc0ff31b4314
#
Name     : perl-Number-WithError
Version  : 1.01
Release  : 27
URL      : https://cpan.metacpan.org/authors/id/S/SM/SMUELLER/Number-WithError-1.01.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/S/SM/SMUELLER/Number-WithError-1.01.tar.gz
Summary  : 'Numbers with error propagation and scientific rounding'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Number-WithError-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Module::Install)
BuildRequires : perl(Params::Util)
BuildRequires : perl(Test::LectroTest)
BuildRequires : perl(prefork)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
Number::WithError - Numbers with error propagation and scientific
rounding
SYNOPSIS
use Number::WithError;

my $num = Number::WithError->new(5.647, 0.31);
print $num . "\n";
# prints '5.65e+00 +/- 3.1e-01'
# (I.e. it automatically does scientific rounding)

my $another = $num * 3;
print $another . "\n";
# propagates the error assuming gaussian errors
# prints '1.69e+01 +/- 9.3e-01'

# trigonometric functions also work:
print sin($another) . "\n";
# prints '-9.4e-01 +/- 3.1e-01'

my $third = $another ** $num;
print $third. "\n";
# propagates both errors into one.
# prints '8.7e+06 +/- 8.1e+06'

# shortcut for the constructor:
use Number::WithError 'witherror';
$num = witherror('0.00032678', ['2.5e-5', '3e-5'], 5e-6);
# can deal with any number of errors, even with asymmetric errors
print $num . "\n";
# prints '3.268e-04 + 2.5e-05 - 3.00e-05 +/- 5.0e-06'
# Note: It may be annyoing that they don't all have the same
# exponent, but they *do* all have the sam significant digit!

%package dev
Summary: dev components for the perl-Number-WithError package.
Group: Development
Provides: perl-Number-WithError-devel = %{version}-%{release}
Requires: perl-Number-WithError = %{version}-%{release}

%description dev
dev components for the perl-Number-WithError package.


%package perl
Summary: perl components for the perl-Number-WithError package.
Group: Default
Requires: perl-Number-WithError = %{version}-%{release}

%description perl
perl components for the perl-Number-WithError package.


%prep
%setup -q -n Number-WithError-1.01
cd %{_builddir}/Number-WithError-1.01

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Number::WithError.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
