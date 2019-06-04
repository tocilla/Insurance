# Insurance API
## Version: v1

**Contact information:**  
enistocilla@gmail.com  

**License:** MIT License

### Security
**Basic**  

|basic|*Basic*|
|---|---|

### /auth/login/

#### POST
##### Description:

Check the credentials and return the REST Token
if the credentials are valid and authenticated.
Calls Django Auth login method to register User ID
in Django session framework

Accept the following POST parameters: username, password
Return the REST Framework Token Object's key.

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| data | body |  | Yes | [Login](#login) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 201 |  | [Login](#login) |

### /auth/logout/

#### GET
##### Summary:

Calls Django logout method and delete the Token object
assigned to the current User object.

##### Description:

Accepts/Returns nothing.

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

#### POST
##### Summary:

Calls Django logout method and delete the Token object
assigned to the current User object.

##### Description:

Accepts/Returns nothing.

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |

##### Responses

| Code | Description |
| ---- | ----------- |
| 201 |  |

### /auth/password/change/

#### POST
##### Summary:

Calls Django Auth SetPasswordForm save method.

##### Description:

Accepts the following POST parameters: new_password1, new_password2
Returns the success/fail message.

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| data | body |  | Yes | [PasswordChange](#passwordchange) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 201 |  | [PasswordChange](#passwordchange) |

### /auth/password/reset/

#### POST
##### Summary:

Calls Django Auth PasswordResetForm save method.

##### Description:

Accepts the following POST parameters: email
Returns the success/fail message.

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| data | body |  | Yes | [PasswordReset](#passwordreset) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 201 |  | [PasswordReset](#passwordreset) |

### /auth/password/reset/confirm/

#### POST
##### Summary:

Password reset e-mail link is confirmed, therefore
this resets the user's password.

##### Description:

Accepts the following POST parameters: token, uid,
    new_password1, new_password2
Returns the success/fail message.

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| data | body |  | Yes | [PasswordResetConfirm](#passwordresetconfirm) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 201 |  | [PasswordResetConfirm](#passwordresetconfirm) |

### /auth/user/

#### GET
##### Summary:

Reads and updates UserModel fields
Accepts GET, PUT, PATCH methods.

##### Description:

Default accepted fields: username, first_name, last_name
Default display fields: pk, username, email, first_name, last_name
Read-only fields: pk, email

Returns UserModel fields.

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [UserDetails](#userdetails) |

#### PUT
##### Summary:

Reads and updates UserModel fields
Accepts GET, PUT, PATCH methods.

##### Description:

Default accepted fields: username, first_name, last_name
Default display fields: pk, username, email, first_name, last_name
Read-only fields: pk, email

Returns UserModel fields.

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| data | body |  | Yes | [UserDetails](#userdetails) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [UserDetails](#userdetails) |

#### PATCH
##### Summary:

Reads and updates UserModel fields
Accepts GET, PUT, PATCH methods.

##### Description:

Default accepted fields: username, first_name, last_name
Default display fields: pk, username, email, first_name, last_name
Read-only fields: pk, email

Returns UserModel fields.

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| data | body |  | Yes | [UserDetails](#userdetails) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [UserDetails](#userdetails) |

### /risk_types/

#### GET
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| page | query | A page number within the paginated result set. | No | integer |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | object |

#### POST
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| data | body |  | Yes | [RiskType](#risktype) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 201 |  | [RiskType](#risktype) |

### /risk_types/{id}/

#### GET
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this risk type. | Yes | integer |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [RiskType](#risktype) |

### /risks/

#### GET
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| page | query | A page number within the paginated result set. | No | integer |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | object |

#### POST
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| data | body |  | Yes | [Risk](#risk) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 201 |  | [Risk](#risk) |

### /risks/{id}/

#### GET
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this risk. | Yes | integer |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [Risk](#risk) |

#### PUT
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this risk. | Yes | integer |
| data | body |  | Yes | [Risk](#risk) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [Risk](#risk) |

#### PATCH
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this risk. | Yes | integer |
| data | body |  | Yes | [Risk](#risk) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [Risk](#risk) |

#### DELETE
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this risk. | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 204 |  |

### Models


#### Login

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| username | string |  | No |
| email | string (email) |  | No |
| password | string |  | Yes |

#### PasswordChange

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| new_password1 | string |  | Yes |
| new_password2 | string |  | Yes |

#### PasswordReset

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| email | string (email) |  | Yes |

#### PasswordResetConfirm

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| new_password1 | string |  | Yes |
| new_password2 | string |  | Yes |
| uid | string |  | Yes |
| token | string |  | Yes |

#### UserDetails

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| pk | integer |  | No |
| username | string | Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. | Yes |
| email | string (email) |  | No |
| first_name | string |  | No |
| last_name | string |  | No |

#### RiskFieldOption

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| content | string |  | Yes |

#### RiskField

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| id | integer |  | No |
| name | string |  | Yes |
| type | string |  | Yes |
| field_options | [ [RiskFieldOption](#riskfieldoption) ] |  | No |
| required | boolean |  | No |

#### RiskType

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| id | integer |  | No |
| name | string |  | Yes |
| description | string |  | Yes |
| risk_fields | [ [RiskField](#riskfield) ] |  | Yes |
| active | boolean |  | No |
| created_at | dateTime |  | No |

#### RiskInput

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| risk_field | integer |  | Yes |
| value | string |  | No |

#### Risk

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| id | integer |  | No |
| name | string |  | Yes |
| risk_type | integer |  | Yes |
| risk_inputs | [ [RiskInput](#riskinput) ] |  | Yes |
| created_at | dateTime |  | No |