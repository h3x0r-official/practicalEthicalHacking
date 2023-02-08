- Domain Controller
- AD DS (Active Directory Domain Services) Data Store 

## 1. Domain Controller

> A domain controller is a server with the AD DS server role installed that has specifically been promoted to a domain controller.

- Host a copy of AD DS directory store.
- Provide authentication and authorization services.
- Replicate updates to other domain controllers in the domain forest.
- Allow administrative access to manage user accounts and network resources.

## 2. AD DS Data Store

> AD DS Data Store contains a database files and processes that store and manage directory information for users, services and applications. 

- Consists of the Ntds.dit file `(Contains passwords hashes and critical data)`.
- Is stored by default in the `%SystemRoot%\NTDS` folder on all domain controllers.
- Is accessible only through the domain controller process and protocols.  