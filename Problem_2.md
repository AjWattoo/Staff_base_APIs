# Problem

Another customer wants to set up an automatic CSV import. The code is ready to run, but it
is not working. They provided you with the mapping they are using:
`profile-field:firstName,profile-field:lastName,profile-field:position,eMail`

## Maping

To do Automatic csv Import customer must have to Map the CSV attributes to the Staffbase Studio profile fields [/users/import/csv/update](https://developers.staffbase.com/api/api-csv-import#tag/usersimportcsvupdate). This mapping ensures that the endpoints can match the data and update the platform.

## Issue in Mapping

Isuue in given mappings from the customer is that they are not according to the [mapping table](https://developers.staffbase.com/references/csv-import-mappings/#prerequisites) which is provided by Staffbase.
According to the mapping table **CSV Attribute** : `externalID` is mandatory in mapping which is missed by customer that's why code is not working because of missing mandatory mapping externalID. Customer had given `Identifier` field in csv file(which he/she uploaded it) but forgot to metion `externalID` in mapping.

| Staffbase Studio Naming | Mandatory | CSV Attribute |
| :---------------------: | :-------: | :-----------: |
|       Identifier        |    Yes    |  externalID   |

## server response to a call with that mapping

When running an import with `dry=true` on the [/users/import/csv/update](https://developers.staffbase.com/api/api-csv-import#tag/usersimportcsvupdate) endpoint, then all warnings and errors will be gathered and stated in the response. According to [Error Reference Table](https://developers.staffbase.com/references/csv-import-references/#errors) if customer forgot to mention `externalID` in mapping then he/she will got the response _`CSV_MISSING_EXTERNAL_ID_MAPPING`_ from the server.

|              Code               |                                  Notes & Examples                                  |
| :-----------------------------: | :--------------------------------------------------------------------------------: |
| CSV_MISSING_EXTERNAL_ID_MAPPING | The mapping of the import does not contain the required user identifier externalID |

## steps required to solve the problem

Steps required to fix this is to mention `externalID` in mapping. New mapping should look like `mappings=externalID,profile-field:firstName,profile-field:lastName,profile-field:position,eMail` and this mappings should mention in the request. Python script to ecexute this mappings would be like this:

```Python

import requests,json

access_token='Basic API TOKEN'
url='https://backend.staffbase.com/api/users/import/csv/update'

headers={'Authorization': access_token,
'Content-Type':'application/x-www-form-urlencoded'}
data={
    "mappings":'externalID,profile-field:firstName,profile-field:lastName,profile-field:position,    eMail',
    'dry':'true'
}
staffbase_news=requests.post(url,data=data,headers=headers)
print(staffbase_news.status_code)
mappings = json.loads(staffbase_news.text)
print(mappings)

```
