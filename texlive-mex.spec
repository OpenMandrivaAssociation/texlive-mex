Name:		texlive-mex
Version:	1.05
Release:	1
Summary:	Polish formats for TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/polish/mex105.zip
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mex.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mex.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Requires:	texlive-pl
Requires:	texlive-hyphen-polish
Requires:	texlive-pdftex
Requires:	texlive-tex
Requires:	texlive-mex.bin
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3
Requires(post):	texlive-tetex

%description
MeX is an adaptation of Plain TeX (MeX) and LaTeX209 (LaMeX)
formats to the Polish language and to Polish printing customs.
It contains a complete set of Metafont sources of Polish fonts,
hyphenation rules for the Polish language and sources of
formats.

%pre
    %_texmf_fmtutil_pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_fmtutil_post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_fmtutil_pre
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_fmtutil_post
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/mex/base/lamex.tex
%{_texmfdistdir}/tex/mex/base/mex.tex
%{_texmfdistdir}/tex/mex/base/mex1.tex
%{_texmfdistdir}/tex/mex/base/mex2.tex
%{_texmfdistdir}/tex/mex/base/mexconf.tex
%{_texmfdistdir}/tex/mex/config/mex.ini
%{_texmfdistdir}/tex/mex/config/pdfmex.ini
%_texmf_fmtutil_d/mex
%doc %{_texmfdistdir}/doc/mex/base/00readme
%doc %{_texmfdistdir}/doc/mex/base/mex.html
%doc %{_texmfdistdir}/doc/mex/base/mexinfo.eng
%doc %{_texmfdistdir}/doc/mex/base/mexinfo.pol
%doc %{_texmfdistdir}/doc/mex/base/qq.eps
%doc %{_texmfdistdir}/doc/mex/base/tstmex.tex
#- source
%doc %{_texmfdistdir}/source/mex/base/eminst.zip
%doc %{_texmfdistdir}/source/mex/base/istyles.zip

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_texmf_fmtutil_d}
cat > %{buildroot}%{_texmf_fmtutil_d}/mex <<EOF
mex pdftex mexconf.tex -translate-file=cp227.tcx *mex.ini
pdfmex pdftex mexconf.tex -translate-file=cp227.tcx *pdfmex.ini
utf8mex pdftex mexconf.tex -enc *utf8mex.ini
EOF