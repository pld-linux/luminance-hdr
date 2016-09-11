#
# Conditional build:
%bcond_with	sse	# SSE instructions
%bcond_with	sse2	# SSE2 instructions

%ifarch pentium3 pentium4 %{x8664} x32
%define	with_sse	1
%endif
%ifarch pentium4 %{x8664} x32
%define	with_sse2	1
%endif
Summary:	Luminance HDR - HDR Image compositor
Summary(pl.UTF-8):	Luminance HDR - narzędzie do składania obrazów HDR
Name:		luminance-hdr
Version:	2.4.0
Release:	1
License:	GPL v2+
Group:		X11/Applications/Graphics
Source0:	http://downloads.sourceforge.net/qtpfsgui/%{name}-%{version}.tar.bz2
# Source0-md5:	b22c9bca0330d80bdec38d37fc94ad93
Patch0:		%{name}-qprinter.patch
URL:		http://qtpfsgui.sourceforge.net/
BuildRequires:	CCfits-devel
BuildRequires:	OpenEXR-devel >= 2.0.1
BuildRequires:	Qt5Concurrent-devel >= 5
BuildRequires:	Qt5Core-devel >= 5
BuildRequires:	Qt5Declarative-devel >= 5
BuildRequires:	Qt5Gui-devel >= 5
BuildRequires:	Qt5Network-devel >= 5
BuildRequires:	Qt5PrintSupport-devel >= 5
BuildRequires:	Qt5Sql-devel >= 5
BuildRequires:	Qt5WebKit-devel >= 5
BuildRequires:	Qt5Widgets-devel >= 5
BuildRequires:	Qt5Xml-devel >= 5
BuildRequires:	boost-devel
BuildRequires:	cfitsio-devel
BuildRequires:	cmake >= 2.8.11
BuildRequires:	exiv2-devel >= 0.21
BuildRequires:	fftw3-single-devel >= 3
BuildRequires:	gcc-c++ >= 6:4.3
BuildRequires:	gsl-devel
BuildRequires:	lcms2-devel >= 2
BuildRequires:	libgomp-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libraw-devel
BuildRequires:	libstdc++-devel >= 6:4.3
BuildRequires:	libtiff-devel
BuildRequires:	qt5-build >= 5
BuildRequires:	qt5-linguist >= 5
BuildRequires:	qt5-qmake >= 5
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	sed >= 4.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	OpenEXR >= 2.0.1
Requires:	Qt5Sql-sqldriver-sqlite3
Requires:	exiv2-libs >= 0.21
Requires:	hicolor-icon-theme
Obsoletes:	qtpfsgui
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Luminance HDR - HDR Image compositor.

%description -l pl.UTF-8
Luminance HDR - narzędzie do składania obrazów HDR.

%prep
%setup -q
%patch0 -p1

%if %{without sse2}
%{__sed} -i -e 's/ -msse2//' cmake/CompilerSettings.cmake
%endif
%if %{without sse}
%{__sed} -i -e 's/ -msse//' cmake/CompilerSettings.cmake
%endif

%build
# "build" dir is already occupied, use other name
mkdir obj
cd obj
%cmake .. \
	-DBUILD_SHARED_LIBS:BOOL=OFF

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C obj install \
	DESTDIR=$RPM_BUILD_ROOT

# packaged as %doc
%{__rm} $RPM_BUILD_ROOT%{_datadir}/luminance-hdr/{AUTHORS,Changelog,LICENSE,README}
# use Qt translations packaged with qt5
%{__rm} $RPM_BUILD_ROOT%{_datadir}/luminance-hdr/i18n/qt_*.qm

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS Changelog README TODO
%attr(755,root,root) %{_bindir}/luminance-hdr
%attr(755,root,root) %{_bindir}/luminance-hdr-cli
%dir %{_datadir}/luminance-hdr
%dir %{_datadir}/luminance-hdr/help
%{_datadir}/luminance-hdr/help/en
%dir %{_datadir}/luminance-hdr/i18n
%lang(cs) %{_datadir}/luminance-hdr/i18n/lang_cs.qm
%lang(da) %{_datadir}/luminance-hdr/i18n/lang_da.qm
%lang(de) %{_datadir}/luminance-hdr/i18n/lang_de.qm
%lang(es) %{_datadir}/luminance-hdr/i18n/lang_es.qm
%lang(fi) %{_datadir}/luminance-hdr/i18n/lang_fi.qm
%lang(fr) %{_datadir}/luminance-hdr/i18n/lang_fr.qm
%lang(hu) %{_datadir}/luminance-hdr/i18n/lang_hu.qm
%lang(id) %{_datadir}/luminance-hdr/i18n/lang_id.qm
%lang(it) %{_datadir}/luminance-hdr/i18n/lang_it.qm
%lang(pl) %{_datadir}/luminance-hdr/i18n/lang_pl.qm
%lang(pt_BR) %{_datadir}/luminance-hdr/i18n/lang_pt_BR.qm
%lang(ro) %{_datadir}/luminance-hdr/i18n/lang_ro.qm
%lang(ru) %{_datadir}/luminance-hdr/i18n/lang_ru.qm
%lang(tr) %{_datadir}/luminance-hdr/i18n/lang_tr.qm
%lang(zh_CN) %{_datadir}/luminance-hdr/i18n/lang_zh.qm
%{_desktopdir}/luminance-hdr.desktop
%{_iconsdir}/hicolor/48x48/apps/luminance-hdr.png
