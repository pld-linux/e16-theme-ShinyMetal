%define	_tname	ShinyMetal
Summary:	Enlightenment ShinyMetal theme
Summary(pl):	Wystrój ShinyMetal dla Enlightenmenta
Name:		enlightenment-theme-%{_tname}
Version:	0.16
Release:	1
License:	GPL
Group:		Themes
Source0:	http://dl.sourceforge.net/enlightenment/%{name}-%{version}.tar.gz
# Source0-md5:	177044a975becdf1a1695a3dc2c63932
Patch0:		%{name}-i18n.patch
URL:		http://www.enlightenment.org/
Requires:	enlightenment >= 0.16.7.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Enlightenment ShinyMetal theme.

%description -l pl
Wystrój ShinyMetal dla Enlightenmenta.

%prep
%setup -q
mkdir %{_tname}
tar -zxf %{_tname}.etheme -C %{_tname}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/enlightenment/themes/
cp -a %{_tname} $RPM_BUILD_ROOT%{_datadir}/enlightenment/themes/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/enlightenment/themes/%{_tname}
