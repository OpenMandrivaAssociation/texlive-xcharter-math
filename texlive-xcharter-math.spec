Name:		texlive-xcharter-math
Version:	69482
Release:	1
Summary:	XCharter-based OpenType Math font for LuaTeX and XeTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/xcharter-math
License:	ofl lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xcharter-math.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xcharter-math.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides an Unicode Math font XCharter-Math.otf
meant to be used together with XCharter Opentype Text fonts
(extension of Bitstream Charter) in LuaLaTeX or XeLaTeX
documents.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/xcharter-math
%{_texmfdistdir}/fonts/opentype/public/xcharter-math
%doc %{_texmfdistdir}/doc/fonts/xcharter-math

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
