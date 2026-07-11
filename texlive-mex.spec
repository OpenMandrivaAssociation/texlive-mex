%global tl_name mex
%global tl_revision 58661

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.05a
Release:	%{tl_revision}.1
Summary:	Polish formats for TeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/polish/mex105a.zip
License:	knuth
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mex.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mex.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(enctex)
Requires:	texlive(hyph-utf8)
Requires:	texlive(hyphen-base)
Requires:	texlive(hyphen-polish)
Requires:	texlive(knuth-lib)
Requires:	texlive(mex.bin)
Requires:	texlive(pdftex)
Requires:	texlive(pl)
Requires:	texlive(plain)
Requires:	texlive(tex)
Requires:	texlive(tex-ini-files)
Requires:	texlive(utf8mex)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
MeX is an adaptation of Plain TeX (MeX) and LaTeX209 (LaMeX) formats to
the Polish language and to Polish printing customs. It contains a
complete set of Metafont sources of Polish fonts, hyphenation rules for
the Polish language and sources of formats.

