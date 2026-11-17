# Context starter packs

30 device/platform profiles, 16 system profiles and 58 domain profiles. These inventories identify what to investigate. They are not fully verified specialist handbooks. Retrieve current platform, domain, jurisdiction and organizational sources for the actual task; record gaps and qualified review needs.

#### Device and platform packs

30 starting packs. Verify actual capabilities and platform guidance for the supported version. A device category can contain materially different environments; split a pack when those differences affect the work.

| Pack | Surface | What changes the design |
| --- | --- | --- |
| `responsive-web` | Browser-based sites and applications | Semantics, routes, browser navigation, zoom, reflow, keyboard access, responsive layouts, multiple browsers, and degraded connectivity. |
| `installed-web-pwa` | Installed and progressive web apps | Install expectations, offline limits, updates, caching, permission prompts, browser differences, and operating-system integration. |
| `ios-phone` | iPhone applications | Current Apple guidance, navigation, native controls, safe areas, text scaling, permission flows, lifecycle, and interruption. |
| `android-phone` | Android phone applications | Current Android and Material guidance, system navigation, window sizes, edge-to-edge constraints, permissions, back behavior, and lifecycle. |
| `ipados-tablet` | iPad and pen-centered tablet use | Multiwindow work, large-screen composition, keyboard, pointer, pen, drag alternatives, and desktop-class task depth. |
| `android-tablet` | Android tablets and large-window use | Canonical multi-pane layouts, resizable windows, input changes, continuity, large-screen task efficiency, and state preservation. |
| `foldable-dual-screen` | Foldables and multi-display devices | Cover and inner displays, hinges, posture, folding transitions, pane changes, continuity, and manufacturer-specific constraints. |
| `macos-desktop` | Mac applications | Windows, menus, keyboard and pointer conventions, toolbars, document models, multitasking, accessibility, and system integrations. |
| `windows-desktop` | Windows applications | Current Windows and Fluent conventions, resize, keyboard efficiency, high contrast, windowing, file workflows, and system behavior. |
| `linux-chromeos-desktop` | Linux and ChromeOS applications | Actual desktop environment, window management, keyboard conventions, browser/native boundaries, distributions, and supported accessibility tooling. |
| `watchos-wearable` | Apple Watch experiences | Glanceable tasks, brief interactions, complications or equivalent surfaces, companion dependence, haptics, input limits, and interruption. |
| `wearos-other-wearables` | Wear OS, bands, and emerging wearables | Small displays or no display, glanceable value, phone dependence, sensors, battery, consent, input, and physical context. |
| `apple-tv` | Apple TV and tvOS experiences | Distance viewing, focus-driven navigation, remotes, media behavior, account entry, readability, and shared households. |
| `connected-tv` | Android TV, Google TV, and other smart TVs | Remote variations, focus traversal, ten-foot viewing, overscan where relevant, input burden, playback, and platform differences. |
| `console-controller` | Game consoles and controller-led apps | Spatial focus, button mapping, controller remapping, couch viewing, multiplayer accounts, accessibility, and interruption. |
| `mobile-ar` | Phone and tablet augmented reality | Camera permission, environment understanding, tracking failure, placement, occlusion, physical context, and accessible alternatives. |
| `immersive-vr` | Virtual reality | Embodied input, locomotion, comfort, readable spatial content, boundaries, orientation, accessibility, and session duration. |
| `mixed-reality-spatial` | Mixed reality and spatial computing | Gaze, hands, depth, spatial layout, passthrough, occlusion, privacy, comfort, physical safety, and 2D alternatives. |
| `automotive-infotainment` | In-vehicle infotainment and projection | Driver/passenger context, distraction constraints, vehicle state, voice, hardware controls, glanceability, and applicable OEM rules. |
| `vehicle-instrumentation` | Vehicle clusters and operational displays | Warnings, prioritization, time-critical interpretation, mode visibility, redundancy, hardware integration, and specialist human-factors validation. |
| `kiosk-atm-pos` | Kiosks, ATMs, checkout terminals, and POS | Standing and seated reach, privacy, shared sessions, payment hardware, receipts, timeouts, gloves, and physical accessibility. |
| `public-large-display` | Signage, control walls, and public large screens | Viewing distance, shared attention, ambient information, legibility, access boundaries, and companion interaction. |
| `industrial-hmi` | Industrial panels and supervisory interfaces | Alarms, abnormal situations, gloves, harsh environments, modes, redundancy, operational workflows, and qualified safety review. |
| `embedded-medical` | Medical-device screens and embedded health systems | Intended users, use environment, risk analysis, alarms, critical tasks, training, traceability, and applicable specialist validation. |
| `iot-smart-home-robotics` | Connected appliances, smart homes, and robots | Pairing, connectivity, ownership transfer, physical/digital state consistency, status, automation, permissions, and manual fallback. |
| `voice-ivr-audio` | Voice assistants, IVR, and audio-only experiences | Turn-taking, prompts, repair, ambiguity, privacy, timeouts, speech differences, interruption, and transfer to humans. |
| `eink-low-power` | E-readers and constrained low-power displays | Refresh limits, monochrome, persistent imagery, slow input, battery, reading tasks, and constrained connectivity. |
| `cross-device-ecosystem` | Journeys spanning multiple devices | Identity, session and task continuity, source of truth, sync, notifications, transfer consent, and conflicting state. |
| `embedded-third-party` | Browser extensions, plugins, and host-app surfaces | Host conventions, constrained space, permissions, context transfer, install/update states, API limitations, and host-version compatibility. |
| `email-document-print` | Email, documents, receipts, and printed service surfaces | Client rendering, semantic documents, accessible exports, pagination, print hierarchy, deep links, and offline continuity. |

#### Design-system and host-product packs

16 starting packs. These are candidates for reference development; inclusion does not imply that a current, fully researched implementation is already bundled.

| Pack | System | What to capture |
| --- | --- | --- |
| `apple-hig` | Apple Human Interface Guidelines | Use the currently applicable platform guidance and native behavior; record platform and OS applicability. |
| `material-android` | Material Design and Android guidance | Map patterns to actual Android capabilities and app quality requirements; preserve project-specific design decisions. |
| `fluent-windows` | Microsoft Fluent and Windows guidance | Use platform-appropriate interaction, input, visual roles, and accessibility guidance. |
| `ibm-carbon` | IBM Carbon | Map enterprise patterns, tokens, components, accessibility guidance, and supported implementation versions. |
| `sap-fiori` | SAP Fiori | Use the applicable SAP product, floorplan, version, extension constraints, and project rules. |
| `oracle-redwood` | Oracle Redwood | Verify the actual product environment, supported components, navigation, and extension constraints. |
| `salesforce-lightning` | Salesforce Lightning | Map object workflows, host constraints, component usage, permissions, and supported versions. |
| `shopify-polaris` | Shopify Polaris | Use relevant commerce and merchant patterns; verify the target surface and current resources. |
| `atlassian-design` | Atlassian Design System | Respect host-product context, component conventions, extensions, and supported versions. |
| `adobe-spectrum` | Adobe Spectrum | Align with applicable product, component, input, theme, and accessibility guidance. |
| `govuk-design` | GOV.UK Design System | Load the relevant service, content, component, accessibility, and service-standard guidance. |
| `uswds` | U.S. Web Design System | Verify applicable government service requirements, component versions, content, and accessibility context. |
| `ant-design` | Ant Design | Apply the project's actual component version, patterns, localization, tokens, and implementation constraints. |
| `other-component-library` | Other UI libraries or framework kits | Capture library identity, version, defaults, missing behavior, semantics, and project overrides; do not treat styling utilities as complete UX guidance. |
| `custom-brand-system` | Company or product design system | Load approved tokens, components, content rules, documented exceptions, ownership, and design-code relationships. |
| `legacy-mixed-system` | Legacy or mixed design environments | Map competing systems, behavior differences, compatibility limits, migration rules, and explicit conflict decisions. |

#### Input and context coverage

| Dimension | Cases to consider when relevant |
| --- | --- |
| Physical input | Touch, mouse, trackpad, hardware keyboard, pen, remote, controller, physical buttons, rotary control, scanner |
| Alternative and assistive input | Voice, switch access, eye or head tracking, screen-reader navigation, speech differences, adaptive controllers |
| Spatial input | Gaze, hands, head pose, tracked controllers, embodied reach, and non-spatial alternatives |
| Output | Visual, speech, sound, captions, transcripts, haptics, printed material, semantic and programmatic state |
| Environment | Noise, quiet spaces, bright light, low light, motion, gloves, wet hands, posture, reach, viewing distance |
| Connectivity and hardware | Offline, unstable networks, latency, background interruption, memory limits, low power, sensor or peripheral failure |
| Social and operational context | Shared devices, public spaces, managed workstations, privacy, expert work, assisted service, caregiving, urgency |
| Human variation | Ability, temporary impairment, literacy, language, experience, age, fatigue, stress, and cultural or regional context |

58 starting packs. Each must be developed around real roles, terminology, entities, rules, exceptions, context, and evidence. These are coverage specifications, not completed regulated-domain guides or certifications. New niches can extend the same contract.

| Pack | Industry or niche | Essential domain coverage |
| --- | --- | --- |
| `banking` | Banking and money movement | Balances, available versus pending amounts, beneficiaries, transfers, authentication, disputes, and clear consequences. |
| `consumer-credit` | Consumer lending and credit | Eligibility, application status, affordability information, disclosures, repayment, hardship, and adverse outcomes. |
| `leasing-asset-finance` | Leasing and asset finance | Dealers, contracts, assets, facilities, quotations, disbursement, settlement, servicing, and exceptions. |
| `insurance` | Insurance | Quote, underwriting questions, coverage, exclusions, documents, renewals, claims, and intermediaries. |
| `wealth-investing` | Investing and wealth | Account context, holdings, orders, risk communication, fees, timing, statements, and transaction status. |
| `payments-remittance` | Payments and remittance | Recipient identity, exchange and fee clarity, authorization, pending states, duplicates, refunds, and reconciliation. |
| `accounting-tax` | Accounting and tax | Ledger meaning, reporting periods, adjustments, approvals, audit history, reconciliation, and filing context. |
| `ecommerce-retail` | Commerce and retail | Catalogs, variants, inventory, comparison, cart, checkout, delivery, returns, and customer support. |
| `marketplaces` | Multi-sided marketplaces | Supply/demand roles, matching, trust, reputation, disputes, payouts, moderation, and platform incentives. |
| `subscription-saas` | Subscription software | Tenants, plans, entitlements, trials, metering, provisioning, billing, upgrades, and cancellation. |
| `erp-backoffice` | ERP and back-office operations | Linked business objects, workflows, permissions, bulk work, data integrity, audit, and configuration. |
| `crm-sales` | CRM and sales systems | Leads, accounts, contacts, opportunities, pipeline, ownership, communication history, and handoffs. |
| `procurement` | Procurement and supplier systems | Requisitions, supplier qualification, approvals, orders, receipt, invoice matching, and exceptions. |
| `warehouse-logistics` | Warehouses and logistics | Receiving, putaway, inventory, picking, packing, shipping, scanning, traceability, and operational exceptions. |
| `manufacturing` | Manufacturing and industrial operations | Work orders, production stages, quality, equipment state, alarms, shift handoffs, and constraints. |
| `hr-workforce` | HR, payroll, and workforce | Applicants, employee records, attendance, payroll status, benefits, sensitive data, approvals, and offboarding. |
| `clinical-healthcare` | Clinical healthcare | Patient identity, clinician workflow, orders, results, documentation, interruptions, critical actions, and clinical specialist review. |
| `patient-healthcare` | Patient and telehealth services | Appointments, records, access, caregiver delegation, consent, comprehension, care navigation, and escalation. |
| `medical-devices` | Medical devices | Intended use, users, environments, critical tasks, alarms, misuse, training, risk controls, and qualified validation. |
| `pharma-laboratory` | Pharma and laboratory systems | Samples, provenance, workflows, test results, traceability, controlled change, review, and specialist requirements. |
| `mental-health-wellness` | Mental health and wellness | User autonomy, sensitive disclosures, wellbeing outcomes, boundaries, escalation pathways, and appropriate clinical review. |
| `education-learning` | Education and learning | Learners, teachers, progress, feedback, assessment, accessibility, attention, mastery, and learning evidence. |
| `children-family` | Children and family products | Developmental needs, caregiver roles, child comprehension, age appropriateness, privacy, agency, and local specialist requirements. |
| `older-adult-care` | Older-adult and care services | Perceptual and cognitive variation, autonomy, caregivers, accessibility, trust, delegation, and continuity. |
| `assistive-products` | Assistive and accessibility products | Real assistive workflows, compatibility, customization, fatigue, recovery, accessible setup, and disabled-user participation. |
| `audio-video-media` | Audio, video, and streaming | Discovery, playback, queues, background behavior, captions, transcripts, rights, offline access, and continuity. |
| `publishing-news` | Publishing and news | Reading, credibility, provenance, subscriptions, corrections, archives, editorial workflow, and accessibility. |
| `creator-design-tools` | Creative and authoring tools | Canvas or document models, precision, layers, versions, export, assets, shortcuts, and collaboration. |
| `social-community` | Social and community platforms | Identity, audience, posting, moderation, reporting, boundaries, community health, and abuse recovery. |
| `messaging-collaboration` | Messaging and collaboration | Conversation structure, presence, notifications, permissions, search, files, context, and async handoffs. |
| `games` | Games and game interfaces | Onboarding, HUD, menus, control mapping, accessibility, progression, feedback, multiplayer state, and responsible monetization. |
| `sports-fitness` | Sports and fitness | Training context, logging, wearable data, goals, recovery, accessibility, and limits of coaching claims. |
| `travel-ticketing` | Travel and passenger ticketing | Search, fare rules, itineraries, traveler data, disruption, check-in, accessibility, and multi-party journeys. |
| `hospitality-booking` | Hospitality and accommodation | Availability, rates, terms, check-in, guest requests, cancellations, service recovery, and staff handoffs. |
| `delivery-ride-hailing` | Delivery and ride-hailing | Location, matching, ETA uncertainty, tracking, substitutions, safety support, payments, and disputes. |
| `transport-navigation` | Transport and navigation | Routes, accessibility, real-time status, wayfinding, ticket context, low-connectivity use, and disruption. |
| `automotive-mobility` | Automotive and mobility products | Vehicle ownership, dealership or fleet roles, driving context, connected services, maintenance, and operational constraints. |
| `real-estate-property` | Real estate and property management | Listings, comparison, viewings, applications, ownership, rent, maintenance, documents, and permissions. |
| `construction-built-environment` | Construction and built-environment tools | Plans, site context, revisions, issues, contractor roles, approvals, offline work, and physical dependencies. |
| `government-civic` | Government and civic services | Eligibility, understandable policy, public access, assisted service, evidence, status, appeals, and inclusion. |
| `legal-justice` | Legal and justice services | Case state, sensitive records, comprehension, deadlines, evidence, access, representation, and specialist review. |
| `nonprofit-humanitarian` | Nonprofit and humanitarian services | Beneficiary dignity, donor and field roles, distribution, access barriers, consent, reporting, and constrained environments. |
| `religious-cultural` | Religious and cultural products | Trusted sourcing, script and audio accuracy, regional practice, accessibility, content verification, and respectful learning. |
| `agriculture` | Agriculture and farming | Seasonal tasks, field conditions, local language, low connectivity, sensors, supply, advisory confidence, and traceability. |
| `energy-utilities` | Energy and utilities | Consumption, billing, outages, field work, tariffs, meters, safety-sensitive operations, and vulnerable customers. |
| `climate-environment` | Climate and environmental tools | Measurement provenance, uncertainty, maps, scenarios, behavior choices, reporting, and credible impact claims. |
| `telecommunications` | Telecommunications | Plans, provisioning, connectivity, usage, roaming, troubleshooting, outages, billing, and support. |
| `developer-infrastructure` | Developer tools and infrastructure | Projects, environments, logs, versions, permissions, APIs, deployments, observability, errors, and expert workflows. |
| `cybersecurity-identity` | Cybersecurity and identity systems | Threat context, access, alerts, triage, permission scope, recovery, audit, escalation, and specialist verification. |
| `science-research` | Scientific and research software | Data provenance, reproducibility, processing, uncertainty, analysis, lab or field workflows, and collaboration. |
| `geospatial-gis` | Geospatial and GIS | Layers, projections, spatial queries, scale, legend, editing, data quality, alternative representations, and field use. |
| `food-grocery` | Food and grocery services | Dietary information, substitutions, freshness, allergens, order changes, delivery, and relevant specialist review. |
| `events-ticketing` | Events and ticketing | Discovery, capacity, seat selection, queues, transfer, refunds, entry, accessibility, and organizer workflows. |
| `blockchain-digital-assets` | Blockchain and digital-asset products | Wallet scope, signing consequences, networks, fees, custody, irreversible actions, uncertainty, and specialist review. |
| `fleet-field-service` | Fleet and field service | Dispatch, route or job assignment, technician tools, evidence capture, parts, offline use, completion, and exception handling. |
| `safety-critical-transport` | Aviation, rail, and maritime interfaces | Modes, alarms, time-critical tasks, redundancy, trained operators, operational context, and applicable expert human-factors validation. |
| `emergency-crisis` | Emergency and crisis services | Urgency, stress, triage, location, communication, uncertain information, access, escalation, and trained specialist oversight. |
| `public-identity-infrastructure` | Public identity and verification | Enrollment, proofing, identity attributes, credentials, accessibility, correction, delegation, recovery, and local authority requirements. |

### Context contract

For each applied profile record the supported product/version, actual actors and tasks, data meanings, object states, business rules, permissions, platform/input, language/region, environment, sources, owner, evidence, specialist responsibilities, known gaps and update trigger. Resolve conflicts explicitly.
