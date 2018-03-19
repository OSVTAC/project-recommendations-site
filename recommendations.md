# Open Source Voting System Project Recommendations

(Approved by OSVTAC on March 8, 2018.)

Last posted: March 19, 2018


* [Introduction & Table of Contents](index) (for multi-page version)

* [Single-page version](single-page) (long, can be used for printing)

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">
<img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" />
</a><br />This work is licensed under a
<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative
Commons Attribution-ShareAlike 4.0 International License</a>.
For copyright and attribution information for this work, see
[this section](copyright). The source files for the text can be found on
GitHub [here](https://github.com/OSVTAC/project-recommendations).


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


[18f-modular-contracting]: https://modularcontracting.18f.gov/
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
