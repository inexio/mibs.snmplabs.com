#
# PySNMP MIB module DS0-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DS0-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:54:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
InterfaceIndexOrZero, InterfaceIndex, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "InterfaceIndex", "ifIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, TimeTicks, ObjectIdentity, NotificationType, Gauge32, ModuleIdentity, IpAddress, Unsigned32, transmission, Counter64, iso, MibIdentifier, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "TimeTicks", "ObjectIdentity", "NotificationType", "Gauge32", "ModuleIdentity", "IpAddress", "Unsigned32", "transmission", "Counter64", "iso", "MibIdentifier", "Bits")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
ds0 = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 81))
ds0.setRevisions(('1998-05-24 20:10',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ds0.setRevisionsDescriptions(('Initial version of the DS0-MIB.',))
if mibBuilder.loadTexts: ds0.setLastUpdated('9807161630Z')
if mibBuilder.loadTexts: ds0.setOrganization('IETF Trunk MIB Working Group')
if mibBuilder.loadTexts: ds0.setContactInfo(' David Fowler Postal: Newbridge Networks Corporation 600 March Road Kanata, Ontario, Canada K2K 2E6 Tel: +1 613 591 3600 Fax: +1 613 599 3619 E-mail: davef@newbridge.com')
if mibBuilder.loadTexts: ds0.setDescription('The MIB module to describe DS0 interfaces objects.')
dsx0ConfigTable = MibTable((1, 3, 6, 1, 2, 1, 10, 81, 1), )
if mibBuilder.loadTexts: dsx0ConfigTable.setStatus('current')
if mibBuilder.loadTexts: dsx0ConfigTable.setDescription('The DS0 Configuration table.')
dsx0ConfigEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 81, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: dsx0ConfigEntry.setStatus('current')
if mibBuilder.loadTexts: dsx0ConfigEntry.setDescription('An entry in the DS0 Configuration table. There is an entry in this table for each DS0 interface.')
dsx0Ds0ChannelNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 81, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx0Ds0ChannelNumber.setStatus('current')
if mibBuilder.loadTexts: dsx0Ds0ChannelNumber.setDescription('This object indicates the channel number of the ds0 on its DS1/E1.')
dsx0RobbedBitSignalling = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 81, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx0RobbedBitSignalling.setStatus('current')
if mibBuilder.loadTexts: dsx0RobbedBitSignalling.setDescription('This object indicates if Robbed Bit Signalling is turned on or off for a given ds0. This only applies to DS0s on a DS1 link. For E1 links the value is always off (false).')
dsx0CircuitIdentifier = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 81, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx0CircuitIdentifier.setStatus('current')
if mibBuilder.loadTexts: dsx0CircuitIdentifier.setDescription("This object contains the transmission vendor's circuit identifier, for the purpose of facilitating troubleshooting.")
dsx0IdleCode = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 81, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx0IdleCode.setStatus('current')
if mibBuilder.loadTexts: dsx0IdleCode.setDescription('This object contains the code transmitted in the ABCD bits when the ds0 is not connected and dsx0TransmitCodesEnable is enabled. The object is a bitmap and the various bit positions are: 1 D bit 2 C bit 4 B bit 8 A bit')
dsx0SeizedCode = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 81, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx0SeizedCode.setStatus('current')
if mibBuilder.loadTexts: dsx0SeizedCode.setDescription('This object contains the code transmitted in the ABCD bits when the ds0 is connected and dsx0TransmitCodesEnable is enabled. The object is a bitmap and the various bit positions are: 1 D bit 2 C bit 4 B bit 8 A bit')
dsx0ReceivedCode = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 81, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx0ReceivedCode.setStatus('current')
if mibBuilder.loadTexts: dsx0ReceivedCode.setDescription('This object contains the code being received in the ABCD bits. The object is a bitmap and the various bit positions are: 1 D bit 2 C bit 4 B bit 8 A bit')
dsx0TransmitCodesEnable = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 81, 1, 1, 7), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx0TransmitCodesEnable.setStatus('current')
if mibBuilder.loadTexts: dsx0TransmitCodesEnable.setDescription('This object determines if the idle and seized codes are transmitted. If the value of this object is true then the codes are transmitted.')
dsx0Ds0BundleMappedIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 81, 1, 1, 8), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx0Ds0BundleMappedIfIndex.setStatus('current')
if mibBuilder.loadTexts: dsx0Ds0BundleMappedIfIndex.setDescription('This object indicates the ifIndex value assigned by the agent for the ds0Bundle(82) ifEntry to which the given ds0(81) ifEntry may belong. If the given ds0(81) ifEntry does not belong to any ds0Bundle(82) ifEntry, then this object has a value of zero. While this object provides information that can also be found in the ifStackTable, it provides this same information with a single table lookup, rather than by walking the ifStackTable to find the possibly non-existent ds0Bundle(82) ifEntry that may be stacked above the given ds0(81) ifTable entry.')
dsx0ChanMappingTable = MibTable((1, 3, 6, 1, 2, 1, 10, 81, 3), )
if mibBuilder.loadTexts: dsx0ChanMappingTable.setStatus('current')
if mibBuilder.loadTexts: dsx0ChanMappingTable.setDescription('The DS0 Channel Mapping table. This table maps a DS0 channel number on a particular DS1/E1 into an ifIndex.')
dsx0ChanMappingEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 81, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "DS0-MIB", "dsx0Ds0ChannelNumber"))
if mibBuilder.loadTexts: dsx0ChanMappingEntry.setStatus('current')
if mibBuilder.loadTexts: dsx0ChanMappingEntry.setDescription('An entry in the DS0 Channel Mapping table. There is an entry in this table corresponding to each ds0 ifEntry within any interface that is channelized to the individual ds0 ifEntry level. This table is intended to facilitate mapping from channelized interface / channel number to DS0 ifEntry. (e.g. mapping (DS1 ifIndex, DS0 Channel Number) -> ifIndex) While this table provides information that can also be found in the ifStackTable and dsx0ConfigTable, it provides this same information with a single table lookup, rather than by walking the ifStackTable to find the various constituent ds0 ifTable entries, and testing various dsx0ConfigTable entries to check for the entry with the applicable DS0 channel number.')
dsx0ChanMappedIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 81, 3, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx0ChanMappedIfIndex.setStatus('current')
if mibBuilder.loadTexts: dsx0ChanMappedIfIndex.setDescription('This object indicates the ifIndex value assigned by the agent for the individual ds0 ifEntry that corresponds to the given DS0 channel number (specified by the INDEX element dsx0Ds0ChannelNumber) of the given channelized interface (specified by INDEX element ifIndex).')
ds0Conformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 81, 2))
ds0Groups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 81, 2, 1))
ds0Compliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 81, 2, 2))
ds0Compliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 81, 2, 2, 1)).setObjects(("DS0-MIB", "ds0ConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ds0Compliance = ds0Compliance.setStatus('current')
if mibBuilder.loadTexts: ds0Compliance.setDescription('The compliance statement for DS0 interfaces.')
ds0ConfigGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 81, 2, 1, 1)).setObjects(("DS0-MIB", "dsx0Ds0ChannelNumber"), ("DS0-MIB", "dsx0RobbedBitSignalling"), ("DS0-MIB", "dsx0CircuitIdentifier"), ("DS0-MIB", "dsx0IdleCode"), ("DS0-MIB", "dsx0SeizedCode"), ("DS0-MIB", "dsx0ReceivedCode"), ("DS0-MIB", "dsx0TransmitCodesEnable"), ("DS0-MIB", "dsx0Ds0BundleMappedIfIndex"), ("DS0-MIB", "dsx0ChanMappedIfIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ds0ConfigGroup = ds0ConfigGroup.setStatus('current')
if mibBuilder.loadTexts: ds0ConfigGroup.setDescription('A collection of objects providing configuration information applicable to all DS0 interfaces.')
mibBuilder.exportSymbols("DS0-MIB", ds0=ds0, dsx0SeizedCode=dsx0SeizedCode, dsx0Ds0BundleMappedIfIndex=dsx0Ds0BundleMappedIfIndex, ds0Compliances=ds0Compliances, dsx0IdleCode=dsx0IdleCode, dsx0ReceivedCode=dsx0ReceivedCode, dsx0ChanMappingEntry=dsx0ChanMappingEntry, dsx0RobbedBitSignalling=dsx0RobbedBitSignalling, ds0Conformance=ds0Conformance, PYSNMP_MODULE_ID=ds0, dsx0ChanMappedIfIndex=dsx0ChanMappedIfIndex, dsx0ConfigTable=dsx0ConfigTable, ds0Groups=ds0Groups, dsx0ConfigEntry=dsx0ConfigEntry, ds0Compliance=ds0Compliance, dsx0CircuitIdentifier=dsx0CircuitIdentifier, ds0ConfigGroup=ds0ConfigGroup, dsx0TransmitCodesEnable=dsx0TransmitCodesEnable, dsx0ChanMappingTable=dsx0ChanMappingTable, dsx0Ds0ChannelNumber=dsx0Ds0ChannelNumber)
