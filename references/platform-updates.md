# Platform and standards updates (2025 to 2026)

Snapshot checked 16 November 2026. These change often: before citing a date or requirement in a deliverable, check the official source. Items marked "press coverage" were not confirmed against the primary source in this pass.

## Apple platforms

- **Liquid Glass (2025).** At WWDC in June 2025 Apple introduced Liquid Glass, a translucent, refractive material for controls, toolbars, tab bars and navigation, across iOS, iPadOS, macOS, watchOS and tvOS, with version numbers aligned to the year (iOS 26 and so on). Standard SwiftUI and UIKit controls adopt it automatically when built with the current SDK.
- **iOS 27 / macOS 27 (WWDC June 2026, press coverage).** Apple refined Liquid Glass after readability complaints: a user setting (slider) controls how strong the effect looks across iOS, iPadOS and macOS. On macOS 27, sidebars extend to the window edge, sidebar icons regain color, and a uniform toolbar returns. Menu item image guidance in the HIG was updated.
- **Design implications:** prefer system controls so they pick up the material and the user's setting. Do not rely on translucency for legibility; test content under controls at every transparency level and with Reduce Transparency and Increase Contrast on. Keep custom glass effects for the navigation layer, not content.
- **Source:** developer.apple.com/design/human-interface-guidelines and the WWDC session pages for the current year.

## Android and Material

- **Material 3 Expressive (2025).** Google extended Material 3 with a more expressive set: spring-based motion, a larger shape library with shape morphing, emphasized type styles, and components such as button groups, split buttons, FAB menus, toolbars and a new loading indicator. It shipped with Android 16 updates in late 2025. Verify current component status at m3.material.io before specifying.
- **Edge-to-edge and adaptive layouts:** recent Android versions enforce edge-to-edge drawing for apps targeting new SDKs and push large-screen adaptivity (resizable windows, ignoring orientation locks on large screens). Plan insets and multi-pane layouts. Verify against developer.android.com for the target SDK.

## Accessibility standards and law

- **WCAG 2.2** (W3C Recommendation, 2023) is the current version to design to. It adds focus not obscured, target size minimum (24×24 CSS px with exceptions), dragging alternatives, consistent help, redundant entry and accessible authentication.
- **WCAG 3** is still a Working Draft (latest confirmed: 3 March 2026). It does not replace WCAG 2 and should not be used as a conformance target. A candidate recommendation is not expected before late 2027.
- **European Accessibility Act.** Applies since 28 June 2025 to many consumer products and services in the EU market (e-commerce, banking, e-books, transport ticketing, communications, some devices), including non-EU businesses selling into the EU. The harmonised standard EN 301 549 maps to WCAG 2.1 AA for web content. Microenterprises providing services are exempt; there are transition periods for some existing products and contracts.
- **ADA Title II (US state and local government).** The 2024 DOJ rule requires WCAG 2.1 AA for web content and mobile apps. On 20 April 2026 an interim final rule extended the deadlines by one year: April 2027 for entities serving 50,000 or more people and April 2028 for smaller ones. The extension was reported as challenged in court; check current status.
- **ADA Title III (private businesses, US):** no specific technical regulation; courts and settlements commonly reference WCAG 2.1 or 2.2 AA.
- **Section 508 (US federal):** references WCAG 2.0 AA via its standards; agencies often target 2.1 or 2.2 in practice.

## Design tokens

- **DTCG Format Module 2025.10** is the first stable version of the Design Tokens Community Group format. It is a Community Group report, not a W3C Standard. Tools (Figma variables export, Style Dictionary, Tokens Studio) support it to varying degrees; check the tool's docs.

## Keeping this file current

When you learn of a newer change, add it with the date, source and whether it was confirmed against the primary source. Remove entries once they are just "how things are" and move that knowledge into the main reference files.
