%define upstream_name    Text-Emoticon
%define upstream_version 0.04

Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	6

Summary:	Factory class for Yahoo! and MSN emoticons
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Text-Emoticon
Source0:	https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Text-Emoticon-%{upstream_version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)
BuildRequires:	perl(UNIVERSAL::require)
BuildArch:	noarch

%description
Text::Emoticon is a factory class to dispatch MSN/YIM emoticon set. It's
made to become handy to be used in other applications like Kwiki/MT
plugins.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 0.40.0-2mdv2011.0
+ Revision: 654328
- rebuild for updated spec-helper

* Sun Nov 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.40.0-1mdv2011.0
+ Revision: 471414
- import perl-Text-Emoticon


* Sun Nov 29 2009 cpan2dist 0.04-1mdv
- initial mdv release, generated with cpan2dist
