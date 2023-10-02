import streamlit as st
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space
import requests
# import template _1 as T1

# print("0000000000000")
# print(T1.Template_1)
# from hugchat import hugchat

st.set_page_config(page_title="HugChat - An LLM-powered Streamlit app")

Template_1=''' Agreement No. 8767-19-IT
0 | P a g e
Table of Contents
Software As A Service “SaaS” Agreement. The following Exhibits 
are incorporated into the SaaS Agreement:
Exhibit A-1 Socrata Open Finance Terms
Exhibit A Investment Summary
Exhibit B Invoicing and Payment Policy
o Schedule 1: Business Travel Policy
Exhibit C Service Level Agreement
o Schedule 1: Support Call Process
Exhibit D Third Party Terms
o Schedule 1: DocOrigin EULA
o Schedule 2: BMI Terms
Exhibit E Statement of Work
End of SaaS agreement
Exhibit F Tyler’s Response to Client’s Original Request for Proposals
Exhibit G Tyler’s Subsequent Responses to Client’s Requests for
Clairfications
Exhibit H Insurance Exhibits (INS- W)
Exhibit I Tyler’s Response to Client’s Best and Final Offer
 
Agreement No. 8767-19-IT
SOFTWARE AS A SERVICE AGREEMENT
This Software as a Service Agreement is made between Tyler Technologies, Inc. and Client. 
WHEREAS, Client selected Tyler to provide certain products and services set forth in the Investment Summary, including providing Client with access to Tyler’s proprietary software products, and Tyler
desires to provide such products and services under the terms of this Agreement. NOW THEREFORE, in consideration of the foregoing and of the mutual covenants and promises set forth 
in this Agreement, Tyler and Client agree as follows: SECTION A – DEFINITIONS
● “Agreement” means this Software as a Services Agreement.
● “Business Travel Policy” means our business travel policy. A copy of our current Business Travel
Policy is attached as Schedule 1 to Exhibit B.
● “Client” means City of Oxnard.
● “Data” means your data necessary to utilize the Tyler Software.
● “Data Storage Capacity” means the contracted amount of storage capacity for your Data 
identified in the Investment Summary.
● “Defect” means a failure of the Tyler Software to substantially conform to the functional 
descriptions set forth in our written proposal to you, or their functional equivalent. Future 
functionality may be updated, modified, or otherwise enhanced through our maintenance and 
support services, and the governing functional descriptions for such future functionality will be 
set forth in our then-current Documentation.
● “Defined Users” means the number of users that are authorized to use the SaaS Services. The Defined Users for the Agreement are as identified in the Investment Summary.
● “Developer” means a third party who owns the intellectual property rights to Third Party
Software.
● “Documentation” means any online or written documentation related to the use or functionality of the Tyler Software that we provide or otherwise make available to you, including 
instructions, user guides, manuals and other training or self-help documentation. ● “Effective Date” means the date by which both your and our authorized representatives have 
signed the Agreement.
● “Force Majeure” means an event beyond the reasonable control of you or us, including, without 
limitation, governmental action, war, riot or civil commotion, fire, natural disaster, or any other 
cause that could not with reasonable diligence be foreseen or prevented by you or us.
● “Investment Summary” means the agreed upon cost proposal for the products and services
attached as Exhibit A.
● “Invoicing and Payment Policy” means the invoicing and payment policy. A copy of our current Invoicing and Payment Policy is attached as Exhibit B. ● “Key Personnel” means Tyler’s project manager and primary implementation consultant for 
each phase of the project
● “SaaS Fees” means the fees for the SaaS Services identified in the Investment Summary.
1 | P a g e
Agreement No. 8767-19-IT
● “SaaS Services” means software as a service consisting of system administration, system 
management, and system monitoring activities that Tyler performs for the Tyler Software, and 
includes the right to access and use the Tyler Software, receive maintenance and support on the 
Tyler Software, including Downtime resolution under the terms of the SLA, and Data storage and 
archiving. SaaS Services do not include support of an operating system or hardware, support 
outside of our normal business hours, or training, consulting or other professional services.
● “SLA” means the service level agreement. A copy of our current SLA is attached hereto as
Exhibit C. ● “Statement of Work” means the industry standard implementation plan describing how our 
professional services will be provided to implement the Tyler Software, and outlining your and 
our roles and responsibilities in connection with that implementation. The Statement of Work is 
attached as Exhibit E. ● “Support Call Process” means the support call process applicable to all of our customers who 
have licensed the Tyler Software. A copy of our current Support Call Process is attached as 
Schedule 1 to Exhibit C.
● “Third Party Terms” means, if any, the end user license agreement(s) or similar terms for the
Third Party Software, as applicable and attached as Exhibit D.
● “Third Party Hardware” means the third party hardware, if any, identified in the Investment
Summary.
● “Third Party Products” means the Third Party Software and Third Party Hardware.
● “Third Party Software” means the third party software, if any, identified in the Investment Summary.
● “Third Party Services” means the third party services, if any, identified in the Investment
Summary.
● “Tyler” means Tyler Technologies, Inc., a Delaware corporation. ● “Tyler Software” means our proprietary software, including any integrations, custom 
modifications, and/or other related interfaces identified in the Investment Summary and 
licensed by us to you through this Agreement.
● “we”, “us”, “our” and similar terms mean Tyler.
● “you” and similar terms mean Client or City. SECTION B – SAAS SERVICES 1. Rights Granted. We grant to you the non-exclusive, non-assignable limited right to use the SaaS 
Services solely for your internal business purposes for the number of Defined Users only. The Tyler 
Software will be made available to you according to the terms of the SLA. You acknowledge that we 
have no delivery obligations and we will not ship copies of the Tyler Software as part of the SaaS 
Services. You may use the SaaS Services to access updates and enhancements to the Tyler Software, 
as further described in Section C(8).
2. SaaS Fees. You agree to pay us the SaaS Fees. Those amounts are payable in accordance with our 
Invoicing and Payment Policy. The SaaS Fees are based on the number of Defined Users and amount 
of Data Storage Capacity. You may add additional users or additional data storage capacity on the 
terms set forth in Section H(1). In the event you regularly and/or meaningfully exceed the Defined 
Users or Data Storage Capacity, we reserve the right to charge you additional fees commensurate 
with the overage(s). Prior to increase charges pursuant to this section, Tyler will provide you notice
of such excess(es) and reasonably cooperate with you to identify opportunities for managing user 
and Data Storage Capacity so as to not incur additional charges.
2 | P a g e
Agreement No. 8767-19-IT
3. Ownership. 3.1 We retain all ownership and intellectual property rights to the SaaS Services, the Tyler Software, 
and anything developed by us under this Agreement. You do not acquire under this Agreement 
any license to use the Tyler Software in excess of the scope and/or duration of the SaaS Services.
3.2 The Documentation is licensed to you and may be used and copied by your employees for 
internal, non-commercial reference purposes only.
3.3 You retain all ownership and intellectual property rights to the Data. You expressly recognize 
that except to the extent necessary to carry out our obligations contained in this Agreement, we 
do not create or endorse any Data used in connection with the SaaS Services.
3.4 Within 30 days of a written request, we will deliver a complete copy of Client’s Database(s) 
currently hosted by Tyler. Alternatively, the Client may request Tyler provide a copy of the 
Client Data in a platform agnostic form (ASCII, for example). Tyler will not unreasonably refuse 
such request. 4. Restrictions. You may not: (a) make the Tyler Software or Documentation resulting from the SaaS 
Services available in any manner to any third party for use in the third party’s business operations; 
(b) modify, make derivative works of, disassemble, reverse compile, or reverse engineer any part of 
the SaaS Services; (c) access or use the SaaS Services in order to build or support, and/or assist a 
third party in building or supporting, products or services competitive to us; or (d) license, sell, rent, 
lease, transfer, assign, distribute, display, host, outsource, disclose, permit timesharing or service 
bureau use, or otherwise commercially exploit or make the SaaS Services, Tyler Software, or 
Documentation available to any third party other than as expressly permitted by this Agreement.
5. Software Warranty. We warrant that the Tyler Software will perform without Defects during the 
term of this Agreement. If the Tyler Software does not perform as warranted, we will use all 
reasonable efforts, consistent with industry standards, to cure the Defect in accordance with the 
maintenance and support process set forth in Section C(8), below, the SLA and our then current 
Support Call Process.
6. Functionality Replacement. For a period of five (5) years from the Effective Date, if a new release of 
the Tyler Software removes functionality that was originally provided under this SaaS Agreement, 
we will provide alternative means for performing the same function, at no additional cost to you 
beyond payment of the annual SaaS Fees.
7. Availability of SaaS Services. So long as Client continuously maintains this SaaS Agreement with 
Tyler, Tyler will make SaaS Services available for the Tyler Software licensed to the Client as of the 
Effective Date for ten (10) years from the Effective Date
8. SaaS Services. 8.1 Our SaaS Services are audited at least yearly in accordance with the AICPA’s Statement on 
Standards for Attestation Engagements (“SSAE”) No. 18. We have attained, and will maintain, 
SOC 1 and SOC 2 compliance, or its equivalent, for so long as you are timely paying for SaaS 
Services. Upon execution of a mutually agreeable Non-Disclosure Agreement (“NDA”), we will 
provide you with a summary of our compliance report(s) or its equivalent. Every year
3 | P a g e
Agreement No. 8767-19-IT
thereafter, for so long as the NDA is in effect and in which you make a written request, we will 
provide that same information. 8.2 The Tyler Software will be hosted on shared hardware in a Tyler data center or a third party 
datacenter, but in a database dedicated to you, which is inaccessible to our other customers.
8.3 We have fully-redundant telecommunications access, electrical power, and the required 
hardware to provide access to the Tyler Software in the event of a disaster or component 
failure. In the event any of your Data has been lost or damaged due to an act or omission of 
Tyler or its subcontractors or due to a defect in Tyler’s software, we will use best commercial 
efforts, as established by applicable California law, to restore all the Data on servers in 
accordance with the architectural design’s capabilities and with the goal of minimizing any Data 
loss as greatly as possible. In no case shall the recovery point objective (“RPO”) exceed a 
maximum of twenty-four (24) hours from declaration of disaster. For purposes of this 
subsection, RPO represents the maximum tolerable period during which your Data may be lost, 
measured in relation to a disaster we declare, said declaration will not be unreasonably 
withheld. 8.4 In the event we declare a disaster, our Recovery Time Objective (“RTO”) is twenty-four (24) 
hours. For purposes of this subsection, RTO represents the amount of time, after we declare a 
disaster, within which your access to the Tyler Software must be restored.
8.5 We conduct annual penetration testing of either the production network and/or web application to be performed. We will maintain industry standard intrusion detection and prevention systems to monitor malicious activity in the network and to log and block any such activity. We
will provide you with a written or electronic record of the actions taken by us in the event that
any unauthorized access to your database(s) is detected as a result of our security protocols. We
will undertake an additional security audit, on terms and timing to be mutually agreed to by the parties, at your written request. You may not attempt to bypass or subvert security restrictions 
in the SaaS Services or environments related to the Tyler Software. Unauthorized attempts to
access files, passwords or other confidential information, and unauthorized vulnerability and
penetration test scanning of our network and systems (hosted or otherwise) is prohibited 
without the prior written approval of our IT Security Officer.
8.6 We test our disaster recovery plan on an annual basis. Our standard test is not client-specific.
Should you request a client-specific disaster recovery test, we will work with you to schedule 
and execute such a test and provide results in accord with a mutually agreeable schedule.
8.7 We will be responsible for importing back-up and verifying that you can log-in. You will be 
responsible for running reports and testing critical processes to verify the returned Data.
8.8 We provide secure Data transmission paths between each of your workstations and our servers.
8.9 For at least the past twelve (12) years, all of our employees have undergone criminal 
background checks prior to hire. All employees sign our confidentiality agreement and security 
policies. Our data centers are accessible only by authorized personnel with a unique key entry. 
All other visitors must be signed in and accompanied by authorized personnel. Entry attempts 
to the data center are regularly audited by internal staff and external auditors to ensure no 
unauthorized access.
4 | P a g e
Agreement No. 8767-19-IT
8.10 Where applicable with respect to our applications that take or process card payment data, we 
are responsible for the security of cardholder data that we possess, including functions relating 
to storing, processing, and transmitting of the cardholder data and affirm that, as of the
Effective Date, we comply with applicable requirements to be considered PCI DSS compliant and 
have performed the necessary steps to validate compliance with the PCI DSS. We agree to
supply the current status of our PCI DSS compliance program in the form of an official 
Attestation of Compliance, which can be found at https://www.tylertech.com/about- us/compliance, and in the event of any change in our status, will comply with applicable notice 
requirements.
SECTION C – OTHER PROFESSIONAL SERVICES
1. Other Professional Services. We will provide you the various implementation-related services 
itemized in the Investment Summary and described in the Statement of Work.
2. Key Personnel. We will maintain an adequate staff of specifically knowledgeable, experienced and
qualified employees sufficient for performing our obligations pursuant to this Agreement. In the 
event Tyler personnel provide services deficient in this regard, Tyler will be given a reasonable 
opportunity to correct the deficiency while preserving overall project schedules. Once Tyler has had 
a reasonable opportunity to correct the deficiency, if the deficiency persists, then Client may 
provide written notice to Tyler, demanding that the Tyler personnel be removed. In such a case, 
Tyler will provide a replacement within a commercially reasonable time while preserving overall 
project timelines. In the event Tyler disagrees with the Client’s demand, the matter shall be 
referred to the Dispute Resolution Process of this Agreement.
3. Professional Services Fees. You agree to pay us the professional services fees in the amounts set 
forth in the Investment Summary. Those amounts are payable in accordance with our Invoicing and 
Payment Policy. We will bill you the actual fees incurred based on the in-scope services provided to 
you. Any discrepancies in the total values set forth in the Investment Summary will be resolved by 
multiplying the applicable hourly rate by the quoted hours. The Investment Summary contains the 
fees for Professional Services reasonably required to implement the Statement of Work. The 
services in the Investment Summary are reasonably sufficient to deliver the mutually agreed scope 
of the project as documented in this Agreement. Both the Oxnard City Manager or designee and 
Tyler shall mutually agree, in writing, prior to Tyler utilizing any Implementation Contingency or 
NTE Contingency Hours listed in the Investment Summary. If the services in the Investment Summary are not reasonably sufficient to deliver such scope of the project through no fault of yours, 
Tyler will perform such services as are reasonably necessary to complete the mutually agreed scope without additional cost to you. 4. Additional Services. The Investment Summary contains, and the Statement of Work describes, the 
scope of services and related costs (including a not-to-exceed amount for programming and/or 
interfaces) required for the project based on our understanding of the specifications you supplied. 
The foregoing notwithstanding, travel costs are estimated. If additional work is required, or if you 
use or request additional services, we will provide you with an addendum or change order, as 
applicable, outlining the costs for the additional work. The price quotes in the addendum or change 
order will be valid for thirty (30) days from the date of the quote. No services will be added to this 
Agreement without your advance written consent.
5 | P a g e
Agreement No. 8767-19-IT
5. Cancellation. If travel is required, we will make all reasonable efforts to schedule travel for our 
personnel, including arranging travel reservations, at least two (2) weeks in advance of 
commitments. Therefore, if you cancel services less than two (2) weeks in advance (other than for 
Force Majeure or breach by us), you will be liable for all (a) non-refundable expenses incurred by us 
on your behalf, and (b) daily fees associated with cancelled professional services if we are unable to 
reassign our personnel. We will make all reasonable efforts to reassign personnel in the event you 
cancel within two (2) weeks of scheduled commitments.
6. Services Warranty. We will perform the services in a professional, workmanlike manner, consistent 
with industry standards. In the event we provide services that do not conform to this warranty, we 
will re-perform such services, including related travel, lodging and meal expenses, at no additional 
cost to you. 7. Site Access and Requirements. At no cost to us, you agree to provide us with full and free access to 
your personnel, facilities, and equipment as may be reasonably necessary for us to provide 
implementation services, subject to any reasonable security protocols or other written policies 
provided to us as of the Effective Date, and thereafter as mutually agreed to by you and us.
8. Client Assistance. You acknowledge that the implementation of the Tyler Software is a cooperative 
process requiring the time and resources of your personnel. You agree to use all reasonable efforts 
to cooperate with and assist us as may be reasonably required to meet the agreed upon project 
deadlines and other milestones for implementation. This cooperation includes at least working with 
us to schedule the implementation-related services outlined in this Agreement. We will not be
liable for failure to meet any deadlines and milestones when such failure is due to Force Majeure or 
to the failure by your personnel to provide such cooperation and assistance (either through action 
or omission), provided such failure is not directly caused by the corresponding failure of Tyler 
personnel to meet agreed project deadlines and milestones assigned to us.
9. Project Schedule. Within thirty (30) business days of the initial implementation phase kick-off, we will deliver to you a detailed Project Plan, which includes Gantt chart, work breakdown structure, schedule and task duration that lists both our and your responsibilitiesto accomplish the tasks set forth in the Statement of Work as well as the specific start and end dates for each activity. The
Project Plan will be in sufficient detail to specify the installation, conversion, training, testing,
acceptance, and live operation activitiesfor each phase, including the planned phase go-live date.
The parties understand and agree that the Project Plan(s) may be modified, as necessary, by mutual
agreement and in accordance with the processes set forth in the Statement of Work. Both parties
will make reasonable efforts to schedule project kickoff within sixty (60) days of the Effective Date.
10. Key Personnel. We will provide you with resumes of our project manager and primary
implementation consultants(“Key Personnel”) assigned to you by us before scheduling the kick-off date of each project phase as identified in the Statement of Work. Tyler will use commercially reasonable efforts to maintain the consistency of its project personnel. We agree to provide you
timely notice of any change in Tyler personnel delivering implementation services pursuant to this
Agreement. Tyler agrees that any replacement personnel will, at no additional cost to you, obtain
sufficient knowledge of project requirements and history in order to perform the services required
pursuant to this Agreement and in accordance with the services warranty of this section.
11. Maintenance and Support. For so long as you timely pay your SaaS Fees according to the Invoicing 
and Payment Policy, then in addition to the terms set forth in the SLA and the Support Call Process,
6 | P a g e
Agreement No. 8767-19-IT
we will:
11.1 Perform our maintenance and support obligations in a professional, good, and workmanlike 
manner, consistent with industry standards, to resolve Defects in the Tyler Software (limited 
to the then-current version and the immediately prior version);
11.2 Provide telephone support during our established support hours;
11.3 Maintain personnel that are sufficiently trained to be familiar with the Tyler Software and
Third Party Software, if any, in order to provide maintenance and support services;
11.4 Make available to you all major and minor releases to the Tyler Software (including updates 
and enhancements) that we make generally available without additional charge to 
customers who have a maintenance and support agreement in effect;
11.5 Provide non-Defect resolution support of prior releases of the Tyler Software in accordance 
with our then-current release life cycle policy;
11.6 Modify the Tyler Software to remain compliant with applicable state and federal laws, for 
no additional SaaS fees, provided, however, that Vendor shall have a reasonable time to 
adapt the Tyler Software Products to comply with changes in the laws;
11.7 We will use all reasonable efforts to perform support services remotely. Currently, we use a 
third-party secure unattended connectivity tool called Bomgar, as well as GotoAssist by 
Citrix. Therefore, you agree to maintain a high-speed internet connection capable of 
connecting us to your PCs and server(s). You agree to provide us with a login account and 
local administrative privileges as we may reasonably require to perform remote services.
We will, at our option, use the secure connection to assist with proper diagnosis and 
resolution, subject to any reasonably applicable security protocols. If we cannot resolve a 
support issue remotely, we may be required to provide onsite services. In such event, we 
will be responsible for our travel expenses, unless it is determined, by both City and Tyler, 
that the reason onsite support was required was a reason outside our control. If the 
parties disagree as to whether the reason onsite support was required was outside our 
control, then the dispute shall be referred to the dispute resolution process of this 
Agreement. Either way, you agree to provide us with full and free access to the Tyler 
Software, working space, adequate facilities within a reasonable distance from the 
equipment, and use of machines, attachments, features, or other equipment reasonably 
necessary for us to provide the maintenance and support services, all at no charge to us.
We strongly recommend that you also maintain your VPN for backup connectivity purposes.
11.8 For the avoidance of doubt, SaaS Fees do not include the following services: (a) onsite 
support (unless Tyler cannot remotely correct a Defect in the Tyler Software, as set forth 
above); (b) customization of software not otherwise provided in new releases pursuant to 
Section 11.4 herein; (c) other consulting services; or (d) support outside our normal 
business hours as listed in our then-current Support Call Process. Requested services such 
as those outlined in this section will be billed to you on a time and materials basis at our 
then current rates. You must request those services with at least one (1) weeks’ advance 
notice. 7 | P a g e
Agreement No. 8767-19-IT
8 | P a g e
SECTION D – THIRD PARTY PRODUCTS 1. Third Party Hardware. We will sell, deliver, and install onsite the Third Party Hardware, if you have 
purchased any, for the price set forth in the Investment Summary. Those amounts are payable in 
accordance with our Invoicing and Payment Policy. 2. Third Party Software. As part of the SaaS Services, you will receive access to the Third Party 
Software and related documentation for internal business purposes only. Your rights to the Third 
Party Software will be governed by the Third Party Terms.
3. Third Party Products Warranties. 3.1 We are authorized by each Developer to grant access to the Third Party Software.
3.2 The Third Party Hardware will be new and unused, and upon payment in full, you will receive 
free and clear title to the Third Party Hardware.
3.3 You acknowledge that we are not the manufacturer of the Third Party Products. We do not 
warrant or guarantee the performance of the Third Party Products. However, we grant and pass 
through to you any warranty that we may receive from the Developer or supplier of the Third 
Party Products.
4. Third Party Services. If you have purchased Third Party Services, those services will be provided 
independent of Tyler by such third-party at the rates set forth in the Investment Summary and in 
accordance with our Invoicing and Payment Policy. SECTION E - INVOICING AND PAYMENT; INVOICE DISPUTES
1. Invoicing and Payment. We will invoice you the SaaS Fees and fees for other professional services in 
the Investment Summary per our Invoicing and Payment Policy, subject to Section E(2).
2. Invoice Disputes. If you believe any delivered software or service does not conform to the warranties
in this Agreement, you will provide us with written notice within forty-five (45) days of your receipt of the applicable invoice. The written notice must contain reasonable detail of the issues you contend are in dispute so that we can confirm the issue and respond to your notice with either a
justification of the invoice, an adjustment to the invoice, or a proposal addressing the issues 
presented in your notice. We will work with you as may be necessary to develop an action plan that 
outlines reasonable steps to be taken by each of us to resolve any issues presented in your notice. 
You may withhold payment of the amount(s) actually in dispute, and only those amounts, until we 
complete the action items outlined in the plan. If we are unable to complete the action items 
outlined in the action plan because of your failure to complete the items agreed to be done by you, 
then you will remit full payment of the invoice. We reserve the right to suspend delivery of all SaaS 
Services, including maintenance and support services, if you fail to pay an invoice not disputed as 
described above within fifteen (15) days of notice of our intent to do so. SECTION F – TERM AND TERMINATION 1. Term. The initial term of this Agreement is five (5) years from the first day of the first month 
following the Effective Date, unless earlier terminated as set forth below. Upon expiration of the 
initial term, this Agreement will renew automatically for additional one (1) year renewal terms at
Agreement No. 8767-19-IT
our then-current SaaS Fees unless terminated in writing by either party at least sixty (60) days prior 
to the end of the then-current renewal term. Your right to access or use the Tyler Software and the SaaS Services will terminate at the end of this Agreement. 2. Termination. This Agreement may be terminated as set forth below. In the event of termination, 
you will pay us for all undisputed fees and expenses related to the software, products, and/or 
services you have received, or we have incurred or delivered, prior to the effective date of 
termination. Disputed fees and expenses in all terminations other than your termination for cause 
must have been submitted as invoice disputes in accordance with Section E(2).
2.1 Failure to Pay SaaS Fees. You acknowledge that continued access to the SaaS Services is 
contingent upon your timely payment of SaaS Fees. If you fail to timely pay the SaaS Fees, we 
may discontinue the SaaS Services and deny your access to the Tyler Software. We may also 
terminate this Agreement if you don’t cure such failure to pay within forty-five (45) days of 
receiving written notice of our intent to terminate. 2.2 For Cause. If you believe we have materially breached this Agreement, you will invoke the 
Dispute Resolution clause set forth in Section H(3). You may terminate this Agreement for cause 
in the event we do not cure, or create a mutually agreeable action plan to address, a material 
breach of this Agreement within the thirty (30) day window set forth in Section H(3).
2.3 For Convenience. Client may terminate this Agreement at any time, with or without cause and 
without penalty, upon thirty (30) days prior written notice. 2.4 Force Majeure. Either party has the right to terminate this Agreement if a Force Majeure event 
suspends performance of the SaaS Services for a period of forty-five (45) days or more.
2.5 Lack of Appropriations. You agree not to use termination for lack of appropriations as a 
substitute for termination for convenience. If you should not appropriate or otherwise receive 
funds sufficient to purchase, lease, operate, or maintain the software or services set forth in this 
Agreement, you may unilaterally terminate this Agreement effective on the final day of the fiscal 
year through which you have funding. You will make every effort to give us at least thirty (30) 
days written notice prior to a termination for lack of appropriations. In the event of termination 
due to a lack of appropriations, you will pay us for all undisputed fees and expenses related to 
the software and/or services you have received prior to the effective date of termination,
subject to the requirement that such travel expenses must have been incurred before the date 
of your notice of termination. Any disputed fees and expenses must have been submitted to 
the Invoice Dispute process at the time of termination in order to be withheld at termination. 
You will not be entitled to a refund or offset of previously paid license and other fees.
2.6 Termination by Mutual Agreement. This Agreement may be terminated at any time during its
 Term upon mutual agreement by both Parties.
2.7 Transition Services. In the event of termination by either party, Tyler shall reasonably 
cooperate with you to provide reasonable transition services to assist with your migration to a 
new solution provider of your choice provided such services are generally made available to 
other similarly situated Tyler clients. The parties agree to work together in good faith to create 
a mutually agreeable scope for those services, to be provided at Tyler’s then-current pricing. In 
no event shall Tyler be required to disclose any Tyler confidential information to any such new
9 | P a g e
Agreement No. 8767-19-IT
vendor but will reasonably cooperate in response to requests to provide information as such is 
commercially and reasonably available.
2.8 Return of Licensee Data: In the event of termination or expiration of this Agreement, and upon 
reasonable advance notice, Tyler shall promptly make all Client Data available to you as may be 
mutually agreed upon, provided through Tyler’s FTP server or such other secure transfer 
method as mutually agreed upon. Client Data will be provided no later than sixty (60) days prior
to the date of expiration or termination, as applicable, (provided at least 10 days advance notice 
by Client) and again seven (7) days after date of expiration or termination, as applicable.
2.9 Once a successful hand-off of that data has been confirmed via written confirmation, all Client 
data shall be permanently removed from all Tyler production servers.
SECTION G – INDEMNIFICATION, LIMITATION OF LIABILITY AND INSURANCE 1. Intellectual Property Infringement Indemnification. 1.1 We will defend you against any third party claim(s) that the Tyler Software or Documentation 
infringes that third party’s patent, copyright, or trademark, or misappropriates its trade secrets, 
and will pay the amount of any resulting adverse final judgment (or settlement to which we 
consent). You must notify us promptly in writing of the claim and give us sole control over its 
defense or settlement. You agree to provide us with reasonable assistance, cooperation, and 
information in defending the claim at our expense.
1.2 Our obligations under this Section G(1) will not apply to the extent the claim or adverse final 
judgment is based on your use of the Tyler Software in contradiction of this Agreement, 
including with non-licensed third parties, or your willful infringement.
1.3 If we receive information concerning an infringement or misappropriation claim related to the 
Tyler Software, we may, at our expense and without obligation to do so, either: (a) procure for 
you the right to continue its use; (b) modify it to make it non-infringing; or (c) replace it with a 
functional equivalent, in which case you will stop running the allegedly infringing Tyler Software 
immediately. Alternatively, we may decide to litigate the claim to judgment, in which case you 
may continue to use the Tyler Software consistent with the terms of this Agreement.
1.4 If an infringement or misappropriation claim is fully litigated and your use of the Tyler Software 
is enjoined by a court of competent jurisdiction, in addition to paying any adverse final 
judgment (or settlement to which we consent), we will, at our option, either: (a) procure the
right to continue its use; (b) modify it to make it non-infringing; or (c) replace it with a functional 
equivalent; or (d) terminate this Agreement and refund you the prepaid but unused SaaS Fees 
for the year in which the Agreement terminates. This section provides your exclusive remedy
for third party copyright, patent, or trademark infringement and trade secret misappropriation 
claims.
2. General Indemnification. 2.1 We will indemnify and hold harmless you and your agents, officials, and employees from and 
against any and all third-party claims, losses, liabilities, damages, costs, and expenses (including
10 | P a g e
Agreement No. 8767-19-IT
reasonable attorney's fees and costs) for (a) personal injury or property damage to the extent 
caused by our negligence or willful misconduct; (b) our breach of Section H(17) of this 
Agreement; or (c) our violation of PCI-DSS requirements or a law applicable to our performance 
under this Agreement. You must notify us promptly in writing of the claim and give us sole 
control over its defense or settlement. You agree to provide us with reasonable assistance, 
cooperation, and information in defending the claim at our expense.
2.2 To the extent permitted by applicable law, you will indemnify and hold harmless us and our 
agents, officials, and employees from and against any and all third-party claims, losses, 
liabilities, damages, costs, and expenses (including reasonable attorney's fees and costs) for 
(a) personal injury or property damage to the extent caused by your negligence or willful misconduct; or (b) our breach of Section (17) of this Agreement; or (c) your violation of a law applicable to your performance under this Agreement. We will notify you promptly in writing of
the claim and will give you sole control over its defense or settlement. We agree to provide you with reasonable assistance, cooperation, and information in defending the claim at your 
expense.
3. DISCLAIMER. EXCEPT FOR THE EXPRESS WARRANTIES PROVIDED IN THIS AGREEMENT AND TO 
THE MAXIMUM EXTENT PERMITTED BY APPLICABLE LAW, WE HEREBY DISCLAIM ALL OTHER 
WARRANTIES AND CONDITIONS, WHETHER EXPRESS, IMPLIED, OR STATUTORY, INCLUDING, BUT 
NOT LIMITED TO, ANY IMPLIED WARRANTIES, DUTIES, OR CONDITIONS OF MERCHANTABILITY OR 
FITNESS FOR A PARTICULAR PURPOSE.
4. LIMITATION OF LIABILITY. EXCEPT AS OTHERWISE EXPRESSLY SET FORTH IN THIS AGREEMENT, 
OUR LIABILITY FOR DAMAGES ARISING OUT OF THIS AGREEMENT, WHETHER BASED ON A THEORY 
OF CONTRACT OR TORT, INCLUDING NEGLIGENCE AND STRICT LIABILITY, SHALL BE LIMITED TO 
YOUR ACTUAL DIRECT DAMAGES, NOT TO EXCEED (A) DURING THE INITIAL TERM, AS SET FORTH IN SECTION F(2), TOTAL FEES PAID AS OF THE TIME OF THE CLAIM; OR (B) DURING ANY RENEWAL 
TERM, THE THEN-CURRENT ANNUAL SAAS FEES PAYABLE IN THAT RENEWAL TERM. THE PARTIES 
ACKNOWLEDGE AND AGREE THAT THE PRICES SET FORTH IN THIS AGREEMENT ARE SET IN 
RELIANCE UPON THIS LIMITATION OF LIABILITY AND TO THE MAXIMUM EXTENT ALLOWED UNDER 
APPLICABLE LAW, THE EXCLUSION OF CERTAIN DAMAGES, AND EACH SHALL APPLY REGARDLESS 
OF THE FAILURE OF AN ESSENTIAL PURPOSE OF ANY REMEDY. THE FOREGOING LIMITATION OF 
LIABILITY SHALL NOT APPLY TO CLAIMS THAT ARE SUBJECT TO SECTIONS G(1) AND G(2). 5. EXCLUSION OF CERTAIN DAMAGES. TO THE MAXIMUM EXTENT PERMITTED BY APPLICABLE LAW, 
IN NO EVENT SHALL WE BE LIABLE FOR ANY SPECIAL, INCIDENTAL, PUNITIVE, INDIRECT, OR 
CONSEQUENTIAL DAMAGES WHATSOEVER, EVEN IF WE HAVE BEEN ADVISED OF THE POSSIBILITY 
OF SUCH DAMAGES. 6. Insurance. During the course of performing services under this Agreement, we agree to maintain 
the following levels of insurance: (a) Commercial General Liability of at least $1,000,000; (b) Automobile Liability of at least $1,000,000; (c) Professional Liability (inclusive of Privacy and Cyber 
Liability) of at least $3,000,000 per occurrence and in the aggregate; (d) Workers Compensation 
complying with applicable statutory requirements;, and (e) Excess/Umbrella Liability of at least
$5,000,000. We will add you as an additional insured to our Commercial General Liability and 
Automobile Liability policies, which will automatically add you as an additional insured to our 
Excess/Umbrella Liability policy as well. Tyler must maintain and provide copies of certificates of 
insurance upon policy renewals.
11 | P a g e '''
# Sidebar contents
with st.sidebar:
    st.title('MLAI Digital')
    # st.markdown('''
    # ## About
    # This app is an LLM-powered chatbot built using:
    # - [Streamlit](https://streamlit.io/)
    # - [HugChat](https://github.com/Soulter/hugging-chat-api)
    # - [OpenAssistant/oasst-sft-6-llama-30b-xor](https://huggingface.co/OpenAssistant/oasst-sft-6-llama-30b-xor) LLM model
    
    # 💡 Note: No API key required!
    # ''')
    add_vertical_space(5)

# Generate empty lists for generated and past.
## generated stores AI generated responses
if 'generated' not in st.session_state:
    st.session_state['generated'] = ["Hi, How may I help you?"]
## past stores User's questions
if 'past' not in st.session_state:
    st.session_state['past'] = ['Hi!']

# Layout of input/response containers
input_container = st.container()
colored_header(label='', description='', color_name='blue-30')
response_container = st.container()

# User input
## Function for taking user provided prompt as input
def get_text():
    input_text = st.text_input("You: ", "", key="input")
    return input_text
## Applying the user input box
with input_container:
    user_input = get_text()

# Response output
## Function for taking user prompt as input followed by producing AI generated responses
def generate_response(prompt):
    API_URL = "https://api-inference.huggingface.co/models/bigscience/bloom"
    headers = {"Authorization": "Bearer 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"}

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()
        
    response = query({
        "inputs": user_input,
    })
    # chatbot = hugchat.ChatBot()
    # response = chatbot.chat(prompt)
    return response

## Conditional display of AI generated responses as a function of user provided prompts
with response_container:
    if user_input:
        response = generate_response(user_input)
        st.session_state.past.append(user_input)
        st.session_state.generated.append(response)
        
    if st.session_state['generated']:
        for i in range(len(st.session_state['generated'])):
            message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
            message(st.session_state["generated"][i], key=str(i))



# import streamlit as st
# import requests
# # from streamlit_extras.colored_header import colored_header



# st.title('🎈 App Name')

# # # Securing app
# # with st.sidebar:
# #     st.title('🤗💬 HugChat')
# #     if ('EMAIL' in st.secrets) and ('PASS' in st.secrets):
# #         st.success('HuggingFace Login credentials already provided!', icon='✅')
# #         hf_email = st.secrets['EMAIL']
# #         hf_pass = st.secrets['PASS']
# #     else:
# #         hf_email = st.text_input('Enter E-mail:', type='password')
# #         hf_pass = st.text_input('Enter password:', type='password')
# #         if not (hf_email and hf_pass):
# #             st.warning('Please enter your credentials!', icon='⚠️')
# #         else:
# #             st.success('Proceed to entering your prompt message!', icon='👉')
# #     st.markdown('📖 Learn how to build this app in this [blog](https://blog.streamlit.io/how-to-build-an-llm-powered-chatbot-with-streamlit/)!')



# API_URL = "https://api-inference.huggingface.co/models/bigscience/bloom"
# headers = {"Authorization": "Bearer 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"}

# def query(payload):
# 	response = requests.post(API_URL, headers=headers, json=payload)
# 	return response.json()
	
# output = query({
# 	"inputs": "Can you please let us know more details about your ",
# })


# st.write('Hello world!')

# # Generate empty lists for generated and past.
# ## generated stores AI generated responses
# if 'generated' not in st.session_state:
#     st.session_state['generated'] = ["I'm HugChat, How may I help you?"]
# ## past stores User's questions
# if 'past' not in st.session_state:
#     st.session_state['past'] = ['Hi!']

# # Layout of input/response containers
# input_container = st.container()
# # colored_header(label='', description='', color_name='blue-30')
# response_container = st.container()

# # User input
# ## Function for taking user provided prompt as input
# def get_text():
#     input_text = st.text_input("You: ", "", key="input")
#     return input_text
# ## Applying the user input box
# with input_container:
#     user_input = get_text()

# # Response output
# ## Function for taking user prompt as input followed by producing AI generated responses
# def generate_response(prompt):
#     chatbot = hugchat.ChatBot()
#     response = chatbot.chat(prompt)
#     return response

# ## Conditional display of AI generated responses as a function of user provided prompts
# with response_container:
#     if user_input:
#         response = generate_response(user_input)
#         st.session_state.past.append(user_input)
#         st.session_state.generated.append(response)
        
#     if st.session_state['generated']:
#         for i in range(len(st.session_state['generated'])):
#             message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
#             message(st.session_state["generated"][i], key=str(i))


