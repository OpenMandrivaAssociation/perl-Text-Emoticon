%define upstream_name    Text-Emoticon
%define upstream_version 0.04

Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	1

Summary:	Factory class for Yahoo! and MSN emoticons
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Text-Emoticon
Source0:	https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Text-Emoticon-0.04.tar.gz

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

