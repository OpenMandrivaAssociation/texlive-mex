# revision 22650
# category Package
# catalog-ctan /language/polish/mex105.zip
# catalog-date 2011-04-11 12:20:39 +0200
# catalog-license pd
# catalog-version 1.05
Name:		texlive-mex
Version:	1.05
Release:	12
Summary:	Polish formats for TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/polish/mex105.zip
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mex.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mex.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires(post):	texlive-tetex
Requires:	texlive-pl
Requires:	texlive-hyphen-polish
Requires:	texlive-pdftex
Requires:	texlive-tex
Requires:	texlive-mex.bin

%description
MeX is an adaptation of Plain TeX (MeX) and LaTeX209 (LaMeX)
formats to the Polish language and to Polish printing customs.
It contains a complete set of Metafont sources of Polish fonts,
hyphenation rules for the Polish language and sources of
formats.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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
#
# from mex:
mex pdftex mexconf.tex -translate-file=cp227.tcx *mex.ini
pdfmex pdftex mexconf.tex -translate-file=cp227.tcx *pdfmex.ini
utf8mex pdftex mexconf.tex -enc *utf8mex.ini
EOF


%changelog
* Tue Feb 21 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.05-3
+ Revision: 778453
- Rebuild after tlpobj2spec.pl bug correction.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.05-2
+ Revision: 753933
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.05-1
+ Revision: 719006
- texlive-mex
- texlive-mex
- texlive-mex
- texlive-mex

