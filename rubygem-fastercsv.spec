# Generated from fastercsv-1.5.4.gem by gem2rpm5 -*- rpm-spec -*-          
%define	rbname	fastercsv

Summary:	FasterCSV is CSV, but faster, smaller, and cleaner
Name:		rubygem-%{rbname}

Version:	1.5.4
Release:	2
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://fastercsv.rubyforge.org
Source0:	http://gems.rubyforge.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildArch:	noarch

%description
FasterCSV is intended as a complete replacement to the CSV standard library.
It
is significantly faster and smaller while still being pure Ruby code. It also
strives for a better interface.

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}
BuildArch:	noarch

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build

%install
%gem_install

%files
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/AUTHORS
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/CHANGELOG
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/COPYING
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/INSTALL
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/LICENSE
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/README
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/TODO
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}


%changelog
* Wed Feb 15 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.5.4-2
+ Revision: 774161
- mass rebuild of ruby packages against ruby 1.9.1

* Mon Jan 23 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.5.4-1
+ Revision: 766959
- imported package rubygem-fastercsv

