# (g)(10) Certification Criteria Support Documentation

## Paragraph (g)(10)(iii) - Application registration
<table>
	<tr>
		<th>System Under Test</th>
	</tr>
	<tr>
		<td>
			<ol>
				<u><b>Application Registration</b></u>
				<li>The health IT developer demonstrates the Health IT Module supports application registration with an authorization server for the purposes of Electronic Health Information (EHI) access for single patients, including support for application registration functions to enable authentication and authorization in § 170.315(g)(10)(v).</li>
				<li>The health IT developer demonstrates the Health IT Module supports application registration with an authorization server for the purposes of EHI access for multiple patients including support for application registration functions to enable authentication and authorization in § 170.315(g)(10)(v).</li>
			</ol>
		</td>
	</tr>
</table>

## Paragraph (g)(10)(iv) – Secure connection
<table>
	<tr>
		<th>System Under Test</th>
	</tr>
	<tr>
		<td>
			<ol>
				<u><b>Secure Connection</b></u>
				<li>For all transmissions between the Health IT Module and the application, the health IT developer demonstrates the use of a secure and trusted connection in accordance with the implementation specifications adopted in § 170.215(a)(2) and § 170.215(a)(3), including:
					<ul>
						<li>Using TLS version 1.2 or higher; and</li>
						<li>Conformance to FHIR Communications Security requirements.</li>
					</ul>
				</li>
			</ol>
		</td>
	</tr>
</table>


# This is why this is so important!!
## Paragraph (g)(10)(v)(A) – Authentication and authorization for patient and user scopes
<table>
	<tr>
		<th>System Under Test</th>
	</tr>
	<tr>
		<td>
			<ol>
				<u><b>Authentication and Authorization for Patient and User Scopes</b></u>
				<li>The health IT developer demonstrates the ability of the Health IT Module to support the following for "EHR-Launch," "Standalone-Launch," and "Both" ("EHR-Launch" and "Standalone-Launch") as specified in the implementation specification adopted in § 170.215(a)(3).</li>
				<li>[EHR-Launch] The health IT developer demonstrates the ability of the Health IT Module to initiate a "launch sequence" using the "launch-ehr" "SMART on FHIR Core Capability" SMART EHR Launch mode detailed in the implementation specification adopted in § 170.215(a)(3), including:
					<ul>
						<li>Launching the registered launch URL of the application; and</li>
						<li>Passing the parameters: "iss" and "launch".</li>
					</ul>
				</li>
				<li>[Standalone-Launch] The health IT developer demonstrates the ability of the Health IT Module to launch using the "launch-standalone" "SMART on FHIR Core Capability" SMART Standalone Launch mode detailed in the implementation specification adopted in § 170.215(a)(3).</li>
				<li>[Standalone-Launch] The health IT developer demonstrates the ability of the Health IT Module to support SMART’s public client profile.</li>
				<li>[Both] The health IT developer demonstrates the ability of the Health IT Module to support the following as detailed in the implementation specification adopted in § 170.215(a)(3) and standard adopted in § 170.215(a)(1):
					<ul>
						<li>The ".well-known/smart-configuration.json" path; and</li>
						<li>A FHIR "CapabilityStatement".</li>
					</ul>
				</li>
				<li>[Both] The health IT developer demonstrates the ability of the ".well-known/smart-configuration.json" path to support at least the following as detailed in the implementation specification adopted in § 170.215(a)(3):
					<ul>
						<li>"authorization_endpoint";</li>
						<li>"token_endpoint"; and</li>
						<li>"capabilities" (including support for all the "SMART on FHIR Core Capabilities").</li>
					</ul>
				</li>
				<li>[Both] The health IT developer demonstrates the ability of the FHIR "CapabilityStatement" to support at least the following components as detailed in the implementation specification adopted in § 170.215(a)(3) and standard adopted in § 170.215(a)(1), including:
					<ul>
						<li>"authorize"; and</li>
						<li>"token".</li>
					</ul>
				</li>
				<li>[Both] The health IT developer demonstrates the ability of the Health IT Module to receive an authorization request according to the implementation specification adopted in § 170.215(a)(3), including support for the following parameters:
					<ul>
						<li>"response_type";</li>
						<li>"client_id";</li>
						<li>"redirect_uri";</li>
						<li>"launch" (for EHR-Launch mode only);</li>
						<li>"scope";</li>
						<li>"state"; and</li>
						<li>"aud".</li>
					</ul>
				</li>
				<li>[Both] The health IT developer demonstrates the ability of the Health IT Module to support the receipt of the following scopes and capabilities according to the implementation specification adopted in § 170.215(a)(3) and standard adopted in § 170.215(b):
					<ul>
						<li>"openid" (to support "sso-openid-connect" "SMART on FHIR Core Capability");</li>
						<li>"fhirUser" (to support "sso-openid-connect" "SMART on FHIR Core Capability");</li>
						<li>"need_patient_banner" (to support "context-banner" "SMART on FHIR Core Capability" for EHR-Launch mode only);</li>
						<li>"smart_style_url" (to support "context-style" "SMART on FHIR Core Capability" for EHR-Launch mode only);</li>
						<li>"launch/patient" (to support "context-standalone-patient" "SMART on FHIR Core Capability" for Standalone-Launch mode only);</li>
						<li>"launch" (for EHR-Launch mode only);</li>
						<li>"offline_access" (to support "permission-offline" "SMART on FHIR Core Capability");</li>
						<li>Patient-level scopes (to support "permission-patient" "SMART on FHIR Core Capability"); and</li>
						<li>User-level scopes (to support "permission-user" "SMART on FHIR Core Capability").</li>
					</ul>
				</li>
				<li>[Both] The health IT developer demonstrates the ability of the Health IT Module to evaluate the authorization request and request end-user input, if applicable (required for patient-facing applications), including the ability for the end-user to authorize an application to receive EHI based on FHIR resource-level scopes for all of the FHIR resources associated with the profiles specified in the standard adopted in § 170.213 and implementation specification adopted in § 170.215(a)(2), including:
					<ul>
						<li>"AllergyIntolerance";</li>
						<li>"CarePlan";</li>
						<li>"CareTeam";</li>
						<li>"Condition";</li>
						<li>"Device";</li>
						<li>"DiagnosticReport";</li>
						<li>"DocumentReference";</li>
						<li>"Goal";</li>
						<li>"Immunization";</li>
						<li>"Medication" (if supported);</li>
						<li>"MedicationRequest";</li>
						<li>"Observation";</li>
						<li>"Patient";</li>
						<li>"Procedure"; and</li>
						<li>"Provenance".</li>
					</ul>
				</li>
				<li>[Both] The health IT developer demonstrates the ability of Health IT Module to evaluate the authorization request and request end-user input, if applicable (required for patient-facing applications), including the ability for the end-user to explicitly enable the "offline_access" scope according to the implementation specification adopted in § 170.215(a)(3).</li>
				<li>[Both] The health IT developer demonstrates the ability of the Health IT Module to deny an application’s authorization request according to a patient’s preferences selected in steps 10 and 11 of this section in accordance with the implementation specification adopted in § 170.215(a)(3).</li>
				<li>[Both] The health IT developer demonstrates the ability of the Health IT Module to return an error response if the following parameters provided by an application to the Health IT Module in step 8 of this section do not match the parameters originally provided to an application by the Health IT Module in step 2 of this section according to the implementation specification adopted in § 170.215(a)(3):
					<ul>
						<li>"launch" (for EHR-Launch mode only); and</li>
						<li>"aud".</li>
					</ul>
				</li>
				<li>[Both] The health IT developer demonstrates the ability of the Health IT Module to grant an application access to EHI by returning an authorization code to the application according to the implementation specification adopted in § 170.215(a)(3), including the following parameters:
					<ul>
						<li>"code"; and</li>
						<li>"state".</li>
					</ul>
				</li>
				<li>[Both] The health IT developer demonstrates the ability of the Health IT Module to receive the following parameters from an application according to the implementation specification adopted in § 170.215(a)(3):
					<ul>
						<li>"grant_type";</li>
						<li>"code";</li>
						<li>"redirect_uri";</li>
						<li>"client_id"; and</li>
						<li>Authorization header including "client_id" and "client_secret".</li>
					</ul>
				</li>
				<li>[Both] The health IT developer demonstrates the ability of the Health IT Module to return a JSON object to applications according to the implementation specification adopted in § 170.215(a)(3) and standard adopted in § 170.215(b), including the following:
					<ul>
						<li>"access_token";</li>
						<li>"token_type";</li>
						<li>"scope";</li>
						<li>"id_token";</li>
						<li>"refresh_token" (valid for a period of no shorter than three months);</li>
						<li>HTTP "Cache-Control" response header field with a value of "no-store";</li>
						<li>HTTP "Pragma" response header field with a value of "no-cache";</li>
						<li>"patient" (to support "context-ehr-patient" and "context-standalone-patient" "SMART on FHIR Core Capabilities");</li>
						<li>"need_patient_banner" (to support "context-banner" "SMART on FHIR Core Capability" for EHR-Launch mode only); and</li>
						<li>"smart_style_url" (to support "context-style" "SMART on FHIR Core Capability" for EHR-Launch mode only).</li>
					</ul>
				</li>
				<li>[Both] The health IT developer demonstrates the ability of the Health IT Module to provide an OpenID Connect well-known URI in accordance with the implementation specification adopted in § 170.215(b), including:
					<ul>
						<li>All required fields populated according to implementation specification adopted in § 170.215(b); and</li>
						<li>Valid JWKS populated according to implementation specification can be retrieved via JWKS URI</li>
					</ul>
				</li>
				<li>[Both] The health IT developer demonstrates the ability of the Health IT Module to deny an application’s authorization request in accordance with the implementation specification adopted in § 170.215(a)(3).</li>
				<li>[Standalone-Launch] The health IT developer demonstrates the ability of the Health IT Module to return a "Patient" FHIR resource that matches the patient context provided in step 9 of this section according to the implementation specification adopted in § 170.215(a)(2).</li>
				<li>[Both] The health IT developer demonstrates the ability of the Health IT Module to grant an access token when a refresh token is supplied according to the implementation specification adopted in § 170.215(a)(2).</li>
				<li>[Both] The health IT developer demonstrates the ability of the Health IT Module to grant a refresh token valid for a period of no less than three months to native applications capable of storing a refresh token.</li>
				<u><b>Subsequent Connections: Authentication and Authorization for Patient and User Scopes</b></u>
				<li>The health IT developer demonstrates the ability of the Health IT Module to issue a new refresh token valid for a period of no shorter than three months without requiring re-authentication and re-authorization when a valid refresh token is supplied by the application according to the implementation specification adopted in § 170.215(a)(3).</li>
				<li>The health IT developer demonstrates the ability of the Health IT Module to return an error response when supplied an invalid refresh token as specified in the implementation specification adopted in § 170.215(a)(3).</li>
			</ol>
		</td>
	</tr>
</table>