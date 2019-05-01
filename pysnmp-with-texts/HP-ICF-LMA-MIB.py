#
# PySNMP MIB module HP-ICF-LMA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-ICF-LMA-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:34:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
HpAutzUserRoleName, = mibBuilder.importSymbols("HP-AUTZ-MIB", "HpAutzUserRoleName")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
VidList, = mibBuilder.importSymbols("HP-ICF-TC", "VidList")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Bits, Unsigned32, NotificationType, Integer32, Gauge32, TimeTicks, IpAddress, MibIdentifier, ObjectIdentity, Counter64, Counter32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Bits", "Unsigned32", "NotificationType", "Integer32", "Gauge32", "TimeTicks", "IpAddress", "MibIdentifier", "ObjectIdentity", "Counter64", "Counter32", "ModuleIdentity")
MacAddress, DisplayString, TruthValue, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "DisplayString", "TruthValue", "RowStatus", "TextualConvention")
hpicfLmaMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97))
hpicfLmaMIB.setRevisions(('2017-06-28 07:10', '2016-02-12 07:10', '2013-04-10 09:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpicfLmaMIB.setRevisionsDescriptions(('Added mac-pinning related MIB Object.', 'Added user role support.', 'Initial version of Local MAC Authentication MIB module.',))
if mibBuilder.loadTexts: hpicfLmaMIB.setLastUpdated('201706280710Z')
if mibBuilder.loadTexts: hpicfLmaMIB.setOrganization('HP Networking')
if mibBuilder.loadTexts: hpicfLmaMIB.setContactInfo('Hewlett-Packard Enterprise Company 8000 Foothills Blvd. Roseville, CA 95747')
if mibBuilder.loadTexts: hpicfLmaMIB.setDescription('This MIB module describes objects for managing the Local MAC Authentication feature of devices in the HP Integrated Communication Facility product line.')
hpicfLmaNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 0))
hpicfLmaObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1))
hpicfLmaConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 2))
hpicfLmaConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1))
hpicfLmaStatsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 2))
hpicfLmaScalarObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 1))
hpicfLmaMacGrpTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 2), )
if mibBuilder.loadTexts: hpicfLmaMacGrpTable.setStatus('current')
if mibBuilder.loadTexts: hpicfLmaMacGrpTable.setDescription('This table is to create MAC group, which is a collection Of MAC address/MAC OUI/MAC mask. There can be a maximum of 256 MAC groups.')
hpicfLmaMacGrpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 2, 1), ).setIndexNames((0, "HP-ICF-LMA-MIB", "hpicfLmaMacGrpName"))
if mibBuilder.loadTexts: hpicfLmaMacGrpEntry.setStatus('current')
if mibBuilder.loadTexts: hpicfLmaMacGrpEntry.setDescription('This table is to create MAC group, which is a collection Of MAC address/MAC OUI/MAC mask. There can be a maximum of 256 MAC groups.')
hpicfLmaMacGrpName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: hpicfLmaMacGrpName.setStatus('current')
if mibBuilder.loadTexts: hpicfLmaMacGrpName.setDescription('Name of the MAC group. A name can have maximum 32 characters.')
hpicfLmaMacGrpRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfLmaMacGrpRowStatus.setStatus('current')
if mibBuilder.loadTexts: hpicfLmaMacGrpRowStatus.setDescription('Status of this row, by which new entries may be created or existing entries deleted from this table.')
hpicfLmaMacTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 3), )
if mibBuilder.loadTexts: hpicfLmaMacTable.setStatus('current')
if mibBuilder.loadTexts: hpicfLmaMacTable.setDescription('This table stores MAC address/MAC OUI/MAC mask bound to a MAC group.A MAC group can be associated to a maximum of 120 entries, Each entry is equivalent to one record in hpicfLmaMacTable and there can be a maximum of 256 records.')
hpicfLmaMacEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 3, 1), ).setIndexNames((0, "HP-ICF-LMA-MIB", "hpicfLmaMacGrpName"), (0, "HP-ICF-LMA-MIB", "hpicfLmaMacType"), (0, "HP-ICF-LMA-MIB", "hpicfLmaMacValue"))
if mibBuilder.loadTexts: hpicfLmaMacEntry.setStatus('current')
if mibBuilder.loadTexts: hpicfLmaMacEntry.setDescription('This table stores MAC address/MAC OUI/MAC mask bound to a MAC group.A MAC group can be associated to a maximum of 120 entries, Each entry is equivalent to one record in hpicfLmaMacTable and there can be a maximum of 256 records.')
hpicfLmaMacType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("macAddress", 1), ("macMask", 2), ("macOui", 3))))
if mibBuilder.loadTexts: hpicfLmaMacType.setStatus('current')
if mibBuilder.loadTexts: hpicfLmaMacType.setDescription('This object specifies whether the type of MAC Address is: macAddress(1) Fully qualified MAC address. macMask(2) MAC address prefiX. Only 32 & 40 bits are allowed. macOUI(3) 24 bit organizationally unique identifier.')
hpicfLmaMacValue = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 3, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(3, 6)))
if mibBuilder.loadTexts: hpicfLmaMacValue.setStatus('current')
if mibBuilder.loadTexts: hpicfLmaMacValue.setDescription('This is to specify the value for the hpicfLmaMacType, value should be in conjunction with MAC Type.')
hpicfLmaMacRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 3, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfLmaMacRowStatus.setStatus('current')
if mibBuilder.loadTexts: hpicfLmaMacRowStatus.setDescription('Status of this row, by which new entries may be created or existing entries deleted from this table.')
hpicfLmaProfileTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 4), )
if mibBuilder.loadTexts: hpicfLmaProfileTable.setStatus('current')
if mibBuilder.loadTexts: hpicfLmaProfileTable.setDescription('This is to create the profile which can be associated to a MAC group/MAC address/MAC OUI/MAC mask. A profile is a collection of attributes. Profiles are not applied when hpSwitchAutzUserRoleEnabled is true.')
hpicfLmaProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 4, 1), ).setIndexNames((0, "HP-ICF-LMA-MIB", "hpicfLmaProfileName"))
if mibBuilder.loadTexts: hpicfLmaProfileEntry.setStatus('current')
if mibBuilder.loadTexts: hpicfLmaProfileEntry.setDescription('This is to create the profile which can be associated to a MAC group/MAC address/MAC OUI/MAC mask.A profile is a collection of attributes.')
hpicfLmaProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 4, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: hpicfLmaProfileName.setStatus('current')
if mibBuilder.loadTexts: hpicfLmaProfileName.setDescription('This object contains the name of Local MAC Authentication profile.')
hpicfLmaProfileUntaggedVid = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4094))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfLmaProfileUntaggedVid.setStatus('current')
if mibBuilder.loadTexts: hpicfLmaProfileUntaggedVid.setDescription('Untagged VLAN ID.A value of 0 implies that untagged VLAN ID is not configured for this profile.Only one untagged VLAN ID can be associated with the profile.')
hpicfLmaProfileTaggedVids = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 4, 1, 3), VidList()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfLmaProfileTaggedVids.setStatus('current')
if mibBuilder.loadTexts: hpicfLmaProfileTaggedVids.setDescription('Tagged VLANs.A maximum of 50 tagged VLANs can be can be associated with the profile.')
hpicfLmaProfileCoS = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 4, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 7))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfLmaProfileCoS.setStatus('current')
if mibBuilder.loadTexts: hpicfLmaProfileCoS.setDescription('CoS value to be associated with this profile.A value of -1 indicates that CoS is not configured for this profile.')
hpicfLmaProfileIsAssociated = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 4, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfLmaProfileIsAssociated.setStatus('current')
if mibBuilder.loadTexts: hpicfLmaProfileIsAssociated.setDescription('This object is to check whether any MAC is associated to this profile.A value of TRUE indicates that it is associated to MAC entry and FALSE indicates that it is not associated to any of the MAC entry.')
hpicfLmaProfileRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 4, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfLmaProfileRowStatus.setStatus('current')
if mibBuilder.loadTexts: hpicfLmaProfileRowStatus.setDescription('Status of this row, by which new entries may be created or existing entries deleted from this table.')
hpicfLmaAssociationTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 5), )
if mibBuilder.loadTexts: hpicfLmaAssociationTable.setStatus('current')
if mibBuilder.loadTexts: hpicfLmaAssociationTable.setDescription('This is association table between profile and MAC entries. This table is not used when hpSwitchAutzUserRoleEnabled is true.')
hpicfLmaAssociationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 5, 1), ).setIndexNames((0, "HP-ICF-LMA-MIB", "hpicfLmaProfileName"), (0, "HP-ICF-LMA-MIB", "hpicfLmaAssociationMacType"), (0, "HP-ICF-LMA-MIB", "hpicfLmaAssociationMacValue"))
if mibBuilder.loadTexts: hpicfLmaAssociationEntry.setStatus('current')
if mibBuilder.loadTexts: hpicfLmaAssociationEntry.setDescription('This is association table between the profile and MAC entries.')
hpicfLmaAssociationMacType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("macGrp", 0), ("macAddress", 1), ("macMask", 2), ("macOui", 3))))
if mibBuilder.loadTexts: hpicfLmaAssociationMacType.setStatus('current')
if mibBuilder.loadTexts: hpicfLmaAssociationMacType.setDescription('This object specifies whether the type of MAC address is: macGrp(0) MAC group which contains a group of MAC Entry. macAddress(1) Fully qualified MAC address. macMask(2) MAC address prefix. Only 32 & 40 bits are allowed. macOUI(3) 24 bit organizationally unique identifier.')
hpicfLmaAssociationMacValue = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 5, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: hpicfLmaAssociationMacValue.setStatus('current')
if mibBuilder.loadTexts: hpicfLmaAssociationMacValue.setDescription('This object specifies the MAC value. This value should be in conjunction with hpicfLmaAssociationMacType.')
hpicfLmaAssociationRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 5, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfLmaAssociationRowStatus.setStatus('current')
if mibBuilder.loadTexts: hpicfLmaAssociationRowStatus.setDescription('Status of this row, by which new entries may be created or existing entries deleted from this table.')
hpicfLmaConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 6), )
if mibBuilder.loadTexts: hpicfLmaConfigTable.setStatus('current')
if mibBuilder.loadTexts: hpicfLmaConfigTable.setDescription('A table that contains the configuration objects for Local MAC based Authentication associated with each port. An entry appears in this table for each port that may authenticate access to itself.')
hpicfLmaConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 6, 1), ).setIndexNames((0, "HP-ICF-LMA-MIB", "hpicfLmaPortNumber"))
if mibBuilder.loadTexts: hpicfLmaConfigEntry.setStatus('current')
if mibBuilder.loadTexts: hpicfLmaConfigEntry.setDescription('A table that contains the configuration objects for Local MAC based Authentication associated with each port. An entry appears in this table for each port that may authenticate access to itself.')
hpicfLmaPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 6, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: hpicfLmaPortNumber.setStatus('current')
if mibBuilder.loadTexts: hpicfLmaPortNumber.setDescription('The port number associated with this switch port.')
hpicfLmaClientLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 6, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 256)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfLmaClientLimit.setStatus('current')
if mibBuilder.loadTexts: hpicfLmaClientLimit.setDescription('The maximum number of authenticated clients to allow on the port.')
hpicfLmaQuietPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 6, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfLmaQuietPeriod.setStatus('current')
if mibBuilder.loadTexts: hpicfLmaQuietPeriod.setDescription('Specifies the time, in seconds, that the switch should refrain from re-attempting an authentication request for a client whose credentials were rejected.')
hpicfLmaLogoffPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 6, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 999999999)).clone(300)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfLmaLogoffPeriod.setStatus('current')
if mibBuilder.loadTexts: hpicfLmaLogoffPeriod.setDescription('Specifies the period, in seconds, at which an authenticated client will be considered unauthenticated due to lack of activity (i.e. traffic originating from client).')
hpicfLmaAuthVid = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 6, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4094))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfLmaAuthVid.setStatus('current')
if mibBuilder.loadTexts: hpicfLmaAuthVid.setDescription("Specifies the port VID (PVID) that should be used for an authenticated client. When hpSwitchAutzUserRoleEnabled is true, this value may be superseded by the value of hpSwitchAutzUserRoleVlanId or hpSwitchAutzUserRoleVlanName from the client's assigned role. ")
hpicfLmaUnauthVid = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 6, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4094))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfLmaUnauthVid.setStatus('current')
if mibBuilder.loadTexts: hpicfLmaUnauthVid.setDescription('Specifies the port VID (PVID) that should be used for an unauthenticated client. When hpSwitchAutzUserRoleEnabled is true, this value may be superseded by the value of hpSwitchAutzUserRoleVlanId or hpSwitchAutzUserRoleVlanName from the role identified by hpSwitchAutzUserRoleInitialRoleName.')
hpicfLmaUnAuthPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 6, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfLmaUnAuthPeriod.setStatus('current')
if mibBuilder.loadTexts: hpicfLmaUnAuthPeriod.setDescription('Specifies the period, in seconds, at which a client will be placed into guest vlan, or assigned the role identified by hpSwitchAutzUserRoleInitialRoleName when hpSwitchAutzUserRoleEnabled is true, if it fails authentication.')
hpicfLmaReauthenticate = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 6, 1, 10), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfLmaReauthenticate.setStatus('current')
if mibBuilder.loadTexts: hpicfLmaReauthenticate.setDescription('The reauthentication control for this port. Setting this attribute TRUE forces all authenticated clients to re-authenticate themselves. Setting this attribute FALSE has no effect. This attribute always returns FALSE when read.')
hpicfLmaMacPin = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 6, 1, 11), TruthValue().clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfLmaMacPin.setStatus('current')
if mibBuilder.loadTexts: hpicfLmaMacPin.setDescription('Enables MAC-Pinning on this port. Setting this attribute TRUE pins the authenticated MAC addresses to the Mac address table. Authenticated clients will not be de-authenticated even when clients are inactive throughout the logoff period.')
hpicfLmaUserRoleAssociationTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 7), )
if mibBuilder.loadTexts: hpicfLmaUserRoleAssociationTable.setStatus('current')
if mibBuilder.loadTexts: hpicfLmaUserRoleAssociationTable.setDescription('A table of associations between user role and MAC entries.')
hpicfLmaUserRoleAssociationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 7, 1), ).setIndexNames((0, "HP-ICF-LMA-MIB", "hpicfLmaUserRoleAssociationName"), (0, "HP-ICF-LMA-MIB", "hpicfLmaUserRoleAssociationMacType"), (0, "HP-ICF-LMA-MIB", "hpicfLmaUserRoleAssociationMacValue"))
if mibBuilder.loadTexts: hpicfLmaUserRoleAssociationEntry.setStatus('current')
if mibBuilder.loadTexts: hpicfLmaUserRoleAssociationEntry.setDescription('The association table entry.')
hpicfLmaUserRoleAssociationName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 7, 1, 1), HpAutzUserRoleName())
if mibBuilder.loadTexts: hpicfLmaUserRoleAssociationName.setStatus('current')
if mibBuilder.loadTexts: hpicfLmaUserRoleAssociationName.setDescription('The name of this user role.')
hpicfLmaUserRoleAssociationMacType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 7, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("macGrp", 0), ("macAddress", 1), ("macMask", 2), ("macOui", 3))))
if mibBuilder.loadTexts: hpicfLmaUserRoleAssociationMacType.setStatus('current')
if mibBuilder.loadTexts: hpicfLmaUserRoleAssociationMacType.setDescription('This object specifies whether the type of MAC address is: macGrp(0) MAC group which contains a group of MAC Entry. macAddress(1) Fully qualified MAC address. macMask(2) MAC address prefix. Only 32 & 40 bits are allowed. macOUI(3) 24 bit organizationally unique identifier.')
hpicfLmaUserRoleAssociationMacValue = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 7, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: hpicfLmaUserRoleAssociationMacValue.setStatus('current')
if mibBuilder.loadTexts: hpicfLmaUserRoleAssociationMacValue.setDescription('This object specifies the MAC value. This value should be used in conjunction with the hpicfLmaUserRoleAssociationMacType.')
hpicfLmaUserRoleAssociationRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 7, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfLmaUserRoleAssociationRowStatus.setStatus('current')
if mibBuilder.loadTexts: hpicfLmaUserRoleAssociationRowStatus.setDescription('Status of this row, by which new entries may be created or existing entries deleted from this table.')
hpicfLmaAssocActiveTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 2, 2), )
if mibBuilder.loadTexts: hpicfLmaAssocActiveTable.setStatus('current')
if mibBuilder.loadTexts: hpicfLmaAssocActiveTable.setDescription('This is an association table to display all the MAC clients that are active for a given profile.')
hpicfLmaAssocActiveEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 2, 2, 1), ).setIndexNames((0, "HP-ICF-LMA-MIB", "hpicfLmaAssocActiveProfileName"), (0, "HP-ICF-LMA-MIB", "hpicfLmaAssocActiveMacAddress"))
if mibBuilder.loadTexts: hpicfLmaAssocActiveEntry.setStatus('current')
if mibBuilder.loadTexts: hpicfLmaAssocActiveEntry.setDescription('This is an association table to display all the MAC clients that are active for a given profile.')
hpicfLmaAssocActiveProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 2, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: hpicfLmaAssocActiveProfileName.setStatus('current')
if mibBuilder.loadTexts: hpicfLmaAssocActiveProfileName.setDescription('This object contains the name of Local MAC authentication profile.')
hpicfLmaAssocActiveMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 2, 2, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfLmaAssocActiveMacAddress.setStatus('current')
if mibBuilder.loadTexts: hpicfLmaAssocActiveMacAddress.setDescription('This object specifies the MAC address of the client.')
hpicfLmaSessionStatsTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 2, 1), )
if mibBuilder.loadTexts: hpicfLmaSessionStatsTable.setStatus('current')
if mibBuilder.loadTexts: hpicfLmaSessionStatsTable.setDescription('A table that contains session statistic objects for each client (i.e. user) attempting to authenticate to a port with MAC authentication enabled. An entry appears in this table for each port in the switch.')
hpicfLmaSessionStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 2, 1, 1), ).setIndexNames((0, "HP-ICF-LMA-MIB", "hpicfLmaPortNumber"), (0, "HP-ICF-LMA-MIB", "hpicfLmaSessionMacAddr"))
if mibBuilder.loadTexts: hpicfLmaSessionStatsEntry.setStatus('current')
if mibBuilder.loadTexts: hpicfLmaSessionStatsEntry.setDescription('The session statistics information for a port with MAC based authentication enabled. This shows the current values being collected for active sessions.')
hpicfLmaSessionMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 2, 1, 1, 1), MacAddress())
if mibBuilder.loadTexts: hpicfLmaSessionMacAddr.setStatus('current')
if mibBuilder.loadTexts: hpicfLmaSessionMacAddr.setDescription('This object specifies the MAC address of the client.')
hpicfLmaSessionState = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("authenticated", 1), ("unauthenticated", 2), ("authenticating", 3), ("authReqRejectNoVlan", 4), ("authReqRejectUnauthVlan", 5), ("authReqTimeoutNoVlan", 6), ("authReqTimeoutUnauthVlan", 7), ("initialRole", 8), ("initialRoleFailed", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfLmaSessionState.setStatus('current')
if mibBuilder.loadTexts: hpicfLmaSessionState.setDescription("Specifies the state of the client as follows: 'authenticated' - authenticated client 'unauthenticated' - unauthenticated client, waiting for credentials 'authenticating' - credentials have been sent for verification, waiting for response 'authReqRejectNoVlan' - credentials invalid; client does not have access to unauthenticated VLAN 'authReqRejectUnauthVlan' - credentials invalid; client does have access to unauthenticated VLAN 'authReqTimeoutNoVlan' - credentials could not be verified; client is still unauthenticated and does not have access to unauthenticated VLAN 'authReqTimeoutUnauthVlan' - credentials could not be verified; client is still unauthenticated, but has access to unauthenticated VLAN 'initialRole' - client is assigned the initial role 'initialRoleFailed' - initial role could not be applied; client does not have access to the network")
hpicfLmaSessionStateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 2, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfLmaSessionStateTime.setStatus('current')
if mibBuilder.loadTexts: hpicfLmaSessionStateTime.setDescription('The duration, in seconds, a client has spent in the state specified by hpicfLmaSessionState.')
hpicfLmaSessionAuthVid = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4094))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfLmaSessionAuthVid.setStatus('current')
if mibBuilder.loadTexts: hpicfLmaSessionAuthVid.setDescription('This object specifies the PVID that the authenticated client is utilizing. If the client is unauthenticated, this object has no meaning.')
hpicfLmaSessionUnauthVid = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4094))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfLmaSessionUnauthVid.setStatus('current')
if mibBuilder.loadTexts: hpicfLmaSessionUnauthVid.setDescription('This object specifies the PVID that the unauthenticated client is utilizing. If the client is authenticated, this object has no meaning.')
hpicfLmaSessionUsrNumberCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfLmaSessionUsrNumberCnt.setStatus('current')
if mibBuilder.loadTexts: hpicfLmaSessionUsrNumberCnt.setDescription('This object specifies the number of authenticated clients currently present on this port. This does not include the clients that are under the process of authentication.')
hpicfLmaSessionUserRole = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 2, 1, 1, 7), HpAutzUserRoleName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfLmaSessionUserRole.setStatus('current')
if mibBuilder.loadTexts: hpicfLmaSessionUserRole.setDescription('When hpSwitchAutzUserRoleEnabled is true, specifies the user role of the client.')
hpicfLmaCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 2, 1))
hpicfLmaGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 2, 2))
hpicfLmaCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 2, 1, 1)).setObjects(("HP-ICF-LMA-MIB", "hpicfLmaMacGroup"), ("HP-ICF-LMA-MIB", "hpicfLmaConfigGroup"), ("HP-ICF-LMA-MIB", "hpicfLmaSessionStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfLmaCompliance1 = hpicfLmaCompliance1.setStatus('deprecated')
if mibBuilder.loadTexts: hpicfLmaCompliance1.setDescription('The compliance statement')
hpicfLmaCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 2, 1, 2)).setObjects(("HP-ICF-LMA-MIB", "hpicfLmaMacGroup1"), ("HP-ICF-LMA-MIB", "hpicfLmaConfigGroup1"), ("HP-ICF-LMA-MIB", "hpicfLmaSessionStatsGroup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfLmaCompliance2 = hpicfLmaCompliance2.setStatus('deprecated')
if mibBuilder.loadTexts: hpicfLmaCompliance2.setDescription('The compliance statement')
hpicfLmaCompliance3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 2, 1, 3)).setObjects(("HP-ICF-LMA-MIB", "hpicfLmaMacGroup1"), ("HP-ICF-LMA-MIB", "hpicfLmaConfigGroup2"), ("HP-ICF-LMA-MIB", "hpicfLmaSessionStatsGroup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfLmaCompliance3 = hpicfLmaCompliance3.setStatus('current')
if mibBuilder.loadTexts: hpicfLmaCompliance3.setDescription('The compliance statement')
hpicfLmaMacGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 2, 2, 1)).setObjects(("HP-ICF-LMA-MIB", "hpicfLmaMacGrpRowStatus"), ("HP-ICF-LMA-MIB", "hpicfLmaMacRowStatus"), ("HP-ICF-LMA-MIB", "hpicfLmaProfileUntaggedVid"), ("HP-ICF-LMA-MIB", "hpicfLmaProfileTaggedVids"), ("HP-ICF-LMA-MIB", "hpicfLmaProfileCoS"), ("HP-ICF-LMA-MIB", "hpicfLmaProfileIsAssociated"), ("HP-ICF-LMA-MIB", "hpicfLmaProfileRowStatus"), ("HP-ICF-LMA-MIB", "hpicfLmaAssociationRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfLmaMacGroup = hpicfLmaMacGroup.setStatus('deprecated')
if mibBuilder.loadTexts: hpicfLmaMacGroup.setDescription('These objects are used for managing Local MAC Authentication configuration parameters.')
hpicfLmaConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 2, 2, 2)).setObjects(("HP-ICF-LMA-MIB", "hpicfLmaClientLimit"), ("HP-ICF-LMA-MIB", "hpicfLmaQuietPeriod"), ("HP-ICF-LMA-MIB", "hpicfLmaLogoffPeriod"), ("HP-ICF-LMA-MIB", "hpicfLmaAuthVid"), ("HP-ICF-LMA-MIB", "hpicfLmaUnauthVid"), ("HP-ICF-LMA-MIB", "hpicfLmaUnAuthPeriod"), ("HP-ICF-LMA-MIB", "hpicfLmaReauthenticate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfLmaConfigGroup = hpicfLmaConfigGroup.setStatus('deprecated')
if mibBuilder.loadTexts: hpicfLmaConfigGroup.setDescription('A collection of objects providing configuration objects for Local MAC authentication associated with each port.')
hpicfLmaSessionStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 2, 2, 3)).setObjects(("HP-ICF-LMA-MIB", "hpicfLmaAssocActiveMacAddress"), ("HP-ICF-LMA-MIB", "hpicfLmaSessionState"), ("HP-ICF-LMA-MIB", "hpicfLmaSessionStateTime"), ("HP-ICF-LMA-MIB", "hpicfLmaSessionAuthVid"), ("HP-ICF-LMA-MIB", "hpicfLmaSessionUnauthVid"), ("HP-ICF-LMA-MIB", "hpicfLmaSessionUsrNumberCnt"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfLmaSessionStatsGroup = hpicfLmaSessionStatsGroup.setStatus('deprecated')
if mibBuilder.loadTexts: hpicfLmaSessionStatsGroup.setDescription('A collection of objects providing statistics about current sessions for Local MAC authentication.')
hpicfLmaMacGroup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 2, 2, 4)).setObjects(("HP-ICF-LMA-MIB", "hpicfLmaMacGrpRowStatus"), ("HP-ICF-LMA-MIB", "hpicfLmaMacRowStatus"), ("HP-ICF-LMA-MIB", "hpicfLmaProfileUntaggedVid"), ("HP-ICF-LMA-MIB", "hpicfLmaProfileTaggedVids"), ("HP-ICF-LMA-MIB", "hpicfLmaProfileCoS"), ("HP-ICF-LMA-MIB", "hpicfLmaProfileIsAssociated"), ("HP-ICF-LMA-MIB", "hpicfLmaProfileRowStatus"), ("HP-ICF-LMA-MIB", "hpicfLmaAssociationRowStatus"), ("HP-ICF-LMA-MIB", "hpicfLmaUserRoleAssociationRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfLmaMacGroup1 = hpicfLmaMacGroup1.setStatus('current')
if mibBuilder.loadTexts: hpicfLmaMacGroup1.setDescription('These objects are used for managing Local MAC Authentication configuration parameters.')
hpicfLmaConfigGroup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 2, 2, 5)).setObjects(("HP-ICF-LMA-MIB", "hpicfLmaClientLimit"), ("HP-ICF-LMA-MIB", "hpicfLmaQuietPeriod"), ("HP-ICF-LMA-MIB", "hpicfLmaLogoffPeriod"), ("HP-ICF-LMA-MIB", "hpicfLmaAuthVid"), ("HP-ICF-LMA-MIB", "hpicfLmaUnauthVid"), ("HP-ICF-LMA-MIB", "hpicfLmaUnAuthPeriod"), ("HP-ICF-LMA-MIB", "hpicfLmaReauthenticate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfLmaConfigGroup1 = hpicfLmaConfigGroup1.setStatus('deprecated')
if mibBuilder.loadTexts: hpicfLmaConfigGroup1.setDescription('A collection of objects providing configuration objects for Local MAC authentication associated with each port.')
hpicfLmaSessionStatsGroup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 2, 2, 6)).setObjects(("HP-ICF-LMA-MIB", "hpicfLmaAssocActiveMacAddress"), ("HP-ICF-LMA-MIB", "hpicfLmaSessionState"), ("HP-ICF-LMA-MIB", "hpicfLmaSessionStateTime"), ("HP-ICF-LMA-MIB", "hpicfLmaSessionAuthVid"), ("HP-ICF-LMA-MIB", "hpicfLmaSessionUnauthVid"), ("HP-ICF-LMA-MIB", "hpicfLmaSessionUsrNumberCnt"), ("HP-ICF-LMA-MIB", "hpicfLmaSessionUserRole"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfLmaSessionStatsGroup1 = hpicfLmaSessionStatsGroup1.setStatus('current')
if mibBuilder.loadTexts: hpicfLmaSessionStatsGroup1.setDescription('A collection of objects providing statistics about current sessions for Local MAC authentication.')
hpicfLmaConfigGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 2, 2, 7)).setObjects(("HP-ICF-LMA-MIB", "hpicfLmaClientLimit"), ("HP-ICF-LMA-MIB", "hpicfLmaQuietPeriod"), ("HP-ICF-LMA-MIB", "hpicfLmaLogoffPeriod"), ("HP-ICF-LMA-MIB", "hpicfLmaAuthVid"), ("HP-ICF-LMA-MIB", "hpicfLmaUnauthVid"), ("HP-ICF-LMA-MIB", "hpicfLmaUnAuthPeriod"), ("HP-ICF-LMA-MIB", "hpicfLmaReauthenticate"), ("HP-ICF-LMA-MIB", "hpicfLmaMacPin"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfLmaConfigGroup2 = hpicfLmaConfigGroup2.setStatus('current')
if mibBuilder.loadTexts: hpicfLmaConfigGroup2.setDescription('A collection of objects providing configuration objects for Local MAC authentication associated with each port.')
mibBuilder.exportSymbols("HP-ICF-LMA-MIB", hpicfLmaUserRoleAssociationTable=hpicfLmaUserRoleAssociationTable, hpicfLmaConfigTable=hpicfLmaConfigTable, hpicfLmaUserRoleAssociationName=hpicfLmaUserRoleAssociationName, hpicfLmaAssocActiveTable=hpicfLmaAssocActiveTable, hpicfLmaSessionStatsEntry=hpicfLmaSessionStatsEntry, hpicfLmaSessionState=hpicfLmaSessionState, hpicfLmaQuietPeriod=hpicfLmaQuietPeriod, hpicfLmaCompliance2=hpicfLmaCompliance2, hpicfLmaAssocActiveProfileName=hpicfLmaAssocActiveProfileName, hpicfLmaProfileName=hpicfLmaProfileName, hpicfLmaProfileUntaggedVid=hpicfLmaProfileUntaggedVid, PYSNMP_MODULE_ID=hpicfLmaMIB, hpicfLmaProfileRowStatus=hpicfLmaProfileRowStatus, hpicfLmaMacGrpRowStatus=hpicfLmaMacGrpRowStatus, hpicfLmaUserRoleAssociationRowStatus=hpicfLmaUserRoleAssociationRowStatus, hpicfLmaAssocActiveEntry=hpicfLmaAssocActiveEntry, hpicfLmaProfileTable=hpicfLmaProfileTable, hpicfLmaMacGroup=hpicfLmaMacGroup, hpicfLmaSessionStatsGroup=hpicfLmaSessionStatsGroup, hpicfLmaConformance=hpicfLmaConformance, hpicfLmaMacEntry=hpicfLmaMacEntry, hpicfLmaGroups=hpicfLmaGroups, hpicfLmaCompliances=hpicfLmaCompliances, hpicfLmaMacGroup1=hpicfLmaMacGroup1, hpicfLmaMacPin=hpicfLmaMacPin, hpicfLmaAssociationTable=hpicfLmaAssociationTable, hpicfLmaConfigGroup=hpicfLmaConfigGroup, hpicfLmaSessionAuthVid=hpicfLmaSessionAuthVid, hpicfLmaCompliance3=hpicfLmaCompliance3, hpicfLmaProfileCoS=hpicfLmaProfileCoS, hpicfLmaAssociationMacValue=hpicfLmaAssociationMacValue, hpicfLmaSessionMacAddr=hpicfLmaSessionMacAddr, hpicfLmaAssocActiveMacAddress=hpicfLmaAssocActiveMacAddress, hpicfLmaConfigGroup1=hpicfLmaConfigGroup1, hpicfLmaObjects=hpicfLmaObjects, hpicfLmaAuthVid=hpicfLmaAuthVid, hpicfLmaConfigEntry=hpicfLmaConfigEntry, hpicfLmaAssociationRowStatus=hpicfLmaAssociationRowStatus, hpicfLmaMacGrpTable=hpicfLmaMacGrpTable, hpicfLmaSessionStatsGroup1=hpicfLmaSessionStatsGroup1, hpicfLmaClientLimit=hpicfLmaClientLimit, hpicfLmaProfileEntry=hpicfLmaProfileEntry, hpicfLmaAssociationMacType=hpicfLmaAssociationMacType, hpicfLmaUserRoleAssociationEntry=hpicfLmaUserRoleAssociationEntry, hpicfLmaMacValue=hpicfLmaMacValue, hpicfLmaProfileTaggedVids=hpicfLmaProfileTaggedVids, hpicfLmaConfigObjects=hpicfLmaConfigObjects, hpicfLmaMIB=hpicfLmaMIB, hpicfLmaUserRoleAssociationMacType=hpicfLmaUserRoleAssociationMacType, hpicfLmaUserRoleAssociationMacValue=hpicfLmaUserRoleAssociationMacValue, hpicfLmaConfigGroup2=hpicfLmaConfigGroup2, hpicfLmaReauthenticate=hpicfLmaReauthenticate, hpicfLmaNotifications=hpicfLmaNotifications, hpicfLmaMacType=hpicfLmaMacType, hpicfLmaSessionUnauthVid=hpicfLmaSessionUnauthVid, hpicfLmaSessionStatsTable=hpicfLmaSessionStatsTable, hpicfLmaScalarObjects=hpicfLmaScalarObjects, hpicfLmaLogoffPeriod=hpicfLmaLogoffPeriod, hpicfLmaSessionUsrNumberCnt=hpicfLmaSessionUsrNumberCnt, hpicfLmaSessionUserRole=hpicfLmaSessionUserRole, hpicfLmaStatsObjects=hpicfLmaStatsObjects, hpicfLmaPortNumber=hpicfLmaPortNumber, hpicfLmaUnAuthPeriod=hpicfLmaUnAuthPeriod, hpicfLmaAssociationEntry=hpicfLmaAssociationEntry, hpicfLmaMacTable=hpicfLmaMacTable, hpicfLmaMacRowStatus=hpicfLmaMacRowStatus, hpicfLmaMacGrpName=hpicfLmaMacGrpName, hpicfLmaMacGrpEntry=hpicfLmaMacGrpEntry, hpicfLmaProfileIsAssociated=hpicfLmaProfileIsAssociated, hpicfLmaCompliance1=hpicfLmaCompliance1, hpicfLmaUnauthVid=hpicfLmaUnauthVid, hpicfLmaSessionStateTime=hpicfLmaSessionStateTime)
