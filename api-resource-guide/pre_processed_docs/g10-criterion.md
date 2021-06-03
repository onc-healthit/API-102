# Standardized API Certification Criterion at § 170.315(g)(10)

This section considers the standardized API for patient and population services certification criterion, including all of the content contained in the ONC Cures Act Final Rule API preamble, the IFC API preamble, and the regulation paragraphs in § 170.315(g)(10).

## Summary
- The criterion defined at § 170.315(g)(10) requires certified Health IT Modules to support: 
    - Standardized HL7 FHIR-based API for single patient services
    - Standardized HL7 FHIR-based API for multiple patient services

### *Applicability*
170.315(g)(10) is for all health IT developers who are certifying to the EHR base definition. The API certification criterion finalized in § 170.315(g)(10) was included as part of the EHR Base Definition at § 170.102. While developers of health information technology are not required by the ONC to meet certification requirements, including certification requirements that are included as part of the EHR Base Definition, several federal, state and tribal entities, including Centers for Medicare & Medicaid Services, Centers for Disease Control and Prevention, and other programs reference the ONC Health IT Certification Program and require the use of certified health IT for program participation.

## Tools for testing and certification

- **Inferno Program Edition**
    - The Inferno Program Edition is used for (g)(10) API testing for the ONC Health IT Certification Program. The Inferno Program Edition is a streamlined testing tool for services seeking to meet the requirements of the Standardized API for Patient and Population Services criterion finalized at § 170.315(g)(10). It is based on the requirements in the ONC Cures Act Final Rule and associated test procedure for § 170.315(g)(10). This tool is used for testing and certification to the § 170.315(g)(10) certification criterion for the ONC Health IT Certification Program.

## Technical Explanations and Clarifications 
### Applies to Entire Criterion
*Clarifications Included in (g)(10) Certification Companion Guide (CCG):*

$ref(g-10:CCG["Applies to Entire Criterion"])

*Additional Clarifications to the (g)(10) CCG:*

!!! example "Examples of “must support” in the US Core IG 3.1.1:"
    In US Core 3.1.1, the profile element Observation.value[x] contains the following Choices:
    `Quantity, CodeableConcept, string, boolean, integer, Range, Ratio, SampledData, time, dateTime, Period`
    A Health IT Module must support at least one of these Choices via the (g)(10) standardized API.

    In US Core 3.1.1, the profile element Provenance.agent.who contains the following References:
    `US Core Practitioner Profile, US Core Patient Profile, US Core Organization Profile`
    A Health IT Module must support at least one of these References via the (g)(10) standardized API.

### Data Response (Single Patient) - § 170.315(g)(10)(i)(A)
**Regulation text**: (i) Data response. (A) Respond to requests for a single patient's data according to the standard adopted in § 170.215(a)(1) and implementation specification adopted in § 170.215(a)(2), including the mandatory capabilities described in “US Core Server CapabilityStatement,” for each of the data included in the standard adopted in § 170.213. All data elements indicated as “mandatory” and “must support” by the standards and implementation specifications must be supported.

*Clarifications Included in (g)(10) Certification Companion Guide (CCG):*

$ref(g-10:CCG["Paragraph (10)(i)(A)"])

### Data Response (Multiple Patients) - § 170.315(g)(10)(i)(B)
**Regulation text**: (B) Respond to requests for multiple patients' data as a group according to the standard adopted in § 170.215(a)(1), and implementation specifications adopted in § 170.215(a)(2) and (4), for each of the data included in the standard adopted in § 170.213. All data elements indicated as “mandatory” and “must support” by the standards and implementation specifications must be supported.

*Clarifications Included in (g)(10) Certification Companion Guide (CCG):*

$ref(g-10:CCG["Paragraph (10)(i)(B)"])

### Supported Search Operations (Single Patient) - § 170.315(g)(10)(ii)(A)
**Regulation text**: (ii) Supported search operations. (A) Respond to search requests for a single patient's data consistent with the search criteria included in the implementation specification adopted in § 170.215(a)(2), specifically the mandatory capabilities described in “US Core Server CapabilityStatement.”

*Clarifications Included in (g)(10) Certification Companion Guide (CCG):*

$ref(g-10:CCG["Paragraph (10)(ii)(A)"])

### Supported Search Operations (Multiple Patients) - § 170.315(g)(10)(ii)(B)
**Regulation text**: (B) Respond to search requests for multiple patients' data consistent with the search criteria included in the implementation specification adopted in § 170.215(a)(4)

*Clarifications Included in (g)(10) Certification Companion Guide (CCG):*

$ref(g-10:CCG["Paragraph (10)(ii)(B)"])

*Additional Clarifications*:

- The scope of data available in the data responses defined in § 170.315(g)(10)(i) must be supported for searches for multiple patients via the supported search operations finalized in § 170.315(g)(10)(ii).
- The HL7 FHIR Bulk Data Access (Flat FHIR) (v1.0.0: STU 1) implementation specification adopted in § 170.215(a)(4) includes mandatory support for the “group-export” “OperationDefinition.”

### Application Registration - § 170.315(g)(10)(iii)
**Regulation text**: (iii) Application registration. Enable an application to register with the Health IT Module's “authorization server.”

*Clarifications Included in (g)(10) Certification Companion Guide (CCG):*

$ref(g-10:CCG["Paragraph (10)(iii)"])

### Secure Connection (Patient / User Scopes) - § 170.315(g)(10)(iv)(A)
**Regulation text**: (iv) Secure connection. (A) Establish a secure and trusted connection with an application that requests data for patient and user scopes in accordance with the implementation specifications adopted in § 170.215(a)(2) and (3).

*Clarifications Included in (g)(10) Certification Companion Guide (CCG):*

$ref(g-10:CCG["Paragraph (10)(iv)(A)"])

### Secure Connection (System Scopes) - § 170.315(g)(10)(iv)(B)
**Regulation text**: (B) Establish a secure and trusted connection with an application that requests data for system scopes in accordance with the implementation specification adopted in § 170.215(a)(4).

*Clarifications Included in (g)(10) Certification Companion Guide (CCG):*

$ref(g-10:CCG["Paragraph (10)(iv)(B)"])

### First-time Authentication / Authorization for Single Patient Services - § 170.315(g)(10)(V)(A)(1)
**Regulation text**: (v) Authentication and authorization—(A) Authentication and authorization for patient and user scopes—(1) First time connections—(i) Authentication and authorization must occur during the process of granting access to patient data in accordance with the implementation specification adopted in § 170.215(a)(3) and standard adopted in § 170.215(b). (ii) A Health IT Module's authorization server must issue a refresh token valid for a period of no less than three months to applications capable of storing a client secret. (iii) A Health IT Module's authorization server must issue a refresh token for a period of no less than three months to native applications capable of securing a refresh token.

*Clarifications Included in (g)(10) Certification Companion Guide (CCG):*

$ref(g-10:CCG["Paragraph (10)(v)(A)(1)"])

### Subsequent Authentication / Authorization for Single Patient Services - § 170.315(g)(10)(V)(A)(2)
**Regulation text**: (2) Subsequent connections. (i) Access must be granted to patient data in accordance with the implementation specification adopted in § 170.215(a)(3) without requiring reauthorization and re-authentication when a valid refresh token is supplied by the application. (ii) A Health IT Module's authorization server must issue a refresh token valid for a new period of no less than three months to applications capable of storing a client secret.

*Clarifications Included in (g)(10) Certification Companion Guide (CCG):*

$ref(g-10:CCG["Paragraph (10)(v)(A)(2)"])

### Authentication / Authorization for Multiple Patient Services - § 170.315(g)(10)(V)(B)
**Regulation text**: (B) Authentication and authorization for system scopes. Authentication and authorization must occur during the process of granting an application access to patient data in accordance with the “SMART Backend Services: Authorization Guide” section of the implementation specification adopted in § 170.215(a)(4) and the application must be issued a valid access token.

*Clarifications Included in (g)(10) Certification Companion Guide (CCG):*

$ref(g-10:CCG["Paragraph (10)(v)(B)"])

### Patient Authorization Revocation - § 170.315(g)(10)(VI)
**Regulation text**: (vi) Patient authorization revocation. A Health IT Module's authorization server must be able to revoke an authorized application's access at a patient's direction.

*Clarifications Included in (g)(10) Certification Companion Guide (CCG):*

$ref(g-10:CCG["Paragraph (10)(vi)"])

### Token Introspection - § 170.315(g)(10)(VII)
**Regulation text**: (vii) Token introspection. A Health IT Module's authorization server must be able to receive and validate tokens it has issued.

*Clarifications Included in (g)(10) Certification Companion Guide (CCG):*

$ref(g-10:CCG["Paragraph (10)(vii)"])

### Technical API Documentation Content - § 170.315(g)(10)(VIII)(A)
**Regulation text**: (viii) Documentation. (A) The API(s) must include complete accompanying documentation that contains, at a minimum: (1) API syntax, function names, required and optional parameters supported and their data types, return variables and their types/structures, exceptions and exception handling methods and their returns. (2) The software components and configurations that would be necessary for an application to implement in order to be able to successfully interact with the API and process its response(s). (3) All applicable technical requirements and attributes necessary for an application to be registered with a Health IT Module's authorization server.

*Clarifications Included in (g)(10) Certification Companion Guide (CCG):*

$ref(g-10:CCG["Paragraph (10)(viii)(A)"])

### Technical API Documentation Availability - § 170.315(g)(10)(VIII)(B)
**Regulation text**: (B) The documentation used to meet paragraph (g)(10)(viii)(A) of this section must be available via a publicly accessible hyperlink without any preconditions or additional steps.

*Clarifications Included in (g)(10) Certification Companion Guide (CCG):*

$ref(g-10:CCG["Paragraph (10)(viii)(B)"])

### *Other standards not directly referenced in § 170.315(g)(10)*

#### Bulk FHIR Import
We have not included a requirement for Bulk FHIR import because the standards for these features are still being developed by industry. Applications or systems seeking to import information formatting according to the HL7® FHIR Bulk Data Access (Flat FHIR) (V1.0.0:STU 1) can use several methods developed by industry, or can refer to Bulk FHIR import methods being defined by HL7 at the HL7 FHIR Bulk Data GitHub page.

## Test Procedures
### Paragraph (g)(10)(iii) – Application registration
**Application Registration**

1. The health IT developer demonstrates the Health IT Module supports application registration with an authorization server for the purposes of Electronic Health Information (EHI) access for single patients, including support for application registration functions to enable authentication and authorization in § 170.315(g)(10)(v).
1. The health IT developer demonstrates the Health IT Module supports application registration with an authorization server for the purposes of EHI access for multiple patients including support for application registration functions to enable authentication and authorization in § 170.315(g)(10)(v).

### Paragraph (g)(10)(iv) – Secure connection
**Secure connection**

--8<-- "includes/abbreviations.md"