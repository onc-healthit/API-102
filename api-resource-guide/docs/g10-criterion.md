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

## Certification Companion Guide clarifications
*Clarifications Included in (g)(10) Certification Companion Guide (CCG):*

- On December 31, 2022, the API certification criterion in § 170.315(g)(10) replaces the “application access—data category request” certification criterion (§ 170.315(g)(8)).
- Health IT Modules are not required to support patient-facing API-enabled “read” services for multiple patients for the purposes of this certification criterion.
- The clinical note text included in any of the notes described in the “Clinical Notes Guidance” section of the US Core IG adopted in § 170.215(a)(2) must be represented in a “plain text” form, and it would be unacceptable for the note text to be converted to another file or format (e.g., .docx, PDF) when it is provided as part of an API response. The intent of this policy is to prohibit Health IT Modules from converting clinical notes from a “machine readable” format to a non-“machine readable” format (e.g., PDF). Clinical note text that originates from outside Health IT Modules should be exchanged using its original format. Additionally, “plain text” does not necessarily mean the FHIR “contentType” “text/plain.”
- The US Core IG (3.1.1) Profile “StructureDefinition-us-core-patient” element “name.suffix” is required for testing and certification in the ONC Health IT Certification Program to meet the USCDI requirement to support the “Patient Demographics” Data Class: “Suffix” Data Element.
- Either the US Core IG (3.1.1) Profile “StructureDefinition-us-core-patient” element “name.period” or “name.use” is required for testing and certification in the ONC Health IT Certification Program to meet the USCDI requirement to support the “Patient Demographics” Data Class: “Previous Name” Data Element.
- A Health IT Module must support at least one Choice or Reference for US Core IG “must support” elements with multiple Choices or References, respectively.

!!! example "Examples of “must support” in the US Core IG 3.1.1:"
    In US Core 3.1.1, the profile element Observation.value[x] contains the following Choices:
    `Quantity, CodeableConcept, string, boolean, integer, Range, Ratio, SampledData, time, dateTime, Period`
    A Health IT Module must support at least one of these Choices via the (g)(10) standardized API.

    In US Core 3.1.1, the profile element Provenance.agent.who contains the following References:
    `US Core Practitioner Profile, US Core Patient Profile, US Core Organization Profile`
    A Health IT Module must support at least one of these References via the (g)(10) standardized API.

- A Health IT Module must be conformant to the US Core IG for all Choices and References included in its standardized API, and cannot misrepresent Choices via the standardized API (e.g. a Health IT Module cannot transform “integer” values to “string” values).
- A health IT developer must document which US Core IG Choices and References are supported by their Health IT Module via public technical documentation to meet the requirements in § 170.315(g)(10)(viii) and the transparency conditions in § 170.404(a)(2).

### *Other standards not directly referenced in § 170.315(g)(10)*

#### Bulk FHIR Import
We have not included a requirement for Bulk FHIR import because the standards for these features are still being developed by industry. Applications or systems seeking to import information formatting according to the HL7® FHIR Bulk Data Access (Flat FHIR) (V1.0.0:STU 1) can use several methods developed by industry, or can refer to Bulk FHIR import methods being defined by HL7 at the HL7 FHIR Bulk Data GitHub page.



--8<-- "includes/abbreviations.md"