#
# PySNMP MIB module SUBNETVLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SUBNETVLAN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:11:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
dlink_common_mgmt, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-common-mgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, ModuleIdentity, Integer32, MibIdentifier, TimeTicks, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Gauge32, Unsigned32, ObjectIdentity, iso, Bits, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ModuleIdentity", "Integer32", "MibIdentifier", "TimeTicks", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Gauge32", "Unsigned32", "ObjectIdentity", "iso", "Bits", "Counter64")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
swSubnetVlanMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 12, 75))
if mibBuilder.loadTexts: swSubnetVlanMIB.setLastUpdated('0812020000Z')
if mibBuilder.loadTexts: swSubnetVlanMIB.setOrganization('D-Link Corp.')
if mibBuilder.loadTexts: swSubnetVlanMIB.setContactInfo('http://support.dlink.com')
if mibBuilder.loadTexts: swSubnetVlanMIB.setDescription('The Subnet (Policy-based) VLAN module MIB for the proprietary enterprise.')
class VlanId(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 4094)

class Ipv6Address(TextualConvention, OctetString):
    description = 'This data type is used to model IPv6 addresses. This is a binary string of 16 octets in network byte-order.'
    status = 'current'
    displayHint = '2x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(16, 16)
    fixedLength = 16

swSubnetVlanCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 75, 1))
swSubnetVlanInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 75, 2))
swSubnetVlanMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 75, 3))
swVlanPrecedenceTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 75, 3, 1), )
if mibBuilder.loadTexts: swVlanPrecedenceTable.setStatus('current')
if mibBuilder.loadTexts: swVlanPrecedenceTable.setDescription('This table contains VLAN classification precedence information for each port.')
swVlanPrecedenceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 75, 3, 1, 1), ).setIndexNames((0, "SUBNETVLAN-MIB", "swVlanPrecedencePortIndex"))
if mibBuilder.loadTexts: swVlanPrecedenceEntry.setStatus('current')
if mibBuilder.loadTexts: swVlanPrecedenceEntry.setDescription('This object indicates VLAN classification precedence information for this entry.')
swVlanPrecedencePortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 75, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swVlanPrecedencePortIndex.setStatus('current')
if mibBuilder.loadTexts: swVlanPrecedencePortIndex.setDescription('This object indicates the port index.')
swVlanPrecedenceClassification = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 75, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("macBased", 1), ("subnetBased", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swVlanPrecedenceClassification.setStatus('current')
if mibBuilder.loadTexts: swVlanPrecedenceClassification.setDescription('This object indicates the VLAN classification precedence.')
swSubnetVLANTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 75, 3, 2), )
if mibBuilder.loadTexts: swSubnetVLANTable.setStatus('current')
if mibBuilder.loadTexts: swSubnetVLANTable.setDescription('This table contains subnet VLAN information.')
swSubnetVLANEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 75, 3, 2, 1), ).setIndexNames((0, "SUBNETVLAN-MIB", "swSubnetVLANIPAddress"), (0, "SUBNETVLAN-MIB", "swSubnetVLANIPMask"))
if mibBuilder.loadTexts: swSubnetVLANEntry.setStatus('current')
if mibBuilder.loadTexts: swSubnetVLANEntry.setDescription('This object indicates subnet VLAN IPv4 entry information.')
swSubnetVLANIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 75, 3, 2, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swSubnetVLANIPAddress.setStatus('current')
if mibBuilder.loadTexts: swSubnetVLANIPAddress.setDescription('This object indicates the IP address.')
swSubnetVLANIPMask = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 75, 3, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swSubnetVLANIPMask.setStatus('current')
if mibBuilder.loadTexts: swSubnetVLANIPMask.setDescription('This object indicates the IP mask.')
swSubnetVLANID = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 75, 3, 2, 1, 3), VlanId()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swSubnetVLANID.setStatus('current')
if mibBuilder.loadTexts: swSubnetVLANID.setDescription('This object indicates the VLAN ID.')
swSubnetVLANPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 75, 3, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swSubnetVLANPriority.setStatus('current')
if mibBuilder.loadTexts: swSubnetVLANPriority.setDescription('This object indicates the priority.')
swSubnetVLANRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 75, 3, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swSubnetVLANRowStatus.setStatus('current')
if mibBuilder.loadTexts: swSubnetVLANRowStatus.setDescription('This object indicates the status of this entry.')
swSubnetVLANIPv6Table = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 75, 3, 3), )
if mibBuilder.loadTexts: swSubnetVLANIPv6Table.setStatus('current')
if mibBuilder.loadTexts: swSubnetVLANIPv6Table.setDescription('This table contains subnet VLAN IPv6 entry information.')
swSubnetVLANIPv6Entry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 75, 3, 3, 1), ).setIndexNames((0, "SUBNETVLAN-MIB", "swSubnetVLANIPv6Address"), (0, "SUBNETVLAN-MIB", "swSubnetVLANIPv6PrefixLength"))
if mibBuilder.loadTexts: swSubnetVLANIPv6Entry.setStatus('current')
if mibBuilder.loadTexts: swSubnetVLANIPv6Entry.setDescription('This object indicates subnet VLAN IPv6 entry information.')
swSubnetVLANIPv6Address = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 75, 3, 3, 1, 1), Ipv6Address()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swSubnetVLANIPv6Address.setStatus('current')
if mibBuilder.loadTexts: swSubnetVLANIPv6Address.setDescription('This object indicates the IPv6 address.')
swSubnetVLANIPv6PrefixLength = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 75, 3, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swSubnetVLANIPv6PrefixLength.setStatus('current')
if mibBuilder.loadTexts: swSubnetVLANIPv6PrefixLength.setDescription('This object indicates the IPv6 prefix length.')
swSubnetVLANIPv6VID = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 75, 3, 3, 1, 3), VlanId()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swSubnetVLANIPv6VID.setStatus('current')
if mibBuilder.loadTexts: swSubnetVLANIPv6VID.setDescription('This object indicates the VLAN ID.')
swSubnetVLANIPv6Priority = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 75, 3, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swSubnetVLANIPv6Priority.setStatus('current')
if mibBuilder.loadTexts: swSubnetVLANIPv6Priority.setDescription('This object indicates the priority.')
swSubnetVLANIPv6RowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 75, 3, 3, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swSubnetVLANIPv6RowStatus.setStatus('current')
if mibBuilder.loadTexts: swSubnetVLANIPv6RowStatus.setDescription('This object indicates the status of this entry.')
mibBuilder.exportSymbols("SUBNETVLAN-MIB", swSubnetVlanMgmt=swSubnetVlanMgmt, swSubnetVLANIPAddress=swSubnetVLANIPAddress, swSubnetVLANIPv6Address=swSubnetVLANIPv6Address, swVlanPrecedenceTable=swVlanPrecedenceTable, swSubnetVLANRowStatus=swSubnetVLANRowStatus, Ipv6Address=Ipv6Address, PYSNMP_MODULE_ID=swSubnetVlanMIB, swSubnetVLANTable=swSubnetVLANTable, swSubnetVlanCtrl=swSubnetVlanCtrl, swSubnetVLANIPMask=swSubnetVLANIPMask, swSubnetVLANIPv6RowStatus=swSubnetVLANIPv6RowStatus, VlanId=VlanId, swVlanPrecedenceClassification=swVlanPrecedenceClassification, swSubnetVlanMIB=swSubnetVlanMIB, swSubnetVLANPriority=swSubnetVLANPriority, swSubnetVLANEntry=swSubnetVLANEntry, swSubnetVlanInfo=swSubnetVlanInfo, swSubnetVLANIPv6Entry=swSubnetVLANIPv6Entry, swSubnetVLANIPv6Table=swSubnetVLANIPv6Table, swVlanPrecedencePortIndex=swVlanPrecedencePortIndex, swSubnetVLANID=swSubnetVLANID, swSubnetVLANIPv6PrefixLength=swSubnetVLANIPv6PrefixLength, swVlanPrecedenceEntry=swVlanPrecedenceEntry, swSubnetVLANIPv6VID=swSubnetVLANIPv6VID, swSubnetVLANIPv6Priority=swSubnetVLANIPv6Priority)
