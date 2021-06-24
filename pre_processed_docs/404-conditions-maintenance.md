$criterion-endpoint{"condition-ccg/application-programming-interfaces"}

# API Condition and Maintenance of Certification - § 170.404

This section considers the API Condition and Maintenance of Certification requirements, including all the content contained in the <a target = "_blank" href = "https://www.federalregister.gov/d/2020-07419/p-1162">ONC Cures Act Final Rule Conditions of Certification API preamble</a>, the <a target = "_blank" href = "https://www.federalregister.gov/d/2020-24376/p-136">ONC Interim Final Rule API preamble</a>, and the regulation paragraphs in <a target = "_blank" href = "https://www.federalregister.gov/d/2020-07419/p-3456">§ 170.315(g)(10)</a>.

## Applicability
§ 170.404 applies to all health IT developers with health IT certified to § 170.315(g)(7) – § 170.315(g)(10).

We described several actors in the <a target = "_blank" href = "https://www.federalregister.gov/d/2020-07419/p-1263">preamble</a> and <a target = "_blank" href = "https://www.federalregister.gov/d/2020-07419/p-3518">regulation text</a> for § 170.404. These actors are defined at <a target = "_blank" href = "https://www.federalregister.gov/d/2020-07419/p-3575">§ 170.404(c)</a>, and include “API Information Source”, “API User”, and “Certified API Developer”. We clarified in preamble and have included in the CCG for § 170.404 that “A person or entity is permitted to serve more than one role for the terms defined in § 170.404(c)” and “Stakeholders meet the definition of a term defined in § 170.404(c) based on the context in which they are acting.” Generally, the API Conditions and Maintenance of Certification requirements finalized in § 170.404 apply to Certified API Developers only, which are health IT developers with Health IT Modules certified to § 170.315(g)(7), § 170.315(g)(8), § 170.315(g)(9) and/or § 170.315(g)(10). API Users and API Information Sources, unless they are also acting as a Certified API Developer, are not required to conform to § 170.315(g)(10) or abide by the requirements in § 170.404. The ONC Health IT Certification Program does not have certification criteria for patientfacing applications developed by API Users.

## Certified APIs and the HIPAA Privacy Rule
Certified API Developers must publish Service Base URLs for patient access.

Certified API Developers are required to publish Service Base URLs (§ 170.404(b)) that can be used by patients to exercise their <a target = "_blank" href = "https://www.hhs.gov/hipaa/index.html">HIPAA Privacy Rule</a> right of access. Additionally, the Standardized API for Patient and Population Services can be used by entities to share <a target = "_blank" href = "https://www.hhs.gov/hipaa/for-professionals/privacy/guidance/disclosures-treatment-payment-health-care-operations/index.html">treatment, payment, and health care operations</a> information with other authorized parties. The Office of Civil Rights created a page titled “<a target = "_blank" href = "https://www.hhs.gov/hipaa/for-professionals/privacy/guidance/access-right-health-apps-apis/index.html">The access right, health apps, & APIs</a>” which explains some of these clarifications in context of APIs.

## Information Clarifications

### Entire Criterion

??? quote "*Clarifications included in the § 170.404 Certification Companion Guide (CCG) that apply to the entire criterion*"
$ref{404:CCG["Applies to Conditions and Maintenance of Certification Requirements"], tabbed}

*Additional Clarifications included to the § 170.404 Certification Companion Guide (CCG):*

 - Regarding the recommendation by commenters that the scope of “all data elements” include the Data Elements of the standard adopted in § 170.213 and FHIR resources referenced by the implementation specification adopted in § 170.215(a)(2), we note that both the standard and implementation specification are included in the interpretation of “all data elements of a patient's electronic health record to the extent permissible under applicable privacy laws” above. We note that this specific interpretation does not extend beyond the API Condition and Maintenance of Certification requirements finalized in § 170.404 and cannot be inferred to reduce the scope or applicability of other Cures Act Conditions of Certification or the <a target = "_blank" href = "https://www.ecfr.gov/cgi-bin/text-idx?SID=034c12732e5cb9328303ecdf94ecde87&mc=true&tpl=/ecfrbrowse/Title45/45cfr171_main_02.tpl">information blocking provisions</a> of the <a target = "_blank" href = "https://www.federalregister.gov/d/2020-07419/p-1665">ONC Cures Act Final Rule</a>, which include a larger scope of data.

### API Condition Of Certification General Requirements - § 170.404(A)(1)
???+ quote "**Regulation text at § 170.404(A)(1)**"
    (a) Condition of certification requirements—(1) General. A Certified API Developer must publish APIs and allow electronic health information from such technology to be accessed, exchanged, and used without special effort through the use of APIs or successor technology or standards, as provided for under applicable law, including providing access to all data elements of a patient's electronic health record to the extent permissible under applicable privacy laws.

??? quote "*Clarifications included in the § 170.404 Certification Companion Guide (CCG) that apply to paragraph § 170.404(A)(1)*"
$ref{404:CCG["(a) Conditions of certification requirements–(1) General."], tabbed}

### API Transparency Conditions - § 170.404(A)(2)
???+ quote "**Regulation text at § 170.404(A)(2)**"
    (2) Transparency conditions—(i) Complete business and technical documentation. A Certified API Developer must publish complete business and technical documentation, including the documentation described in paragraph (a)(2)(ii) of this section, via a publicly accessible hyperlink that allows any person to directly access the information without any preconditions or additional steps. (ii) Terms and conditions—(A) Material information. A Certified API Developer must publish all terms and conditions for its certified API technology, including any fees, restrictions, limitations, obligations, registration process requirements, or other similar requirements that would be: (1) Needed to develop software applications to interact with the certified API technology; (2) Needed to distribute, deploy, and enable the use of software applications in production environments that use the certified API technology; (3) Needed to use software applications, including to access, exchange, and use electronic health information by means of the certified API technology; (4) Needed to use any electronic health information obtained by means of the certified API technology; (5) Used to verify the authenticity of API Users; and (6) Used to register software applications. (B) API fees. Any and all fees charged by a Certified API Developer for the use of its certified API technology must be described in detailed, plain language. The description of the fees must include all material information, including but not limited to: (1) The persons or classes of persons to whom the fee applies; (2) The circumstances in which the fee applies; and (3) The amount of the fee, which for variable fees must include the specific variable(s) and methodology(ies) that will be used to calculate the fee.

??? quote "*Clarifications included in the § 170.404 Certification Companion Guide (CCG) that apply to paragraph § 170.404(A)(2)*"
$ref{404:CCG["(a) Conditions of certification requirements–(2) Transparency conditions."], tabbed}

### API Fees - General Conditions - § 170.404(A)(3)(I)
???+ quote "**Regulation text at § 170.404(A)(3)(I)**"
    (3) Fees conditions—(i) General conditions—(A) All fees. All fees related to certified API technology not otherwise permitted by this section are prohibited from being imposed by a Certified API Developer. The permitted fees in paragraphs (a)(3)(ii) and (iv) of this section may include fees that result in a reasonable profit margin in accordance with § 171.302. (B) Permitted fees requirements. For all permitted fees, a Certified API Developer must: (1) Ensure that such fees are based on objective and verifiable criteria that are uniformly applied to all similarly situated API Information Sources and API Users; (2) Ensure that such fees imposed on API Information Sources are reasonably related to the Certified API Developer's costs to supply certified API technology to, and if applicable, support certified API technology for, API Information Sources; (3) Ensure that such fees to supply and, if applicable, support certified API technology are reasonably allocated among all similarly situated API Information Sources; and (4) Ensure that such fees are not based on whether API Information Sources or API Users are competitors, potential competitors, or will be using the certified API technology in a way that facilitates competition with the Certified API Developer. (C) Prohibited fees. A Certified API Developer is prohibited from charging fees for the following: (1) Costs associated with intangible assets other than actual development or acquisition costs of such assets; (2) Opportunity costs unrelated to the access, exchange, or use of electronic health information; and (3) The permitted fees in this section cannot include any costs that led to the creation of intellectual property if the actor charged a royalty for that intellectual property pursuant to § 171.303 and that royalty included the development costs for the creation of the intellectual property. (D) Record-keeping requirements. A Certified API Developer must keep for inspection detailed records of any fees charged with respect to the certified API technology, the methodology(ies) used to calculate such fees, and the specific costs to which such fees are attributed.

??? quote "*Clarifications included in the § 170.404 Certification Companion Guide (CCG) that apply to paragraph § 170.404(A)(3)(I)*"
$ref{404:CCG["(a) Conditions of certification requirements–(3) Fees conditions–(i) General conditions."], tabbed}

*Additional Clarifications to the § 170.404 CCG:*

- A requirement in § 170.404(a)(3)(i)(A) states that permitted fees in paragraphs § 170.404(a)(3)(ii) and § 170.404(a)(3)(iv) may include fees that result in a reasonable profit margin in accordance with the information blocking Fees Exception finalized in § 171.302.
- Any fee that is not covered by an exception would be suspect under the <a target = "blank" href = "https://www.ecfr.gov/cgi-bin/text-idx?SID=034c12732e5cb9328303ecdf94ecde87&mc=true&tpl=/ecfrbrowse/Title45/45cfr171_main_02.tpl">information blocking provisions</a> established in the <a target = "_blank" href = "https://www.federalregister.gov/d/2020-07419/p-1665">ONC Cures Act Final Rule</a>, and would equally not be permitted by this API Condition of Certification requirement.
- Health IT developers are permitted to offer discounts to customers, as long as the discounted fees do not constitute information blocking and otherwise conform to ONC Cures Act Final Rule requirements as well as all other applicable laws.

### API Fees – Permitted Fee (Development, Deployment, Upgrades) - § 170.404(A)(3)(II)
???+ quote "**Regulation text at § 170.404(A)(3)(II)**"
    (ii) Permitted fee—development, deployment, and upgrades. A Certified API Developer is permitted to charge fees to an API Information Source to recover the costs reasonably incurred by the Certified API Developer to develop, deploy, and upgrade certified API technology.

??? quote "*Clarifications included in the § 170.404 Certification Companion Guide (CCG) that apply to paragraph § 170.404(A)(3)(II)*"
$ref{404:CCG["(a) Conditions of certification requirements–(3) Fees conditions–(ii) Permitted fee – development, deployment, and upgrades."], tabbed}

*Additional Clarifications to the § 170.404 CCG:*

- Should API Users stand to generate revenue from the use of their apps, any fee an API Information Source may impose would not be in scope for this Condition of Certification but would be subject to <a target = "_blank" href = "https://www.ecfr.gov/cgi-bin/text-idx?SID=034c12732e5cb9328303ecdf94ecde87&mc=true&tpl=/ecfrbrowse/Title45/45cfr171_main_02.tpl">information blocking provisions</a> established by the <a target = "_blank" href = "https://www.federalregister.gov/d/2020-07419/p-1665">ONC Cures Act Final Rule</a> if the API Information Source is a <a target = "_blank" href = "https://www.healthit.gov/cures/sites/default/files/cures/2020-03/InformationBlockingActors.pdf">“covered actor”</a> for purposes of information blocking. Accordingly, we emphasize that such stakeholders should take care to ensure they do not engage in <a target = "_blank" href = "https://www.ecfr.gov/cgi-bin/text-idx?SID=3b4dac3619b28e03f8d045691fae4fd5&mc=true&node=se45.2.171_1103&rgn=div8">information blocking</a> and are compliant with other Federal and State laws and regulations that may prohibit or limit certain types of relationships involving remuneration.

### API Fees – Permitted Fee (Recovering API Usage Costs) - § 170.404(A)(3)(III)
???+ quote "**Regulation text at § 170.404(A)(3)(III)**"
    (iii) Permitted fee—recovering API usage costs. A Certified API Developer is permitted to charge fees to an API Information Source related to the use of certified API technology. The fees must be limited to the recovery of incremental costs reasonably incurred by the Certified API Developer when it hosts certified API technology on behalf of the API Information Source.

??? quote "*Clarifications included in the § 170.404 Certification Companion Guide (CCG) that apply to paragraph § 170.404(A)(3)(III)*"
$ref{404:CCG["(a) Conditions of certification requirements–(3) Fees conditions–(iii) Permitted fee – recovering API usage costs."], tabbed}

### API Fees – Permitted Fee (Value-Added Services) - § 170.404(A)(3)(IV)
???+ quote "**Regulation text at § 170.404(A)(3)(IV)**"
    (iv) Permitted fee—value-added services. A Certified API Developer is permitted to charge fees to an API User for value-added services related to certified API technology, so long as such services are not necessary to efficiently and effectively develop and deploy production-ready software that interacts with certified API technology.

??? quote "*Clarifications included in the § 170.404 Certification Companion Guide (CCG) that apply to paragraph § 170.404(A)(3)(IV)*"
$ref{404:CCG["(a) Conditions of certification requirements–(3) Fees conditions–(iv) Permitted fee – value-added services."], tabbed}

### API Openness And Pro-Competitive Conditions - § 170.404(A)(4)
???+ quote "**Regulation text at § 170.404(A)(4)**"
    (4) Openness and pro-competitive conditions; general condition. A Certified API Developer must grant an API Information Source the independent ability to permit an API User to interact with the certified API technology deployed by the API Information Source. (i) Nondiscrimination. (A) A Certified API Developer must provide certified API technology to an API Information Source on terms that are no less favorable than it provides to itself and its own customers, suppliers, partners, and other persons with whom it has a business relationship. (B) The terms on which a Certified API Developer provides certified API technology must be based on objective and verifiable criteria that are uniformly applied to all substantially similar or similarly situated classes of persons and requests. (C) A Certified API Developer must not offer different terms or services based on: (1) Whether a competitive relationship exists or would be created; (2) The revenue or other value that another party may receive from using the API technology. (ii) Rights to access and use certified API technology— (A) Rights that must be granted. A Certified API Developer must have and, upon request, must grant to API Information Sources and API Users all rights that may be reasonably necessary to: (1) Access and use the Certified API Developer's certified API technology in a production environment; (2) Develop products and services that are designed to interact with the Certified API Developer's certified API technology; and (3) Market, offer, and distribute products and services associated with the Certified API Developer's certified API technology. (B) Prohibited conduct. A Certified API Developer is prohibited from conditioning the receipt of the rights described in paragraph (a)(4)(ii)(A) of this section on: (1) Receiving a fee, including but not limited to a license fee, royalty, or revenue-sharing arrangement; (2) Agreeing to not compete with the Certified API Developer in any product, service, or market; (3) Agreeing to deal exclusively with the Certified API Developer in any product, service, or market; (4) Obtaining additional licenses, products, or services that are not related to or can be unbundled from the certified API technology; (5) Licensing, granting, assigning, or transferring any intellectual property to the Certified API Developer; (6) Meeting any Certified API Developer-specific testing or certification requirements; and (7) Providing the Certified API Developer or its technology with reciprocal access to application data. (iii) Service and support obligations. A Certified API Developer must provide all support and other services reasonably necessary to enable the effective development, deployment, and use of certified API technology by API Information Sources and API Users in production environments. (A) Changes and updates to certified API technology. A Certified API Developer must make reasonable efforts to maintain the compatibility of its certified API technology and to otherwise avoid disrupting the use of certified API technology in production environments. (B) Changes to terms and conditions. Except as exigent circumstances require, prior to making changes to its certified API technology or to the terms and conditions thereof, a Certified API Developer must provide notice and a reasonable opportunity for API Information Sources and API Users to update their applications to preserve compatibility with certified API technology and to comply with applicable terms and conditions.

??? quote "*Clarifications included in the § 170.404 Certification Companion Guide (CCG) that apply to paragraph § 170.404(A)(4)*"
$ref{404:CCG["(a) Conditions of certification requirements–(4) Openness and pro-competitive conditions."], tabbed}

### API Maintenance Of Certification Requirements - § 170.404(B)(1)
???+ quote "**Regulation text at § 170.404(B)(1)**"
    (b) Maintenance of certification requirements—(1) Authenticity verification and registration for production use. The following apply to a Certified API Developer with a Health IT Module certified to the certification criterion adopted in § 170.315(g)(10): (i) Authenticity verification. A Certified API Developer is permitted to institute a process to verify the authenticity of API Users so long as such process is objective and the same for all API Users and completed within ten business days of receipt of an API User's request to register their software application for use with the Certified API Developer's Health IT Module certified to § 170.315(g)(10). (ii) Registration for production use. A Certified API Developer must register and enable all applications for production use within five business days of completing its verification of an API User's authenticity, pursuant to paragraph (b)(1)(i) of this section.

??? quote "*Clarifications included in the § 170.404 Certification Companion Guide (CCG) that apply to paragraph § 170.404(B)(1)*"
$ref{404:CCG["(b) Maintenance of certification requirements—(1) Authenticity verification and registration for production use."], tabbed}

### API Service Base URL Publication - § 170.404(B)(2)
???+ quote "**Regulation text at § 170.404(B)(2)**"
    (2) Service base URL publication. A Certified API Developer must publish the service base URLs for all Health IT Modules certified to § 170.315(g)(10) that can be used by patients to access their electronic health information. The Certified API Developer must publicly publish the service base URLs: (i) For all of its customers regardless of whether the Health IT Modules certified to § 170.315(g)(10) are centrally managed by the Certified API Developer or locally deployed by an API Information Source; and (ii) In a machine-readable format at no charge.

??? quote "*Clarifications included in the § 170.404 Certification Companion Guide (CCG) that apply to paragraph § 170.404(B)(2)*"
$ref{404:CCG["(b) Maintenance of certification requirements—(2) Service base URL publication."], tabbed}

### Rollout Of (G)(10)-Certifies APIs - § 170.404(B)(3)
???+ quote "**Regulation text at § 170.404(B)(2)**"
    (3) Rollout of (g)(10)-certified APIs. A Certified API Developer with certified API technology previously certified to the certification criterion in § 170.315(g)(8) must provide all API Information Sources with such certified API technology deployed with certified API technology certified to the certification criterion in § 170.315(g)(10) by no later than December 31, 2022.

??? quote "*Clarifications included in the § 170.404 Certification Companion Guide (CCG) that apply to paragraph § 170.404(B)(3)*"
$ref{404:CCG["(b) Maintenance of certification requirements—(3) Rollout of (g)(10)-certified APIs."], tabbed}

### Compliance For Existing Certified API Technology - § 170.404(B)(4)
???+ quote "**Regulation text at § 170.404(B)(4)**"
    (4) Compliance for existing certified API technology. By no later than April 5, 2021, a Certified API Developer with Health IT Module(s) certified to the certification criteria in § 170.315(g)(7), (8), or (9) must comply with paragraph (a) of this section, including revisions to their existing business and technical API documentation and make such documentation available via a publicly accessible hyperlink that allows any person to directly access the information without any preconditions or additional steps.

??? quote "*Clarifications included in the § 170.404 Certification Companion Guide (CCG) that apply to paragraph § 170.404(B)(4)*"
$ref{404:CCG["(b) Maintenance of certification requirements—(4) Compliance for existing certified API technology."], tabbed}

### Definitions - § 170.404(C)
???+ quote "**Regulation text at § 170.404(C)**"
    (c) Definitions. The following definitions apply to this section: API Information Source means an organization that deploys certified API technology created by a “Certified API Developer;” API User means a person or entity that creates or uses software applications that interact with the “certified API technology” developed by a “Certified API Developer” and deployed by an “API Information Source;” Certified API Developer means a health IT developer that creates the “certified API technology” that is certified to any of the certification criteria adopted in § 170.315(g)(7) through (10); and Certified API technology means the capabilities of Health IT Modules that are certified to any of the API-focused certification criteria adopted in § 170.315(g)(7) through (10).

??? quote "*Clarifications included in the § 170.404 Certification Companion Guide (CCG) that apply to paragraph § 170.404(C)*"
$ref{404:CCG["(c) Definitions."], tabbed}

--8<-- "includes/abbreviations.md"