Summary:	Luminance HDR - HDR Image compositor
Summary(pl.UTF-8):	Luminance HDR - narzędzie do składania obrazów HDR
Name:		luminance-hdr
Version:	2.2.0
Release:	2
License:	GPL v2+
Group:		X11/Applications/Graphics
Source0:	http://downloads.sourceforge.net/qtpfsgui/%{name}-%{version}.tar.bz2
# Source0-md5:	15caab0747cc5d5f1a3a496752b733d4
URL:		http://qtpfsgui.sourceforge.net/
BuildRequires:	OpenEXR-devel
BuildRequires:	QtCore-devel >= 4.3
BuildRequires:	QtGui-devel >= 4.3
BuildRequires:	QtSql-devel >= 4.3
BuildRequires:	QtWebKit-devel >= 4.3
BuildRequires:	QtXml-devel >= 4.3
BuildRequires:	cmake >= 2.6.0
BuildRequires:	exiv2-devel
BuildRequires:	fftw3-single-devel
BuildRequires:	gcc-c++ >= 6:4.3
BuildRequires:	gsl-devel
BuildRequires:	libgomp-devel
BuildRequires:	libraw-devel
BuildRequires:	libtiff-devel
BuildRequires:	qt4-build >= 4.3.3-3
BuildRequires:	qt4-linguist >= 4.3.3-3
BuildRequires:	qt4-qmake >= 4.3.3-3
BuildRequires:	rpmbuild(macros) >= 1.605
Obsoletes:	qtpfsgui
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Luminance HDR - HDR Image compositor.

%description -l pl.UTF-8
Luminance HDR - narzędzie do składania obrazów HDR.

%prep
%setup -q -c

%build
# "build" dir is already occupied, use other name
mkdir obj
cd obj
%cmake ..
%{__make}
#lrelease project.pro

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C obj install \
	DESTDIR=$RPM_BUILD_ROOT

# packaged as %doc
%{__rm} $RPM_BUILD_ROOT%{_datadir}/luminance/{AUTHORS,Changelog,LICENSE,README}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS Changelog README TODO
%attr(755,root,root) %{_bindir}/luminance-hdr
%{_desktopdir}/luminance-hdr.desktop
%{_iconsdir}/hicolor/48x48/apps/luminance-hdr.png
%dir %{_datadir}/luminance
%dir %{_datadir}/luminance/help
%{_datadir}/luminance/help/en
%{_datadir}/luminance/help/js
%dir %{_datadir}/luminance/i18n
%lang(cs) %{_datadir}/luminance/i18n/lang_cs.qm
%lang(de) %{_datadir}/luminance/i18n/lang_de.qm
%lang(es) %{_datadir}/luminance/i18n/lang_es.qm
%lang(fi) %{_datadir}/luminance/i18n/lang_fi.qm
%lang(fr) %{_datadir}/luminance/i18n/lang_fr.qm
%lang(hu) %{_datadir}/luminance/i18n/lang_hu.qm
%lang(id) %{_datadir}/luminance/i18n/lang_id.qm
%lang(it) %{_datadir}/luminance/i18n/lang_it.qm
%lang(pl) %{_datadir}/luminance/i18n/lang_pl.qm
%lang(ro) %{_datadir}/luminance/i18n/lang_ro.qm
%lang(ru) %{_datadir}/luminance/i18n/lang_ru.qm
%lang(tr) %{_datadir}/luminance/i18n/lang_tr.qm
