#
# PySNMP MIB module Wellfleet-WFDOT1D-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Wellfleet-WFDOT1D-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:42:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, enterprises, mgmt, MibIdentifier, Bits, Opaque, mib_2, TimeTicks, Counter64, IpAddress, iso, Unsigned32, Counter32, ModuleIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Gauge32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "enterprises", "mgmt", "MibIdentifier", "Bits", "Opaque", "mib-2", "TimeTicks", "Counter64", "IpAddress", "iso", "Unsigned32", "Counter32", "ModuleIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Gauge32", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
wfBridgeGroup, = mibBuilder.importSymbols("Wellfleet-COMMON-MIB", "wfBridgeGroup")
wfDot1d = MibIdentifier((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 6))
wfDot1dBaseGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 6, 1))
wfDot1dStaticGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 6, 5))
wfDot1dBaseBridgeAddress = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 6, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfDot1dBaseBridgeAddress.setStatus('mandatory')
if mibBuilder.loadTexts: wfDot1dBaseBridgeAddress.setDescription('The MAC address used by this bridge when it must be referred to in a unique fashion. It is recommended that this be the numerically smallest MAC address of all ports that belong to this bridge. However it is only required to be unique. When concatenated with dot1dStpPriority a unique BridgeIdentifier is formed which is used in the Spanning Tree Protocol.')
wfDot1dBaseNumPorts = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 6, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfDot1dBaseNumPorts.setStatus('mandatory')
if mibBuilder.loadTexts: wfDot1dBaseNumPorts.setDescription('The number of ports controlled by this bridging entity.')
wfDot1dBaseType = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 6, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unk", 1), ("only", 2), ("sr", 3), ("srt", 4))).clone('only')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfDot1dBaseType.setStatus('mandatory')
if mibBuilder.loadTexts: wfDot1dBaseType.setDescription('Indicates what type of bridging this bridge can perform. If a bridge is actually performing a certain type of bridging this will be indicated by entries in the port table for the given type.')
wfDot1dStaticTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 6, 5, 1), )
if mibBuilder.loadTexts: wfDot1dStaticTable.setStatus('mandatory')
if mibBuilder.loadTexts: wfDot1dStaticTable.setDescription("'A table containing filtering information configured into the bridge by (local or network) management specifying the set of ports to which frames received from specific ports and containing specific destination addresses are allowed to be forwarded. The value of zero in this table as the port number from which frames with a specific destination address are received, is used to specify all ports for which there is no specific entry in this table for that particular destination address. Entries are valid for unicast and for group/broadcast addresses.'")
wfDot1dStaticTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 6, 5, 1, 1), ).setIndexNames((0, "Wellfleet-WFDOT1D-MIB", "wfDot1dStaticAddress"), (0, "Wellfleet-WFDOT1D-MIB", "wfDot1dStaticReceivePort"))
if mibBuilder.loadTexts: wfDot1dStaticTableEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wfDot1dStaticTableEntry.setDescription("'Filtering information configured into the bridge by (local or network) management specifying the set of ports to which frames received from a specific port and containing a specific destination address are allowed to be forwarded.'")
wfDot1dStaticAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 6, 5, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfDot1dStaticAddress.setStatus('mandatory')
if mibBuilder.loadTexts: wfDot1dStaticAddress.setDescription("'The destination MAC address in a frame to which this entry's filtering information applies. This object can take the value of a unicast address, a group address or the broadcast address.'")
wfDot1dStaticReceivePort = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 6, 5, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfDot1dStaticReceivePort.setStatus('mandatory')
if mibBuilder.loadTexts: wfDot1dStaticReceivePort.setDescription("'Either the value '0', or the port number of the port from which a frame must be received in order for this entry's filtering information to apply. A value of zero indicates that this entry applies on all ports of the bridge for which there is no other applicable entry.'")
wfDot1dStaticAllowedToGoTo = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 6, 5, 1, 1, 3), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfDot1dStaticAllowedToGoTo.setStatus('mandatory')
if mibBuilder.loadTexts: wfDot1dStaticAllowedToGoTo.setDescription("'The set of ports to which frames received from a specific port and destined for a specific MAC address, are allowed to be forwarded. Each octet within the value of this object specifies a set of eight ports, with the first octet specifying ports 1 through 8, the second octet specifying ports 9 through 16, etc. Within each octet, the most significant bit represents the lowest numbered port, and the least significant bit represents the highest numbered port. Thus, each port of the bridge is represented by a single bit within the value of this object. If that bit has a value of '1' then that port is included in the set of ports; the port is not included if its bit has a value of '0'. (Note that the setting of the bit corresponding to the port from which a frame is received is irrelevant.)'")
wfDot1dStaticStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 6, 5, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("invalid", 2), ("permanent", 3), ("reset", 4), ("timeout", 5))).clone('invalid')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfDot1dStaticStatus.setStatus('mandatory')
if mibBuilder.loadTexts: wfDot1dStaticStatus.setDescription("'This object indicates the status of this entry. other(1) - this entry is currently in use but the conditions under which it will remain so are different from each of the following values. invalid(2) - writing this value to the object removes the corresponding entry. permanent(3) - this entry is currently in use and will remain so after the next reset of the bridge. deleteOnReset(4) - this entry is currently in use and will remain so until the next reset of the bridge. deleteOnTimeout(5) - this entry is currently in use and will remain so until it is aged out.'")
mibBuilder.exportSymbols("Wellfleet-WFDOT1D-MIB", wfDot1dStaticReceivePort=wfDot1dStaticReceivePort, wfDot1dBaseType=wfDot1dBaseType, wfDot1dStaticTableEntry=wfDot1dStaticTableEntry, wfDot1dBaseBridgeAddress=wfDot1dBaseBridgeAddress, wfDot1dStaticTable=wfDot1dStaticTable, wfDot1dBaseGroup=wfDot1dBaseGroup, wfDot1dStaticAllowedToGoTo=wfDot1dStaticAllowedToGoTo, wfDot1dStaticGroup=wfDot1dStaticGroup, wfDot1dStaticStatus=wfDot1dStaticStatus, wfDot1dBaseNumPorts=wfDot1dBaseNumPorts, wfDot1dStaticAddress=wfDot1dStaticAddress, wfDot1d=wfDot1d)
