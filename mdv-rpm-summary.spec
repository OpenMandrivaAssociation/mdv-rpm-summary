Summary:	Localization files for packages summaries
Name:		mdv-rpm-summary
Version:	0.9.4
Release:	7
License:	GPLv2
Group:		System/Internationalization
Source0:	%{name}-%{version}.tar.bz2
BuildRequires:	gettext
BuildArch:	noarch

%description
This package includes translations of summaries the Mandriva Linux packages.
They are used by rpmdrake.

%prep
%setup -q

%build
make

%install
%makeinstall_std PREFIX=%{buildroot}/

%find_lang rpm-summary-contrib rpm-summary-devel rpm-summary-main rpm-summary-non-free %{name}.lang

%files -f %{name}.lang 

