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
Version:	2.3.1
Release:	1
License:	GPL v2+
Group:		X11/Applications/Graphics
Source0:	http://downloads.sourceforge.net/qtpfsgui/%{name}-%{version}.tar.bz2
# Source0-md5:	86499294fb9a6dc211a54cbaa9af2b8a
Patch0:		%{name}-qt4pld.patch
URL:		http://qtpfsgui.sourceforge.net/
BuildRequires:	OpenEXR-devel
BuildRequires:	QtCore-devel >= 4.3
BuildRequires:	QtGui-devel >= 4.3
BuildRequires:	QtNetwork-devel >= 4.3
BuildRequires:	QtSql-devel >= 4.3
BuildRequires:	QtWebKit-devel >= 4.3
BuildRequires:	QtXml-devel >= 4.3
BuildRequires:	boost-devel
BuildRequires:	cmake >= 2.6.0
BuildRequires:	exiv2-devel >= 0.12
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
BuildRequires:	qt4-build >= 4.3.3-3
BuildRequires:	qt4-linguist >= 4.3.3-3
BuildRequires:	qt4-qmake >= 4.3.3-3
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	sed >= 4.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	QtCore >= 4.3
Requires:	QtGui >= 4.3
Requires:	QtNetwork >= 4.3
Requires:	QtSql >= 4.3
Requires:	QtSql-sqlite3 >= 4.3
Requires:	QtWebKit >= 4.3
Requires:	QtXml >= 4.3
Requires:	exiv2 >= 0.12
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
# use Qt translations packaged with qt4
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
%lang(hi) %{_datadir}/luminance-hdr/i18n/lang_hi.qm
%lang(hu) %{_datadir}/luminance-hdr/i18n/lang_hu.qm
%lang(id) %{_datadir}/luminance-hdr/i18n/lang_id.qm
%lang(it) %{_datadir}/luminance-hdr/i18n/lang_it.qm
%lang(pl) %{_datadir}/luminance-hdr/i18n/lang_pl.qm
%lang(ro) %{_datadir}/luminance-hdr/i18n/lang_ro.qm
%lang(ru) %{_datadir}/luminance-hdr/i18n/lang_ru.qm
%lang(sk) %{_datadir}/luminance-hdr/i18n/lang_sk.qm
%lang(tr) %{_datadir}/luminance-hdr/i18n/lang_tr.qm
%lang(zh_CN) %{_datadir}/luminance-hdr/i18n/lang_zh.qm
%{_desktopdir}/luminance-hdr.desktop
%{_iconsdir}/hicolor/48x48/apps/luminance-hdr.png
