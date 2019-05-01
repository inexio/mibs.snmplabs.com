#
# PySNMP MIB module Unisphere-Data-PROFILE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-PROFILE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:32:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Gauge32, ModuleIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, IpAddress, iso, Counter32, NotificationType, Counter64, MibIdentifier, Integer32, Bits, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ModuleIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "IpAddress", "iso", "Counter32", "NotificationType", "Counter64", "MibIdentifier", "Integer32", "Bits", "TimeTicks")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
usDataMibs, = mibBuilder.importSymbols("Unisphere-Data-MIBs", "usDataMibs")
usdProfileMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 25))
usdProfileMIB.setRevisions(('2002-11-19 20:47', '2001-04-04 12:50', '2000-04-20 00:00', '1999-06-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: usdProfileMIB.setRevisionsDescriptions(('Added bridgedEthernet(19) to UsdProfileIfEncaps TEXTUAL-CONVENTION.', 'Added ppp(1), pppoe(17) and any(127) to UsdProfileIfEncaps TEXTUAL-CONVENTION.', 'Added usdProfAssignIfTable, usdProfToIfMapTable to configure and report assignments of profiles to interface/encapsulation pairs.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: usdProfileMIB.setLastUpdated('200211192047Z')
if mibBuilder.loadTexts: usdProfileMIB.setOrganization('Unisphere Networks, Inc.')
if mibBuilder.loadTexts: usdProfileMIB.setContactInfo(' Unisphere Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886 USA Tel: +1 978 589 5800 Email: mib@UnisphereNetworks.com')
if mibBuilder.loadTexts: usdProfileMIB.setDescription('The Profile MIB for the Unisphere Networks Inc. enterprise.')
class UsdProfileIfEncaps(TextualConvention, Integer32):
    description = "Encapsulated protocol type. The 'any' value is a wildcard value. The DESCRIPTION clause for an object having this syntax must describe how the 'any' value applies, if at all."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 17, 19, 127))
    namedValues = NamedValues(("ip", 0), ("ppp", 1), ("pppoe", 17), ("bridgedEthernet", 19), ("any", 127))

usdProfileObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1))
usdProfileName = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 1))
usdProfileAssign = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 2))
usdProfileNameTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 1, 1), )
if mibBuilder.loadTexts: usdProfileNameTable.setStatus('current')
if mibBuilder.loadTexts: usdProfileNameTable.setDescription('The entries in this table provide mappings of configuration profile names to local integer identifiers for those profiles. These integers are used as indexes into other MIB tables containing profile configuration parameters associated with the same profile name.')
usdProfileNameEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 1, 1, 1), ).setIndexNames((1, "Unisphere-Data-PROFILE-MIB", "usdProfileNameName"))
if mibBuilder.loadTexts: usdProfileNameEntry.setStatus('current')
if mibBuilder.loadTexts: usdProfileNameEntry.setDescription('A mapping of a profile name to an integer identifier for that name.')
usdProfileNameName = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdProfileNameName.setStatus('current')
if mibBuilder.loadTexts: usdProfileNameName.setDescription('The profile name uniquely identifying this entry.')
usdProfileNameRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 1, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdProfileNameRowStatus.setStatus('current')
if mibBuilder.loadTexts: usdProfileNameRowStatus.setDescription("Controls creation/deletion of entries in this table. Only the values 'createAndGo' and 'destroy' may be SET.")
usdProfileNameId = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 1, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdProfileNameId.setStatus('current')
if mibBuilder.loadTexts: usdProfileNameId.setDescription('The integer identifier associated with this profile name. This value of this identifier is assigned by the device when an entry in this table is created.')
usdProfileIdTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 1, 2), )
if mibBuilder.loadTexts: usdProfileIdTable.setStatus('current')
if mibBuilder.loadTexts: usdProfileIdTable.setDescription('Provides inverse mapping of profile IDs to profile names.')
usdProfileIdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 1, 2, 1), ).setIndexNames((0, "Unisphere-Data-PROFILE-MIB", "usdProfileIdId"))
if mibBuilder.loadTexts: usdProfileIdEntry.setStatus('current')
if mibBuilder.loadTexts: usdProfileIdEntry.setDescription('A mapping of an integer identifier to a profile name.')
usdProfileIdId = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 1, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: usdProfileIdId.setStatus('current')
if mibBuilder.loadTexts: usdProfileIdId.setDescription('The integer identifier associated with this profile name.')
usdProfileIdName = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdProfileIdName.setStatus('current')
if mibBuilder.loadTexts: usdProfileIdName.setDescription('The profile name having the associated identifier.')
usdProfAssignIf = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 2, 1))
usdProfAssignIfTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 2, 1, 1), )
if mibBuilder.loadTexts: usdProfAssignIfTable.setStatus('current')
if mibBuilder.loadTexts: usdProfAssignIfTable.setDescription('Table providing profile assignment to interface/encapsulation pair. The entries in this table specify which profile to use when creating and configuring a dynamic interface (whose type is identified by the encapsulation) above a specified interface.')
usdProfAssignIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 2, 1, 1, 1), ).setIndexNames((0, "Unisphere-Data-PROFILE-MIB", "usdProfAssignIfIndex"), (0, "Unisphere-Data-PROFILE-MIB", "usdProfAssignIfEncaps"))
if mibBuilder.loadTexts: usdProfAssignIfEntry.setStatus('current')
if mibBuilder.loadTexts: usdProfAssignIfEntry.setDescription('An assignment of a profile to an interface/encapsulation pair.')
usdProfAssignIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 2, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: usdProfAssignIfIndex.setStatus('current')
if mibBuilder.loadTexts: usdProfAssignIfIndex.setDescription('The ifIndex of the interface to which the profile is assigned.')
usdProfAssignIfEncaps = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 2, 1, 1, 1, 2), UsdProfileIfEncaps())
if mibBuilder.loadTexts: usdProfAssignIfEncaps.setStatus('current')
if mibBuilder.loadTexts: usdProfAssignIfEncaps.setDescription("The encapsulated protocol type to which the assigned profile pertains. An interface may have a different profile assigned for each encapsulation it supports. If an entry for a specific encapsulation is absent, the profile assigned for the 'any' encapsulation will be used (if that assignment is present in this table).")
usdProfAssignIfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 2, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdProfAssignIfRowStatus.setStatus('current')
if mibBuilder.loadTexts: usdProfAssignIfRowStatus.setDescription('For SET, supports only createAndGo(4) and destroy(6). Returns active(1) when read.')
usdProfAssignIfProfileId = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 2, 1, 1, 1, 4), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdProfAssignIfProfileId.setStatus('current')
if mibBuilder.loadTexts: usdProfAssignIfProfileId.setDescription('The ID of the profile assigned to this interface/encapsulation pair.')
usdProfToIfMapTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 2, 1, 2), )
if mibBuilder.loadTexts: usdProfToIfMapTable.setStatus('current')
if mibBuilder.loadTexts: usdProfToIfMapTable.setDescription('Table to report the set of interface/encapsulation pairs assigned to each profile.')
usdProfToIfMapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 2, 1, 2, 1), ).setIndexNames((0, "Unisphere-Data-PROFILE-MIB", "usdProfToIfMapProfileId"), (0, "Unisphere-Data-PROFILE-MIB", "usdProfToIfMapIndex"), (0, "Unisphere-Data-PROFILE-MIB", "usdProfToIfMapEncaps"))
if mibBuilder.loadTexts: usdProfToIfMapEntry.setStatus('current')
if mibBuilder.loadTexts: usdProfToIfMapEntry.setDescription('Reports an interface/encapsulation pair assigned to a profile.')
usdProfToIfMapProfileId = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 2, 1, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: usdProfToIfMapProfileId.setStatus('current')
if mibBuilder.loadTexts: usdProfToIfMapProfileId.setDescription('The ID of the profile assigned to this interface/encapsulation pair.')
usdProfToIfMapIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 2, 1, 2, 1, 2), InterfaceIndex())
if mibBuilder.loadTexts: usdProfToIfMapIndex.setStatus('current')
if mibBuilder.loadTexts: usdProfToIfMapIndex.setDescription('The ifIndex of the interface to which the profile is assigned.')
usdProfToIfMapEncaps = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 2, 1, 2, 1, 3), UsdProfileIfEncaps()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdProfToIfMapEncaps.setStatus('current')
if mibBuilder.loadTexts: usdProfToIfMapEncaps.setDescription('The encapsulation type to which the assigned profile pertains. An interface may have a different profile assigned for each encapsulation type it supports.')
usdProfileMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 4))
usdProfileMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 4, 1))
usdProfileMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 4, 2))
usdProfileCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 4, 1, 1)).setObjects(("Unisphere-Data-PROFILE-MIB", "usdProfileGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdProfileCompliance = usdProfileCompliance.setStatus('obsolete')
if mibBuilder.loadTexts: usdProfileCompliance.setDescription('Obsolete compliance statement for systems supporting naming of configuration profiles. This statement became obsolete when the interface profile assignment group was added.')
usdProfileCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 4, 1, 2)).setObjects(("Unisphere-Data-PROFILE-MIB", "usdProfileGroup"), ("Unisphere-Data-PROFILE-MIB", "usdProfileIfGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdProfileCompliance2 = usdProfileCompliance2.setStatus('current')
if mibBuilder.loadTexts: usdProfileCompliance2.setDescription('The compliance statement for systems supporting naming of configuration profiles and profile assignment to interfaces.')
usdProfileGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 4, 2, 1)).setObjects(("Unisphere-Data-PROFILE-MIB", "usdProfileNameName"), ("Unisphere-Data-PROFILE-MIB", "usdProfileNameRowStatus"), ("Unisphere-Data-PROFILE-MIB", "usdProfileNameId"), ("Unisphere-Data-PROFILE-MIB", "usdProfileIdName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdProfileGroup = usdProfileGroup.setStatus('current')
if mibBuilder.loadTexts: usdProfileGroup.setDescription('The basic collection of objects providing management of Profile naming functionality in a Unisphere product.')
usdProfileIfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 4, 2, 2)).setObjects(("Unisphere-Data-PROFILE-MIB", "usdProfAssignIfRowStatus"), ("Unisphere-Data-PROFILE-MIB", "usdProfAssignIfProfileId"), ("Unisphere-Data-PROFILE-MIB", "usdProfToIfMapEncaps"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdProfileIfGroup = usdProfileIfGroup.setStatus('current')
if mibBuilder.loadTexts: usdProfileIfGroup.setDescription('The basic collection of objects providing management of Profile assignment to interfaces in a Unisphere product.')
mibBuilder.exportSymbols("Unisphere-Data-PROFILE-MIB", usdProfileObjects=usdProfileObjects, UsdProfileIfEncaps=UsdProfileIfEncaps, usdProfileGroup=usdProfileGroup, usdProfAssignIfIndex=usdProfAssignIfIndex, usdProfileMIB=usdProfileMIB, usdProfAssignIf=usdProfAssignIf, usdProfileIdEntry=usdProfileIdEntry, usdProfileName=usdProfileName, PYSNMP_MODULE_ID=usdProfileMIB, usdProfAssignIfTable=usdProfAssignIfTable, usdProfileNameId=usdProfileNameId, usdProfToIfMapProfileId=usdProfToIfMapProfileId, usdProfileMIBCompliances=usdProfileMIBCompliances, usdProfileIfGroup=usdProfileIfGroup, usdProfileIdName=usdProfileIdName, usdProfAssignIfRowStatus=usdProfAssignIfRowStatus, usdProfileIdId=usdProfileIdId, usdProfileMIBGroups=usdProfileMIBGroups, usdProfToIfMapIndex=usdProfToIfMapIndex, usdProfileAssign=usdProfileAssign, usdProfToIfMapTable=usdProfToIfMapTable, usdProfToIfMapEncaps=usdProfToIfMapEncaps, usdProfileCompliance=usdProfileCompliance, usdProfAssignIfProfileId=usdProfAssignIfProfileId, usdProfAssignIfEntry=usdProfAssignIfEntry, usdProfileIdTable=usdProfileIdTable, usdProfToIfMapEntry=usdProfToIfMapEntry, usdProfileCompliance2=usdProfileCompliance2, usdProfileNameName=usdProfileNameName, usdProfileNameEntry=usdProfileNameEntry, usdProfAssignIfEncaps=usdProfAssignIfEncaps, usdProfileNameRowStatus=usdProfileNameRowStatus, usdProfileMIBConformance=usdProfileMIBConformance, usdProfileNameTable=usdProfileNameTable)
