%{?scl:%scl_package nodejs-jsonpointer}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

%global enable_tests 0
%global npm_name jsonpointer

Name:       %{?scl_prefix}nodejs-%{npm_name}
Version:    2.0.0
Release:    2%{?dist}
Summary:    Simple JSON Addressing
License:    MIT
URL:        http://github.com/janl/node-jsonpointer/issues
Source0:    http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
Source1:    https://github.com/janl/node-jsonpointer/blob/4.0.0/LICENSE.md
BuildRequires: %{?scl_prefix}nodejs-devel
BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

%description
Simple JSON Addressing.

%prep
%setup -q -n package
cp %{SOURCE1} .

rm -rf node_modules

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr jsonpointer.js package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
# If any binaries are included, symlink them to bindir here


%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
#not running tests in RHSCL
%endif

%files
%{nodejs_sitelib}/%{npm_name}

%doc LICENSE.md 
%doc README.md

%changelog
* Tue Sep 20 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.0.0-2
- Initial build

