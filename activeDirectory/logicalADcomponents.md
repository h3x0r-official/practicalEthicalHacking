1. AD DS Schema 
2. Domains
3. Tree
4. Forest
5. Organizational Units (OUs)
6. Trusts
7. Objects


## 1. AD DS Schema 

> - Defines every type of object that can be stored in the directory.
> - Enforces rule regarding object creation and configuration.

| Object Types | Function | Examples |
| --- | --- | --- |
| Class Object | What objects can be created in a directory | User, Computer |
| Attribute Object | Information that can be attached to an object | Display Name |

## 2. Domains

> Used to group and manage objects in an organization. 

- Administrative boundary for applying policies to group and objects.
- A replication boundary for replicating data between domain controllers.
- And authentication and authorization boundary that provides a way to limit the scope of access to resources.

## 3. Tree

> A domain tree is a hierarchy of domains in AD DS.

#### All domain in the Tree:
- Share a contiguous namespace with the parent domain.
- Can have additional child domains. 
- By default create a two-way transitive trust with other domains.

## 4. Forest 

> A forest is a collection of one or more domain trees.

- Share a common schema.
- Share a common configuration partition.
- Share a global catalog to enable searching.
- Enable trust between all the domains in the forest.
- Share the Enterprise Admins and Schema Admin groups. 


## 5. Organizational Unit (OUs)

> OUs are AD containers that can contain users, groups, computers, and other OUs.

#### Used to:
- Represents your organization hierarchically and logically.
- Manage a collection of objects in a consistent way.
- Delegate permissions to administrator group of objects. 
- Apply policies.

## Trusts

> Trusts provide a mechanism for users to gain access to resources in another domain.

| Type of Trusts | Description |
| --- | ---- |
| Directional | The Trust direction flows from trusted domain to trusting domain |
| Transitive | Trust relationship is extended beyond the two-domain trust to include other trusted domains |

- All domains in the forest trusts all domains in the forest.
- Trust can extend outside the forest.


## 7. Objects

| Object | Description |
| --- |---- |
| User | Enables network resources access to a user. |
| InetOrgPerson | Similar to a user account & Used for compatibility with other directory services. |
| Contacts | Used primarily to assign e-mail addresses to external users & Does not enable network access. |
| Groups | Used to simplify the administration of access control. | 
| Computers | Enable authentication and auditing of computer access to resources. |
| Printers | Used to simplify the process of locating and connecting to printers. |
| Shared Folders | Enable users to search for shared folders on priority. | 

