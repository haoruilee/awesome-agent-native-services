---
layout: default
title: Privacy Policy
description: "How The Agent-Native Index handles ordinary request data, first-party scripts, and advertising. An AdSense account exists for site verification. Advertising is not enabled."
permalink: /privacy/
page_kind: document
ads: false
---

Effective 10 November 2026.

This policy describes https://theagentnative.com/, the public site for The Agent-Native Index (Awesome Agent-Native Services). The site is a curated index of agent-native services. It publishes short introductions and links. It is not an account service, and it does not sell the services it lists.

The site is maintained through the public repository [haoruilee/awesome-agent-native-services](https://github.com/haoruilee/awesome-agent-native-services). This policy does not name a company, because the repository does not publish one.

## What this site does

Visitors can read the catalog, open collection and service pages, and search the index in the browser. There is no account, newsletter, comment form, or other form that asks for a name, email address, or message. The site does not ask you to create a profile.

Service pages describe third-party products and link out to them. Those products are not operated by this site.

## Requests handled by the host

The site is a static Jekyll site hosted on GitHub Pages. Public responses are served by GitHub Pages through its content delivery network. Response headers on the live site identify that network as Fastly, including `server: GitHub.com`, `via: 1.1 varnish`, and `x-fastly-request-id`.

When a browser requests a page, GitHub Pages and that network receive the ordinary data a browser sends with the request. That includes:

- IP address
- user agent
- the URL requested, including the path and query string
- the time of the request
- a referrer, if the browser sends one

This project does not run its own application server. The repository does not configure a separate copy of those host or CDN logs, and it does not add a script that reads them.

## Cookies and browser storage

This site’s own pages and scripts do not set cookies and do not use local storage or session storage. The catalog search keeps results in memory for the current page only.

A response from the public homepage did not include a `Set-Cookie` header set by this project. GitHub Pages and its CDN still receive the connection data described above when they deliver a page.

## Scripts on these pages

This release does not load an analytics product. The repository and the public site do not include Google Analytics, Google Tag Manager, or another analytics script.

Pages load one first-party search script, `/assets/js/catalog-search.js`. When you use the search box, that script fetches `/assets/search-index.json` from this same site and filters it in the browser. It does not send the search text to a third party.

Pages that reserve an advertising space also load `/assets/js/publisher.js`. That script fetches `/publisher-config.json` from this same site and then stops, because `adsense.enabled` is false, slot IDs are null, and consent is not configured. It does not contact an advertising network in this release.

Each page also includes a `google-adsense-account` meta tag for the AdSense publisher `ca-pub-7668037987581637`. The tag is not a script. It does not load `adsbygoogle.js`, and it does not turn on Auto ads.

Inline JSON-LD on the pages describes the catalog for search engines. It is not a tracker. The type used for headings and body text is a system font stack. The site does not load a third-party font service.

## Advertising

An AdSense account exists for this site (`ca-pub-7668037987581637`). Advertising is not enabled.

Some pages include reserved layout spaces. Those spaces are placeholders. Each one is labeled “Advertisements” and reads “Advertising placement reserved.” They are not live ads. This release does not request ads, does not load `adsbygoogle.js`, and does not turn on Auto ads. The privacy policy page has no reserved space.

`/ads.txt` is a plain-text file served at the site root. It contains one publisher record for that same account, `google.com, pub-7668037987581637, DIRECT, f08c47fec0942fa0`, plus a comment that advertising is not enabled. The record lets Google match the account to this site. It does not request or display ads.

`/publisher-config.json` keeps advertising off: `adsense.enabled` is false, the client ID is `ca-pub-7668037987581637`, every named slot ID is null, and `consentIntegration` is `not_configured`. The first-party script does nothing unless all of the following are true at once: the config enables advertising, every reserved slot on that page has a numeric slot ID, `consentIntegration` is set to a consent setup other than `not_configured`, and the page carries an explicit consent signal (`window.agentNativeAdConsent` set to `granted`). A client ID in that file does not load an ad by itself.

This release does not include a cookie-consent popup. A certified consent-management platform is required before advertising is enabled for regions that require consent. That platform is what would set the consent signal above. It is not part of this release.

If advertising is enabled later, third-party providers may use cookies or similar signals, subject to that consent setup and to their own policies. Reserved spaces would still be normal in-page placements. This site does not use full-screen interstitial or vignette ads.

## Links to other sites

Pages link to the [public GitHub repository](https://github.com/haoruilee/awesome-agent-native-services), to the services in the catalog, and to [ReleaseLog](https://releaselog.site). Those sites are run separately and have their own policies. This policy applies only to https://theagentnative.com/.

## Contact

This site does not publish a contact email address. Questions about this policy can be raised on the public repository, including by opening a [GitHub issue](https://github.com/haoruilee/awesome-agent-native-services/issues).

## Changes

This policy is updated by editing it in that repository. The date at the top of the page is the date of this version.
