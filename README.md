# liveagent_api

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 3.0.0
- Package version: 1.0.0
- Build date: 2017-02-14T13:30:20.529+01:00
- Build package: class io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/YOUR_GIT_USR_ID/YOUR_GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/YOUR_GIT_USR_ID/YOUR_GIT_REPO_ID.git`)

Then import the package:
```python
import liveagent_api 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import liveagent_api
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
import time
import liveagent_api
from liveagent_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: privileges
liveagent_api.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# create an instance of the API class
api_instance = liveagent_api.AgentphoneApi
agent_id = 'agent_id_example' # str | 

try:
    # Gets phone currently used by agent (use me as agentId for self)
    api_response = api_instance.get_agent_phone(agent_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AgentphoneApi->get_agent_phone: %s\n" % e

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost/api/v3*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AgentphoneApi* | [**get_agent_phone**](docs/AgentphoneApi.md#get_agent_phone) | **GET** /agent_phone/{agentId} | Gets phone currently used by agent (use me as agentId for self)
*AgentphoneApi* | [**set_agent_phone**](docs/AgentphoneApi.md#set_agent_phone) | **PUT** /agent_phone/{agentId} | Sets phone currently used by agent (use me as agentId for self)
*AgentsApi* | [**create_agent**](docs/AgentsApi.md#create_agent) | **POST** /agents/ | Create agent
*AgentsApi* | [**delete_agent**](docs/AgentsApi.md#delete_agent) | **DELETE** /agents/{userId} | Agent
*AgentsApi* | [**get_agent**](docs/AgentsApi.md#get_agent) | **GET** /agents/{userId} | Agent
*AgentsApi* | [**get_agents**](docs/AgentsApi.md#get_agents) | **GET** /agents/ | Agent list
*AgentsApi* | [**update_agent**](docs/AgentsApi.md#update_agent) | **PUT** /agents/{userId} | Update agent
*BillingApi* | [**check_vat**](docs/BillingApi.md#check_vat) | **POST** /billing/_check_vat | Vat validity
*BillingApi* | [**get_coupon**](docs/BillingApi.md#get_coupon) | **GET** /coupons/{couponCode} | Coupon
*CallsApi* | [**call_add_message**](docs/CallsApi.md#call_add_message) | **POST** /calls/{callId}/messages | Adds a message to the call group in corresponfing ticket
*CallsApi* | [**call_answer**](docs/CallsApi.md#call_answer) | **POST** /calls/{callId}/_answer | Set call as answered by agent
*CallsApi* | [**call_create**](docs/CallsApi.md#call_create) | **POST** /calls/{callId} | Create new call
*CallsApi* | [**call_get_status**](docs/CallsApi.md#call_get_status) | **GET** /calls/{callId}/status | Return the status of call
*CallsApi* | [**call_reroute**](docs/CallsApi.md#call_reroute) | **POST** /calls/{callId}/_reroute | Let the call ring to another agent
*CallsApi* | [**call_ring**](docs/CallsApi.md#call_ring) | **POST** /calls/{callId}/_ring | Let the call ring
*CallsApi* | [**call_start**](docs/CallsApi.md#call_start) | **POST** /call/_start | Starts new outcoming / internal call
*CallsApi* | [**call_stop**](docs/CallsApi.md#call_stop) | **POST** /calls/{callId}/_stop | Stops the call
*CallsApi* | [**call_transfer**](docs/CallsApi.md#call_transfer) | **POST** /calls/{callId}/_transfer | Transfer call to other agent
*CallsApi* | [**call_transfer_answer**](docs/CallsApi.md#call_transfer_answer) | **POST** /calls/{callId}/_transferAnswer | Set call transfer as answered by agent
*CallsApi* | [**call_transfer_complete**](docs/CallsApi.md#call_transfer_complete) | **POST** /calls/{callId}/_transferComplete | Set call transfer complete
*CallsApi* | [**confirm_ring**](docs/CallsApi.md#confirm_ring) | **POST** /calls/{callId}/_confirmRing | Confirm that call is ringing
*CompaniesApi* | [**create_company**](docs/CompaniesApi.md#create_company) | **POST** /companies | Create new company
*CompaniesApi* | [**get_companies_list**](docs/CompaniesApi.md#get_companies_list) | **GET** /companies | Gets list of companies
*CompaniesApi* | [**get_specific_company**](docs/CompaniesApi.md#get_specific_company) | **GET** /companies/{companyId} | Get company by specific id
*CompaniesApi* | [**update_company**](docs/CompaniesApi.md#update_company) | **PUT** /companies/{companyId} | Update company
*ContactsApi* | [**create_contact**](docs/ContactsApi.md#create_contact) | **POST** /contacts | Create new contact
*ContactsApi* | [**get_contacts_list**](docs/ContactsApi.md#get_contacts_list) | **GET** /contacts | Gets list of contacts. Special filters hasEmail (Y/N), hasPhone (Y/N)\nY - Yes, N - No\n
*ContactsApi* | [**get_specific_contact**](docs/ContactsApi.md#get_specific_contact) | **GET** /contacts/{contactId} | Get contact by specific id
*ContactsApi* | [**update_contact**](docs/ContactsApi.md#update_contact) | **PUT** /contacts/{contactId} | Update contact
*CountriesApi* | [**get_countries**](docs/CountriesApi.md#get_countries) | **GET** /countries/ | Country list
*DefaultApi* | [**ping**](docs/DefaultApi.md#ping) | **GET** /ping | Check that API is responding
*FilesApi* | [**upload_file**](docs/FilesApi.md#upload_file) | **POST** /files | Upload new file to the system
*HostingApi* | [**get_info**](docs/HostingApi.md#get_info) | **GET** /hosting/info | Used hosting system info
*InvoicesApi* | [**dowload_invoice**](docs/InvoicesApi.md#dowload_invoice) | **POST** /invoices/{invoiceNumber}/_download | Download invoice
*InvoicesApi* | [**get_invoices**](docs/InvoicesApi.md#get_invoices) | **GET** /invoices/ | Invoice list
*PhonenumbersApi* | [**add_number**](docs/PhonenumbersApi.md#add_number) | **POST** /phone_numbers | Add new number
*PhonenumbersApi* | [**get_phone_number**](docs/PhonenumbersApi.md#get_phone_number) | **GET** /phone_numbers/{phoneNumberId} | Gets phone number
*PhonenumbersApi* | [**get_phone_numbers_list**](docs/PhonenumbersApi.md#get_phone_numbers_list) | **GET** /phone_numbers | Gets list of available phone numbers
*PhonesApi* | [**create_phone**](docs/PhonesApi.md#create_phone) | **POST** /phones | Creates external phone
*PhonesApi* | [**get_phone**](docs/PhonesApi.md#get_phone) | **GET** /phones/{phoneId} | Gets phone device (use _app_ for LiveAgent Phone app device and _web_ for web device)
*PhonesApi* | [**get_phones_list**](docs/PhonesApi.md#get_phones_list) | **GET** /phones | Gets list of available phone devices.\nSpecial filters (userId - filter phones available for specified user only)\n
*PhonesApi* | [**update_phone_params**](docs/PhonesApi.md#update_phone_params) | **PUT** /phones/{phoneId}/_updateParams | Update phone paramas
*SubscriptionsApi* | [**change_addons**](docs/SubscriptionsApi.md#change_addons) | **PUT** /subscriptions/{subscriptionId}/addons/ | Addon change
*SubscriptionsApi* | [**change_plan**](docs/SubscriptionsApi.md#change_plan) | **POST** /subscriptions/{subscriptionId}/_upgrade | Change plan
*SubscriptionsApi* | [**get_active_addons**](docs/SubscriptionsApi.md#get_active_addons) | **GET** /subscriptions/{subscriptionId}/addons/ | Addon list
*SubscriptionsApi* | [**get_billing_info**](docs/SubscriptionsApi.md#get_billing_info) | **GET** /subscriptions/{subscriptionId}/billingInfo | Billing info
*SubscriptionsApi* | [**get_billing_metrics**](docs/SubscriptionsApi.md#get_billing_metrics) | **GET** /subscriptions/{subscriptionId}/billingMetrics | Billing metrics
*SubscriptionsApi* | [**get_billing_status**](docs/SubscriptionsApi.md#get_billing_status) | **GET** /subscriptions/{subscriptionId}/billingStatus | Billing status
*SubscriptionsApi* | [**get_domain_info**](docs/SubscriptionsApi.md#get_domain_info) | **GET** /subscriptions/{subscriptionId}/domain | Domain info
*SubscriptionsApi* | [**get_payment_method**](docs/SubscriptionsApi.md#get_payment_method) | **GET** /subscriptions/{subscriptionId}/paymentMethod | Payment method
*SubscriptionsApi* | [**get_payment_processor**](docs/SubscriptionsApi.md#get_payment_processor) | **GET** /subscriptions/{subscriptionId}/paymentProcessor | Payment processor
*SubscriptionsApi* | [**get_subscription**](docs/SubscriptionsApi.md#get_subscription) | **GET** /subscriptions/{subscriptionId} | Subscription
*SubscriptionsApi* | [**get_subscription_attributes**](docs/SubscriptionsApi.md#get_subscription_attributes) | **GET** /subscriptions/{subscriptionId}/attributes/ | Subscription attribute list
*SubscriptionsApi* | [**get_subscription_discounts**](docs/SubscriptionsApi.md#get_subscription_discounts) | **GET** /subscriptions/{subscriptionId}/discounts | Subscription discounts
*SubscriptionsApi* | [**get_subscription_invoices**](docs/SubscriptionsApi.md#get_subscription_invoices) | **GET** /subscriptions/{subscriptionId}/invoices/ | Subscription invoice list
*SubscriptionsApi* | [**get_upgrade_variations**](docs/SubscriptionsApi.md#get_upgrade_variations) | **GET** /subscriptions/{subscriptionId}/upgradeVariations | Upgrade variation list
*SubscriptionsApi* | [**resume_billing**](docs/SubscriptionsApi.md#resume_billing) | **POST** /subscriptions/{subscriptionId}/_cancelStop | Restart billing
*SubscriptionsApi* | [**set_billing_info**](docs/SubscriptionsApi.md#set_billing_info) | **PUT** /subscriptions/{subscriptionId}/billingInfo | Billing info
*SubscriptionsApi* | [**set_custom_domain**](docs/SubscriptionsApi.md#set_custom_domain) | **PUT** /subscriptions/{subscriptionId}/domain | Custom domain
*SubscriptionsApi* | [**set_payment_method**](docs/SubscriptionsApi.md#set_payment_method) | **PUT** /subscriptions/{subscriptionId}/paymentMethod | Payment method
*SubscriptionsApi* | [**set_subscription_usage**](docs/SubscriptionsApi.md#set_subscription_usage) | **PUT** /subscriptions/{subscriptionId}/usage | Subscription usage
*SubscriptionsApi* | [**stop_billing**](docs/SubscriptionsApi.md#stop_billing) | **POST** /subscriptions/{subscriptionId}/_stop | Stop billing
*SubscriptionsApi* | [**update_application**](docs/SubscriptionsApi.md#update_application) | **POST** /subscriptions/{subscriptionId}/_update | Update subscription
*SubscriptionsApi* | [**validate_billing_info**](docs/SubscriptionsApi.md#validate_billing_info) | **POST** /subscriptions/{subscriptionId}/_validateBillingInfo | Test Billing info
*TokenApi* | [**get_access_token**](docs/TokenApi.md#get_access_token) | **GET** /token | Access token
*VariationsApi* | [**get_variation**](docs/VariationsApi.md#get_variation) | **GET** /variations/{variationId} | Variation


## Documentation For Models

 - [Addon](docs/Addon.md)
 - [AddonList](docs/AddonList.md)
 - [Agent](docs/Agent.md)
 - [AttributeSimple](docs/AttributeSimple.md)
 - [BillingInfo](docs/BillingInfo.md)
 - [BillingMetric](docs/BillingMetric.md)
 - [BillingStatus](docs/BillingStatus.md)
 - [Call](docs/Call.md)
 - [CallAgent](docs/CallAgent.md)
 - [CallMessage](docs/CallMessage.md)
 - [CallStatus](docs/CallStatus.md)
 - [Company](docs/Company.md)
 - [CompanyListItem](docs/CompanyListItem.md)
 - [Contact](docs/Contact.md)
 - [ContactListItem](docs/ContactListItem.md)
 - [Country](docs/Country.md)
 - [Coupon](docs/Coupon.md)
 - [Customer](docs/Customer.md)
 - [DiscountValue](docs/DiscountValue.md)
 - [Domain](docs/Domain.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [HostingInfo](docs/HostingInfo.md)
 - [Invoice](docs/Invoice.md)
 - [InvoiceItem](docs/InvoiceItem.md)
 - [Ivr](docs/Ivr.md)
 - [IvrChoice](docs/IvrChoice.md)
 - [IvrStep](docs/IvrStep.md)
 - [OkResponse](docs/OkResponse.md)
 - [PaymentInfo](docs/PaymentInfo.md)
 - [PaymentMethod](docs/PaymentMethod.md)
 - [PaymentProcessorType](docs/PaymentProcessorType.md)
 - [PhoneDevice](docs/PhoneDevice.md)
 - [PhoneNumber](docs/PhoneNumber.md)
 - [StoredFile](docs/StoredFile.md)
 - [Subscription](docs/Subscription.md)
 - [Token](docs/Token.md)
 - [Upgrade](docs/Upgrade.md)
 - [UsageData](docs/UsageData.md)
 - [Variation](docs/Variation.md)
 - [VariationUpgrade](docs/VariationUpgrade.md)
 - [VariationUpgrades](docs/VariationUpgrades.md)


## Documentation For Authorization


## privileges

- **Type**: OAuth
- **Flow**: accessCode
- **Authorizatoin URL**: 
- **Scopes**: 
 - **invoice.read**: Read invoices
 - **subscription.own**: Read/write own subscriptions (use 'me' as subscriptionId)
 - **subscription.read**: Subscriptions read
 - **subscription.write**: Subscriptions write
 - **hosted_account.read**: Hosted account read
 - **hosted_account.write**: Hosted account write
 - **call.write**: Call write
 - **call.read**: Call read
 - **agent.read**: Agent read
 - **agent.write**: Agent write
 - **phone.read**: Read all phones
 - **phone.write**: Write all phones
 - **phone.own**: Read/write phones available to me
 - **phone_number.read**: Read all phone numbers
 - **phone_number.own**: Read phone numbers available to me
 - **phone_number.write**: Write all phone numbers
 - **user.read**: Read all contacts
 - **file.add**: Upload files
 - **agent_phone.read**: Read agent phone device assigments
 - **agent_phone.write**: Change agent phone device assigments
 - **agent_phone.own**: Change my own phone device assigments
 - **user.write**: Write contact
 - **conversation.create**: Create new conversation

## apikey

- **Type**: API key
- **API key parameter name**: apikey
- **Location**: HTTP header


## Author

support@qualityunit.com

