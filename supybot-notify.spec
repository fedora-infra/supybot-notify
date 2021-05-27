Name:           supybot-notify
Version:        0.2.1
Release:        1%{?dist}
Summary:        Notification plugin for Supybot

Group:          Applications/Internet
License:        BSD
URL:            http://git.fedorahosted.org/git/supybot-notify.git
Source0:        https://fedorahosted.org/released/supybot-notify/%{name}-%{version}.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:       supybot

BuildArch:      noarch
BuildRequires:  python3-devel

%description
A Supybot plugin which relays messages from a TCP server to
an IRC channel.


%prep
%setup -q


%build


%install
%{__rm} -rf %{buildroot}
%{__install} -dm 755 %{buildroot}/%{python_sitelib}/supybot/plugins/Notify
%{__install} -pm 644 supybot_notify/*.py %{buildroot}/%{python_sitelib}/supybot/plugins/Notify


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc README COPYING
%{python3_sitelib}/supybot/plugins/Notify


%changelog
* Fri Jan 07 2011 Ricky Zhou <ricky@fedoraproject.org> - 0.2.1-1
- Update for 0.2.1 release.

* Mon Nov 01 2010 Ricky Zhou <ricky@fedoraproject.org> - 0.2-1
- Update for 0.2 release.

* Mon Mar 16 2009 Ricky Zhou <ricky@fedoraproject.org> - 0.1-1
- Initial RPM package.
