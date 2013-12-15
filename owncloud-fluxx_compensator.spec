%define		pkgname	fluxx_compensator
Summary:	Framework for the ownCloud News app
Name:		owncloud-%{pkgname}
Version:	0.2.5
Release:	1
License:	AGPL
Group:		Development/Languages/PHP
Source0:	http://apps.owncloud.com/CONTENT/content-files/157091-fluxx_compensator.zip
# Source0-md5:	415a367241797df464d17fd278a9b7b6
URL:		http://apps.owncloud.com/content/show.php/FluXX+Compensator+%28Y%29?content=157091
BuildRequires:	rpmbuild(macros) >= 1.461
Requires:	owncloud >= 5.0.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir		%{_datadir}/owncloud/apps/%{pkgname}

%description
This simple app adds a handle each to the header and navigation
panels. That handle allows to slide the panels in and out of view.
This helps to gain valuable space on small displays. The app is kept
extremely simple. No configuration section required, all is integrated
right at your finger tip. Just activate and use, hold and slide the
handles to where you want them.

%prep
%setup -qc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}

cp -a * $RPM_BUILD_ROOT%{_appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_appdir}
