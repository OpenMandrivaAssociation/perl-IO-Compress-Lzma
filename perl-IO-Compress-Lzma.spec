%define	module	IO-Compress-Lzma
%bcond_with	long_tests

Name:		perl-%{module}
Version:	2.049
Release:	3
Summary:	Read and write lzma compressed data
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}/
Source0:	http://www.cpan.org/authors/id/P/PM/PMQS/%{module}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Compress::Raw::Lzma) >= %{version}
BuildRequires:	perl(IO::Compress::Base) >= %{version}
BuildRequires:	perl(IO::String)
BuildRequires:	perl(Test::Pod)
BuildRequires:	pkgconfig(liblzma)

%description
This distribution provides a Perl interface to allow reading and writing of
compressed data created with the lzma library.

%prep
%setup -q -n %{module}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%check
# Build using "--without long_tests" to avoid very long tests
# (full suite can take nearly an hour on an i7)
make test %{with long_tests:COMPRESS_ZLIB_RUN_ALL=1}

%files
%doc Changes README
%{perl_vendorlib}/IO/
%{_mandir}/man3/IO::Compress::Lzma.3pm*
%{_mandir}/man3/IO::Compress::Xz.3pm*
%{_mandir}/man3/IO::Uncompress::UnLzma.3pm*
%{_mandir}/man3/IO::Uncompress::UnXz.3pm*



%changelog
* Fri Mar 16 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.049-1
+ Revision: 785230
- add perl-devel to buildrequires
- imported package perl-IO-Compress-Lzma


* Mon Mar 13 2012 Per Øyvind Karlsen <pkarlsen@mandriva.com> 2.049-1
- initial release
