#
# Conditional build:
%bcond_with	tests		# build without tests

%define	pkgname	celluloid-io
Summary:	Celluloid::IO allows you to monitor multiple IO objects within a Celluloid actor
Name:		ruby-%{pkgname}
Version:	0.15.0
Release:	2
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	39d561d3596c24eb81c1d500f0b82c25
URL:		http://github.com/celluloid/celluloid-io
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
%if %{with tests}
BuildRequires:	ruby-benchmark_suite
BuildRequires:	ruby-guard-rspec
BuildRequires:	ruby-rake
BuildRequires:	ruby-rb-fsevent < 0.10
BuildRequires:	ruby-rb-fsevent >= 0.9.1
BuildRequires:	ruby-rspec
%endif
Requires:	ruby-celluloid >= 0.15.0
Requires:	ruby-nio4r >= 0.5.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Evented IO for Celluloid actors

%prep
%setup -q -n %{pkgname}-%{version}

%build
%__gem_helper spec

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md CHANGES.md LICENSE.txt
%{ruby_vendorlibdir}/celluloid/io.rb
%{ruby_vendorlibdir}/celluloid/io
%{ruby_specdir}/%{pkgname}-%{version}.gemspec
