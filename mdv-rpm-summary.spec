Summary:	Localization files for packages summaries
Name:		mdv-rpm-summary
Version:	0.7
Release:	%mkrel 2
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
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std PREFIX=%buildroot/

for i in rpm-summary-contrib rpm-summary-devel rpm-summary-main; do 
%find_lang $i
done
cat rpm-summary-contrib.lang rpm-summary-devel.lang >> rpm-summary-main.lang 

%clean
rm -rf $RPM_BUILD_ROOT


%files -f rpm-summary-main.lang 
%defattr(-,root,root,0755)
%{_datadir}/locale/*/*


