Summary:	Localization files for packages summaries
Name:		mdv-rpm-summary
Version:	0.9
Release:	%mkrel 4
Source0:	%name-%version.tar.bz2
License:	GPL
Group:		System/Internationalization
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
BuildRequires:	gettext
BuildArchitectures: noarch

%description
This package includes translations of summaries the Mandriva Linux packages.
They are used by rpmdrake.

%prep
%setup -q

%build
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std PREFIX=%buildroot/

%find_lang %name rpm-summary-contrib rpm-summary-devel rpm-summary-main rpm-summary-non-free

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang 
%defattr(-,root,root,0755)
