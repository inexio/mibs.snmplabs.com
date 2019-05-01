#
# PySNMP MIB module SNMP-VIEW-BASED-ACM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SNMP-VIEW-BASED-ACM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:12:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
SnmpSecurityLevel, SnmpAdminString, SnmpSecurityModel = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpSecurityLevel", "SnmpAdminString", "SnmpSecurityModel")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
NotificationType, Gauge32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter64, Unsigned32, IpAddress, Counter32, snmpModules, MibIdentifier, ObjectIdentity, ModuleIdentity, Integer32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Gauge32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter64", "Unsigned32", "IpAddress", "Counter32", "snmpModules", "MibIdentifier", "ObjectIdentity", "ModuleIdentity", "Integer32", "TimeTicks")
TextualConvention, TestAndIncr, StorageType, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TestAndIncr", "StorageType", "DisplayString", "RowStatus")
snmpVacmMIB = ModuleIdentity((1, 3, 6, 1, 6, 3, 16))
snmpVacmMIB.setRevisions(('2002-10-16 00:00', '1999-01-20 00:00', '1997-11-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: snmpVacmMIB.setRevisionsDescriptions(('Clarifications, published as RFC3415', 'Clarifications, published as RFC2575', 'Initial version, published as RFC2275',))
if mibBuilder.loadTexts: snmpVacmMIB.setLastUpdated('200210160000Z')
if mibBuilder.loadTexts: snmpVacmMIB.setOrganization('SNMPv3 Working Group')
if mibBuilder.loadTexts: snmpVacmMIB.setContactInfo('WG-email: snmpv3@lists.tislabs.com Subscribe: majordomo@lists.tislabs.com In message body: subscribe snmpv3 Co-Chair: Russ Mundy Network Associates Laboratories postal: 15204 Omega Drive, Suite 300 Rockville, MD 20850-4601 USA email: mundy@tislabs.com phone: +1 301-947-7107 Co-Chair: David Harrington Enterasys Networks Postal: 35 Industrial Way P. O. Box 5004 Rochester, New Hampshire 03866-5005 USA EMail: dbh@enterasys.com Phone: +1 603-337-2614 Co-editor: Bert Wijnen Lucent Technologies postal: Schagen 33 3461 GL Linschoten Netherlands email: bwijnen@lucent.com phone: +31-348-480-685 Co-editor: Randy Presuhn BMC Software, Inc. postal: 2141 North First Street San Jose, CA 95131 USA email: randy_presuhn@bmc.com phone: +1 408-546-1006 Co-editor: Keith McCloghrie Cisco Systems, Inc. postal: 170 West Tasman Drive San Jose, CA 95134-1706 USA email: kzm@cisco.com phone: +1-408-526-5260 ')
if mibBuilder.loadTexts: snmpVacmMIB.setDescription('The management information definitions for the View-based Access Control Model for SNMP. Copyright (C) The Internet Society (2002). This version of this MIB module is part of RFC 3415; see the RFC itself for full legal notices. ')
vacmMIBObjects = MibIdentifier((1, 3, 6, 1, 6, 3, 16, 1))
vacmMIBConformance = MibIdentifier((1, 3, 6, 1, 6, 3, 16, 2))
vacmContextTable = MibTable((1, 3, 6, 1, 6, 3, 16, 1, 1), )
if mibBuilder.loadTexts: vacmContextTable.setStatus('current')
if mibBuilder.loadTexts: vacmContextTable.setDescription('The table of locally available contexts. This table provides information to SNMP Command Generator applications so that they can properly configure the vacmAccessTable to control access to all contexts at the SNMP entity. This table may change dynamically if the SNMP entity allows that contexts are added/deleted dynamically (for instance when its configuration changes). Such changes would happen only if the management instrumentation at that SNMP entity recognizes more (or fewer) contexts. The presence of entries in this table and of entries in the vacmAccessTable are independent. That is, a context identified by an entry in this table is not necessarily referenced by any entries in the vacmAccessTable; and the context(s) referenced by an entry in the vacmAccessTable does not necessarily currently exist and thus need not be identified by an entry in this table. This table must be made accessible via the default context so that Command Responder applications have a standard way of retrieving the information. This table is read-only. It cannot be configured via SNMP. ')
vacmContextEntry = MibTableRow((1, 3, 6, 1, 6, 3, 16, 1, 1, 1), ).setIndexNames((0, "SNMP-VIEW-BASED-ACM-MIB", "vacmContextName"))
if mibBuilder.loadTexts: vacmContextEntry.setStatus('current')
if mibBuilder.loadTexts: vacmContextEntry.setDescription('Information about a particular context.')
vacmContextName = MibTableColumn((1, 3, 6, 1, 6, 3, 16, 1, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vacmContextName.setStatus('current')
if mibBuilder.loadTexts: vacmContextName.setDescription('A human readable name identifying a particular context at a particular SNMP entity. The empty contextName (zero length) represents the default context. ')
vacmSecurityToGroupTable = MibTable((1, 3, 6, 1, 6, 3, 16, 1, 2), )
if mibBuilder.loadTexts: vacmSecurityToGroupTable.setStatus('current')
if mibBuilder.loadTexts: vacmSecurityToGroupTable.setDescription('This table maps a combination of securityModel and securityName into a groupName which is used to define an access control policy for a group of principals. ')
vacmSecurityToGroupEntry = MibTableRow((1, 3, 6, 1, 6, 3, 16, 1, 2, 1), ).setIndexNames((0, "SNMP-VIEW-BASED-ACM-MIB", "vacmSecurityModel"), (0, "SNMP-VIEW-BASED-ACM-MIB", "vacmSecurityName"))
if mibBuilder.loadTexts: vacmSecurityToGroupEntry.setStatus('current')
if mibBuilder.loadTexts: vacmSecurityToGroupEntry.setDescription('An entry in this table maps the combination of a securityModel and securityName into a groupName. ')
vacmSecurityModel = MibTableColumn((1, 3, 6, 1, 6, 3, 16, 1, 2, 1, 1), SnmpSecurityModel().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: vacmSecurityModel.setStatus('current')
if mibBuilder.loadTexts: vacmSecurityModel.setDescription("The Security Model, by which the vacmSecurityName referenced by this entry is provided. Note, this object may not take the 'any' (0) value. ")
vacmSecurityName = MibTableColumn((1, 3, 6, 1, 6, 3, 16, 1, 2, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: vacmSecurityName.setStatus('current')
if mibBuilder.loadTexts: vacmSecurityName.setDescription('The securityName for the principal, represented in a Security Model independent format, which is mapped by this entry to a groupName. ')
vacmGroupName = MibTableColumn((1, 3, 6, 1, 6, 3, 16, 1, 2, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vacmGroupName.setStatus('current')
if mibBuilder.loadTexts: vacmGroupName.setDescription('The name of the group to which this entry (e.g., the combination of securityModel and securityName) belongs. This groupName is used as index into the vacmAccessTable to select an access control policy. However, a value in this table does not imply that an instance with the value exists in table vacmAccesTable. ')
vacmSecurityToGroupStorageType = MibTableColumn((1, 3, 6, 1, 6, 3, 16, 1, 2, 1, 4), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vacmSecurityToGroupStorageType.setStatus('current')
if mibBuilder.loadTexts: vacmSecurityToGroupStorageType.setDescription("The storage type for this conceptual row. Conceptual rows having the value 'permanent' need not allow write-access to any columnar objects in the row. ")
vacmSecurityToGroupStatus = MibTableColumn((1, 3, 6, 1, 6, 3, 16, 1, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vacmSecurityToGroupStatus.setStatus('current')
if mibBuilder.loadTexts: vacmSecurityToGroupStatus.setDescription("The status of this conceptual row. Until instances of all corresponding columns are appropriately configured, the value of the corresponding instance of the vacmSecurityToGroupStatus column is 'notReady'. In particular, a newly created row cannot be made active until a value has been set for vacmGroupName. The RowStatus TC [RFC2579] requires that this DESCRIPTION clause states under which circumstances other objects in this row can be modified: The value of this object has no effect on whether other objects in this conceptual row can be modified. ")
vacmAccessTable = MibTable((1, 3, 6, 1, 6, 3, 16, 1, 4), )
if mibBuilder.loadTexts: vacmAccessTable.setStatus('current')
if mibBuilder.loadTexts: vacmAccessTable.setDescription("The table of access rights for groups. Each entry is indexed by a groupName, a contextPrefix, a securityModel and a securityLevel. To determine whether access is allowed, one entry from this table needs to be selected and the proper viewName from that entry must be used for access control checking. To select the proper entry, follow these steps: 1) the set of possible matches is formed by the intersection of the following sets of entries: the set of entries with identical vacmGroupName the union of these two sets: - the set with identical vacmAccessContextPrefix - the set of entries with vacmAccessContextMatch value of 'prefix' and matching vacmAccessContextPrefix intersected with the union of these two sets: - the set of entries with identical vacmSecurityModel - the set of entries with vacmSecurityModel value of 'any' intersected with the set of entries with vacmAccessSecurityLevel value less than or equal to the requested securityLevel 2) if this set has only one member, we're done otherwise, it comes down to deciding how to weight the preferences between ContextPrefixes, SecurityModels, and SecurityLevels as follows: a) if the subset of entries with securityModel matching the securityModel in the message is not empty, then discard the rest. b) if the subset of entries with vacmAccessContextPrefix matching the contextName in the message is not empty, then discard the rest c) discard all entries with ContextPrefixes shorter than the longest one remaining in the set d) select the entry with the highest securityLevel Please note that for securityLevel noAuthNoPriv, all groups are really equivalent since the assumption that the securityName has been authenticated does not hold. ")
vacmAccessEntry = MibTableRow((1, 3, 6, 1, 6, 3, 16, 1, 4, 1), ).setIndexNames((0, "SNMP-VIEW-BASED-ACM-MIB", "vacmGroupName"), (0, "SNMP-VIEW-BASED-ACM-MIB", "vacmAccessContextPrefix"), (0, "SNMP-VIEW-BASED-ACM-MIB", "vacmAccessSecurityModel"), (0, "SNMP-VIEW-BASED-ACM-MIB", "vacmAccessSecurityLevel"))
if mibBuilder.loadTexts: vacmAccessEntry.setStatus('current')
if mibBuilder.loadTexts: vacmAccessEntry.setDescription('An access right configured in the Local Configuration Datastore (LCD) authorizing access to an SNMP context. Entries in this table can use an instance value for object vacmGroupName even if no entry in table vacmAccessSecurityToGroupTable has a corresponding value for object vacmGroupName. ')
vacmAccessContextPrefix = MibTableColumn((1, 3, 6, 1, 6, 3, 16, 1, 4, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)))
if mibBuilder.loadTexts: vacmAccessContextPrefix.setStatus('current')
if mibBuilder.loadTexts: vacmAccessContextPrefix.setDescription("In order to gain the access rights allowed by this conceptual row, a contextName must match exactly (if the value of vacmAccessContextMatch is 'exact') or partially (if the value of vacmAccessContextMatch is 'prefix') to the value of the instance of this object. ")
vacmAccessSecurityModel = MibTableColumn((1, 3, 6, 1, 6, 3, 16, 1, 4, 1, 2), SnmpSecurityModel())
if mibBuilder.loadTexts: vacmAccessSecurityModel.setStatus('current')
if mibBuilder.loadTexts: vacmAccessSecurityModel.setDescription('In order to gain the access rights allowed by this conceptual row, this securityModel must be in use. ')
vacmAccessSecurityLevel = MibTableColumn((1, 3, 6, 1, 6, 3, 16, 1, 4, 1, 3), SnmpSecurityLevel())
if mibBuilder.loadTexts: vacmAccessSecurityLevel.setStatus('current')
if mibBuilder.loadTexts: vacmAccessSecurityLevel.setDescription('The minimum level of security required in order to gain the access rights allowed by this conceptual row. A securityLevel of noAuthNoPriv is less than authNoPriv which in turn is less than authPriv. If multiple entries are equally indexed except for this vacmAccessSecurityLevel index, then the entry which has the highest value for vacmAccessSecurityLevel is selected. ')
vacmAccessContextMatch = MibTableColumn((1, 3, 6, 1, 6, 3, 16, 1, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("exact", 1), ("prefix", 2))).clone('exact')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vacmAccessContextMatch.setStatus('current')
if mibBuilder.loadTexts: vacmAccessContextMatch.setDescription('If the value of this object is exact(1), then all rows where the contextName exactly matches vacmAccessContextPrefix are selected. If the value of this object is prefix(2), then all rows where the contextName whose starting octets exactly match vacmAccessContextPrefix are selected. This allows for a simple form of wildcarding. ')
vacmAccessReadViewName = MibTableColumn((1, 3, 6, 1, 6, 3, 16, 1, 4, 1, 5), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)).clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vacmAccessReadViewName.setStatus('current')
if mibBuilder.loadTexts: vacmAccessReadViewName.setDescription('The value of an instance of this object identifies the MIB view of the SNMP context to which this conceptual row authorizes read access. The identified MIB view is that one for which the vacmViewTreeFamilyViewName has the same value as the instance of this object; if the value is the empty string or if there is no active MIB view having this value of vacmViewTreeFamilyViewName, then no access is granted. ')
vacmAccessWriteViewName = MibTableColumn((1, 3, 6, 1, 6, 3, 16, 1, 4, 1, 6), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)).clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vacmAccessWriteViewName.setStatus('current')
if mibBuilder.loadTexts: vacmAccessWriteViewName.setDescription('The value of an instance of this object identifies the MIB view of the SNMP context to which this conceptual row authorizes write access. The identified MIB view is that one for which the vacmViewTreeFamilyViewName has the same value as the instance of this object; if the value is the empty string or if there is no active MIB view having this value of vacmViewTreeFamilyViewName, then no access is granted. ')
vacmAccessNotifyViewName = MibTableColumn((1, 3, 6, 1, 6, 3, 16, 1, 4, 1, 7), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)).clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vacmAccessNotifyViewName.setStatus('current')
if mibBuilder.loadTexts: vacmAccessNotifyViewName.setDescription('The value of an instance of this object identifies the MIB view of the SNMP context to which this conceptual row authorizes access for notifications. The identified MIB view is that one for which the vacmViewTreeFamilyViewName has the same value as the instance of this object; if the value is the empty string or if there is no active MIB view having this value of vacmViewTreeFamilyViewName, then no access is granted. ')
vacmAccessStorageType = MibTableColumn((1, 3, 6, 1, 6, 3, 16, 1, 4, 1, 8), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vacmAccessStorageType.setStatus('current')
if mibBuilder.loadTexts: vacmAccessStorageType.setDescription("The storage type for this conceptual row. Conceptual rows having the value 'permanent' need not allow write-access to any columnar objects in the row. ")
vacmAccessStatus = MibTableColumn((1, 3, 6, 1, 6, 3, 16, 1, 4, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vacmAccessStatus.setStatus('current')
if mibBuilder.loadTexts: vacmAccessStatus.setDescription('The status of this conceptual row. The RowStatus TC [RFC2579] requires that this DESCRIPTION clause states under which circumstances other objects in this row can be modified: The value of this object has no effect on whether other objects in this conceptual row can be modified. ')
vacmMIBViews = MibIdentifier((1, 3, 6, 1, 6, 3, 16, 1, 5))
vacmViewSpinLock = MibScalar((1, 3, 6, 1, 6, 3, 16, 1, 5, 1), TestAndIncr()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vacmViewSpinLock.setStatus('current')
if mibBuilder.loadTexts: vacmViewSpinLock.setDescription("An advisory lock used to allow cooperating SNMP Command Generator applications to coordinate their use of the Set operation in creating or modifying views. When creating a new view or altering an existing view, it is important to understand the potential interactions with other uses of the view. The vacmViewSpinLock should be retrieved. The name of the view to be created should be determined to be unique by the SNMP Command Generator application by consulting the vacmViewTreeFamilyTable. Finally, the named view may be created (Set), including the advisory lock. If another SNMP Command Generator application has altered the views in the meantime, then the spin lock's value will have changed, and so this creation will fail because it will specify the wrong value for the spin lock. Since this is an advisory lock, the use of this lock is not enforced. ")
vacmViewTreeFamilyTable = MibTable((1, 3, 6, 1, 6, 3, 16, 1, 5, 2), )
if mibBuilder.loadTexts: vacmViewTreeFamilyTable.setStatus('current')
if mibBuilder.loadTexts: vacmViewTreeFamilyTable.setDescription("Locally held information about families of subtrees within MIB views. Each MIB view is defined by two sets of view subtrees: - the included view subtrees, and - the excluded view subtrees. Every such view subtree, both the included and the excluded ones, is defined in this table. To determine if a particular object instance is in a particular MIB view, compare the object instance's OBJECT IDENTIFIER with each of the MIB view's active entries in this table. If none match, then the object instance is not in the MIB view. If one or more match, then the object instance is included in, or excluded from, the MIB view according to the value of vacmViewTreeFamilyType in the entry whose value of vacmViewTreeFamilySubtree has the most sub-identifiers. If multiple entries match and have the same number of sub-identifiers (when wildcarding is specified with the value of vacmViewTreeFamilyMask), then the lexicographically greatest instance of vacmViewTreeFamilyType determines the inclusion or exclusion. An object instance's OBJECT IDENTIFIER X matches an active entry in this table when the number of sub-identifiers in X is at least as many as in the value of vacmViewTreeFamilySubtree for the entry, and each sub-identifier in the value of vacmViewTreeFamilySubtree matches its corresponding sub-identifier in X. Two sub-identifiers match either if the corresponding bit of the value of vacmViewTreeFamilyMask for the entry is zero (the 'wild card' value), or if they are equal. A 'family' of subtrees is the set of subtrees defined by a particular combination of values of vacmViewTreeFamilySubtree and vacmViewTreeFamilyMask. In the case where no 'wild card' is defined in the vacmViewTreeFamilyMask, the family of subtrees reduces to a single subtree. When creating or changing MIB views, an SNMP Command Generator application should utilize the vacmViewSpinLock to try to avoid collisions. See DESCRIPTION clause of vacmViewSpinLock. When creating MIB views, it is strongly advised that first the 'excluded' vacmViewTreeFamilyEntries are created and then the 'included' entries. When deleting MIB views, it is strongly advised that first the 'included' vacmViewTreeFamilyEntries are deleted and then the 'excluded' entries. If a create for an entry for instance-level access control is received and the implementation does not support instance-level granularity, then an inconsistentName error must be returned. ")
vacmViewTreeFamilyEntry = MibTableRow((1, 3, 6, 1, 6, 3, 16, 1, 5, 2, 1), ).setIndexNames((0, "SNMP-VIEW-BASED-ACM-MIB", "vacmViewTreeFamilyViewName"), (0, "SNMP-VIEW-BASED-ACM-MIB", "vacmViewTreeFamilySubtree"))
if mibBuilder.loadTexts: vacmViewTreeFamilyEntry.setStatus('current')
if mibBuilder.loadTexts: vacmViewTreeFamilyEntry.setDescription("Information on a particular family of view subtrees included in or excluded from a particular SNMP context's MIB view. Implementations must not restrict the number of families of view subtrees for a given MIB view, except as dictated by resource constraints on the overall number of entries in the vacmViewTreeFamilyTable. If no conceptual rows exist in this table for a given MIB view (viewName), that view may be thought of as consisting of the empty set of view subtrees. ")
vacmViewTreeFamilyViewName = MibTableColumn((1, 3, 6, 1, 6, 3, 16, 1, 5, 2, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: vacmViewTreeFamilyViewName.setStatus('current')
if mibBuilder.loadTexts: vacmViewTreeFamilyViewName.setDescription('The human readable name for a family of view subtrees. ')
vacmViewTreeFamilySubtree = MibTableColumn((1, 3, 6, 1, 6, 3, 16, 1, 5, 2, 1, 2), ObjectIdentifier())
if mibBuilder.loadTexts: vacmViewTreeFamilySubtree.setStatus('current')
if mibBuilder.loadTexts: vacmViewTreeFamilySubtree.setDescription('The MIB subtree which when combined with the corresponding instance of vacmViewTreeFamilyMask defines a family of view subtrees. ')
vacmViewTreeFamilyMask = MibTableColumn((1, 3, 6, 1, 6, 3, 16, 1, 5, 2, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16)).clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vacmViewTreeFamilyMask.setStatus('current')
if mibBuilder.loadTexts: vacmViewTreeFamilyMask.setDescription("The bit mask which, in combination with the corresponding instance of vacmViewTreeFamilySubtree, defines a family of view subtrees. Each bit of this bit mask corresponds to a sub-identifier of vacmViewTreeFamilySubtree, with the most significant bit of the i-th octet of this octet string value (extended if necessary, see below) corresponding to the (8*i - 7)-th sub-identifier, and the least significant bit of the i-th octet of this octet string corresponding to the (8*i)-th sub-identifier, where i is in the range 1 through 16. Each bit of this bit mask specifies whether or not the corresponding sub-identifiers must match when determining if an OBJECT IDENTIFIER is in this family of view subtrees; a '1' indicates that an exact match must occur; a '0' indicates 'wild card', i.e., any sub-identifier value matches. Thus, the OBJECT IDENTIFIER X of an object instance is contained in a family of view subtrees if, for each sub-identifier of the value of vacmViewTreeFamilySubtree, either: the i-th bit of vacmViewTreeFamilyMask is 0, or the i-th sub-identifier of X is equal to the i-th sub-identifier of the value of vacmViewTreeFamilySubtree. If the value of this bit mask is M bits long and there are more than M sub-identifiers in the corresponding instance of vacmViewTreeFamilySubtree, then the bit mask is extended with 1's to be the required length. Note that when the value of this object is the zero-length string, this extension rule results in a mask of all-1's being used (i.e., no 'wild card'), and the family of view subtrees is the one view subtree uniquely identified by the corresponding instance of vacmViewTreeFamilySubtree. Note that masks of length greater than zero length do not need to be supported. In this case this object is made read-only. ")
vacmViewTreeFamilyType = MibTableColumn((1, 3, 6, 1, 6, 3, 16, 1, 5, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("included", 1), ("excluded", 2))).clone('included')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vacmViewTreeFamilyType.setStatus('current')
if mibBuilder.loadTexts: vacmViewTreeFamilyType.setDescription('Indicates whether the corresponding instances of vacmViewTreeFamilySubtree and vacmViewTreeFamilyMask define a family of view subtrees which is included in or excluded from the MIB view. ')
vacmViewTreeFamilyStorageType = MibTableColumn((1, 3, 6, 1, 6, 3, 16, 1, 5, 2, 1, 5), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vacmViewTreeFamilyStorageType.setStatus('current')
if mibBuilder.loadTexts: vacmViewTreeFamilyStorageType.setDescription("The storage type for this conceptual row. Conceptual rows having the value 'permanent' need not allow write-access to any columnar objects in the row. ")
vacmViewTreeFamilyStatus = MibTableColumn((1, 3, 6, 1, 6, 3, 16, 1, 5, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vacmViewTreeFamilyStatus.setStatus('current')
if mibBuilder.loadTexts: vacmViewTreeFamilyStatus.setDescription('The status of this conceptual row. The RowStatus TC [RFC2579] requires that this DESCRIPTION clause states under which circumstances other objects in this row can be modified: The value of this object has no effect on whether other objects in this conceptual row can be modified. ')
vacmMIBCompliances = MibIdentifier((1, 3, 6, 1, 6, 3, 16, 2, 1))
vacmMIBGroups = MibIdentifier((1, 3, 6, 1, 6, 3, 16, 2, 2))
vacmMIBCompliance = ModuleCompliance((1, 3, 6, 1, 6, 3, 16, 2, 1, 1)).setObjects(("SNMP-VIEW-BASED-ACM-MIB", "vacmBasicGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vacmMIBCompliance = vacmMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: vacmMIBCompliance.setDescription('The compliance statement for SNMP engines which implement the SNMP View-based Access Control Model configuration MIB. ')
vacmBasicGroup = ObjectGroup((1, 3, 6, 1, 6, 3, 16, 2, 2, 1)).setObjects(("SNMP-VIEW-BASED-ACM-MIB", "vacmContextName"), ("SNMP-VIEW-BASED-ACM-MIB", "vacmGroupName"), ("SNMP-VIEW-BASED-ACM-MIB", "vacmSecurityToGroupStorageType"), ("SNMP-VIEW-BASED-ACM-MIB", "vacmSecurityToGroupStatus"), ("SNMP-VIEW-BASED-ACM-MIB", "vacmAccessContextMatch"), ("SNMP-VIEW-BASED-ACM-MIB", "vacmAccessReadViewName"), ("SNMP-VIEW-BASED-ACM-MIB", "vacmAccessWriteViewName"), ("SNMP-VIEW-BASED-ACM-MIB", "vacmAccessNotifyViewName"), ("SNMP-VIEW-BASED-ACM-MIB", "vacmAccessStorageType"), ("SNMP-VIEW-BASED-ACM-MIB", "vacmAccessStatus"), ("SNMP-VIEW-BASED-ACM-MIB", "vacmViewSpinLock"), ("SNMP-VIEW-BASED-ACM-MIB", "vacmViewTreeFamilyMask"), ("SNMP-VIEW-BASED-ACM-MIB", "vacmViewTreeFamilyType"), ("SNMP-VIEW-BASED-ACM-MIB", "vacmViewTreeFamilyStorageType"), ("SNMP-VIEW-BASED-ACM-MIB", "vacmViewTreeFamilyStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vacmBasicGroup = vacmBasicGroup.setStatus('current')
if mibBuilder.loadTexts: vacmBasicGroup.setDescription('A collection of objects providing for remote configuration of an SNMP engine which implements the SNMP View-based Access Control Model. ')
mibBuilder.exportSymbols("SNMP-VIEW-BASED-ACM-MIB", vacmSecurityName=vacmSecurityName, vacmMIBViews=vacmMIBViews, vacmViewTreeFamilyTable=vacmViewTreeFamilyTable, vacmContextName=vacmContextName, vacmAccessSecurityModel=vacmAccessSecurityModel, vacmAccessContextMatch=vacmAccessContextMatch, vacmViewTreeFamilyViewName=vacmViewTreeFamilyViewName, vacmMIBConformance=vacmMIBConformance, vacmMIBObjects=vacmMIBObjects, vacmViewTreeFamilySubtree=vacmViewTreeFamilySubtree, vacmMIBGroups=vacmMIBGroups, vacmSecurityModel=vacmSecurityModel, vacmMIBCompliance=vacmMIBCompliance, vacmContextEntry=vacmContextEntry, vacmContextTable=vacmContextTable, vacmAccessContextPrefix=vacmAccessContextPrefix, vacmAccessSecurityLevel=vacmAccessSecurityLevel, vacmAccessEntry=vacmAccessEntry, vacmViewTreeFamilyEntry=vacmViewTreeFamilyEntry, PYSNMP_MODULE_ID=snmpVacmMIB, vacmViewTreeFamilyStatus=vacmViewTreeFamilyStatus, vacmAccessStatus=vacmAccessStatus, vacmSecurityToGroupTable=vacmSecurityToGroupTable, vacmSecurityToGroupStatus=vacmSecurityToGroupStatus, vacmViewTreeFamilyType=vacmViewTreeFamilyType, vacmAccessWriteViewName=vacmAccessWriteViewName, vacmAccessNotifyViewName=vacmAccessNotifyViewName, vacmViewTreeFamilyStorageType=vacmViewTreeFamilyStorageType, vacmSecurityToGroupStorageType=vacmSecurityToGroupStorageType, snmpVacmMIB=snmpVacmMIB, vacmAccessStorageType=vacmAccessStorageType, vacmGroupName=vacmGroupName, vacmAccessTable=vacmAccessTable, vacmViewTreeFamilyMask=vacmViewTreeFamilyMask, vacmBasicGroup=vacmBasicGroup, vacmViewSpinLock=vacmViewSpinLock, vacmSecurityToGroupEntry=vacmSecurityToGroupEntry, vacmMIBCompliances=vacmMIBCompliances, vacmAccessReadViewName=vacmAccessReadViewName)
