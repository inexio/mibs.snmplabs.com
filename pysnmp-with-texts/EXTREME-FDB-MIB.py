#
# PySNMP MIB module EXTREME-FDB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EXTREME-BASE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:07:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
extremeAgent, PortList = mibBuilder.importSymbols("EXTREME-BASE-MIB", "extremeAgent", "PortList")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, IpAddress, Integer32, Gauge32, Counter32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, NotificationType, ModuleIdentity, ObjectIdentity, TimeTicks, Bits, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "IpAddress", "Integer32", "Gauge32", "Counter32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "NotificationType", "ModuleIdentity", "ObjectIdentity", "TimeTicks", "Bits", "Unsigned32")
MacAddress, DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "DisplayString", "TextualConvention", "RowStatus")
extremeFdb = ModuleIdentity((1, 3, 6, 1, 4, 1, 1916, 1, 16))
if mibBuilder.loadTexts: extremeFdb.setLastUpdated('0010310000Z')
if mibBuilder.loadTexts: extremeFdb.setOrganization('Extreme Networks, Inc.')
if mibBuilder.loadTexts: extremeFdb.setContactInfo('www.extremenetworks.com')
if mibBuilder.loadTexts: extremeFdb.setDescription('Extreme FDB and IP FDB tables.')
extremeFdbMacFdbTable = MibTable((1, 3, 6, 1, 4, 1, 1916, 1, 16, 1), )
if mibBuilder.loadTexts: extremeFdbMacFdbTable.setStatus('current')
if mibBuilder.loadTexts: extremeFdbMacFdbTable.setDescription('A table that contains information about the hardware MAC FDB table.')
extremeFdbMacFdbEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1916, 1, 16, 1, 1), ).setIndexNames((0, "EXTREME-FDB-MIB", "extremeFdbMacFdbVlanIfIndex"), (0, "EXTREME-FDB-MIB", "extremeFdbMacFdbSequenceNumber"))
if mibBuilder.loadTexts: extremeFdbMacFdbEntry.setStatus('current')
if mibBuilder.loadTexts: extremeFdbMacFdbEntry.setDescription('An entry in the table of MAC FDB information.')
extremeFdbMacFdbVlanIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 16, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: extremeFdbMacFdbVlanIfIndex.setStatus('current')
if mibBuilder.loadTexts: extremeFdbMacFdbVlanIfIndex.setDescription('The ifIndex of the Vlan on which this mac is learned.')
extremeFdbMacFdbSequenceNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 16, 1, 1, 2), Integer32())
if mibBuilder.loadTexts: extremeFdbMacFdbSequenceNumber.setStatus('current')
if mibBuilder.loadTexts: extremeFdbMacFdbSequenceNumber.setDescription('The sequence number of this FDB entry in the forwarding database.')
extremeFdbMacFdbMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 16, 1, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeFdbMacFdbMacAddress.setStatus('current')
if mibBuilder.loadTexts: extremeFdbMacFdbMacAddress.setDescription('A MAC address for which the bridge has forwarding and/or filtering information.')
extremeFdbMacFdbPortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 16, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeFdbMacFdbPortIfIndex.setStatus('current')
if mibBuilder.loadTexts: extremeFdbMacFdbPortIfIndex.setDescription("Either the value '0', or the IfIndex of the port on which a frame having a source address equal to the value of the corresponding instance of dot1dTpFdbAddress has been seen. A value of '0' indicates that the port IfIndex has not been learned but that the bridge does have some forwarding/filtering information about this address (e.g. in the dot1dStaticTable).")
extremeFdbMacFdbStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 16, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("invalid", 2), ("learned", 3), ("self", 4), ("mgmt", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeFdbMacFdbStatus.setStatus('current')
if mibBuilder.loadTexts: extremeFdbMacFdbStatus.setDescription('The status of this entry. This is the value of dot1dTpFdbStatus in RFC1493.')
extremeFdbIpFdbTable = MibTable((1, 3, 6, 1, 4, 1, 1916, 1, 16, 2), )
if mibBuilder.loadTexts: extremeFdbIpFdbTable.setStatus('current')
if mibBuilder.loadTexts: extremeFdbIpFdbTable.setDescription('A table that contains information about the hardware IP FDB table.')
extremeFdbIpFdbEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1916, 1, 16, 2, 1), ).setIndexNames((0, "EXTREME-FDB-MIB", "extremeFdbIpFdbSequenceNumber"))
if mibBuilder.loadTexts: extremeFdbIpFdbEntry.setStatus('current')
if mibBuilder.loadTexts: extremeFdbIpFdbEntry.setDescription('An entry in the table of IP FDB information.')
extremeFdbIpFdbSequenceNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 16, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: extremeFdbIpFdbSequenceNumber.setStatus('current')
if mibBuilder.loadTexts: extremeFdbIpFdbSequenceNumber.setDescription('The sequence number of this entry in the IP FDB')
extremeFdbIpFdbIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 16, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeFdbIpFdbIPAddress.setStatus('current')
if mibBuilder.loadTexts: extremeFdbIpFdbIPAddress.setDescription('The IP Address of the IP FDB entry')
extremeFdbIpFdbMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 16, 2, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeFdbIpFdbMacAddress.setStatus('current')
if mibBuilder.loadTexts: extremeFdbIpFdbMacAddress.setDescription('The MAC address corresponding to the IP Address.')
extremeFdbIpFdbVlanIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 16, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeFdbIpFdbVlanIfIndex.setStatus('current')
if mibBuilder.loadTexts: extremeFdbIpFdbVlanIfIndex.setDescription('The ifIndex of the Vlan on which this ip is learned')
extremeFdbIpFdbPortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 16, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeFdbIpFdbPortIfIndex.setStatus('current')
if mibBuilder.loadTexts: extremeFdbIpFdbPortIfIndex.setDescription('The IfIndex of the port on which this entry was learned')
extremeFdbPermFdbTable = MibTable((1, 3, 6, 1, 4, 1, 1916, 1, 16, 3), )
if mibBuilder.loadTexts: extremeFdbPermFdbTable.setStatus('current')
if mibBuilder.loadTexts: extremeFdbPermFdbTable.setDescription('This table contains information on the secure-mac permanent FDB entries. It may later be extended to display other types of permanent FDB entries.')
extremeFdbPermFdbEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1916, 1, 16, 3, 1), ).setIndexNames((0, "EXTREME-FDB-MIB", "extremeFdbPermFdbFilterNum"), (0, "EXTREME-FDB-MIB", "extremeFdbPermFdbMacAddress"), (0, "EXTREME-FDB-MIB", "extremeFdbPermFdbVlanId"))
if mibBuilder.loadTexts: extremeFdbPermFdbEntry.setStatus('current')
if mibBuilder.loadTexts: extremeFdbPermFdbEntry.setDescription('An entry in the table of secure-mac permanent FDB information.')
extremeFdbPermFdbFilterNum = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 16, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeFdbPermFdbFilterNum.setStatus('current')
if mibBuilder.loadTexts: extremeFdbPermFdbFilterNum.setDescription('This object always returns 1. In future, it may be used to provide additional capability.')
extremeFdbPermFdbMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 16, 3, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeFdbPermFdbMacAddress.setStatus('current')
if mibBuilder.loadTexts: extremeFdbPermFdbMacAddress.setDescription('The is the MAC Address to which this FDB entry pertains.')
extremeFdbPermFdbVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 16, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeFdbPermFdbVlanId.setStatus('current')
if mibBuilder.loadTexts: extremeFdbPermFdbVlanId.setDescription('The VLAN ID of the VLAN to which this FDB entry pertains.')
extremeFdbPermFdbPortList = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 16, 3, 1, 4), PortList()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: extremeFdbPermFdbPortList.setStatus('current')
if mibBuilder.loadTexts: extremeFdbPermFdbPortList.setDescription('This is the list of port(s) on which the given MAC Address is configured Note that this port list is constructed assuming there are as many ports per slot as given in the object extremeChassisPortsPerSlot. Thus, if extremeChassisPortsPerSlot is 128, then the 129th bit in the port list (reading left to right) indicates port 2:1. Similarly, the 256th bit would indicate port 2:128 while the 257th bit would indicate port 3:1. Note especially that the bit positions in port list do not depend on the actual physical presence or absence of the given ports on the blade or of any blade itself.')
extremeFdbPermFdbFlags = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 16, 3, 1, 5), Bits().clone(namedValues=NamedValues(("isSecure", 0)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: extremeFdbPermFdbFlags.setStatus('current')
if mibBuilder.loadTexts: extremeFdbPermFdbFlags.setDescription('This object contains the flags associated with the FDB entry. The flags are similar to those displayed on the device Command Line Interface. At present, only the isSecure bit i.e. bit 0 will be supported and it will always be ON since only secure-mac entries are configurable and displayed in this table.')
extremeFdbPermFdbStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 16, 3, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: extremeFdbPermFdbStatus.setStatus('current')
if mibBuilder.loadTexts: extremeFdbPermFdbStatus.setDescription('The status of this entry as per standard RowStatus conventions. Note however, that createAndWait and notInService states are not supported.')
extremeFdbMacFdbCounterTable = MibTable((1, 3, 6, 1, 4, 1, 1916, 1, 16, 5), )
if mibBuilder.loadTexts: extremeFdbMacFdbCounterTable.setStatus('current')
if mibBuilder.loadTexts: extremeFdbMacFdbCounterTable.setDescription('A table that contains change counters for the Operational FDB. Each entry in the table corresponds to an individual port. Whenever a change occurs to the operational FDB (MAC learned, aged out or removed), the counter associated with the port is incremented by one. The counters are reset at agent startup and when the port is down. They are not cleared when the port is enabled or disabled.')
extremeFdbMacFdbCounterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1916, 1, 16, 5, 1), ).setIndexNames((0, "EXTREME-FDB-MIB", "extremeFdbMacFdbCounterPortIfIndex"))
if mibBuilder.loadTexts: extremeFdbMacFdbCounterEntry.setStatus('current')
if mibBuilder.loadTexts: extremeFdbMacFdbCounterEntry.setDescription('An entry in the table of MAC FDB change counters.')
extremeFdbMacFdbCounterPortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 16, 5, 1, 1), Integer32())
if mibBuilder.loadTexts: extremeFdbMacFdbCounterPortIfIndex.setStatus('current')
if mibBuilder.loadTexts: extremeFdbMacFdbCounterPortIfIndex.setDescription('The ifIndex of the Port for which the counte applies.')
extremeFdbMacFdbCounterValue = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 16, 5, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeFdbMacFdbCounterValue.setStatus('current')
if mibBuilder.loadTexts: extremeFdbMacFdbCounterValue.setDescription('The count of the number of FDB changes for the given port since the counter was last reset.')
mibBuilder.exportSymbols("EXTREME-FDB-MIB", extremeFdbPermFdbStatus=extremeFdbPermFdbStatus, extremeFdbMacFdbCounterValue=extremeFdbMacFdbCounterValue, PYSNMP_MODULE_ID=extremeFdb, extremeFdbPermFdbMacAddress=extremeFdbPermFdbMacAddress, extremeFdbMacFdbVlanIfIndex=extremeFdbMacFdbVlanIfIndex, extremeFdbMacFdbCounterEntry=extremeFdbMacFdbCounterEntry, extremeFdbPermFdbEntry=extremeFdbPermFdbEntry, extremeFdbIpFdbIPAddress=extremeFdbIpFdbIPAddress, extremeFdbPermFdbPortList=extremeFdbPermFdbPortList, extremeFdb=extremeFdb, extremeFdbIpFdbEntry=extremeFdbIpFdbEntry, extremeFdbPermFdbTable=extremeFdbPermFdbTable, extremeFdbIpFdbTable=extremeFdbIpFdbTable, extremeFdbMacFdbPortIfIndex=extremeFdbMacFdbPortIfIndex, extremeFdbPermFdbFlags=extremeFdbPermFdbFlags, extremeFdbMacFdbEntry=extremeFdbMacFdbEntry, extremeFdbMacFdbTable=extremeFdbMacFdbTable, extremeFdbMacFdbMacAddress=extremeFdbMacFdbMacAddress, extremeFdbIpFdbPortIfIndex=extremeFdbIpFdbPortIfIndex, extremeFdbMacFdbCounterPortIfIndex=extremeFdbMacFdbCounterPortIfIndex, extremeFdbMacFdbCounterTable=extremeFdbMacFdbCounterTable, extremeFdbPermFdbVlanId=extremeFdbPermFdbVlanId, extremeFdbMacFdbStatus=extremeFdbMacFdbStatus, extremeFdbMacFdbSequenceNumber=extremeFdbMacFdbSequenceNumber, extremeFdbIpFdbSequenceNumber=extremeFdbIpFdbSequenceNumber, extremeFdbIpFdbMacAddress=extremeFdbIpFdbMacAddress, extremeFdbPermFdbFilterNum=extremeFdbPermFdbFilterNum, extremeFdbIpFdbVlanIfIndex=extremeFdbIpFdbVlanIfIndex)
