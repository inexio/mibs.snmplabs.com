#
# PySNMP MIB module Juniper-BRIDGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-BRIDGE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:01:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
InterfaceIndex, InterfaceIndexOrZero = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "InterfaceIndexOrZero")
juniMibs, = mibBuilder.importSymbols("Juniper-MIBs", "juniMibs")
JuniNextIfIndex, = mibBuilder.importSymbols("Juniper-TC", "JuniNextIfIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, NotificationType, Unsigned32, Gauge32, TimeTicks, MibIdentifier, iso, IpAddress, ModuleIdentity, Counter32, Bits, Integer32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "NotificationType", "Unsigned32", "Gauge32", "TimeTicks", "MibIdentifier", "iso", "IpAddress", "ModuleIdentity", "Counter32", "Bits", "Integer32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, RowStatus, MacAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "MacAddress", "TextualConvention")
juniBridgeMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 63))
juniBridgeMIB.setRevisions(('2003-11-04 20:39', '2002-09-16 21:44',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniBridgeMIB.setRevisionsDescriptions(('Import MacAddress from SNMPv2-TC.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: juniBridgeMIB.setLastUpdated('200311042039Z')
if mibBuilder.loadTexts: juniBridgeMIB.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniBridgeMIB.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniBridgeMIB.setDescription('The Bridge MIB for the Juniper enterprise.')
juniBridgeIfLayer = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 63, 1))
juniBridgeAgeLayer = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 63, 2))
juniBridgeMiscCounters = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 63, 3))
juniBridgeIfNextIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 63, 1, 1), JuniNextIfIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniBridgeIfNextIfIndex.setStatus('current')
if mibBuilder.loadTexts: juniBridgeIfNextIfIndex.setDescription('Coordinate ifIndex value allocation for entries in juniBridgeIfTable. A GET of this object returns the next available ifIndex value to be used to create an entry in the associated interface table; or zero, if no valid ifIndex value is available. This object also returns a value of zero when it is the lexicographic successor of a varbind presented in an SNMP GETNEXT or GETBULK request, for which circumstance it is assumed that ifIndex allocation is unintended. Successive GETs will typically return different values, thus avoiding collisions among cooperating management clients seeking to create table entries simultaneously.')
juniBridgeIfTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 63, 1, 2), )
if mibBuilder.loadTexts: juniBridgeIfTable.setStatus('current')
if mibBuilder.loadTexts: juniBridgeIfTable.setDescription('This table contains entries for Bridge interfaces present in the system.')
juniBridgeIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 63, 1, 2, 1), ).setIndexNames((0, "Juniper-BRIDGE-MIB", "juniBridgeIfIndex"))
if mibBuilder.loadTexts: juniBridgeIfEntry.setStatus('current')
if mibBuilder.loadTexts: juniBridgeIfEntry.setDescription('Each entry describes the characteristics of a Bridge interface. Creating/deleting entries in this table causes corresponding entries for be created/deleted in ifTable/ifXTable/juniIfTable.')
juniBridgeIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 63, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: juniBridgeIfIndex.setStatus('current')
if mibBuilder.loadTexts: juniBridgeIfIndex.setDescription('The ifIndex of the Bridge interface. When creating entries in this table, suitable values for this object are determined by reading juniBridgeIfNextIfIndex.')
juniBridgeIfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 63, 1, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniBridgeIfRowStatus.setStatus('current')
if mibBuilder.loadTexts: juniBridgeIfRowStatus.setDescription('Controls creation/deletion of entries in this table according to the RowStatus textual convention, constrained to support the following values only: createAndGo destroy To create an entry in this table, the following entry objects MUST be explicitly configured: juniBridgeIfRowStatus juniBridgeIfLowerIfIndex In addition, when creating an entry the following conditions must hold: A value for juniBridgeIfIndex must have been determined previously, by reading juniBridgeIfNextIfIndex. A corresponding entry in ifTable/ifXTable/juniIfTable is created/destroyed as a result of creating/destroying an entry in this table.')
juniBridgeIfLowerIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 63, 1, 2, 1, 3), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniBridgeIfLowerIfIndex.setStatus('current')
if mibBuilder.loadTexts: juniBridgeIfLowerIfIndex.setDescription('The ifIndex of an interface over which this Bridge interface to be layered. A value of zero indicates no layering. An implementation may choose to require that a nonzero value be configured at entry creation.')
juniBridgeSPolicyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 63, 1, 2, 1, 4), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniBridgeSPolicyIndex.setStatus('current')
if mibBuilder.loadTexts: juniBridgeSPolicyIndex.setDescription('The index of the associated subscriber policy.')
juniBridgeIfMaxLearnCount = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 63, 1, 2, 1, 5), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniBridgeIfMaxLearnCount.setStatus('current')
if mibBuilder.loadTexts: juniBridgeIfMaxLearnCount.setDescription('The maximum number of entries that can be learned on this interface.')
juniBridgeAgeTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 63, 2, 1), )
if mibBuilder.loadTexts: juniBridgeAgeTable.setStatus('current')
if mibBuilder.loadTexts: juniBridgeAgeTable.setDescription('A table that contains information about unicast entries for which the bridge has aging information.')
juniBridgeAgeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 63, 2, 1, 1), ).setIndexNames((0, "Juniper-BRIDGE-MIB", "juniBridgeMacAddress"))
if mibBuilder.loadTexts: juniBridgeAgeEntry.setStatus('current')
if mibBuilder.loadTexts: juniBridgeAgeEntry.setDescription('Information about a specific unicast MAC address for which the bridge has some forwarding and/or filtering information.')
juniBridgeMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 63, 2, 1, 1, 1), MacAddress())
if mibBuilder.loadTexts: juniBridgeMacAddress.setStatus('current')
if mibBuilder.loadTexts: juniBridgeMacAddress.setDescription('A unicast MAC address for which the bridge has aging information.')
juniBridgeAge = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 63, 2, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniBridgeAge.setStatus('current')
if mibBuilder.loadTexts: juniBridgeAge.setDescription('The age of this entry in the forwarding table.')
juniBridgeDupMacCounter = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 63, 3, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniBridgeDupMacCounter.setStatus('current')
if mibBuilder.loadTexts: juniBridgeDupMacCounter.setDescription('The total number of duplicate mac entries found for this bridge group. A duplicate mac address is considered duplicate if found on more than one interface(port).')
juniBridgeConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 63, 4))
juniBridgeCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 63, 4, 1))
juniBridgeGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 63, 4, 2))
juniBridgeCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 63, 4, 1, 1)).setObjects(("Juniper-BRIDGE-MIB", "juniBridgeGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniBridgeCompliance = juniBridgeCompliance.setStatus('current')
if mibBuilder.loadTexts: juniBridgeCompliance.setDescription('The compliance statement for entities which implement the Juniper Bridge MIB.')
juniBridgeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 63, 4, 2, 1)).setObjects(("Juniper-BRIDGE-MIB", "juniBridgeIfNextIfIndex"), ("Juniper-BRIDGE-MIB", "juniBridgeIfRowStatus"), ("Juniper-BRIDGE-MIB", "juniBridgeIfLowerIfIndex"), ("Juniper-BRIDGE-MIB", "juniBridgeSPolicyIndex"), ("Juniper-BRIDGE-MIB", "juniBridgeIfMaxLearnCount"), ("Juniper-BRIDGE-MIB", "juniBridgeAge"), ("Juniper-BRIDGE-MIB", "juniBridgeDupMacCounter"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniBridgeGroup = juniBridgeGroup.setStatus('current')
if mibBuilder.loadTexts: juniBridgeGroup.setDescription('A collection of objects providing management of bridges in a Juniper product.')
mibBuilder.exportSymbols("Juniper-BRIDGE-MIB", juniBridgeCompliance=juniBridgeCompliance, juniBridgeAgeLayer=juniBridgeAgeLayer, juniBridgeCompliances=juniBridgeCompliances, juniBridgeIfIndex=juniBridgeIfIndex, juniBridgeGroups=juniBridgeGroups, juniBridgeAgeTable=juniBridgeAgeTable, juniBridgeConformance=juniBridgeConformance, juniBridgeIfTable=juniBridgeIfTable, juniBridgeIfLayer=juniBridgeIfLayer, juniBridgeAge=juniBridgeAge, juniBridgeSPolicyIndex=juniBridgeSPolicyIndex, juniBridgeAgeEntry=juniBridgeAgeEntry, juniBridgeGroup=juniBridgeGroup, PYSNMP_MODULE_ID=juniBridgeMIB, juniBridgeIfEntry=juniBridgeIfEntry, juniBridgeIfMaxLearnCount=juniBridgeIfMaxLearnCount, juniBridgeMacAddress=juniBridgeMacAddress, juniBridgeMIB=juniBridgeMIB, juniBridgeIfNextIfIndex=juniBridgeIfNextIfIndex, juniBridgeIfRowStatus=juniBridgeIfRowStatus, juniBridgeMiscCounters=juniBridgeMiscCounters, juniBridgeDupMacCounter=juniBridgeDupMacCounter, juniBridgeIfLowerIfIndex=juniBridgeIfLowerIfIndex)
