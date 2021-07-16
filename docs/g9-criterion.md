# HL7 C-CDA API criterion at § 170.315(g)(9)

## Information and Clarifications

### Entire Criterion

??? quote "*Clarifications included in the (g)(9) CCG that apply to the entire criterion*"
	- Security:

		- For the purposes of certification there is no conformance requirement related to the registration of third-party applications that use the application programming interfaces (APIs). If a Health IT module requires registration as a pre-condition for accessing the APIs, then, the process must be clearly specified in the API documentation as required by the criterion. We strongly believe that registration should not be used to block information sharing via APIs.
		- This criterion does not currently include any security requirements beyond the privacy and security approach detailed above, but we encourage organizations to follow security best practices and implement security controls, such as penetration testing, encryption, audits, and monitoring as appropriate. We expect health IT developers to include information on how to securely use their APIs in the public documentation required by the certification criteria and follow industry best practices. [see also <a href="http://www.federalregister.gov/a/2015-25597/p-1072" target="_blank">80 FR 62676</a> and <a href="https://www.federalregister.gov/d/2020-07419/p-3518" target="_blank">85 FR 25642</a>]
		- We strongly encourage developers to build security into their APIs following best practice guidance, such as the Department of Homeland Security’s Build Security In initiative.1 [see also <a href="http://www.federalregister.gov/a/2015-25597/p-1084" target="_blank">80 FR 62677</a>]
		- A “trusted connection” means the link is encrypted/integrity protected according to § 170.210(a)(2) or (c)(2). As such, we do not believe it is necessary to specifically name HTTPS and/or SSL/TLS as this standard already covers encryption and integrity protection for data in motion. [see also <a href="https://www.federalregister.gov/d/2015-25597/p-1072" target="_blank">80 FR 62676</a>]
		- APIs could be used when consent or authorization by an individual is required. In circumstances where there is a requirement to document a patient’s request or particular preferences, APIs can enable compliance with documentation requirements. The Health Insurance Portability and Accountability Act of 1996 Privacy Rule2 permits the use of electronic documents to qualify as writings for the purpose of proving signature, e.g., electronic signatures. [see also <a href="http://www.federalregister.gov/a/2015-25597/p-1094" target="_blank">80 FR 62677</a>]
	- The audit record should be able to distinguish the specific user who accessed the data using a third-party application through the certified API to meet the requirements of § 170.315(d)(2) or (d)(10).
	- A health IT developer must demonstrate the API functionality of the Health IT Module properly performs consistent with this certification criterion’s requirements. As part of the demonstration process, a health IT developer is permitted, but is not limited to, using existing tools for creating its own app or “client” to interact with the API or using a third-party application for demonstration.
	- By requiring that documentation and terms of use be open and transparent to the public by requiring a hyperlink to such documentation to be published with the product on the ONC Certified Health IT Product List, we hope to encourage an open ecosystem of diverse and innovative applications that can successfully and easily interact with different Health IT Modules’ APIs. [see also <a href="http://www.federalregister.gov/a/2015-25597/p-1112" target="_blank">80 FR 62679</a> and <a href="https://www.federalregister.gov/d/2020-07419/p-3518" target="_blank">85 FR 25642</a>]
	- By no later than April 5, 2021, a Certified API Developer with Health IT Module(s) certified to the certification criteria in § 170.315(g)(7), (8), or (9) must comply with paragraph (a) of this section, including revisions to their existing business and technical API documentation and make such documentation available via a publicly accessible hyperlink that allows any person to directly access the information without any preconditions or additional steps.


### Functional Requirements (Data Categories)

???+ quote "**Regulation text at § 170.315(g)(9)(i)(A)**"
     (i) Functional requirements. (A)(1) Respond to requests for patient data (based on an ID or other token) for all of the data classes expressed in the standards in § 170.213 at one time and return such data (according to the specified standards, where applicable) in a summary record formatted in accordance with § 170.205(a)(4) and (5) following the CCD document template, and as specified in paragraphs (g)(9)(i)(A)(3)(i) through (iii) of this section, or (2) The Common Clinical Data Set in accordance with paragraphs (g)(9)(i)(A)(3)(i) through (iv) of this section for the period before December 31, 2022, and (3) The following data classes: (i) Assessment and plan of treatment. In accordance with the “Assessment and Plan Section (V2)” of the standards specified in § 170.205(a)(4); or in accordance with the “Assessment Section (V2)” and “Plan of Treatment Section (V2)” of the standards specified in § 170.205(a)(4). (ii) Goals. In accordance with the “Goals Section” of the standards specified in § 170.205(a)(4). (iii) Health concerns. In accordance with the “Health Concerns Section” of the standards specified in § 170.205(a)(4). (iv) Unique device identifier(s) for a patient's implantable device(s). In accordance with the “Product Instance” in the “Procedure Activity Procedure Section” of the standards specified in § 170.205(a)(4).

??? quote "*Clarifications included in the (g)(9) CCG that apply to paragraph § 170.315(g)(9)(i)(A)*"
	- Please refer to the USCDI for the data standards that are required.
	- The technology specifications should be designed and implemented in such a way as to return meaningful responses to queries, particularly with regard to exceptions and exception handling, and should make it easy for applications to discover what data exists for the patient. [see also <a href="http://www.federalregister.gov/a/2015-25597/p-1109" target="_blank">80 FR 62678</a>]
	- The term “token” that is used here is not to be interpreted as the token in the OAuth2 workflow, but simply as something that would uniquely identify a patient.
	- In order to mitigate potential interoperability errors and inconsistent implementation of the HL7 Implementation Guide for CDA® Release 2: Consolidated CDA Templates for Clinical Notes, Draft Standard for Trial Use, Release 2.1, ONC assesses, approves, and incorporates corrections as part of required testing and certification to this criterion. Certified health IT adoption and compliance with the following corrections are necessary because they implement updates to vocabularies, update rules for cardinality and conformance statements, and promote proper exchange of C-CDA documents. There will be  a 90-day delay from the time the CCG has been updated with the ONC-approved corrections to when compliance with the corrections will be required to pass testing (i.e., C-CDA 2.1 Validator).There will be an 18-month delay before a finding of a correction’s absence in certified health IT during surveillance would constitute a non-conformity under the Program.


### Functional Requirements (Date & Date Range)

???+ quote "**Regulation text at § 170.315(g)(9)(i)(B)**"
    (B) Respond to requests for patient data associated with a specific date as well as requests for patient data within a specified date range.

??? quote "*Clarifications included in the (g)(9) CCG that apply to paragraph § 170.315(g)(9)(i)(B)*"
	- Health IT returning an entire patient record that does not reflect the specific date or date range requested is not permissible when a specific date or date range is requested. [see also <a href="http://www.federalregister.gov/a/2015-25597/p-1109" target="_blank">80 FR 62678</a>]
	- The developer can determine the method and the amount of data by which the health IT uniquely identifies a patient. [see also <a href="http://www.federalregister.gov/a/2015-25597/p-1101" target="_blank">80 FR 62678</a>]
	- The API must be able to send, at minimum all required data for a specified date range(s). We acknowledge that there will be organizational policies and/or safety best practices that will dictate additional data to be sent and when data is considered complete and/or ready for being sent. This should be appropriately described in the API documentation.
	- The approach used to provide the CCD document(s) is set by the API. An approach based on providing one or more CCD documents matching to the patient’s selected date or date range is a valid approach.


### Documentation Requirements (API Interface)

???+ quote "**Regulation text at § 170.315(g)(9)(ii)(A)(1)**"
    (A) The API must include accompanying documentation that contains, at a minimum: (1) API syntax, function names, required and optional parameters and their data types, return variables and their types/structures, exceptions and exception handling methods and their returns.

??? quote "*Clarifications included in the (g)(9) CCG that apply to paragraph § 170.315(g)(9)(ii)(A)(1)*"
	- No additional clarifications available.


### Documentation Requirements (API Interaction)

???+ quote "**Regulation text at § 170.315(g)(9)(ii)(A)(2)**"
    (2) The software components and configurations that would be necessary for an application to implement in order to be able to successfully interact with the API and process its response(s).

??? quote "*Clarifications included in the (g)(9) CCG that apply to paragraph § 170.315(g)(9)(ii)(A)(2)*"
	- No additional clarifications available.


### Documentation Requirements (Availability)

???+ quote "**Regulation text at § 170.315(g)(9)(ii)(B)**"
    (B) The documentation used to meet paragraph (g)(9)(ii)(A) of this section must be available via a publicly accessible hyperlink.

??? quote "*Clarifications included in the (g)(9) CCG that apply to paragraph § 170.315(g)(9)(ii)(B)*"
	- The hyperlink provided for all of the documentation referenced by provision (g)(9)(ii)(A) must reflect the most current version of the Health IT developer’s documentation.
	- All of the documentation referenced by provision (g)(9)(ii)(A) must be accessible to the public via a hyperlink without additional access requirements, including, without limitation, any form of registration, account creation, “click-through” agreements, or requirement to provide contact details or other information prior to accessing the documentation.


--8<-- "includes/abbreviations.md"