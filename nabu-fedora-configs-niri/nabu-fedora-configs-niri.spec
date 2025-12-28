%global debug_package %{nil}
%global pkg_release 1

Name:           nabu-fedora-configs-niri
Version:        0.1.18
Release:        %{pkg_release}%{?dist}
Summary:        Configurations for Fedora for Nabu with niri Composer
License:        MIT
URL:            https://github.com/jhuang6451/nabu_fedora_packages
Source0:        %{url}/archive/refs/tags/%{name}-%{version}-%{pkg_release}.tar.gz
BuildArch:      noarch
BuildRequires:  systemd-rpm-macros

Requires:       pipewire-pulseaudio
Requires:       wireplumber
Requires:       niri
Requires:       dms

%description
This package contains configurations specific for Fedora for Nabu with niri composer

%prep
%autosetup -n nabu_fedora_packages-%{name}-%{version}-%{pkg_release}

%build
# Nothing to build

%install
cd nabu-fedora-configs-niri

cp -a etc %{buildroot}/
cp -a usr %{buildroot}/

%files
# General Configs
%attr(644, root, root) %config(noreplace) %{_sysconfdir}/locale.conf
%attr(644, root, root) %config(noreplace) %{_sysconfdir}/environment.d/99-im.conf
%attr(644, root, root) %config(noreplace) %{_sysconfdir}/greetd/config.toml
%attr(644, root, root) %{_prefix}/lib/systemd/system/fcitx5-autostart.service
%attr(644, root, root) %{_userpresetdir}/91-fcitx5-autostart.preset
%attr(644, root, root) %{_userpresetdir}/92-niri-dms.preset
%attr(644, root, root) %{_userpresetdir}/93-audio.preset
%attr(644, root, root) %{_presetdir}/91-greetd.preset

# Wallpapers Dir
%defattr(644, root, root, 755)
%{_sysconfdir}/skel/Pictures/Wallpapers

%post
# ----------------------------------------------------------------------
# appending to bashrc
# ---------------------------------------------------------------------- 
if [ -f /etc/skel/.bashrc ]; then
    echo "Appending custom configurations to /etc/skel/.bashrc"
    cat << 'EOF' >> /etc/skel/.bashrc

# ---- Added by nabu-fedora-configs-niri ----
alias code='code --ozone-platform=wayland'
fastfetch
# ---- End of nabu-fedora-configs-niri section ----
EOF
fi

# ----------------------------------------------------------------------
# add wants to niri service
# ----------------------------------------------------------------------
mkdir -p /etc/systemd/user/niri.service.wants/

ln -s /usr/lib/systemd/user/dms.service /etc/systemd/user/niri.service.wants/dms.service

%postun

%changelog
* Fri Dec 26 2025 jhuang6451 <xplayerhtz123@outlook.com> - 0.1.11-1
- Pre-installing DankMaterialShell. 

* Thu Oct 16 2025 jhuang6451 <xplayerhtz123@outlook.com> - 0.1.10-1
- Add postinstall script for pipwire user services.

* Thu Oct 16 2025 jhuang6451 <xplayerhtz123@outlook.com> - 0.1.6-1
- Remove deploy_user_configs.sh.

* Thu Oct 16 2025 jhuang6451 <xplayerhtz123@outlook.com> - 0.1.4-1
- Fix fcitx5-autostart systemd preset name.

* Thu Oct 16 2025 jhuang6451 <xplayerhtz123@outlook.com> - 0.1.3-1
- Postinstall script and some config updates.

* Sun Oct 12 2025 jhuang6451 <xplayerhtz123@outlook.com> - 0.1.2-1
- Initial release.