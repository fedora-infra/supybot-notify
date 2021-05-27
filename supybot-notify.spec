Name:           supybot-notify
Version:        0.3
Release:        1%{?dist}
Summary:        Notification plugin for Supybot

Group:          Applications/Internet
License:        BSD
URL:            https://github.com/fedora-infra/supybot-notify
Source0:        https://github.com/fedora-infra/%{name}/archive/%{version}/%{name}-%{version}.tar.gz 

Requires:       limnoria

BuildArch:      noarch
BuildRequires:  python3-devel

%description
A Supybot plugin which relays messages from a TCP server to
an IRC channel.


%prep
%setup -q


%build


%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__install} -dm 755 $RPM_BUILD_ROOT/%{python3_sitelib}/supybot/plugins/Notify
%{__install} -pm 644 supybot_notify/*.py $RPM_BUILD_ROOT/%{python3_sitelib}/supybot/plugins/Notify


%clean
%{__rm} -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README COPYING
%{python3_sitelib}/supybot/plugins/Notify


%changelog
* Thu May 27 2021 Ryan Lerch <rlerch@redhat.com> - 0.3-1
- Update for 0.3 release.
- Python 3 Conversion

* Fri Jan 07 2011 Ricky Zhou <ricky@fedoraproject.org> - 0.2.1-1
- Update for 0.2.1 release.

* Mon Nov 01 2010 Ricky Zhou <ricky@fedoraproject.org> - 0.2-1
- Update for 0.2 release.

* Mon Mar 16 2009 Ricky Zhou <ricky@fedoraproject.org> - 0.1-1
- Initial RPM package.
