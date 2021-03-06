# Open Source Voting System Project Recommendations

(Approved by OSVTAC on March 14, 2019.)

Last posted: June 9, 2019


* [Introduction & Table of Contents](index) (for multi-page version)

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">
<img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" />
</a><br />This work is licensed under a
<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative
Commons Attribution-ShareAlike 4.0 International License</a>.
For copyright and attribution information for this work, see
[this section](copyright). The source files for the text can be found on
GitHub [here](https://github.com/OSVTAC/project-recommendations).


## Contents

* [1. Copyright and Attribution](#1-copyright-and-attribution)
  * [1.1. Copyright](#11-copyright)
  * [1.2. Contributors](#12-contributors)
* [2. Goals](#2-goals)
  * [2.1. Scope](#21-scope)
  * [2.2. Priorities](#22-priorities)
  * [2.3. Non-goals](#23-non-goals)
* [3. Background](#3-background)
  * [3.1. History of Open Source Voting in San Francisco](#31-history-of-open-source-voting-in-san-francisco)
  * [3.2. Voting System](#32-voting-system)
  * [3.3. Other Voting System Projects](#33-other-voting-system-projects)
  * [3.4. Resources](#34-resources)
* [4. Facts & Assumptions](#4-facts--assumptions)
  * [4.1. Facts](#41-facts)
  * [4.2. Assumptions](#42-assumptions)
* [5. Components](#5-components)
  * [5.1. Component Listing](#51-component-listing)
  * [5.2. Component Details](#52-component-details)
* [6. Recommendations](#6-recommendations)
  * [6.1. Interim Voting System](#61-interim-voting-system)
  * [6.2. Requirements-gathering](#62-requirements-gathering)
  * [6.3. Requirements](#63-requirements)
  * [6.4. Project Management](#64-project-management)
  * [6.5. Open Source](#65-open-source)
  * [6.6. Procurement](#66-procurement)
  * [6.7. Software architecture and design](#67-software-architecture-and-design)
  * [6.8. Software development](#68-software-development)
  * [6.9. Hardware design](#69-hardware-design)
  * [6.10. Documentation](#610-documentation)
  * [6.11. Security](#611-security)
  * [6.12. Testing](#612-testing)
  * [6.13. Certification](#613-certification)
  * [6.14. Hardware manufacturing or assembly](#614-hardware-manufacturing-or-assembly)
  * [6.15. Deployment](#615-deployment)
  * [6.16. Software maintenance](#616-software-maintenance)
  * [6.17. Hardware maintenance](#617-hardware-maintenance)
* [7. Recommended Implementation Order](#7-recommended-implementation-order)
  * [7.1. Recommended First Components](#71-recommended-first-components)
  * [7.2. Rationale](#72-rationale)
  * [7.3. Results Reporter Rationale](#73-results-reporter-rationale)
  * [7.4. Vote Totaler Rationale](#74-vote-totaler-rationale)
  * [7.5. Central Ballot Scanner Rationale](#75-central-ballot-scanner-rationale)
  * [7.6. Deployment Strategies](#76-deployment-strategies)
  * [7.7. Central Ballot Scanner Phases](#77-central-ballot-scanner-phases)
* [8. Equipment (“Product”) Decisions](#8-equipment-“product”-decisions)
  * [8.1. Will vote centers be used for early and/or election day voting?](#81-will-vote-centers-be-used-for-early-andor-election-day-voting)
  * [8.2. Should precinct polling and vote centers use the same paper ballots as those used in vote-by-mail?](#82-should-precinct-polling-and-vote-centers-use-the-same-paper-ballots-as-those-used-in-vote-by-mail)
  * [8.3. Should ballots to be hand-marked be preprinted or printed on demand?](#83-should-ballots-to-be-hand-marked-be-preprinted-or-printed-on-demand)
  * [8.4. Should voting at a precinct or vote center be primarily based on paper ballots hand-marked with a pen, or voting machine with a printer?](#84-should-voting-at-a-precinct-or-vote-center-be-primarily-based-on-paper-ballots-hand-marked-with-a-pen-or-voting-machine-with-a-printer)
  * [8.5. If voters use machines to mark ballots, should the machine store CVRs of the marked selections?](#85-if-voters-use-machines-to-mark-ballots-should-the-machine-store-cvrs-of-the-marked-selections)
  * [8.6. Should a machine-marked ballot contain a bar code with a digital signature and/or CVR?](#86-should-a-machine-marked-ballot-contain-a-bar-code-with-a-digital-signature-andor-cvr)
  * [8.7. If voting machines are used at a precinct, should there be one printer per voting station?](#87-if-voting-machines-are-used-at-a-precinct-should-there-be-one-printer-per-voting-station)
  * [8.8. If voters at precincts use hand-marked ballots, should ballots be scanned centrally or at the precinct/vote center?](#88-if-voters-at-precincts-use-hand-marked-ballots-should-ballots-be-scanned-centrally-or-at-the-precinctvote-center)
  * [8.9. If a precinct scanner is used, does the scanner need to be integrated with a ballot collection bin?](#89-if-a-precinct-scanner-is-used-does-the-scanner-need-to-be-integrated-with-a-ballot-collection-bin)
  * [8.10. If a precinct scanner (or central scanner) is used, does it need to include an imprinter to record a ballot/scan ID?](#810-if-a-precinct-scanner-or-central-scanner-is-used-does-it-need-to-include-an-imprinter-to-record-a-ballotscan-id)
  * [8.11. If a voting machine is used to print all precinct ballots and possibly save CVRs, does the ballot collection box need to have an integrated scanner?](#811-if-a-voting-machine-is-used-to-print-all-precinct-ballots-and-possibly-save-cvrs-does-the-ballot-collection-box-need-to-have-an-integrated-scanner)
  * [8.12. Is voting equipment required to run off a battery (without outside AC power) for a set outage duration or all day?](#812-is-voting-equipment-required-to-run-off-a-battery-without-outside-ac-power-for-a-set-outage-duration-or-all-day)
  * [8.13. What kind of printing technology should be used at a poll site or vote center?](#813-what-kind-of-printing-technology-should-be-used-at-a-poll-site-or-vote-center)
  * [8.14. What size paper should be used for precinct voting and vote by mail?](#814-what-size-paper-should-be-used-for-precinct-voting-and-vote-by-mail)
  * [8.15. What options should be provided to people with disabilities?](#815-what-options-should-be-provided-to-people-with-disabilities)
  * [8.16. Should "remote accessible vote-by-mail" (RAVBM) printing used by voters with disabilities to vote by mail using home computers also be used for accessible precinct voting?](#816-should-remote-accessible-vote-by-mail-ravbm-printing-used-by-voters-with-disabilities-to-vote-by-mail-using-home-computers-also-be-used-for-accessible-precinct-voting)
  * [8.17. Does ballot collection order or CVR recordings need to be randomized to protect voter privacy (be disassociated by order of appearance at a precinct)?](#817-does-ballot-collection-order-or-cvr-recordings-need-to-be-randomized-to-protect-voter-privacy-be-disassociated-by-order-of-appearance-at-a-precinct)
  * [8.18. Should scanned ballot images or compiled CVRs be an open public record, possibly electronically accessible?](#818-should-scanned-ballot-images-or-compiled-cvrs-be-an-open-public-record-possibly-electronically-accessible)
  * [8.19. End-to-end verifiability](#819-end-to-end-verifiability)
* [9. FAQ](#9-faq)
* [10. Glossary](#10-glossary)


## 1. Copyright and Attribution

This section contains the copyright and attribution information for
the Open Source Voting System Technical Advisory Committee's (OSVTAC)
[Open Source Voting System Project Recommendations](index).


### 1.1. Copyright

Copyright (C) 2017, 2018 Larry Bafundo

Copyright (C) 2017, 2018 Carl Hage

Copyright (C) 2017, 2018 Christopher Jerdonek

Copyright (C) 2017, 2018 Roan Kattouw

Copyright (C) 2017, 2018 Tony Wasserman


### 1.2. Contributors

* Larry Bafundo
* Carl Hage
* Christopher Jerdonek
* Roan Kattouw
* Tony Wasserman


## 2. Goals

This section discusses the goals, scope, and priorities of this document and
the Committee.

The TAC’s Bylaws say that the TAC’s purpose is to “provide technical
guidance, ideas, and support to the Elections Commission on ways to improve
and help ensure the success of the City and County of San Francisco's open
source voting system project.” The focus of TAC's effort will be on
establishing parameters and recommendations to guide the future development
of the voting system.

The TAC will draw on its technical expertise, the expertise of other members
in the community, and from similar efforts (including other open source
voting efforts) to provide guidance in areas including but not limited to
open source, requirements-gathering, design, architecture, development,
documentation, security, testing, certification, manufacturing, deployment,
system maintenance, strategies for procurement, and project management.


### 2.1. Scope

1. This document will limit itself to current laws that San Francisco must
  satisfy, or to changes in law that San Francisco anticipates (e.g. possibly
  transitioning to the “vote center” model allowed by [SB
  450][bill-sb-450-2015] of 2015-2016). In particular, the document will
  restrict itself to considering paper-ballot systems.

2. For the purposes of this document, “voting system” includes anything that
  is currently the responsibility of the voting system in use today.
  Responsibilities of a voting system include allowing voters to mark ballots
  (if not using pen and paper), counting ballots, reporting election
  results, and ensuring the integrity of the process.
  In addition, it may include ballot design and layout, as well as
  the functionality of a “remote accessible vote by mail system” as described
  in [AB 2252][bill-ab-2252-2015] (2015-2016). It should also facilitate
  auditing the results of an election. The responsibilities of a voting
  system do not include the responsibilities of a voter registration system.
  The voting system may need to interoperate with the Department’s EIMS®
  application. If the ballots
  are pre-printed, the voting system need not be capable of printing ballots.


### 2.2. Priorities

1. This document should prioritize high-level recommendations over low-level
  recommendations.

2. This document should prioritize recommendations that are needed sooner
  rather than later.


### 2.3. Non-goals

1. The Committee will not be designing or developing a voting system.

2. The Committee will not be drafting detailed, low-level specs that the
  voting system should satisfy.

3. The Committee will not be drafting an exhaustive list of requirements.

4. The Committee will not be recommending particular vendors. However, the
  Committee may evaluate particular _systems_.

5. The Committee will not make explicit attempts to accommodate internet
  voting in any form, nor voting methods not used in San Francisco. This does
  not preclude the Committee from recommending software designs or practices
  that could make such things easier to accommodate as a side effect.

6. The Committee's recommendations will prioritize the voting system needs of
  San Francisco without emphasizing the needs of other jurisdictions.
  The needs of other
  jurisdictions will be considered insofar as it could help to develop and
  certify a system for use in San Francisco sooner (for example, if San
  Francisco were to collaborate with another jurisdiction and share costs).
  However, as stated in the previous point, this does not preclude
  recommending designs and practices that could make it easier to accommodate
  other jurisdictions.


## 3. Background


### 3.1. History of Open Source Voting in San Francisco

To provide context to the recommendations in this document, this section
describes some of the history of the open source voting topic in San
Francisco government.

In May 2007, the [San Francisco Elections Commission][elections-commission]
passed a resolution that, among other things, established a policy that the
Department of Elections give priority to voting systems that “provide the
maximum level of security and transparency possible consistent with the
principles of public disclosure.” However, like today, no certified open
source voting systems were available at that time.

In December 2007 the City, through the Department of Elections, entered into
contract with Sequoia Voting Systems, Inc. for a new, proprietary voting
system. In June 2010, [Dominion Voting Systems,
Inc.](http://www.dominionvoting.com/) acquired Sequoia and assumed Sequoia's
contract. The Department and City extended the contract with Dominion more
than once. The current contract is scheduled to end at the end of 2018. The
total cost of the extended contract over the eleven years (including hardware
and hardware maintenance, software license fees, and election services) was
approximately $22 million, with $9.6 million of that up front. This averages
to around $2 million per year (see [this table][dominion-costs-2008] for an
annual breakdown).

In November 2008, the [Board of Supervisors][board-of-supervisors] passed an
[ordinance][bos-ordinance-vstf] creating a [Voting Systems Task Force][vstf]
(VSTF) to provide the City with recommendations on voting systems and related
matters, including “models for [the] development of a voting system including
proprietary, disclosed and open source software and hardware approaches.”

In June 2011, the VSTF issued its [final report][vstf-report],
“Recommendations on Voting Systems for the City and County of San Francisco”
(57 pages). Here are two excerpts from the recommendation text that mention
open source (from page 52):

> **2.5.4.3 Transparency, Source Code Disclosure, Licensing, and Contingency
Planning**
>
> 6\. The DOE should give strong preference to a voting system licensing
structure that gives San Francisco all of the rights provided by an
OSI-approved license, even if the system is maintained by an external party.
>
> ...
>
> 8\. San Francisco should be an active participant in the movement toward
more open and transparent voting systems. We acknowledge the complexity of
moving from the existing marketplace toward more innovative voting systems
and urge San Francisco to move steadily toward the goal of transparency—even
if it must do so in incremental steps.

In December 2014, the San Francisco Board of Supervisors unanimously passed a
[resolution][bos-open-source-voting-res] supporting the creation of open
source voting systems and requesting that the [San Francisco Local Agency
Formation Commission][lafco] (LAFCo) conduct a feasibility study. In October
2015, LAFCo issued its [final report][lafco-report], “Study on Open Source
Voting Systems” (37 pages).

In November 2015, the Elections Commission unanimously passed an [Open Source
Voting Systems Resolution (PDF)][commission-res-pdf-local] (also in
[plain-text][commission-res-txt-local]; both from the [Commission's "Motions
and Resolutions" page][commission-resolutions]) requesting that the Mayor
and Board of Supervisors initiate and fund a project to develop and certify
an open source voting system.

In August 2016, San Francisco Mayor Ed Lee
[signed][mayor-budget-press-release] the City and County of San Francisco’s
two-year budget for the 2016-2017 and 2017-2018 fiscal years. The budget
allocated $300,000 towards the planning phase of an open source voting system
project. Below are two excerpts from the [proposed budget
document][proposed-budget-2016] that reference the open source voting project.

The section for the Department of Elections references the project on pages
204-205:

> As the City's current voting system nears end-of-life, the proposed budget
includes $300,000 towards planning and development of a new voting system
based on open source software. If completed, San Francisco would be the first
City to do this. Development of an open source voting system would enable the
City to own the voting system's software and to have a choice of publicly
releasing it under open source license. Additionally, other jurisdictions as
well as the general people could use, participate, and improve the software.

The section for the [Committee on Information Technology][coit] (COIT)
includes the project as one of five highlighted projects out of twenty-four,
alongside initiatives like the City's new [Digital
Services][sf-digital-services] Team, cybersecurity, and improving the City's
network (pages 447-448):

> ANNUAL PROJECTS
>
> ...
>
> Over the two-year period, the proposed budget recommends $15.7 million of
General Fund COIT allocation to support 24 projects. Below are a few
highlighted projects.
>
> ...
>
> OPEN SOURCE VOTING SYSTEM
>
> As the City’s current voting system is aging, the Department of Elections
is exploring an opportunity to develop a new voting system based on open
source software. If completed, San Francisco would be the first city to do
this. Development of an open source voting system would enable the City to
own the voting system’s software and have a choice of publicly releasing it
under an open source license. Additionally, other jurisdictions as well as
the general public could use and improve the software. The proposed budget
supports initial project planning and scoping of this project.

In April 2017, the Board of Supervisors approved the City’s fourth Five-Year
[Information & Communication Technology (ICT) Plan for Fiscal Years 2018-22][ict-plan-2008].
The plan included the open source voting system project among four major IT
projects under consideration for the future, alongside projects like
Universal Broadband and Voice over Internet Protocol (VoIP). For example, on
page 11:

> However, several future projects are currently being scoped out as
potentially the City’s next Major IT Project, including:
>
> ...
>
> **Voting System Replacement:** The Department of Elections is currently
investigating alternative voting systems, including the possibility of
building an open source system.

And on page 53:

> **Future Major IT Projects**
>
> In addition, the City has begun investigating what may become the next major
technology project. Before beginning any new technology venture, the City
recommends extensive planning and scoping to better understand the true cost
of any new technology. The City has begun evaluating various different
projects that may be considered as major investments, which include:
>
> ...
>
> **Voting System Replacement:** The City’s current voting system license is
set to expire in 2018. Without a long-term contract in place, the City has an
opportunity to pursue alternative voting systems that could promote
transparency and more security. The City is currently investigating
alternative options, including the possibility of building an open source
system.

In April 2017, the Elections Commission voted to create an [Open Source Voting
System Technical Advisory Committee][commission-osvtac] to “provide technical guidance, ideas,
and support to the Elections Commission (’Commission’) on ways to improve and
help ensure the success of the City and County of San Francisco's open source
voting system project.” The Commission voted on the Committee's initial
membership at its May meeting. The Committee was fully constituted on June 2,
2017, when the appointment of the fifth member was made final.

In May 2017, the Department of Elections [issued an
RFP][rfp-business-case-pdf] (REG RFP #2017‑01)
for a contractor to “prepare a business case for developing an accessible,
open source voting system.” The RFP would use a portion of the $300,000
budgeted in August 2016. In September 2017, Slalom was selected as the
winning bidder. Slalom's deliverable will be due in January 2018, and it
will inform the City's next budget process, which will begin around that time.
See here for [Slalom's RFP response][slalom-rfp-response], the City's
[contract][slalom-contract] with Slalom, and
[Appendix A][slalom-contract-appendix-a] and
[Appendix B][slalom-contract-appendix-b] of the contract.

The Department of Elections' contract for its current voting system expires
at the end of December 2018. The Director of Elections is aiming to lease an
interim system from that point forward that can be used while an open source
voting system is developed and certified. The RFP for the interim system may
be issued as early as the fall of 2017.


### 3.2. Voting System


#### 3.2.1. Definition

The [Help America Vote Act][hava] (HAVA) of 2002 defines a voting system as
follows (from 52 USC §21081: Voting systems standards):

    (b) Voting system defined
     In this section, the term "voting system" means—
     (1) the total combination of mechanical, electromechanical,
      or electronic equipment (including the software, firmware,
      and documentation required to program, control, and support
      the equipment) that is used—
      (A) to define ballots;
      (B) to cast and count votes;
      (C) to report or display election results; and
      (D) to maintain and produce any audit trail information; and
     (2) the practices and associated documentation used—
      (A) to identify system components and versions of such
       components;
      (B) to test the system during its development and maintenance;
      (C) to maintain records of system errors and defects;
      (D) to determine specific system changes to be made to a system
       after the initial qualification of the system; and
      (E) to make available any materials to the voter (such as
       notices, instructions, forms, or paper ballots).

[hava]: https://www.eac.gov/about/help-america-vote-act/


### 3.3. Other Voting System Projects

This section includes information about some of the other voting system
projects that are either (1) open source and have been or plan to be used in
a US jurisdiction, or (2) are or were being developed by a jurisdiction in
the US.

Special attention is paid in this section towards whether the various
projects are open source because that determines whether and to what extent
the source code will be available for use in San Francisco's project.


#### 3.3.1. New Hampshire - Prime III

[TODO]


#### 3.3.2. Los Angeles County - VSAP

Los Angeles County has been planning or working on its [Voting Systems
Assessment Project][la-vsap] (VSAP) at least since 2009, when
it held an event at Caltech on September 16, 2009. VSAP is a project for Los
Angeles County to develop its own voting system using a “voter-centered
approach.“ The project is led by Los Angeles County Registrar-Recorder/County
Clerk (RR/CC) Dean Logan.

There is conflicting evidence as to whether any of the VSAP system will be
open source and, if so, how much. On the one hand, press coverage of the
project frequently mentions that the system will be open source, and Mr.
Logan says it will be open source when he speaks publicly and is quoted in
the media. For example, in [this
tweet](https://twitter.com/LACountyRRCC/status/904871828799209472) he says,
“Encouraging to see movement in this direction. #LACounty advances
#opensource in #votingmodernization effort too.“

Los Angeles County's April 24, 2017 [VSAP RFI #17-001][la-vsap-rfi] also supports the
view that it will be open source. For example, on page 24, it says:

> Accordingly, RR/CC is considering a Copyleft type of license such as GNU
General Public License (GPL) or OSET Public License (OPL), that promotes
“forever free” provisions, however it has not ruled out the use of more
“permissive” open source licenses, such as the Mozilla Public License Version
2.0 (MPL), the Apache License, Version 2.0 (ALv2), the BSD 3.0 or MIT
licenses. Whatever the chosen license, the transparency and ability to share
the IP and the technology would need to be ensured.
> ...
> LA County is seeking candid feedback from the vendor community on the
intellectual property approach for VSAP.

On the other hand, there is no obvious mention of open source on VSAP's main
website (e.g. on its [“Principles“](http://vsap.lavote.net/principles/)
page). Moreover, Los Angeles County's 54-page [RFP Phase 1: #17-008][la-vsap-rfp-phase-1],
which was issued five months after the RFI on September 18, 2017 to
prequalify vendors, does not mention open source. The Phase 1 RFP also
describes a new “Tally System“ the County is working on:

> A new Tally System is required to capture and process ballot images so that
vote selections on paper ballots can be digitally counted. This includes
votes cast on BMD ballots at Vote Centers, as well as on Vote By Mail
ballots. Similar to the ECBMS, RR/CC is currently developing the software
required for the new Tally System in anticipation of a pilot in June 2018.

Los Angeles County submitted its VSAP Tally Version 1.0 to the California
Secretary of State for certification on September 19, 2017.  See their
application for approval [here][la-vsap-application-tally] (PDF, 21 pages).

However, even though the County is developing the Tally System and submitted
it for certification, as
of October 2017, none of the code for the Tally System appears to be publicly
available, let alone open source. In addition, on page 41 of the RFP in
Section 6.2 “Non-Disclosure Agreement,“ the RFP says—

> Prime Contractor-Led Teams who are prequalified as a result of this RFP
Phase 1 will be required to sign a Non-Disclosure Agreement (NDA) as part of
RFP Phase 2 prior to receiving County IP.

The requirement to sign an NDA seems inconsistent with the technology being
open source.

Finally, in response to an October 5 question on Twitter about whether
VSAP will be open source, Mr. Logan [replied](https://twitter.com/LACountyRRCC/status/916114599241330689):

> Open source platform for UI and tally; publicly owned design specs and
code. More detail in RFI docs at http://vsap.lavote.net

And in a [second reply](https://twitter.com/LACountyRRCC/status/916381787605000192):

> Tally stack is all open source; details of licensing for custom code will
be in Phase II RFP & was discussed in RFI; all publicly owned.

So if “platform“ and “stack“ refer to things like the operating system,
database, programming language, etc. but not the code itself, it seems
possible that none of the code will be open source but instead simply be
“publicly owned.“ It would be helpful if Los Angeles County can provide a
clearer guarantee if this interpretation isn't correct.


#### 3.3.3. Travis County, Texas - STAR-Vote™

In 2012, Travis County, Texas started researching and designing a new voting
system it called STAR-Vote™. The County spent over $330,000 in its research
and design phase.

In October 2016, Travis County issued a detailed 208-page [RFP][star-vote-rfp]
covering the first phase of STAR-Vote, which was the “in-person voting
module of the STAR-Vote system.“ The RFP made frequent reference to open
source software. For example, on page 5:

> The STAR-Vote system requirements were developed from the ground up with
the purpose, among other objectives, of specifying an entire voting system
developed under the open source code software model.

However, the commitment to open source seemed uncertain because the RFP said
the code would start out not as open source but as disclosed source,
and possibly be made open source later. For example, on page 37 (note the
phrase, “with a view toward ultimately ...“):

> Source code for all modules would be published, but usage rights for actual
elections as well as derivative rights (as in using the code to create a
derivative voting system) would be controlled by Travis County (and/or
consortium) with a view toward ultimately releasing usage and derivative
rights under a “suitable” (as determined by Travis County and/or consortium)
open source license that would allow and encourage preparation of third-party
derivative work, recognizing that voting systems must be state and federally
certified;

The RFP was accompanied by an additional 16-page [“Statement of Intent“][star-vote-entity]
document, which sought $25 million (initially a minimum of
$15 million) for an entity (likely a non-profit) called the “STAR-Vote
Entity.“

On September 28, 2017, Travis County announced via a [press
release][star-vote-final-press-release] that the County would not be pursuing
STAR-Vote. From their [Final Report][star-vote-final-report] (6 pages)--

> In a nutshell, we have run into too many obstacles. There has not been
enough funding, time, or support to bring STAR-Vote into the phase of being a
start-up, through development and the legally-required certification process
and then into use.


### 3.4. Resources

This section contains links to other resources and documents that may be
useful for the project.


#### 3.4.1. San Francisco

   * The San Francisco Department of Elections' [planning phase
     RFP][rfp-business-case-pdf] (REG RFP #2017‑01, "Preparing a Business
     Case for Developing an Accessible, Open Source Voting System"). In
     particular, see the list of links in Section I.A. starting on page 5.
   * [San Francisco Digital Services Team][sf-digital-services]


#### 3.4.2. Procurement

   * U.S. Digital Services' [TechFAR Handbook][techfar-handbook]
   * 18F's [Modular Contracting][18f-modular-contracting] page


#### 3.4.3. Related Software Projects for US Government Elections

   * [ColoradoRLA][colorado-rla-home], (Risk Limiting Audit) Project. Colorado Secretary of State.
     Software to upload electronic CVRs (cast-vote-records), randomly
     select ballots to audit, then hand check hand selected paper ballots
     against stored CVRs or re-scanned paper ballots.

     Contractor for open source software is [Free & Fair][free-and-fair]
     git: [ColoradoRLA][colorado-rla-repo], [OpenRLA][open-rla-repo].

     OpenCount now from Free & Fair \[[git][open-count]\] is software to
     tabulate scanned ballots, used with RLA when original systems
     do not store CVRs. \[[Presentation][open-count-pres]\].

   * [Voting Systems Assessment Project][la-vsap] (VSAP), Los Angeles County
     Voting station design with tablet and printer-scanner. Blank ballot sheets
     are inserted into printer-scanner, tablet used to make selections,
     printer emits printed and marked ballot for review, scanner records
     and feeds into collection box. Smartphone app allows pre-recorded
     votes to be entered via QR code. Soliciting vendors for implementation.

   * [Prime III][prime-iii], Dr. Juan E. Gilbert (now hosted at University of Florida)
     Tablet with docking station with keyboard and laser printer, open software.
     Allows home computer or phone to prepare QR code.
     \[[Video Demo][prime-iii-video]\] \[[Online Demo][prime-iii-demo]\]
     \[[git][prime-iii-repo]\]

     Used by NH in 2016 for accessible voting (ballot marking device) statewide.
     NH revised version is known as [one4all][one4all-vvf]
     (no known source code location). Can print OCR ballot or mark
     ovals on preprinted ballot. A [slide presentation ][one4all-ppt]
     describes the hardware (windows tablet, keyboard, and printer).
     Videos: \[[Demo][one4all-demo]\], \[[How to Use][one4all-howto]\],
     \[[Setup Instructions][one4all-setup]\].
     The Secretary of State, William Gardner, sent a [letter][one4all-ltr]
     to [CAVO][cavo] describing the program.

     _[Item edited: Feb. 8, 2018 meeting.]_

   * [STAR-Vote][star-vote-usenix], Travis County, TX
     PDF paper and slides for presentation on Travis County TX proposed system.
     Uses off the shelf tablet to produce printed ballot with only choices
     made. Scanner only reads IDs of ballots placed in box to record which
     ballots printed are cast. Electronic records separate. (No mail ballots.)
     Voters can check receipt with QR code.
     [Demo/prototype implementation by Free & Fair][star-vote-faf-repo].


#### 3.4.4. Other Open Source Voting Projects and Research

   * [Pvote][pvote], a model for an open source voting application where
     sensitive software is minimized-- 460 lines of python code, audited
     in a security review.

   * [VoteBox][votebox], a prototype electronic voting machine based on
     COTS hardware. Several technical publications are available with
     detailed descriptions of the system components.

   * [Low Error Voting Interface][levi] (LEVI), research paper of a voting
     machine GUI designed to reduce user errors. Used by Prime-III.

   * [RCV package in CRAN][cran-rcv], a package for R that tabulates
     ranked-choice elections. The README uses San Francisco's 2016 races as
     examples, and it has been used by members of the public to
     [visualize the RCV eliminations][fromira-twitter-rcv] in the June 2018
     election.

_[Subsection added: Jan. 18, 2018 meeting; edited: June 14, 2018 meeting.]_


#### 3.4.5. Open Source Voting Organizations

   * [OSET Foundation][oset-foundation] 501c umbrella nonprofit to support [Trust the Vote][trust-the-vote],
     site with actual software. \[Currently, mostly Ruby-On-Rails in ruby
     using IEEE 1622 data models.\]

     Useful diagrams of voting software architecture: ([PDF][oset-arch-pdf], [broken interactive HTML][oset-arch-html]),
     Simpler [diagram of modules][oset-modules].

     Prototype of [VoteStream][trust-the-vote-votestream] election results display.

   * [Open Voting Consortium][open-voting-consortium] Inactive (since 2011)
     prior effort to develop open source software. Efforts moved to CAVO.
     A demo implementation was created and
     [technical paper][open-voting-consortium-usenix-paper] with a
     detailed description of the system using COTS hardware.

     _[Item edited: Jan. 18, 2018 meeting.]_

   * [California Association of Voting Officials][cavo] (CAVO)
     Nonprofit organization to promote open source voting. Election officials
     from several California counties are members, as well as other groups.

   * [Verified Voting Foundation][verified-voting-foundation],
     nonprofit to provide resources on election systems and equipment.
     Has links and information on voting equipment and usage across the US.


#### 3.4.6. Election Data Standards & Organizations

   * [Voluntary Voting System Guidelines][eac-vvsg] (VVSG). In January 2016,
     the [U.S. Election Assistance Commission][eac] (EAC) adopted a plan
     where, starting in July 2017, all new voting systems would be required
     to be tested against the Voluntary Voting System Guidelines Version 1.1
     (VVSG 1.1). The EAC approved the VVSG 1.1 in March 2015.

     The EAC was established by the Help America Vote Act of 2002 (HAVA) to
     develop guidance on HAVA requirements. The EAC works with NIST to
     sponsor Technical Guidelines Development Committee (TGDC) working groups
     for newer versions of the VVSG.

     _[Item edited: Dec. 14, 2017 meeting.]_

   * Election Markup Language (EML), Original XML-based election data interchange format.
     [Wikipedia Overview][eml-wikipedia], [Specifications][eml-specs]. \[2011\] (Obsolete)

   * [IEEE VSSC/1622: Common Data Format for Election Equipment][ieee-1622]
     (Institute of Electrical and Electronic Engineers), Voting Systems
     Standards Committee). Based on EML, Superceeded by NIST SP1500.

   * [NIST SP1500-10x Voting Common Data Format][nist-voting] standards.
     Ongoing effort on XML standards for interoperable election information.
     From the [NIST Voting section of the Information Technology Laboratory][nist-itl].
     Coordinating and funded by EAC to produce new *Voluntary Voting Systems Guidelines*.

     Includes a good [VVSG Principles and Guidelines][nist-vvsg-principles] summary.

   * [Voting Information Project][vip-project] Google/Pew effort to develop
     election data interchange standards, originally based on EML.
     Project includes collecting data from election officials nationwide.
     Used for Google's Civic API and third parties using Civic API.
     In 2016, California Secretary of State collected data from all CA counties.
     \[2016 original contributed data is not public/open--
     private to Google/Pew except by special arrangement.\]
     The VIP spec allows contest definitions, but in practice,
     only used for poll lookup. [git][vip-repo]


#### 3.4.7. California Election Laws and Regulations

   * [Advisories to County Election Officials][sos-advisories], announcements
     from the California Secretary of State on new regulations, required
     procedures, and notices on statewide propositions and elected offices.
     Includes certifications of new equipment including remote accessible
     vote by mail.

   * [Elections Officers Digest][sos-digest], an annotated summary of election
     laws prepared for local election officials, with procedures,
     responsibilites and definitions of terms.
     Includes references to code sections.

_[Subsection added: Jan. 18, 2018 meeting.]_


#### 3.4.8. Additional Links

   * [GitHub][github]
   * [Open Source Initiative][osi] (OSI)
   * [OpenCount][open-count]


## 4. Facts & Assumptions

This section lists certain facts and assumptions the committee has made while
drafting this document.


### 4.1. Facts

1. The Director of Elections' [March 2017 Director's
   Report][directors-report-march-2017-original] began outlining characteristics of
   the development plan for the open source voting system. These included—

   * For the system to be "Developed under version 3 of the GNU General
     Public License where possible, otherwise preferring similar licenses
     with copyleft characteristics." This is consistent with the
     recommendation in the Commission’s [Open Source Voting Systems
     Resolution (PDF)][commission-res-pdf-local] in its third "resolved"
     paragraph:
     > (d) Express a preference for open source licenses
     with copyleft characteristics so that San Francisco and other
     jurisdictions can benefit from future improvements that others make to
     the voting system components;

   * To post the software developed for the new system "as it is written."
     This is also consistent with the recommendations in the same "resolved"
     paragraph of the Commission's resolution:
     > (b) Incorporate openness and transparency into the project, for
     example ... by releasing all development products, including software
     source code and documentation, as they are developed;


### 4.2. Assumptions

1. The Department of Elections does not currently have the expertise to
   conduct the day-to-day management of the development and certification of
   an open source voting system.

2. The voting system should not require counting the votes on ballots by
   hand (not including hand-counting for audit or recount purposes).


## 5. Components

This section provides one possible way of dividing a “generic” optical-scan
paper-ballot voting system into components or modules. This can be used as
the starting point for an agile development plan (e.g. incremental
implementation, modular contracting, etc).


### 5.1. Component Listing

This subsection contains the listing of components without detail. Caveats
are discussed after. More detailed descriptions of each component are in the
subsections that follow.

**Hardware**

1. Accessible Ballot-Marking Device
2. Central Ballot Scanner
3. Precinct Ballot Scanner
4. Standard laptop or desktop computers

**Software**

1. Voting System Database / Management
2. Ballot Batch Management
3. EIMS® Integration
4. Ballot Layout Creator
5. Ballot Layout Encoder
6. Accessible Ballot-Marking Device Software
7. Ballot Picture Interpreter
8. Scanner Device Drivers (one for precinct and one for central)
9. Central Ballot Scanner Software
10. Precinct Ballot Scanner Software
11. Vote Totaler
12. Results Reporter
13. Ballot Tabulation Audit Support

The lists above are not rigorous or exhaustive. Rather, they are meant for
discussion purposes and to provide a sense of what functionalities are needed
and how they are divided up, etc.

For simplicity, we assume that the voting system uses pre-printed ballots, as
opposed to being a ballot on-demand system. We also assume that in-precinct
voters are allowed to mark their ballot with a pen, as opposed to being
required to interact with an electronic device. Finally, we assume the voting
system includes a precinct tally, which means the system tallies the
in-precinct ballots at the precinct.

The assumptions above are only for the purposes of the example illustration
in this section. They were made partly because they reflect how San
Francisco's voting system works today. However, they should not be construed
in any way as recommendations of the Committee or to constrain the type of
voting system that San Francisco should develop. See the "Key Decisions"
section below for how this list of components could change depending on
certain choices.

The components in this particular list are not necessarily independent. They
may overlap or contain one another. For example, the precinct ballot scanner
hardware component contains a scanner device driver, the ballot picture
interpreter, and the high-level scanner software components.

Finally, note that there are many possible ways to divide a given voting
system into components. For example, the granularity at which one views the
system affects the number of components. We chose a mid-level granularity for
this list. This lets us show how some software components are used in more
than one hardware component. Differences can also result from where the
“boundaries” are drawn between components (e.g. what functionalities one
assigns to different components).


### 5.2. Component Details

This section lists more details about each of the four components we
suggested above. For each of these deliverables, we provide—

* A rough level of the relative complexity (low / medium / high),

* A brief description (though this already appears for the most part in the
Background section of this document),

* What components the deliverable interacts with,

* Possible interfaces / data formats that might be needed,

* Sub-components,

* Dependencies from a project management perspective (i.e. what might be
needed in advance), and

* Other outcomes / deliverables associated with delivering the component.


#### 5.2.1. Hardware Component Details

Each of the hardware components below also needs software to function. In
most cases, we list this software in the “Software Components” section.


##### 5.2.1.1. Accessible Ballot-Marking Device

A device used in polling places that lets people with disabilities vote
independently. It supports different accessible interfaces like audio,
sip-and-puff, etc. If the computer is COTS, it may also need a custom casing
or shell to increase durability and assist with polling-place transport and
setup.

For a Remote Accessible Vote By Mail system (required by 2020), the
hardware used would likely be the voter's personal electronic
device and printer.

_[Item edited: Jan. 18, 2018 meeting.]_


##### 5.2.1.2. Central Ballot Scanner

A device responsible for high-speed, high-volume ballot scanning (e.g. for
vote-by-mail ballots). The scanning with these machines is done in a
controlled environment under staff supervision.

**Complexity:** High

**Description.** This is a hardware component responsible for high-speed,
high-volume ballot scanning in a controlled environment under staff
supervision (e.g. vote-by-mail ballots). It should be capable of (1)
exporting CVR’s and digital pictures of the ballots it scans, (2)
“out-stacking” ballots that require manual inspection or handling, and (3)
possibly printing unique identifiers on each ballot when scanning to support
the auditing of individual ballots.

**Interfaces / data formats.**

* Same as for the Ballot Picture Interpreter.

* Also needs to store digital pictures of ballots in a defined image format.

**Sub-components.**

* Device drivers (software API’s to control low-level scanner functionality
and, if present, the printer).

* Ballot picture interpreter (see component description above).

* High-level software to orchestrate calls between the device drivers and the
ballot picture interpreter.

* Printer component to print unique identifiers (possibly required).

**Other outcomes / deliverables.** The required input data and formats should be
spelled out.

**Possible dependencies / pre-requisites.** Real data from past elections for
prototyping and testing. Samples of ballots from past elections and/or the
interim voting system.


##### 5.2.1.3. Precinct Ballot Scanner

A device used in polling places to scan and tabulate ballots cast in person.
It has features like returning the ballot to the voter for possible
correction if the ballot contains an overvote. Similar to the accessible
device, this device may also need a custom casing or shell for durability and
to facilitate polling-place use.


##### 5.2.1.4. Standard laptop or desktop computers

Standard computers will also be needed for administrative tasks like ballot
layout, adjudicating digital pictures of ballots, aggregating and totaling
votes, and generating results reports.


#### 5.2.2. Software Component Details


##### 5.2.2.1. Voting System Database / Management

Central store (e.g. file system and/or database) and software application
providing access to the voting-system information needed to conduct an
election. This can include things like contest and ballot definitions,
digital ballot pictures, cast vote records, and election results.

A management interface can let staff perform
tasks like importing and exporting data in open data formats, adjudicating
ballots that require manual inspection (e.g. ballots with write-in candidates
or borderline marks)—but from the digital ballot picture rather than from
the physical paper—and performing other
functions needed during the canvass. This software could perhaps also
provide an interface to running other software components and functions
like the EIMS integration, tabulation, and results reporting.


##### 5.2.2.2. Ballot Batch Management

**Complexity:** Low

**Description.** This is a software component that allows boxes of ballots
to be organized into batches for scanning and auditing. Labels may be
printed to be attached to ballot boxes collected, transported, and stored.
Batches of ballots might include a scannable header page, marking the
beginning of a batch of ballots, and a scannable footer page, marking the
end of the batch. The header/footer pages mark the consolidated precinct
and other information identifying the ballot batch, and might also include
signatures from poll workers, and digital audit information, e.g.
IDs, temporary digital signatures and keys, starting and ending hash chain
codes from a precinct scanner. An additional header/footer page might be
created to wrap and identify outstacked ballots.

The batch management system would be used to:

* create box labels and header/footer pages,

* provide a database of batch IDs with associated precinct and grouping
  IDs,

* provide a means to scan box labels and log departure/arrival of ballot boxes
  transported or stored/retrieved,

* provide the input to the ballot picture interpreter identifying the
  batch being processed, and associated information (e.g. precinct ID),

* organize scan batches to associate CVR (Cast Vote Record) data
  with ballot box storage ID and location, and

* track progress of scanning, adjudication, and auditing of ballot batches.

**Interfaces / data formats.** Needs to accept as input:

* a definition of precincts, precinct consolidation, and ballot type
  by precinct, used to organize batch collections.

* bar code scans of box labels used for tracking

* scans of batch header/footer pages

Needs to output:

* data files with batch IDs and associated precinct/group information

* printable labels and header/footer pages

* data with batch scan/audit status and transport logs

**Other outcomes / deliverables.** The required input and output data and
formats should be spelled out.

**Possible dependencies / pre-requisites.** Batch management procedures
need to be defined so batch IDs can be included with the Ballot Picture
Interpreter output CVRs and used with the Vote Totaler.

_[Subsection added: Jan. 18, 2018 meeting.]_


##### 5.2.2.3. EIMS® Integration

This component is responsible for interfacing with the Department's EIMS®
software. It pulls or takes election definition information exported from
EIMS and imports it into the voting system database. This information can
include things like what offices and candidates are on the ballot, and
in what precincts, districts, and ballot styles, etc.


##### 5.2.2.4. Ballot Layout Creator

This is a software application that lets staff generate paper-ballot layouts
from the election definition for each ballot type in automated or
semi-automated fashion, including support for multiple languages.


##### 5.2.2.5. Ballot Layout Encoder

**Complexity:** Medium

**Description.** This is a software component to let one "reverse engineer"
structured ballot layout data from existing paper ballots from another vendor.
This component may be needed during a possible interim phase in which
open source components are used for scanning and interpreting ballots that are
generated by a different vendor (i.e. the City's vendor during the time
when the open source system is being developed).  This component will be
needed if that vendor is not able to provide structured ballot layout data
along with the paper ballots.  It is likely that this component will
not be completely automated, but rather will be semi-automated.

**Interfaces / data formats.** Needs to accept as input:

* the “election definition” data (e.g. contests, candidates, districts, etc.).

* the digital ballot pictures (scanned images or PDF)

Needs to output for each ballot type:

* the “ballot layout” data (e.g. where contests are located on each ballot
card for each ballot type, etc.) that will be used as input to the Ballot
Picture Interpreter component.

**Other outcomes / deliverables.** The required input and output data and
formats should be spelled out.

**Possible dependencies / pre-requisites.** Real data from past elections for
prototyping and testing. Samples of ballots from past elections and/or the
interim voting system.

_[Section added: Dec. 14, 2017 meeting.]_


##### 5.2.2.6. Accessible Ballot-Marking Device Software

This is the software corresponding to the Accessible Ballot-Marking Device
hardware component.

A Remote Accessible Vote By Mail system would likely rely on a reasonably
updated web browser rather than requiring installation of OS-specific
software installation. Text to speech capabilities could be either the
voter's own accessibility software or a web browser component provided
with the ballot.

_[Item edited: Jan. 18, 2018 meeting.]_


##### 5.2.2.7. Ballot Picture Interpreter

This is a software library responsible for interpreting digital ballot pictures. It
generates a cast vote record (CVR) from a digital picture of a ballot. This
software component could potentially be used in all of the precinct scanners,
the central scanners, and a software-only ballot adjudication application.

**Complexity:** Medium

**Description.** This is a software-only component responsible for
interpreting digital ballot pictures, namely by generating a cast vote record
(CVR) given a digital picture of a ballot. The component must support ballots
from “third-parties” (e.g. the interim voting system) to support incremental
roll-outs like pilot and hybrid rollouts, and possibly to support
home-printed "remote accessible vote by mail" ballots. The open source
software OpenCount developed at UC Berkeley could be a foundation for this.

The picture interpreter should be able to identify and remove the base
printing and watermarks so any remaining extraneous marks can be identified.
The presence of a significant amount of extraneous marks might require
that ballot be identified for adjudication. Likewise, marks clearly not
present or not fully marked must be identified for adjudication.

_[Paragraph added: Jan. 18, 2018 meeting.]_

**Applicability.** This component can possibly be used in the following
components:

* precinct ballot scanners

* central ballot scanner

* software application for adjudicating or auditing ballots using their
digital pictures, independent of a hardware scanner.

**Interfaces / data formats.** Needs to accept as input:

* the “election definition” data (e.g. contests, candidates, districts, etc.).

* the “ballot layout” data (e.g. where contests are located on each ballot
card for each ballot type, etc.).

* the digital ballot pictures themselves.

* batch header/footer pages and/or box label codes

  _[Item added: Jan. 18, 2018 meeting.]_

Needs to output for each ballot:

* a cast vote record (CVR) of the markings on the ballot.

* a report of extraneous or ambiguous marks requiring adjudication,
  with a data file referencing the CVR, ballot picture, and contest
  selections.

  _[Item added: Jan. 18, 2018 meeting.]_

**Sub-components.** This component can possibly have the following sub-component:

* a “contest-unaware” interpreter that accepts a digital picture of a ballot
and ballot layout data and outputs what markings are on the ballot (e.g. what
bubbles are filled in, independent of their contest or candidate meaning).

**Other outcomes / deliverables.** The required input data and formats should be
spelled out.

**Possible dependencies / pre-requisites.** Real data from past elections for
prototyping and testing.


##### 5.2.2.8. Scanner Device Drivers (one for precinct and one for central)

This is low-level software needed on both precinct and central ballot
scanners that provides a software API to the basic hardware functionality of
a ballot scanner (e.g. out-stacking a ballot, returning a ballot, advancing a
ballot, etc.). This might come with COTS hardware. Separate versions are
likely needed for the precinct and central scanners.


##### 5.2.2.9. Central Ballot Scanner Software

This is high-level software controlling the central ballot
scanner. It interacts with the scanner device driver and ballot picture
interpreter components and is responsible for things like scanning and
storing digital ballot pictures, detecting the ballot layout, interpreting and
tabulating ballot markings, controlling the scanner in response to the
markings on a ballot, and exporting ballot data after scanning is complete.


##### 5.2.2.10. Precinct Ballot Scanner Software

This component is similar to the central ballot scanner software component
above and can likely share much software with it. However, it's different
because it is for the case of an individual voter rather than for high-volume
scanning. For example, unlike the central ballot scanner, this software will
need to support returning a ballot back to the voter in the case of errors
like an overvote. For the central scanner, such ballots might simply be
outstacked.


##### 5.2.2.11. Vote Totaler

Aggregates and counts all vote totals and generates the results in an open
data format. Includes the RCV tabulation algorithm.

**Complexity:** Low

**Description.** This is a software-only component responsible for
aggregating vote data and generating election results in a machine-readable
format. This includes running the RCV algorithm to generate round-by-round
results. Normally votes have subtotals reported by consolidated precinct, and
may separate election-day precinct voting and vote-by-mail ballot subtotals.

_[Paragraph edited: Jan. 18, 2018 meeting.]_

**Interfaces / data formats.** Needs to accept as input:

* the “election definition” data (e.g. contests, candidates, districts, etc.).

* cast vote records (aka CVR’s) for all ballots.

**Sub-components.**

* the code responsible for running the RCV algorithm could be its own
component.

**Other outcomes / deliverables.** The required input data and formats should be
spelled out.

**Possible dependencies / pre-requisites.** Real data from past elections for
prototyping and testing.


##### 5.2.2.12. Results Reporter

Generates human-readable results reports from the results data from the vote
totaler (e.g. printable results and results posted on the Department website).

**Complexity:** Low

**Description.** This is a software-only component responsible for generating
human-readable reports in various formats from structured results data.

**Interfaces / data formats.** Needs to accept as input:

* the “election definition” data (e.g. contests, candidates, districts, etc.).

* the vote total data for the contests as a whole as well as at the desired
aggregation levels (e.g. neighborhood, precinct, district, election day vs.
vote-by-mail, etc.), including the round-by-round vote totals for RCV
elections.

**Sub-components.** The reporter should be able to generate:

* the Statement of Vote (e.g. in PDF format),

* tables for the Election Certification letter (e.g. in PDF format),

* computer-readable equivalent to the Statement of Vote (e.g. in spreadsheet (xls),
delimited text (tsv), and NIST-SP1500-100 (xml) formats),

  _[Paragraph added: Jan. 18, 2018 meeting.]_

* HTML pages for the Department website, and

* Possibly also reports to facilitate the public observation and carrying out
of post-Election Day audit processes (e.g. vote totals divided by batch or
precinct).

**Other outcomes / deliverables.** The required input data and formats should be
spelled out.

**Possible dependencies / pre-requisites.** Real data from past elections for
prototyping and testing.


##### 5.2.2.13. Ballot Tabulation Audit Support

**Complexity:** Medium

**Description.** This is a software component that manages an audit
process that includes a manual count. A precinct-based audit might
be performed, where all ballots in randomly selected precincts are
hand-counted, or a RLA (Risk Limiting Audit) might be performed,
where a randomly selected set of ballots among all precincts are
selected for a hand-count. The number of ballot selected in an
RLA is based on a statistical formula depending on the closeness of
votes between top contenders.

More general election auditing (like chain of custody) is outside
the scope of this component.

Audit support software could include the following:

* Save manually generated random input (e.g. dice roll) for precinct selections
  or RLA random number seed.

* For an RLA, a public high-quality random number generator is used to randomly
  select ballots to be pulled.

* For ballots selected by order within a batch (does not have a printed
  and sorted ID), a scanner might be used to sheet feed ballots, stopping
  where a ballot needs to be pulled.

* If the order in a stored ballot batch does not match the order on stored
  CVRs (cast vote records) and no ballot IDs are available, a new central scan
  and picture image analysis might be required.

* Retrieve the CVRs for selected ballots and pass them to the vote totaler.

* Enter hand-count results and compare totals with the official precinct
  totals or the totaled CVR selection.

**Interfaces / data formats.** Needs to accept as input:

* the “election definition” data (e.g. contests, candidates, districts, etc.).

* a definition of batches with precincts, precinct consolidation, and ballot type.

* results of the vote totaler.

* random number seed

* Cast Vote Records (for an RLA)

* Hand-count results

Needs to output:

* for an RLA, the randomly selected ballots with either ID or sequence in
  a batch.

* comparison of hand counts and machine counts

* scanner controls if used to pull RLA selected ballots

**Other outcomes / deliverables.** The required input and output data and
formats should be spelled out.

**Possible dependencies / pre-requisites.** If an RLA audit is performed
and stored ballots might not match ordered CVRs, then the central ballot
scan and picture interpreter would be required to perform an electronic
recount of all ballots and generate matching CVRs. If the picture interpreter
can run at the speed of the scanner, regenerating CVRs (for an electronic
recount) adds no extra cost.

_[Subsection added: Jan. 18, 2018 meeting.]_


## 6. Recommendations


### 6.1. Interim Voting System

* The contract for the interim system (i.e. the system to be used after 2018)
  should permit all possible combinations of phasing in an open source system
  alongside it. Examples of possible combinations include:

  * using open source components to scan vote-by-mail ballots and the interim
    system to scan precinct ballots, or vice versa;

  * using an open source accessible voting device in conjunction with the
    interim system’s precinct-based scanner, or vice versa;

  * scanning the ballots of the interim system using an open source scanner;

  * tabulating ballots scanned by an open source scanner using the interim
    system’s tabulation software;

  * using an open source reporting and/or tabulation system with the output
    from the interim system’s scanners;

  * using open source components alongside the interim system in some subset
    of precincts (e.g. for a pilot rollout); or

  * using open source components alongside the interim system in all
    precincts (e.g. for an incremental roll-out of the open source system).

* The requirements for the interim system should include interoperability
  with other systems, and the interoperability formats should be documented
  so they don’t need to be reverse-engineered.


### 6.2. Requirements-gathering

This section contains recommendations related to gathering requirements. For
committee recommendations of specific requirements, see the Requirements
section below.

[TODO]


### 6.3. Requirements

This section lists some of the requirements the system should satisfy.


#### 6.3.1. Accessibility

* In addition to an audio component and touchscreen, the voting system should
  support accessible features including, but not limited to: sip and puff
  input, a keyboard for write-in votes, voice activation, synchronized audio
  and video, joystick input, Tecla switch, and tactile buttons. These
  [two letters][disability-rights-ca-letters] from Mr. Fred Nisen
  (Supervising Attorney for Voting Rights, Disability Rights California)
  provide more detail.


#### 6.3.2. Other

* [TODO: should we recommend (1) supporting manually marked ballots in the
  polling place, or (2) requiring the use of a computer ballot-marking and/or
  ballot-printing device?]

* [TODO: should we recommend (1) pre-printed ballots at polling places, or
  (2) printing ballots on-demand?]

* [TODO: should we recommend for or against end-to-end verifiability?]


### 6.4. Project Management

* The Department should align itself with other efforts within the City to
  use agile procurement and methods, and it should seek assistance where
  possible. Notable parts of San Francisco government beginning to use agile
  methods include the San Francisco [Mayor’s Office of Civic
  Innovation][sf-moci] (MOCI) and the San Francisco [Digital Services
  Team][sf-dst]. See also San Francisco's [_Digital Services
  Strategy_][sf-digital-services-strategy] (PDF).

  _[Item added: Dec. 14, 2017 meeting.]_

* Developing user stories is an essential part of an agile development
  process. We recommend that the development team create user stories for
  each of the situations representing voter, Department staff, and other
  activities. These user stories include, among others:

  1. a registered voter voting at an assigned precinct on election day;

  2. a registered voter voting at a vote center or early voting station;

  3. a registered voter voting remotely and mailing in a marked ballot, and;

  4. a registered voter with a disability in need of special accommodation
     (several types).

  In following an agile development process, the implementation team would
  typically break down each user story into smaller stories as needed, and
  handle one of those within a sprint.

  _[Item added: Jan. 18, 2018 meeting.]_

* The Department should hire a staff person to be in charge of managing the
  project. The person should have experience and expertise in managing
  technical projects of a similar size and complexity.

* As soon as possible, the Department should
  develop and publicize a rough project plan and timeline for the development
  and certification of an open source system, for the case that the project
  is funded. It is okay for this plan to be tentative. It can be refined over
  time as more information becomes available. Articulating even a tentative
  plan would also help in crafting an RFP for the interim system.

* For deliverables, favor smaller deliverables that can be tested
  independently of other components. In particular, if developing a software
  application, it may make sense for one or more of the underlying libraries
  to be delivered separately and/or earlier, rather than the application as a
  whole being the only software deliverable.

  One example is an application to tabulate the results of an RCV contest.
  The code responsible for running the algorithm could be delivered and
  tested as a stand-alone library separate from any user-interface.

  Another example is an application to adjudicate ballots. The code for
  automatically interpreting the digital ballot picture could be separated
  out as its own library. Indeed, this corresponds to the Ballot Picture
  Interpreter software component.

  [TODO: add a comment about the vendor providing a UI shim to support
  the testing of software libraries.]

* [TODO: think about the division of responsibilities between the City and
  vendor. For example, who should be responsible for project management—the
  City or a vendor?]

* [TODO: provide specific recommendations around agile.]


### 6.5. Open Source

This section covers topics related to open source.

* Each software component being developed should be licensed under an
  [OSI-approved][osi-approved-licenses] software license, with a copyleft
  license being preferred (see also the Facts & Assumptions section).

* All software development should occur in public (e.g. on GitHub), rather
  than, for example, waiting for the software to reach a certain level of
  completion before becoming public.
  (See also item (b) of the third "resolved" paragraph of the Commission's
  [Open Source Voting Systems Resolution (PDF)][commission-res-pdf-local].)

* All software being developed in public should have an open source license
  when development first starts, rather than, for example, adding a license
  file later on. This would eliminate any confusion and uncertainty from
  members of the public as to whether the software will really be open
  source. This would encourage members of the public to start contributing to
  the project as early as possible.

* All software being developed should be developed using an open source
  programming language and toolchain. This means an open source compiler or
  runtime should be available for the language(s) used, and it should be
  possible to build and run the software from source using only open source
  tools. For programming languages and build tools, any OSI-approved license
  should be okay; they need not be copyleft.

* Reuse of existing open source libraries, tools and software is encouraged.
  Any such pre-existing third-party code used should be available under
  an OSI-approved license, but need not be copyleft. If modifications to
  third-party code are developed, and the original third-party code has
  a different license than the main software's license, the modifications
  should be dual-licensed under both licenses, if possible.
  (See also item (e) of the third "resolved" paragraph of the Commission's
  [Open Source Voting Systems Resolution (PDF)][commission-res-pdf-local].)

* The aggregate system (including the infrastructure, stack, and services)
  should be open source. This includes but is not limited to things like
  the operating system, database, web server, etc, if present.

* In addition to the software being open source, project documentation
  should be openly licensed. This includes things like design documents,
  installation and setup documents, user manuals, and testing documents.
  The recommended license for documentation is the Creative Commons
  Attribution-ShareAlike 4.0 license ([CC-BY-SA 4.0][cc-by-sa]).
  (See also the reference to ”freely and openly licensed” documentation
  in the Commission's
  [Open Source Voting Systems Resolution (PDF)][commission-res-pdf-local].)

* [TODO: provide recommendations related to managing community feedback and
  contributions during project development. Also think about whether
  [contributor license agreements][cla] (CLA’s) should be required.]


### 6.6. Procurement

[TODO]


### 6.7. Software architecture and design

* When defining software components to develop, favor designs that promote
  reusing components. For example, a software library that can read a digital ballot
  picture and return the marked “votes” (what we are calling a “ballot picture
  interpreter” component) can be used in both precinct scanners and central
  scanners (as well as software applications for adjudication or auditing).
  Favoring component reuse can mean having less code to write and test, which
  in turn can reduce required time and costs.


### 6.8. Software development

* The project should not depend on volunteers for the successful completion
  or security of the project. However, useful volunteer contributions should
  be encouraged and not turned away.


### 6.9. Hardware design

[TODO]


### 6.10. Documentation

[TODO]


### 6.11. Security

[TODO]


### 6.12. Testing

1. **Gather real election data.** Datasets of real election data (e.g. a
couple past elections in San Francisco of different types) should be compiled
in a structured format for product prototyping and testing. This includes not
just vote totals but also candidate and contest data. This will help in
establishing requirements and designing the system.

2. **Gather real digital ballot pictures.** Starting with the June 2018
election, during each election the Department should gather and save large
numbers (e.g. thousands) of digital ballot pictures for future testing
purposes. The Director has already expressed a willingness to do this in the
case that the voting system supports it. The Department should do this during
the canvass after each election because it may not be possible to obtain
ballot pictures after the ballots are physically sealed and eventually
destroyed. Having a variety of real-world digital ballot pictures will aid in
developing and testing the ballot picture interpreter component, even if the
ballot design is different from what will eventually be used. Also, using
real ballots can provide test cases that might not be thought of if trying to
construct test cases manually.

   _[Item added: Dec. 14, 2017 meeting.]_

3. **Stand-alone test data.** In the course of developing the open source
voting system, where possible, structure and store test data separate from
the software application (e.g. in separate repositories) and in an
application-agnostic form (e.g. using open data formats). These can be
separate deliverables. The test data
should include both test inputs and, when appropriate, test outputs (aka test
expectations). Doing this allows the test data to be used by other
applications and in particular could help facilitate additional open source
implementations of components. Making the test data independent and more
easily available can also improve the quality and correctness of the test
data, for example by making it easier for others to check or add more test
cases.

   This recommendation makes more sense for higher level end-to-end tests rather
than lower-level tests like unit tests since unit tests are often tied to a
particular implementation. Examples of test cases for higher-level tests
include things like (1) for the ballot picture interpreter component, a
digital ballot picture as the input and the corresponding cast vote record as
the output, and (2) for the RCV tabulator, the cast vote records for an RCV
contest as the input and the round-by-round vote totals as the output.

   _[Item added: Dec. 14, 2017 meeting.]_


### 6.13. Certification

[TODO]


### 6.14. Hardware manufacturing or assembly

[TODO]


### 6.15. Deployment

[TODO]


### 6.16. Software maintenance

[TODO]


### 6.17. Hardware maintenance

* The City should prefer professional, commercial support for
  maintaining the aggregate system (including the operating system, stack,
  and software services, etc.) over “in-house“ maintenance -- even though
  the components are open source. This will make it easier, for example,
  to ensure that security patches are applied on a timely basis. An example
  of such a provider is [Red Hat](https://www.redhat.com).


## 7. Recommended Implementation Order

To reduce project risk, complexity, and initial costs, it is important to
have a strategy to break the open source voting system project up into
smaller, independent deliverables that can be developed and used in real
elections before the full system is completed.

This is part of an agile approach and has several advantages. It would let
the City start getting real value from the project earlier. It would let the
City get confirmation earlier that the project is “on the right track”
without necessarily having to commit funds for the entire project. It also
builds in a way for the City to take corrective action (e.g. if a vendor
developing a particular component isn’t performing to expectation). Finally,
it eliminates the need to come up with accurate cost and time estimates for
the entire project before starting work.

For example, instead of committing $8 million up front for a single project
to develop a full voting system, the City could instead start out by spending
$2 million on three deliverables, say: one for $1.5 million and two for $250,000.
Based on the success or progress of the initial projects, the City could
decide to move forward with additional sub-projects, or change its approach
(even before the three deliverables are completed). In this way, the City
limits its financial exposure to risk.

This section recommends some approaches to achieve this. The purpose of this
section is not to serve as an actual plan, but rather to provide concrete
suggestions for how the Department can proceed incrementally in developing
and deploying an open source voting system.


### 7.1. Recommended First Components

The Committee recommends the following as components to start work on and
deliver first (see the “Components” section for brief descriptions of
most of these components):

1. Results Reporter (Software)
2. Vote Totaler (Software)
3. Ballot Picture Interpreter (Software)
4. Central Ballot Scanner (Hardware & Software)
5. Ballot Layout Encoder (Software)
6. Ballot Batch Management (Software)
7. Ballot Tabulation Audit Support (Software)

Choosing the above as first components seems to mirror the approach that Los
Angeles County is taking in its VSAP project. In particular, Los Angeles
County developed and submitted its "Tally System" for certification even
before its in-precinct Ballot Marking Device was engineered and manufactured.
Los Angeles County's "RFP Phase 1: #17-008" defines its Tally System on page
48 as--

> A system of hardware and software that reads and captures the vote
selections on ballots, applies required business rules and adjudications,
tabulates the totals of votes, ballots cast, and other metrics, and publishes
the results the election. The tally system also supports transparent auditing
processes to ensure the accuracy and integrity of the election tally results.

This seems to encompass the functionality of the four components listed above.

Los Angeles County submitted its VSAP Tally Version 1.0 to the California
Secretary of State for certification on September 19, 2017. Section 3.3
(pages 25-28) of its Phase 1 RFP provides more detail on the completion of
Los Angeles County's Tally System in relation to other components like their
Ballot Marking Device.


### 7.2. Rationale

Below are some reasons for selecting the components above:

* Each component has relatively few dependencies.

* The components are on the easier side to implement.

* The components are independently useful and so can help prove the value of
open source.

* The components can be worked on in parallel. Their development can also be
staggered in conjunction with other deliverables. For example, development on
other components can be started before these are finished.

* In each case, there is open source code that already exists that
development of the components might be able to start from, or at least learn
from.

* Working on the components will help to work through and resolve core issues
that need to be worked out anyways

* Each of these components supports incremental deployment. Each component
  can be deployed and used by replacing the corresponding component of a
  non-open source interim system, and then interoperating with the other
  components of the voting system (interim or not). This is true even without
  requiring anything extra of the interim system. See the "Deployment
  Strategies" sub-section below for further details.

  In contrast, an example of a component that probably _wouldn't_ support
  incremental deployment as easily is the ballot layout software application.
  This is because an interim system's scanners probably can't be guaranteed
  to scan ballots created by a third-party.

  Similarly, it is probably more difficult to design an accessible
  ballot-marking device that can mark another vendor's ballot than it is to
  design a scanner that can interpret another vendor's ballot. This is
  because marking a ballot is a harder problem to solve than interpreting a
  ballot. While the latter is primarily a software problem (which would be
  addressed by the ballot image interpreter component), the former leans more
  towards being a hardware problem.


### 7.3. Results Reporter Rationale

* The results reporter is probably the “easiest” component to implement and
has the least amount of risk, since it is responsible merely for formatting
and presenting information. In this way, it would be a good warm-up project.

* Since many members of the public view the Department’s election results
pages online, it would nevertheless be a highly visible use of open source
software.

* It could also be a good public outreach / educational tool around open
source and the open source voting project. The Department could solicit
feedback from the public on how the results pages could look or be improved,
and the Department could implement the best suggestions (since the reporter
would be open source).

* Making the reporter open source would also be inherently useful because it
would give the Department the ability to customize and improve the current
format, and accept contributions from the public.


### 7.4. Vote Totaler Rationale

* This component is also one of the easiest components and so would be good
to start with.

* This is also a component that other jurisdictions would be able to use and
benefit from relatively easily (e.g. jurisdictions using RCV would be able to
use the RCV algorithm functionality). In this way, other jurisdictions could
start to understand the benefits of open source.

For the Ballot Picture Interpreter:

* This is a core software component that would be used in a number of
different components, so it is natural to start working on it first.

* Even in the absence of deployed open source hardware components, it could
be used by members of the public to “check” the scanning done by the interim
system, provided the digital ballot pictures are made public. The visually impaired
could use a ballot picture interpreter on their device with a speech synthesis
application to validate/check a home printed or marked ballot.

  _[Paragraph edited: Jan. 18, 2018 meeting.]_

* The open source software OpenCount might go a long way towards implementing
this component.


### 7.5. Central Ballot Scanner Rationale

* This is probably the “easiest” hardware component to work on and implement
first, for reasons that will be described below.

* Deploying this component alone would result in a majority of votes being
counted by open source software. For example, in the November 8, 2016
election 63% of ballots were vote-by-mail (263,091 out of 414,528 ballots in
all). In this sense, this component provides the biggest “bang for the buck.”

* This component doesn’t require answering the question of whether to use
vote centers, since vote-by-mail ballots need to be tabulated centrally
whether or not San Francisco moves to a vote-center model.

* Unlike precinct-based hardware components like the accessible voting device
and precinct-based scanners, this hardware component would be operated in a
more controlled environment with more highly trained staff. As a result, it
also doesn't need to meet the same portability, durability, usability, and
transportation requirements as precinct-based equipment (which also might
require a custom casing or shell in the case of precinct equipment).

* Also unlike precinct-based hardware components, fewer units would need to
be purchased or manufactured, so it is probably less costly and expensive to
do this step first. For example, for comparison, San Francisco currently has
four high-speed central scanners, but around 600 precincts.

* Central scanners provide multiple possibilities for incremental rollout,
including using the component alongside and in parallel with the interim
system, which all help to mitigate risk. These approaches are described in
the “Deployment Strategy” section.

* Implementing the central scanner before the precinct scanner also makes
sense from a software dependency perspective. The central scanner includes
most of the software that an in-precinct scanner would need anyway, like
ballot interpretation, understanding election definition and ballot layouts,
etc. However, the central scanner provides a safer and more controlled
environment in which to exercise these code paths for the first time. In
other words, with the exception of the high-speed and high-volume nature of
the hardware, it is a strictly simpler component than the precinct-based
scanner.


### 7.6. Deployment Strategies

The components listed above can be deployed and used in conjunction with a
non-open source interim system even before a full open source voting system
is ready. This section provides more details about how this could be done.

For example, an open source results reporter could be used to report the
election results of the non-open source interim system. It would simply need
to take in the aggregate, numeric results from the interim system. The output
would not need to interact with the interim system.

Similarly, an open source vote totaler could be used to compute the numeric
results of an election run with the interim system. It would only require
taking in the non-aggregated numeric results from the interim system, and
then feeding the aggregate results into the results reporter.


### 7.7. Central Ballot Scanner Phases

For the central ballot scanner, there are a number of options for
incrementally phasing in an open source version.

In chronological order, some of these possible phases are--

1. Even before the scanner hardware is ready to be tested, the software-only
ballot image interpreter component could be used to check the vote counts of
the interim system from the information of the digital ballot pictures. In
addition, if the pictures are made public during the canvass (along with the
ballot image interpreter software), even members of the public could perform
this "check."

2. When the open source central scanners are ready enough to test, the
scanners could be used to scan vote-by-mail ballots _in addition_ to the
interim system scanning them. This could be used both to check or audit the
interim system, as well as to test the open source scanners. This can likely
be done even without certifying the scanners. This is essentially what the
Humboldt County Elections Transparency Project did in the late 2000's.

3. Once we have enough confidence in the open source scanners, they could be
used as the primary scanner for _some_ of the vote-by-mail ballots (e.g. in a
pilot of the open source scanners that precedes a full-scale rollout). This
option could possibly be done prior to certifying the scanners, by taking
advantage of California bill [SB 360 (2013-2014)][bill-sb-360-2013].

4. Finally, once the open source central scanners are certified, they could
be used to scan _all_ of the vote-by-mail ballots (while the interim system
could be responsible for counting in-precinct ballots). In this scenario, the
interim system could perhaps even be used as a fail-safe backup in case of an
unexpected issue with the open source system (or else as a check, in the
same way that the open source scanners were used as a check in bullet point
(2) above).


## 8. Equipment (“Product”) Decisions

The following are some key decisions about system requirements that need to be made
at some point when designing and developing the voting system. Some pro and
con tradeoffs are included.

At this point, the intent here is to just present options with some
discussion, not a particular recommendation.

**Assumptions:**

* Votes are cast (recorded, submitted, and stored) on paper in a human-readable form.

* An electronic representation of ballots made either by voting machines or
  scanners serves only as a copy of the official paper ballot.

* Ballots marked are on paper that meets the California regulations for
  printing (counterfeit resistance).

* By 2020, CA [AB973][bill-ab-973-2017] requires support of _Remote Accessible
Vote By Mail_ ballots ([AB2252][bill-ab-2252-2015]) for voters with disabilities
or overseas and military voters. Home computers are used to print ballots on
ordinary paper, but returned via special mail envelopes.

* Voting types to be considered:
  + Vote by mail (preprinted and special accessible/overseas)
  + Vote on election day at a polling location (precinct voting)
  + Vote prior to election day at an early vote center
  + Vote by people preferring or needing an accessible option (e.g. ballot
    marking device), like people with disabilities
  + Vote with Provisional Ballots (enclosed in a special envelope for later
    qualification)

_[Assumptions added: Feb. 8, 2018 meeting.]_


### 8.1. Will vote centers be used for early and/or election day voting?

California [SB 450][bill-sb-450-2015] ("Elections: vote by mail voting and
mail ballot elections") authorizes counties to conduct elections using vote
centers. The Department of Elections should develop a sense as soon as
possible of the likelihood of using vote centers because that could affect
the requirements and design of the system. Making this decision earlier could
decrease costs since the design and development wouldn’t have to cover
multiple scenarios.

While voters can be assigned to the traditional election-day precinct polling
site, with the right equipment, each poll site could have the full features of
a vote center, i.e. allow voters from any precinct to vote at that site.

Vote centers could be used for:
   1. Early voting only
   2. Election day voting at selected locations
   3. All election day polling locations

_[Answer edited: Feb. 8, 2018 meeting.]_


### 8.2. Should precinct polling and vote centers use the same paper ballots as those used in vote-by-mail?

  Background: If a voting machine is used to prepare ballots for printing, the
paper ballots marked could use the same printing and layout as a vote-by mail
ballot, or could have a simpler and shorter format listing just the contests and
selected choices (called _paper cast vote record_ (CVR) in California Election Code).
The shorter format could be on smaller paper, possibly only a single sheet, vs a
larger multipage scanned mail ballot. Voting machines (ballot marking devices)
at a precinct or vote center could be used only for the purposes of providing
an accessible option, while voters not requiring an accessible option could
use a normal mail ballot, or all voters at a precinct or vote center could
use voting machines with printed ballots.

Mail-Only Format Pros:

* Only one style of ballot printing is required
* No need for precinct voters to use voting machines-- voters not
    requiring an accessible option can use a "low-tech" solution of only
    a marker or pen
* Central storage and recounting has all the same ballot size/type
* Better ballot secrecy because all ballots look the same.
* Reduced requirements for printers and possible problems with printer
  malfunction and paper jams.
* Voting with hand-marked ballots could be done with no electric power.

Mail-Only Format Cons:
* Printing on large mail ballot paper, usually double sided,  requires
    special, possibly nonstandard, equipment. Sheets might need to be
    hand-inserted individually.

_[Question added: Feb. 8, 2018 meeting.]_


### 8.3. Should ballots to be hand-marked be preprinted or printed on demand?

  Background: If precinct voting is based on the low-tech paper ballot marked
with a pen, pads of preprinted paper ballots could be used. However, separate
pads are required for each ballot type, party preference and language preference
used at that precinct. A vote center might need to store ballots for all ballot
types in the county, each in all languages. An alternative is to use blank
ballot card stock with a printer to create any desired ballot type and language
preference, known as "ballot on demand" (BOD).

Ballot on Demand Pros:
* Reduced printing cost and paper use: no need to stock extra preprinted
    ballots in case all voters show up.
* Easier to accommodate multiple languages
* Allows any poll site to be a vote-center. Eliminates the problem of people
    at the wrong poll site casting provisional ballots with an incorrect
    ballot type.

Ballot on Demand Cons:
* On site printers can fail and probably require AC power, stopping voting.
* Printing on large mail ballot paper, usually double sided requires special,
  possibly nonstandard, equipment.

_[Question & answer edited: Feb. 8, 2018 meeting.]_


### 8.4. Should voting at a precinct or vote center be primarily based on paper ballots hand-marked with a pen, or voting machine with a printer?

Background: After voters check in at a precinct, they could be given a
paper ballot (similar or the same as a mail ballot) and pen to mark it.
Alternatively, they could be given a blank ballot sheet and sent to
a voting machine (e.g. computer/tablet) where choices can be entered and
reviewed. To access the correct ballot type, voters may be given a
_token_ containing the ballot type or else the blank ballot sheet could have
a ballot type code preprinted. When voters complete their selections, the
paper is inserted into a printer, then they check the final printed ballot
prior to casting into a ballot box.

Machines used by all non-mail voters Pros:
* Paper+Electronic CVR has the highest security/integrity. Digital signatures
  can be printed on ballots to authenticate paper.
* Time to vote can be less than marking.
* Mistakes can be undone without needing another ballot to mark.
* Eliminates errors like overvotes and ambiguous marks requiring adjudication.
* Ranked Choice contests can have rankings for all candidates, vs a limit
on paper ballots, eliminating exhausted ballots (except from undervotes), while paper ballots typically have limits.
* Eliminates ambiguous marks that would otherwise require adjudication.
* Machines could read a QR code from a vote at home app to print a ballot
  immediately.
* A separate non-mail ballot format from voting machines would be the same
  for ordinary voters and those with special needs.
* It will be easier to ensure that all voters have the same level and
  quality of experience if all voters use the same process.
* Extra machines provide redundancy vs a single accessible machine.
* Vote centers could handle all ballot types without the need for a ballot
  on demand system.
* Election-day machines could only allow authorized write-ins to be recorded,
  simplifying write-in voting and enabling end of day totals that include
  write-ins.
* A full precinct scanner is not required-- just a simple bar code scanner
    to track paper cast by entering into a ballot box. (The bar code is matched
    against the electronic CVR.)
* Voting machines have the same effect as precinct scanners with
stored electronic CVRs and end of day totals available.

Machines used by all non-mail voters Cons:
* Requires more equipment and more software, with increased cost, complexity,
    attack surface, and the possibility of something going wrong. May require
    backup power.
* More possible problems with paper jams and printer malfunction.
* It is difficult for voters to accurately verify their machine-printed ballot,
    especially when there are many contests on the ballot. For example, in the
    November 2016 election, there were 52 contests.
    A [2018 paper][ballot-verification-2018-paper] suggests voters struggle
    with much smaller ballots than that.
* Voters need to be occupying a machine while voting, unless a vote-at-home app
    is used.
* Mail ballot processing is still a separate sizable operation.

_[Question & answer edited: March 14, 2019 meeting.]_


### 8.5. If voters use machines to mark ballots, should the machine store CVRs of the marked selections?

Background: When a machine is used by voters to select choices that are
then printed on a voter verified ballot, the machine could save the
printed choices as a Cast Vote Record. CVRs could then be used as an audit record
or for unofficial election night results. (Actually the machine might
store vote records with uncertain cast status, so they would need to be linked
to a scan of an ID for a ballot when cast and inserted into the ballot box.)

The recommendation is for the voter-verified paper ballot to be the
official record counted. However, machine-stored CVRs could be used as
official data if validated by a 100% scan of the cast paper record, or
else a reliable audit of the paper record.

Voting machine stored CVRs Pros:
* Provides a separate audit record created on election day
* Digital signatures can prove data was created by that machine on election day
* Preliminary results can be obtained without needing to scan ballots
* Combining electronic and paper records is more secure, because they authenticate each other

Voting machine stored CVRs Cons:
* Need ballot ID scan to distinguish a cast CVR from discarded CVR
* Need to collect data from each machine, possible extra hardware
* Extra high-sensitivity software might be needed
* More digital security required; not storing CVRs would mean not having to digitally secure them

_[Question added: May 9, 2018 meeting.]_


### 8.6. Should a machine-marked ballot contain a bar code with a digital signature and/or CVR?

Background: Machines that record voter selections and print a ballot can
easily add a bar code (e.g. 2D QR code) that could contain a digital
signature of the electronic representation of the printed choices,
possibly with the electronic CVR. A digital signature would function
as a check for accurate interpretation of a scanned ballot, and also
could validate the printout as being created on a particular machine
on election day (or early voting period). The signature prevents anyone
from replacing the paper ballot with a substitute, provided appropriate
digital signature protocols are implemented.

The electronic CVR could be printed as a bar code as well, either as
a separate check or to assist the optical scan interpretation.

\[Note, a digital signature could be printed as text, e.g. base64 letters
and numbers, but a pile of numbers is no more human readable than a bar code.]

Ballots with digital signature bar codes Pros:
* Prevents tampering of paper ballots, either alterations or substitution
* Proves this paper was printed by a particular machine on particular day(s)

Ballots with digital signature bar codes Cons:
* Some people dislike (do not trust) printing that is not human readable and verifiable

_[Question added: May 9, 2018 meeting.]_


### 8.7. If voting machines are used at a precinct, should there be one printer per voting station?

Background: Each electronic voting station could be configured with a
printer to create the ballots to be cast. Alternatively, there could be
many voting stations (e.g. just a tablet computer), then a separate
printing station would be used to print completed ballots. With separate
printing stations, a _token_ is required to be scanned to identify the
ballot completed at a voting station.

Voters using a home computer or phone to record personal ballot choices
could bring a QR code printed or saved in a smartphone and go directly
to the printing station. A token might be required to verify the ballot
type.

Note: a _token_ could simply be a bar code with ballot type and unique
random number printed on the outside of a privacy folder. The number has
no association with a voter-- just a way to associate the ballot entered
at a voting station with the ballot to be printed. Another form of token
in use is an RFID chip.

_[Question added: Feb. 8, 2018 meeting.]_


### 8.8. If voters at precincts use hand-marked ballots, should ballots be scanned centrally or at the precinct/vote center?

Precinct ballot scanner Pros:
* Overvotes/Undervotes and invalid or ambiguous marks can be reported by the
    scanner prior to submitting
* Precinct vote counts are available immediately at the end of the day
* Reduces the need for central scanning equipment

Precinct ballot scanner Cons:
* More equipment is required than central-only scanners
* If the scanner and ballot collection is integrated (the scanner feeds
    into a ballot collection bin), custom equipment may be required.
* Not required if all ballots are printed by a voting machine

_[Question added: Feb. 8, 2018 meeting.]_


### 8.9. If a precinct scanner is used, does the scanner need to be integrated with a ballot collection bin?

  Background: Custom-built precinct ballot scanners sold by election vendors
usually include a ballot collection bin within same box containing the scanner.
The scanner feeds the ballot into the collection box, or else reverses the paper
feed in case of an error detected. Scanners may need multiple collection bins
in case of ambiguous marks or write-in votes. An integrated device likely
means custom hardware vs COTS equipment.

_[Question added: Feb. 8, 2018 meeting.]_


### 8.10. If a precinct scanner (or central scanner) is used, does it need to include an imprinter to record a ballot/scan ID?

  Background: To match a specific paper ballot in a ballot box with a scanned
CVR, either the order of insertion must be maintained, or a unique identifier
associated with the scan needs to be added to the ballot. Alternatively,
ordered ballots could be rescanned centrally during a recount or audit and
matched as a batch with the original scan.

Scanner Imprinter Pros:

* This would permit more sophisticated auditing approaches that involve
  selecting individual ballots at random, which could reduce time and costs
  (e.g. risk-limiting audits). Without this feature, auditing needs to be
  done in larger “batches,” or ballots need to be kept in careful order to
  allow accessing individual ballots.

Scanner Imprinter Cons:

* It is not clear if COTS scanners support the feature of printing while
  scanning. Available imprinters are expensive and might reduce scan speed.

* The scanner hardware would become more complicated since there would be
  another “moving part” that can break, and may require consumables, e.g.
  printer ink or ribbon changes.

_[Question & answer edited: Feb. 8, 2018 meeting.]_


### 8.11. If a voting machine is used to print all precinct ballots and possibly save CVRs, does the ballot collection box need to have an integrated scanner?

Background: Using a voting machine with voter-verified ballot does not
constitute casting a ballot-- the act of submitting the ballot after
verification is the cast ballot. Voters might choose to discard a ballot and
revote, so a simple bar-code scanner is useful to match the electronic CVR with
paper ballots submitted (i.e. exclude discarded ballots). Discarded ballots
could be scanned instead, but a voter could still walk off with a ballot, or a
ballot might not print correctly.

(The LA County VSAP integrates the voting machine, printer, and ballot collection bin. The printer has a bar code scanner to read the ballot type on blank ballot paper and to re-read the ballot ID (to match with a CVR) as it enters the integrated ballot box.)

Whether or not an electronic CVR exists within the voting machine, it may still be
useful to have a full scanner at the precinct, so all CVRs are derived from
the scanned paper read by the voter, and scanned images are available immediately
at the end of election day. However, without a full precinct scanner, vote
totals would still be available at the end of the day, and a central scanner
could be used after the election for a 100% audit of paper ballots (paper CVRs).

If only machine-printed ballots are collected (no undervote/overvote/ambiguous
mark detection is required), then a simple plain COTS scanner could be used
to feed the ballot paper in the collection bin, only recording the ballot images.

Additional ballot box scanner Pros:

* CVRs are derived from the paper verified by voters, not an indirect stored CVR (one criticism of "Voter Verified Paper Audit Trail" is that the human-read paper record is typically not 100% checked)

* Scanned ballot images can be recorded during the election and available
immediately afterwards.

* Voting machines and scanners could use independent equipment and software,
increasing security.

* Precinct scanners for casting voting-machine printed ballots could also be
used to scan vote-by-mail (hand-marked) ballots.

* A precinct scanner could be used with text-to-speech to read back a ballot
for the visually impaired.

Additional ballot box scanner Cons:

* Additional equipment is required which is in theory, unnecessary.

* A full scanner capable of error detection on hand-marked ballots might
require custom hardware (not COTS) for integration with a collection bin.
A simplified scanner that only can feed into the ballot box could be COTS.

_[Question & answer edited: April 12, 2018 meeting.]_


### 8.12. Is voting equipment required to run off a battery (without outside AC power) for a set outage duration or all day?

No outside power Pros:
* Eliminates extension cords and possible special power requirements.
* Voting can continue in a power outage.
* Some equipment (tablets and laptops) has a built in battery that can work
  during a power outage.

No outside power Cons:
* Limits the type of equipment used
* Might require special external batteries and power conversion

_[Question added: Feb. 8, 2018 meeting.]_


### 8.13. What kind of printing technology should be used at a poll site or vote center?

Background: There are many options for COTS and custom printers, including
several options for printing technology. Each option has different tradeoffs
in power requirements, consumables (ink, toner, etc.), an types of paper
supported.

There is not necessarily a requirement that the printing technology be the
same across all locations. For example, a vote center might use a laser printer
for printing ballots on demand whereas a voting machine at a precinct might
use a thermal printer running off a battery.

Options Include:

* Laser Printer (single/double sided)

    Pros:
    + High quality, durable printing
    + Toner lasts for a large number of pages
    + Fast printing

    Cons:
    + Requires AC power (limited life on backup power)
    + Tracking/replacing toner cartridges is required

* Ink Jet (single/double sided)

    Pros:
    + Low power
    + Available as portable battery powered COTS

    Cons:
    + Ink cartridges drain quickly and dry out between elections
    + Ink can smear before drying
    + Head cleaning might be required

* Direct Thermal (on special paper)

    Pros:
    + Low power
    + No consumables that need monitoring and reloading

    Cons:
    + Requires special paper
    + Limited life - disappearing ink
    + Temperature sensitive
    + Lower resolution

* Thermal Transfer (uses a ribbon)
    Pros:
    + Low power
    + High quality printing

    Cons:
    + Ribbon usage needs to be tracked and replaced
    + Not normally used for letter size printers

_[Question added: Feb. 8, 2018 meeting; edited April 12, 2018 meeting.]_


### 8.14. What size paper should be used for precinct voting and vote by mail?

Background: Vote-by-mail ballots are typically printed on wide paper
stock (sometimes 11"x17") folded to fit within a mailing envelope.
Precinct voting with a scanner does not need to be folded, and could
be a different size than mailed ballot.

With a larger paper size, more columns could be used, larger fonts, and
fewer sheets. With a smaller paper size (8.5"x11" or 8.5"x14"),
standard printers and scanners could be used. LA County published
a [usability study][la-vsap-vbm-study] of mail ballot design including
2 paper sizes (8.5x11" and 10.5x17").

If voting machines are used to print a _paper cast vote record_, then
only the selections made are shown, so a single sheet could be used.

_[Question added: Feb. 8, 2018 meeting.]_


### 8.15. What options should be provided to people with disabilities?

Accessible voting could be accomplished with:

* Voting machines (BMD) at all precincts (or vote centers) and early
  voting stations
* Voting machines at selected precincts or vote centers with transportation
  provided (Question: is this really permitted?)
* Vote by mail using home computer and printer

_[Question added: Feb. 8, 2018 meeting.]_


### 8.16. Should "remote accessible vote-by-mail" (RAVBM) printing used by voters with disabilities to vote by mail using home computers also be used for accessible precinct voting?

  Background: California Election code specifies that remote accessible vote by
mail capability should be provided by 2020 for people with disabilities and
military and overseas voters. Software to prepare these RAVBM ballots could in
principle be used at a precinct poll site or early vote center. Some states have
used a similar system (e.g. Prime-III) for disability access voting at
precincts.

RAVBM used in precincts Pros:

* Simplifies the software-- a single accessible voting software system is required
both for accessible vote-by-mail and precinct voting. Likewise scanner software for
reading RAVBM ballot paper would be reused for precinct voting.

* An RAVBM system must be usable with home COTS hardware, so only COTS hardware
would be needed to implement accessible precinct voting.

RAVBM used in precincts Cons:

* The hardware and software used by RAVBM would probably not be considered as secure as smaller and more specialized software running on a secure microcomputer.

* RAVBM ballots might require a paper size different from other precinct ballots. (Although Prime-III as modified by NH could print on hand-marked ballot paper.)

_[Question added: Feb. 8, 2018 meeting; edited April 12, 2018 meeting.]_


### 8.17. Does ballot collection order or CVR recordings need to be randomized to protect voter privacy (be disassociated by order of appearance at a precinct)?

Background: To protect voter privacy, either the time and order of appearance
of a voter must not be recorded, or else the order of scanned or submitted
ballots must be randomized. Otherwise voter order and ballot order could
be correlated and secrecy compromized. If ballot box order must be randomized,
then poll workers might need to shuffle ballots.

Scanned ballots imprinted with an ID could have sequential number assigned,
could simplify pulling ballots with a specific ID, e.g. for a ballot
requiring adjudication, or in an audit. Otherwise, a randomly assigned
unique ID could be imprinted, and stored electronic cast vote records
could have order randomized.

_[Question added: Feb. 8, 2018 meeting.]_


### 8.18. Should scanned ballot images or compiled CVRs be an open public record, possibly electronically accessible?

In the interest of making the election process transparent, the electronic
records of scanned ballots and/or CVRs could be made public (vs sealed
paper ballot storage containers). Is open ballot data possible within the
legal requirements of privacy and not being able to identify and prove a vote?
Would open ballot data be part of end-end verifiability or mutually exclusive
to it?

Ranked Choice Voting (RCV) might require a public set of cast vote records (CVR)
to fully disclose voter choices and validate the elimination rounds.

South Carolina publishes CVRs as part of its [election audit process][south-carolina-audits].
This data has been [republished in alternate formats][south-carolina-json] by
interested members of the public, and been used by political scientists to
[research voting patterns][south-carolina-poster].

_[Question added: Feb. 8, 2018 meeting; edited: March 14, 2019 meeting.]_


### 8.19. End-to-end verifiability

[TODO: Introduction - why we want it ...]

It should be determined how much additional work would need to be done to
make the voting process end-to-end verifiable, and whether and which designs
are more compatible (e.g. among approaches listed above, hand-marked vs
machine-printed ballots). Also, is this something that could
be incorporated later on in the process, or does it need to be incorporated
from the beginning?

Is it possible to have end-end verifiability without also being able to
prove how one voted?

[TODO: List current research on E2E voting.]

_[Question & answer edited: Feb. 8, 2018 meeting.]_


## 9. FAQ

**1. Is open source software more or less secure than proprietary
software?**

Independent studies have shown that, in general, open source software is
neither more secure nor less secure than proprietary software (see for
example Synopsys's ["Coverity® Scan Open Source Report
2014"][coverity-report-2014]). Both secure and insecure open source software
can be written. Similarly, both secure and insecure proprietary software can
be written.

A key difference though is that, because it is publicly viewable, claims
about the security of open source software can be _independently verified_,
and by _anyone_ (provided they have the necessary skills and time). With
proprietary code, such claims can be based only on trusting those who are
able to view the code.

The security of a given piece of software is primarily a function of how well
the software is written. It does not (and should not) depend on keeping the
code secret. The idea that software can be made secure by keeping it secret
is an idea known as "security by obscurity" and is widely rejected in the
security community.

Open source is already heavily used and relied upon throughout the world for
security-critical applications. For example, much of the code that allows
the secure transmission of information over the internet is open source.

**2. How can members of the public be sure that the open source code is
what is actually running on the machine?**

The short answer is that there is no way to be certain that the code
running on a particular device or computer is what one expects it to be
(whether the software is open source or not). This is true even if very
careful measures are taken. This is an extremely hard problem to solve and
is an active area of research. One reason is that there is no way to be
sure that the computer hardware itself can be trusted.

Having said that, good auditing practices that involve randomly checking
computer results by hand against the original paper ballots are an adequate
countermeasure, provided the audits are done correctly. This is why good
audit procedures are important when computers are used to count ballots.

_[Answer added: Dec. 14, 2017 meeting.]_

**3. How much of the code must be open source for the voting system to
be considered open source?**

Whether something is open source or not is best answered not as a yes or
no question but as a matter of degree.  For example, a hardware device could
be 99% open source except for one small bit of proprietary firmware.

In general, our committee recommends the approach of trying to maximize
the amount of open source -- i.e. the more open source, the better.
There is no fundamental reason why the entire voting system can't be open
source. However, if some portion isn't open source, it is better if that
portion is as small as possible and if it's for optional functionality
rather than required functionality.

Also, if the eventual system does contain any non-open source code, in
the spirit of agile, one could work to replace that code with an open source
equivalent in later versions of the system.

_[Answer added: Dec. 14, 2017 meeting.]_


## 10. Glossary

* **adjudicate**. [TODO]

* **agile**. [TODO]

* **ballot**. [TODO]

* **ballot on-demand**. [TODO]

* **ballot type**. [TODO]

* **cast-vote record (CVR)**. [TODO]

* **central ballot scanner**. [TODO]

* **commercial off-the-shelf (COTS)**. [TODO]

* **comparison audit**. [TODO]

* **component**. [TODO]

* **digital ballot picture**. [TODO]

* **EIMS®**. [EIMS®](http://www.dfmassociates.com/eims.asp) is the software
  application that the Department of Elections uses for certain
  election-related functions like maintaining voter registration data,
  administering polling place information, defining ballot styles, and
  tracking candidate filings for office (see
  [Appendix A][dfm-contract-appendix-a] of the City's contract with DFM for
  a detailed listing of the required capabilities).
  The Department signed a nine-year contract
  with [DFM Associates](http://www.dfmassociates.com) for the software
  in June 2011 ([DFM contract][dfm-contract-main],
  [Appendix A][dfm-contract-appendix-a],
  [Appendix B][dfm-contract-appendix-b],
  [Appendix C][dfm-contract-appendix-c],
  [Appendix D][dfm-contract-appendix-d],
  [Appendix E][dfm-contract-appendix-e]). The contract lists the per-year
  maintenance and support costs as ranging between $170,820.00 and
  $274,299.60 (see [Appendix D][dfm-contract-appendix-d] of the contract
  for more detail).

* **end-to-end verifiability**. [TODO]

* **firmware**. [TODO]

* **free and open source software (FOSS)**. [TODO]

* **free software**. [TODO]

* **hardware**. [TODO]

* **hardware component**. [TODO]

* **open hardware**. [TODO]

* **open source software**. [TODO]

* **operating system**. [TODO]

* **outstack**. [TODO]

* **paper cast vote record**. "an auditable document that corresponds to the
  selection made on the voter's ballot and lists the contests on the ballot and
  the voter's selections for those contests. A paper cast vote record is not a ballot."[\[CEC19271\]][cec-19271]

  _[Item added: Jan. 18, 2018 meeting.]_

* **precinct ballot scanner**. [TODO]

* **remake**. [TODO]

* **remote accessible vote by mail system**.
  Software or electronic system that allows a voter with
  disabilities or a military or overseas voter to print a ballot
  (_paper cast vote record_) at home and return by mail.

  _[Item added: Jan. 18, 2018 meeting.]_

* **risk-limiting audit (RLA)**. [TODO]

* **software**. [TODO]

* **software API**. [TODO]

* **software application**. [TODO]

* **software library**. [TODO]

* **software service**. [TODO]

* **software stack**. [TODO]

* **stack**. See ”software stack.”

* **statement of vote**. [TODO]

* **voter verified paper audit trail**. "a _paper cast vote record_ containing a
  copy of each of the voter's selections that allows each voter to confirm his
  or her selections before the voter casts his or her ballot for systems that
  do not contain a paper ballot.'[\[CEC19271\]][cec-19271]

  _[Item added: Jan. 18, 2018 meeting.]_


[18f-modular-contracting]: https://modularcontracting.18f.gov/
[ballot-verification-2018-paper]: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3292208
[bill-ab-2252-2015]: https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=201520160AB2252
[bill-sb-360-2013]: https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=201320140SB360
[bill-sb-450-2015]: https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=201520160SB450
[board-of-supervisors]: http://sfbos.org/
[bos-open-source-voting-res]: files/BOS_Resolution_460-14_Open_Source_Voting.pdf
[bos-ordinance-vstf]: files/BOS_Ordinance_268-08_VSTF.pdf
[cavo]: http://www.cavo-us.org/index.html
[cc-by-sa]: https://creativecommons.org/licenses/by-sa/4.0/
[cec-19271]:https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=ELEC&sectionNum=19271.
[cla]: https://en.wikipedia.org/wiki/Contributor_License_Agreement
[coit]: http://sfcoit.org/
[colorado-rla-home]: http://bcn.boulder.co.us/~neal/elections/corla/
[colorado-rla-repo]: https://github.com/FreeAndFair/ColoradoRLA
[commission-osvtac]: http://sfgov.org/electionscommission/osvtac
[commission-res-pdf-local]: files/commission-resolution/SF_Elections_Comm_Open_Source_Voting_Res.pdf
[commission-res-txt-local]: files/commission-resolution/SF_Elections_Comm_Open_Source_Voting_Res.txt
[commission-resolutions]: http://sfgov.org/electionscommission/motions-and-resolutions
[coverity-report-2014]: http://go.coverity.com/rs/157-LQW-289/images/2014-Coverity-Scan-Report.pdf
[cran-rcv]: https://github.com/ds-elections/rcv
[dfm-contract-appendix-a]: files/dfm-contract/DFM_Contract_Appendix_A_Perf_Reqs.pdf
[dfm-contract-appendix-b]: files/dfm-contract/DFM_Contract_Appendix_B_Scope.pdf
[dfm-contract-appendix-c]: files/dfm-contract/DFM_Contract_Appendix_C_Maintenance.pdf
[dfm-contract-appendix-d]: files/dfm-contract/DFM_Contract_Appendix_D_Fee_Schedule.pdf
[dfm-contract-appendix-e]: files/dfm-contract/DFM_Contract_Appendix_E_Hardware_Specs.pdf
[dfm-contract-main]: files/dfm-contract/DFM_Contract_060111.pdf
[directors-report-march-2017-local]: files/SF_Elections_March_2017_Director_Report.pdf
[directors-report-march-2017-original]: http://sfgov.org/electionscommission/sites/default/files/Documents/meetings/2017/2017-03-15-commission/March%202017%20Director%20Report.pdf
[disability-rights-ca-letters]: files/Disability_Rights_Letters_Nisen.pdf
[dominion-costs-2008]: files/Dominion_System_Costs_2008_Jerdonek.pdf
[eac-vvsg]: https://www.eac.gov/voting-equipment/voluntary-voting-system-guidelines/
[eac]: https://www.eac.gov/
[elections-commission]: http://sfgov.org/electionscommission
[eml-specs]: http://docs.oasis-open.org/election/eml/v7.0/eml-v7.0.html
[eml-wikipedia]: https://en.wikipedia.org/wiki/Election_Markup_Language
[free-and-fair]: http://freeandfair.us/blog/open-free-election-technology/
[fromira-twitter-rcv]: https://twitter.com/fromira/status/1004484579334340608
[github]: https://github.com/
[ict-plan-2008]: files/SF_ICT_Plan_2018-22.pdf
[ieee-1622]: http://grouper.ieee.org/groups/1622/
[jets-0202]: https://pdfs.semanticscholar.org/30c0/9a87a67516ce91a339d7059ff6a211872e41.pdf
[la-vsap-application-tally]: files/la-vsap/LA_Application_VSAP_Tally_1.0_2017-09-19.pdf
[la-vsap-rfi]: files/la-vsap/LA_RFI_20170524.pdf
[la-vsap-rfp-phase-1]: files/la-vsap/LA_RFP_20170918.pdf
[la-vsap]: http://vsap.lavote.net/
[la-vsap-vbm-study]: http://vsap.lavote.net/wp-content/uploads/2016/06/Vox-VBM-Report-V1.3.pdf
[lafco-report]: files/LAFCo_Report_Open_Source_Voting.pdf
[lafco]: http://sfgov.org/lafco/
[levi]: https://dspace.mit.edu/handle/1721.1/96560
[mayor-budget-press-release]: http://sfmayor.org/article/mayor-lee-signs-citys-balanced-budget-fiscal-years-2016-17-2017-18
[nist-itl]: https://www.nist.gov/itl/voting
[nist-voting]: http://collaborate.nist.gov/voting/bin/view/Voting/WebHome
[nist-vvsg-principles]: http://collaborate.nist.gov/voting/bin/view/Voting/VVSGPrinciplesAndGuidelines
[one4all-demo]: https://www.youtube.com/watch?v=g6jgmIdG56M
[one4all-howto]: https://www.youtube.com/watch?v=3FSjzHVPAkQ
[one4all-ppt]: http://bowencenterforpublicaffairs.org/wp-content/uploads/2016/06/NH-One4all-Technical-Overview-2016-06-15.pdf
[one4all-vvf]: https://www.verifiedvoting.org/one4all/
[one4all-setup]: https://www.youtube.com/watch?v=c2WXpQjihJI
[one4all-ltr]: http://www.cavo-us.org/PDFS/Open_source_letter_from_Bill_Gardner.pdf
[open-count-pres]: https://www.usenix.org/conference/evtwote12/workshop-program/presentation/wang_kai
[open-count]: https://github.com/FreeAndFair/OpenCount
[open-rla-repo]: https://github.com/FreeAndFair/OpenRLA
[open-voting-consortium]: http://www.openvotingconsortium.org
[open-voting-consortium-usenix-paper]: http://gnosis.cx/publish/voting/electronic-voting-machine.pdf
[oset-arch-html]: https://trustthevote.org/our-work/framework/
[oset-arch-pdf]: http://www.dubberly.com/wp-content/uploads/2014/09/TTV_Framework_Book.pdf
[oset-foundation]: http://www.osetfoundation.org/
[oset-modules]: https://trustthevote.org/our-work/overview-2/
[osi-approved-licenses]: https://opensource.org/licenses
[osi]: https://opensource.org/
[osvtac-about-recs]: https://osvtac.github.io/about#project-recommendations
[osvtac]: https://osvtac.github.io
[prime-iii-repo]: https://github.com/HXRL/Prime-III
[prime-iii]: http://www.primevotingsystem.com/
[prime-iii-demo]: https://hxr.cise.ufl.edu/PrimeIII/index.html
[prime-iii-video]: https://www.youtube.com/watch?v=bM5DKP4c4aw
[proposed-budget-2016]: files/SF_Mayor_Proposed_Budget_2016-18.pdf
[pvote]: http://pvote.org/
[rfp-business-case-pdf]: files/SF_Business_Case_RFP_FINAL.pdf
[sf-digital-services]: https://digitalservices.sfgov.org/
[sf-digital-services-strategy]: files/SF_DigitalServiceStrategy.pdf
[sf-dst]: https://digitalservices.sfgov.org/
[sf-moci]: http://www.innovation.sfgov.org/
[slalom-contract-appendix-a]: files/slalom/contract/Business_Case_Appendix_A.pdf
[slalom-contract-appendix-b]: files/slalom/contract/Business_Case_Appendix_B.pdf
[slalom-contract]: files/slalom/contract/Business_Case_Contract.pdf
[sos-advisories]: http://www.sos.ca.gov/elections/advisories-county-elections-officials/
[sos-digest]: http://www.sos.ca.gov/elections/publications-and-resources/elections-officers-digest-2018/
[south-carolina-audits]: https://www.scvotes.org/election-audits-south-carolina
[south-carolina-json]: https://github.com/hodgesmr/south_carolina_2018_ballot_image_json
[south-carolina-poster]: http://www.shirokuriwaki.com/papers/kuriwaki_scvotes.pdf
[slalom-rfp-response]: files/slalom/REG_RFP_2017-01_Slalom_Response.pdf
[star-vote-entity]: files/star-vote/STAR-Vote_Statement_of_Intent.pdf
[star-vote-final-press-release]: http://www.traviscountyclerk.org/eclerk/Content.do?code=star-vote-a-change-of-plans
[star-vote-faf-repo]: https://github.com/FreeAndFair/STAR-Vote
[star-vote-final-report]: files/star-vote/STAR_Vote_Final_Report.pdf
[star-vote-rfp]: files/star-vote/RFP_STAR-Vote_Unofficial_Copy.pdf
[star-vote-usenix]: https://www.usenix.org/conference/evtwote13/workshop-program/presentation/bell
[techfar-handbook]: https://playbook.cio.gov/techfar/
[trust-the-vote]: https://trustthevote.org
[trust-the-vote-votestream]:http://votestream.trustthevote.org/
[verified-voting-foundation]: https://www.verifiedvoting.org/
[vip-project]: https://votinginfoproject.org/
[vip-repo]: https://github.com/votinginfoproject
[votebox]: http://votebox.cs.rice.edu/
[vstf-report]: files/VSTF_Report.pdf
[vstf]: http://sfgov.org/ccsfgsa/voting-systems-task-force


<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">
<img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" />
</a><br />This work is licensed under a
<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative
Commons Attribution-ShareAlike 4.0 International License</a>.
For copyright and attribution information for this work, see
[this section](copyright). The source files for the text can be found on
GitHub [here](https://github.com/OSVTAC/project-recommendations).
