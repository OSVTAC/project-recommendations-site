# Open Source Voting System Project Recommendations

(Approved by OSVTAC on June 14, 2018.)

Last posted: December 12, 2018


**Note: these recommendations are a work in progress and not yet complete.**

This document contains the recommendations of San Francisco's [Open Source
Voting System Technical Advisory Committee][osvtac] (OSVTAC, or TAC) for
the City and County of San Francisco's open source voting system project, as
of the version date that appears above.

The committee started this document on August 30, 2017 and will continue to
work on it over time. Substantive updates to this document occur by a vote of
the committee at a committee meeting. Meetings occur approximately once a
month.

To learn more about the committee, visit the committee's website at
[https://osvtac.github.io][osvtac]. To learn how to suggest changes to this
document, view the "Project Recommendations" section of the [About
page][osvtac-about-recs] of the committee's website.


* [Single-page version](single-page) (long, can be used for printing)

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">
<img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" />
</a><br />This work is licensed under a
<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative
Commons Attribution-ShareAlike 4.0 International License</a>.
For copyright and attribution information for this work, see
[this section](copyright). The source files for the text can be found on
GitHub [here](https://github.com/OSVTAC/project-recommendations).


## Contents

* [1. Copyright and Attribution](copyright#1-copyright-and-attribution)
  * [1.1. Copyright](copyright#11-copyright)
  * [1.2. Contributors](copyright#12-contributors)
* [2. Goals](goals#2-goals)
  * [2.1. Scope](goals#21-scope)
  * [2.2. Priorities](goals#22-priorities)
  * [2.3. Non-goals](goals#23-non-goals)
* [3. Background](background#3-background)
  * [3.1. History of Open Source Voting in San Francisco](background#31-history-of-open-source-voting-in-san-francisco)
  * [3.2. Voting System](background#32-voting-system)
  * [3.3. Other Voting System Projects](background#33-other-voting-system-projects)
  * [3.4. Resources](background#34-resources)
* [4. Facts & Assumptions](facts-assumptions#4-facts--assumptions)
  * [4.1. Facts](facts-assumptions#41-facts)
  * [4.2. Assumptions](facts-assumptions#42-assumptions)
* [5. Components](components#5-components)
  * [5.1. Component Listing](components#51-component-listing)
  * [5.2. Component Details](components#52-component-details)
* [6. Recommendations](recommendations#6-recommendations)
  * [6.1. Interim Voting System](recommendations#61-interim-voting-system)
  * [6.2. Requirements-gathering](recommendations#62-requirements-gathering)
  * [6.3. Requirements](recommendations#63-requirements)
  * [6.4. Project Management](recommendations#64-project-management)
  * [6.5. Open Source](recommendations#65-open-source)
  * [6.6. Procurement](recommendations#66-procurement)
  * [6.7. Software architecture and design](recommendations#67-software-architecture-and-design)
  * [6.8. Software development](recommendations#68-software-development)
  * [6.9. Hardware design](recommendations#69-hardware-design)
  * [6.10. Documentation](recommendations#610-documentation)
  * [6.11. Security](recommendations#611-security)
  * [6.12. Testing](recommendations#612-testing)
  * [6.13. Certification](recommendations#613-certification)
  * [6.14. Hardware manufacturing or assembly](recommendations#614-hardware-manufacturing-or-assembly)
  * [6.15. Deployment](recommendations#615-deployment)
  * [6.16. Software maintenance](recommendations#616-software-maintenance)
  * [6.17. Hardware maintenance](recommendations#617-hardware-maintenance)
* [7. Recommended Implementation Order](implementation-order#7-recommended-implementation-order)
  * [7.1. Recommended First Components](implementation-order#71-recommended-first-components)
  * [7.2. Rationale](implementation-order#72-rationale)
  * [7.3. Results Reporter Rationale](implementation-order#73-results-reporter-rationale)
  * [7.4. Vote Totaler Rationale](implementation-order#74-vote-totaler-rationale)
  * [7.5. Central Ballot Scanner Rationale](implementation-order#75-central-ballot-scanner-rationale)
  * [7.6. Deployment Strategies](implementation-order#76-deployment-strategies)
  * [7.7. Central Ballot Scanner Phases](implementation-order#77-central-ballot-scanner-phases)
* [8. Equipment (“Product”) Decisions](decisions#8-equipment-“product”-decisions)
  * [8.1. Will vote centers be used for early and/or election day voting?](decisions#81-will-vote-centers-be-used-for-early-andor-election-day-voting)
  * [8.2. Should precinct polling and vote centers use the same paper ballots as those used in vote-by-mail?](decisions#82-should-precinct-polling-and-vote-centers-use-the-same-paper-ballots-as-those-used-in-vote-by-mail)
  * [8.3. Should ballots to be hand-marked be preprinted or printed on demand?](decisions#83-should-ballots-to-be-hand-marked-be-preprinted-or-printed-on-demand)
  * [8.4. Should voting at a precinct or vote center be primarily based on paper ballots hand-marked with a pen, or voting machine with a printer?](decisions#84-should-voting-at-a-precinct-or-vote-center-be-primarily-based-on-paper-ballots-hand-marked-with-a-pen-or-voting-machine-with-a-printer)
  * [8.5. If voters use machines to mark ballots, should the machine store CVRs of the marked selections?](decisions#85-if-voters-use-machines-to-mark-ballots-should-the-machine-store-cvrs-of-the-marked-selections)
  * [8.6. Should a machine-marked ballot contain a bar code with a digital signature and/or CVR?](decisions#86-should-a-machine-marked-ballot-contain-a-bar-code-with-a-digital-signature-andor-cvr)
  * [8.7. If voting machines are used at a precinct, should there be one printer per voting station?](decisions#87-if-voting-machines-are-used-at-a-precinct-should-there-be-one-printer-per-voting-station)
  * [8.8. If voters at precincts use hand-marked ballots, should ballots be scanned centrally or at the precinct/vote center?](decisions#88-if-voters-at-precincts-use-hand-marked-ballots-should-ballots-be-scanned-centrally-or-at-the-precinctvote-center)
  * [8.9. If a precinct scanner is used, does the scanner need to be integrated with a ballot collection bin?](decisions#89-if-a-precinct-scanner-is-used-does-the-scanner-need-to-be-integrated-with-a-ballot-collection-bin)
  * [8.10. If a precinct scanner (or central scanner) is used, does it need to include an imprinter to record a ballot/scan ID?](decisions#810-if-a-precinct-scanner-or-central-scanner-is-used-does-it-need-to-include-an-imprinter-to-record-a-ballotscan-id)
  * [8.11. If a voting machine is used to print all precinct ballots and possibly save CVRs, does the ballot collection box need to have an integrated scanner?](decisions#811-if-a-voting-machine-is-used-to-print-all-precinct-ballots-and-possibly-save-cvrs-does-the-ballot-collection-box-need-to-have-an-integrated-scanner)
  * [8.12. Is voting equipment required to run off a battery (without outside AC power) for a set outage duration or all day?](decisions#812-is-voting-equipment-required-to-run-off-a-battery-without-outside-ac-power-for-a-set-outage-duration-or-all-day)
  * [8.13. What kind of printing technology should be used at a poll site or vote center?](decisions#813-what-kind-of-printing-technology-should-be-used-at-a-poll-site-or-vote-center)
  * [8.14. What size paper should be used for precinct voting and vote by mail?](decisions#814-what-size-paper-should-be-used-for-precinct-voting-and-vote-by-mail)
  * [8.15. What options should be provided to people with disabilities?](decisions#815-what-options-should-be-provided-to-people-with-disabilities)
  * [8.16. Should "remote accessible vote-by-mail" (RAVBM) printing used by voters with disabilities to vote by mail using home computers also be used for accessible precinct voting?](decisions#816-should-remote-accessible-vote-by-mail-ravbm-printing-used-by-voters-with-disabilities-to-vote-by-mail-using-home-computers-also-be-used-for-accessible-precinct-voting)
  * [8.17. Does ballot collection order or CVR recordings need to be randomized to protect voter privacy (be disassociated by order of appearance at a precinct)?](decisions#817-does-ballot-collection-order-or-cvr-recordings-need-to-be-randomized-to-protect-voter-privacy-be-disassociated-by-order-of-appearance-at-a-precinct)
  * [8.18. Should scanned ballot images or compiled CVRs be an open public record, possibly electronically accessible?](decisions#818-should-scanned-ballot-images-or-compiled-cvrs-be-an-open-public-record-possibly-electronically-accessible)
  * [8.19. End-to-end verifiability](decisions#819-end-to-end-verifiability)
* [9. FAQ](faq#9-faq)
* [10. Glossary](glossary#10-glossary)


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
