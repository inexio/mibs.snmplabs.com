#
# PySNMP MIB module ENTERASYS-ESWITCH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ENTERASYS-ESWITCH-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:03:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Gauge32, Integer32, Bits, Unsigned32, TimeTicks, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ObjectIdentity, IpAddress, ModuleIdentity, iso, MibIdentifier, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Integer32", "Bits", "Unsigned32", "TimeTicks", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ObjectIdentity", "IpAddress", "ModuleIdentity", "iso", "MibIdentifier", "Counter64")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
enterasysESwitchMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 10))
enterasysESwitchMIB.setRevisions(('2002-03-07 19:50', '2001-02-13 11:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: enterasysESwitchMIB.setRevisionsDescriptions(('Imported etsysModules from the correct MIB.', 'The initial version of this MIB module.',))
if mibBuilder.loadTexts: enterasysESwitchMIB.setLastUpdated('200203071950Z')
if mibBuilder.loadTexts: enterasysESwitchMIB.setOrganization('Enterasys Networks, Inc')
if mibBuilder.loadTexts: enterasysESwitchMIB.setContactInfo('Postal: Enterasys Networks 35 Industrial Way, P.O. Box 5005 Rochester, NH 03867-0505 Phone: +1-603-332-9400 E-Mail: support@enterasys.com WWW: http://www.enterasys.com')
if mibBuilder.loadTexts: enterasysESwitchMIB.setDescription('The Enterasys Networks Proprietary MIB module for entities implementing the Extended Switch Objects.')
etsysESwitchObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 1))
etsysESwitchParams = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 1, 1))
etsysESwitchRateLimiting = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 1, 2))
etsysESwitchFilter = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 1, 3))
etsysESwitchProtocolObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 1, 4))
etsysESwitchAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 1, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysESwitchAdminStatus.setStatus('current')
if mibBuilder.loadTexts: etsysESwitchAdminStatus.setDescription("DURABLE: The meanings of the values are: enabled(1) - setting this object to enabled causes the device to begin it's power up sequence and attempt to enter its operational state. If the value of this object was disabled, then the non-volatile value of this object is changed to enabled. As part of the power up sequence, the device's management parameters may or may not be reset. (In other words, the device may go through the equivalent of a reset or before returning to the online state. If the device is capable of going directly from the disabled state to the enabled state without resetting any of its management parameters, then it may do so. Such action is product specific.) disabled(2) - setting this object to offline causes the device to cease network activity and enter a quiescent state. A disabled device must still be able to respond to management messages. The value enable(1) or disable(2) shall be stored in non-volatile memory for the initial reset value of this variable. The factory default NV value is enable(1).")
etsysESwitchRateLimitingTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 1, 2, 1), )
if mibBuilder.loadTexts: etsysESwitchRateLimitingTable.setStatus('current')
if mibBuilder.loadTexts: etsysESwitchRateLimitingTable.setDescription('This table allows rate limiting of multicast frames received on bridge ports. A typical application of this might be to limit a broadcast storm to the confines of the LAN connected by the bridge. All objects in this table must be saved across a system reset and/or a power cycle.')
etsysESwitchRateLimitingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: etsysESwitchRateLimitingEntry.setStatus('current')
if mibBuilder.loadTexts: etsysESwitchRateLimitingEntry.setDescription('An Entry (conceptual row) in the RateLimiting Table. A collection of objects containing information for enabling and configuring RateLimiting.')
etsysESwitchRateLimitSwitch = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 1, 2, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysESwitchRateLimitSwitch.setStatus('current')
if mibBuilder.loadTexts: etsysESwitchRateLimitSwitch.setDescription("DURABLE: By default, rate limiting will be disabled. It can be enabled by setting this object to 'true(1)'.")
etsysESwitchRateLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 1, 2, 1, 1, 2), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysESwitchRateLimit.setStatus('current')
if mibBuilder.loadTexts: etsysESwitchRateLimit.setDescription('DURABLE: This is the maximum number of rate-limited frames per second that the bridge will forward per second.')
etsysESwitchAddrFilterTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 1, 3, 1), )
if mibBuilder.loadTexts: etsysESwitchAddrFilterTable.setStatus('current')
if mibBuilder.loadTexts: etsysESwitchAddrFilterTable.setDescription('A list of interface entries. The number of entries is given by ifNumber, defined in MIB-II.')
etsysESwitchAddrFilterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 1, 3, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: etsysESwitchAddrFilterEntry.setStatus('current')
if mibBuilder.loadTexts: etsysESwitchAddrFilterEntry.setDescription('A collection of objects containing information for a given interface.')
etsysESwitchAddressFilter = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 1, 3, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysESwitchAddressFilter.setStatus('current')
if mibBuilder.loadTexts: etsysESwitchAddressFilter.setDescription('DURABLE: A switch that controls address filtering. When true, the bridge purges the learned entries from its forwarding database, stops its learning process, and forwards only frames with destination and source addresses that have been specified via management.')
etsysESwitchEtherTypeTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 1, 4, 1), )
if mibBuilder.loadTexts: etsysESwitchEtherTypeTable.setStatus('current')
if mibBuilder.loadTexts: etsysESwitchEtherTypeTable.setDescription("A table for defining the meaning of the 'userEtherType' rows in the etsysESwitchProtocolTable.")
etsysESwitchEtherTypeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 1, 4, 1, 1), ).setIndexNames((0, "ENTERASYS-ESWITCH-MIB", "etsysESwitchEtherTypeIndex"))
if mibBuilder.loadTexts: etsysESwitchEtherTypeEntry.setStatus('current')
if mibBuilder.loadTexts: etsysESwitchEtherTypeEntry.setDescription('Each row defines a particular EtherType that may be used as a basis for protocol filtering and VLAN classification.')
etsysESwitchEtherTypeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 1, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000)))
if mibBuilder.loadTexts: etsysESwitchEtherTypeIndex.setStatus('current')
if mibBuilder.loadTexts: etsysESwitchEtherTypeIndex.setDescription('A number between 1 and N that identifies a table row, and that serves to link entries in this table to those in etsysESwitchProtocolTable.')
etsysESwitchEtherTypeValue = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 1, 4, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysESwitchEtherTypeValue.setStatus('current')
if mibBuilder.loadTexts: etsysESwitchEtherTypeValue.setDescription('Defines an EtherType for use with etsysESwitchESwitchProtocolTable.')
etsysESwitchEtherTypeStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 1, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("invalid", 2), ("permanent", 3), ("deleteOnReset", 4))).clone('permanent')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysESwitchEtherTypeStatus.setStatus('current')
if mibBuilder.loadTexts: etsysESwitchEtherTypeStatus.setDescription('This object indicates the administrative status of this entry. other(1) - This entry is currently in effect, but the conditions under which it will remain so differ from the ones described for the other enumeration values invalid(2) - Writing this value invalidates the entry. The agent may (but is not required to) delete the row. permanent(3) - This entry is currently in use and will remain so after the next reset of the bridge. deleteOnReset(4) - This entry is currently in use and will remain so until the next reset of the bridge.')
etsysESwitchEtherTypePreempted = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 1, 4, 1, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysESwitchEtherTypePreempted.setStatus('current')
if mibBuilder.loadTexts: etsysESwitchEtherTypePreempted.setDescription('If true, indicates that the switch has taken control of this row and its associated resources (e.g., to support 802.1x authentication).')
etsysESwitchProtocolTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 1, 4, 2), )
if mibBuilder.loadTexts: etsysESwitchProtocolTable.setStatus('current')
if mibBuilder.loadTexts: etsysESwitchProtocolTable.setDescription('A table for configuring, and obtaining information about, protocol- based filtering and VLAN assignment.')
etsysESwitchProtocolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 1, 4, 2, 1), ).setIndexNames((0, "ENTERASYS-ESWITCH-MIB", "etsysESwitchProtocolReceivePort"), (0, "ENTERASYS-ESWITCH-MIB", "etsysESwitchProtocolType"), (0, "ENTERASYS-ESWITCH-MIB", "etsysESwitchProtocolIndex"))
if mibBuilder.loadTexts: etsysESwitchProtocolEntry.setStatus('current')
if mibBuilder.loadTexts: etsysESwitchProtocolEntry.setDescription('Each row in etsysESwitchProtocolTable holds filtering instructions, or VLAN classification instructions, for one (port, protocol) pair.')
etsysESwitchProtocolReceivePort = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 1, 4, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: etsysESwitchProtocolReceivePort.setStatus('current')
if mibBuilder.loadTexts: etsysESwitchProtocolReceivePort.setDescription("Identifies the receive port to which the protocol filter is to be applied. The value '0' (when allowed) represents 'all ports'.")
etsysESwitchProtocolType = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 1, 4, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("userEtherType", 1), ("ipv4", 2), ("ipxEthernet", 3), ("ipxRaw", 4), ("ipxLlc", 5), ("ipxSnap", 6), ("sna", 7), ("netBios", 8), ("decnet", 9), ("ipv6", 10))))
if mibBuilder.loadTexts: etsysESwitchProtocolType.setStatus('current')
if mibBuilder.loadTexts: etsysESwitchProtocolType.setDescription('Identifies the protocol type. The switch chip in the RoamAbout M2 can recognize nine predefined high-level protocol types, and up to three user-defined EtherTypes. (Some or all EtherType filters may be reserved for use in implementing other features.) Protocol types are as follows: userEtherType(1) - Packets whose Ethernet V2 EtherTypes or IEEE 802.3 LLC/SNAP EtherTypes match the user-defined EtherType etsysESwitchEtherType[ etsysESwitchProtocolIndex ]. ipv4(2) - Internet Protocol version 4 carried in Ethernet V2 frames or IEEE 802.3 frames with LLC/SNAP headers. Also, ARP packets carried in Ethernet V2 frames. ipxEthernet(3) - IPX carried in Ethernet V2 frames. ipxRaw(4) - IPX carried in IEEE 802.3 frames with no LLC. ipxLlc(5) - IPX carried in IEEE 802.3 frames with LLC headers. ipxSnap(6) - IPX carried in IEEE 802.3 frames with LLC/SNAP headers. sna(7) - SNA carried in IEEE 802.3 frames with LLC headers. netBios(8) - NetBIOS carried in IEEE 802.3 frames with LLC headers. decnet(9) - DECnet carried in Ethernet V2 frames or in IEEE 802.3 frames with LLC/SNAP headers. ipv6(10) - Internet Protocol version 6 carried in Ethernet V2 frames or IEEE 802.3 frames with LLC/SNAP headers')
etsysESwitchProtocolIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 1, 4, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000)))
if mibBuilder.loadTexts: etsysESwitchProtocolIndex.setStatus('current')
if mibBuilder.loadTexts: etsysESwitchProtocolIndex.setDescription("When etsysESwitchProtocolType indicates a user-defined protocol type, this index should identify the corresponding protocol definition. That is, to say, for a 'userEtherType' row, this index should point to a row in the etsysESwitchEtherTypeTable. When etsysESwitchProtocolType completely specifies the protocol type, this index should be set to 1.")
etsysESwitchProtocolConstraint = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 1, 4, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("portMask", 1), ("vlan", 2))).clone('portMask')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysESwitchProtocolConstraint.setStatus('current')
if mibBuilder.loadTexts: etsysESwitchProtocolConstraint.setDescription('Indicates what type of constraint the switch should apply to packets caught by the (port, protocol) filter. portMask(1) - Use the etsysESwitchProtocolAllowedToGoTo mask to determine where the packets may be forwarded. vlan(2) - Classify the packets as belonging to the VLAN etsysESwitchProtocolVlanId. Note that on the RoamAbout AccessPoint R2, port/protocol constraints can sometimes take a back seat to other kinds of access controls.')
etsysESwitchProtocolAllowedToGoTo = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 1, 4, 2, 1, 5), PortList()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysESwitchProtocolAllowedToGoTo.setStatus('current')
if mibBuilder.loadTexts: etsysESwitchProtocolAllowedToGoTo.setDescription("A port mask object indicating where packets that match this row's (port, protocol) filter are allowed to go. It applies when etsysESwitchProtocolConstraint has the value portMask(1) and this row is valid.")
etsysESwitchProtocolVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 1, 4, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysESwitchProtocolVlanId.setStatus('current')
if mibBuilder.loadTexts: etsysESwitchProtocolVlanId.setDescription("A number identifying a VLAN to which packets that match this row's (port, protocol) filter should be assigned. It applies when etsysESwitchProtocolConstraint has the value vlan(2) and this row is valid.")
etsysESwitchProtocolStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 1, 4, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("invalid", 2), ("permanent", 3), ("deleteOnReset", 4))).clone('permanent')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysESwitchProtocolStatus.setStatus('current')
if mibBuilder.loadTexts: etsysESwitchProtocolStatus.setDescription("This object indicates the administrative status of this entry. other(1) - This entry is currently in effect, but the conditions under which it will remain so differ from the ones described for the other enumeration values invalid(2) - Writing this value to the object deletes the filter or VLAN constraint. The agent may delete the SNMP table row or return an AdminStatus of 'invalid' at its discretion. permanent(3) - This entry is currently in use and will remain so after the next reset of the bridge. deleteOnReset(4) - This entry is currently in use and will remain so until the next reset of the bridge.")
etsysESwitchProtocolPreempted = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 1, 4, 2, 1, 8), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysESwitchProtocolPreempted.setStatus('current')
if mibBuilder.loadTexts: etsysESwitchProtocolPreempted.setDescription('If true, indicates that the switch has taken control of this row and its associated resources (e.g., to support 802.1x authentication).')
etsysESwitchConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 2))
etsysESwitchGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 2, 1))
etsysESwitchCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 2, 2))
etsysESwitchBaseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 2, 1, 1)).setObjects(("ENTERASYS-ESWITCH-MIB", "etsysESwitchAdminStatus"), ("ENTERASYS-ESWITCH-MIB", "etsysESwitchRateLimitSwitch"), ("ENTERASYS-ESWITCH-MIB", "etsysESwitchRateLimit"), ("ENTERASYS-ESWITCH-MIB", "etsysESwitchAddressFilter"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysESwitchBaseGroup = etsysESwitchBaseGroup.setStatus('current')
if mibBuilder.loadTexts: etsysESwitchBaseGroup.setDescription('The basic etsysESwitch objects.')
etsysESwitchEtherTypeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 2, 1, 2)).setObjects(("ENTERASYS-ESWITCH-MIB", "etsysESwitchEtherTypeValue"), ("ENTERASYS-ESWITCH-MIB", "etsysESwitchEtherTypeStatus"), ("ENTERASYS-ESWITCH-MIB", "etsysESwitchEtherTypePreempted"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysESwitchEtherTypeGroup = etsysESwitchEtherTypeGroup.setStatus('current')
if mibBuilder.loadTexts: etsysESwitchEtherTypeGroup.setDescription('A collection of objects for configuring user-defined EtherTypes.')
etsysESwitchProtocolGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 2, 1, 3)).setObjects(("ENTERASYS-ESWITCH-MIB", "etsysESwitchProtocolConstraint"), ("ENTERASYS-ESWITCH-MIB", "etsysESwitchProtocolAllowedToGoTo"), ("ENTERASYS-ESWITCH-MIB", "etsysESwitchProtocolVlanId"), ("ENTERASYS-ESWITCH-MIB", "etsysESwitchProtocolStatus"), ("ENTERASYS-ESWITCH-MIB", "etsysESwitchProtocolPreempted"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysESwitchProtocolGroup = etsysESwitchProtocolGroup.setStatus('current')
if mibBuilder.loadTexts: etsysESwitchProtocolGroup.setDescription('A collection of objects for configuring protocol-based filtering.')
etsysESwitchCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 10, 2, 2, 1)).setObjects(("ENTERASYS-ESWITCH-MIB", "etsysESwitchBaseGroup"), ("ENTERASYS-ESWITCH-MIB", "etsysESwitchEtherTypeGroup"), ("ENTERASYS-ESWITCH-MIB", "etsysESwitchProtocolGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysESwitchCompliance = etsysESwitchCompliance.setStatus('current')
if mibBuilder.loadTexts: etsysESwitchCompliance.setDescription('The compliance statement for devices that support Extended Switch.')
mibBuilder.exportSymbols("ENTERASYS-ESWITCH-MIB", etsysESwitchEtherTypeEntry=etsysESwitchEtherTypeEntry, etsysESwitchEtherTypeStatus=etsysESwitchEtherTypeStatus, etsysESwitchParams=etsysESwitchParams, etsysESwitchAddrFilterTable=etsysESwitchAddrFilterTable, etsysESwitchRateLimitSwitch=etsysESwitchRateLimitSwitch, etsysESwitchGroups=etsysESwitchGroups, etsysESwitchRateLimit=etsysESwitchRateLimit, etsysESwitchProtocolAllowedToGoTo=etsysESwitchProtocolAllowedToGoTo, etsysESwitchProtocolConstraint=etsysESwitchProtocolConstraint, etsysESwitchBaseGroup=etsysESwitchBaseGroup, etsysESwitchProtocolGroup=etsysESwitchProtocolGroup, etsysESwitchRateLimiting=etsysESwitchRateLimiting, etsysESwitchEtherTypeGroup=etsysESwitchEtherTypeGroup, etsysESwitchAddressFilter=etsysESwitchAddressFilter, etsysESwitchEtherTypePreempted=etsysESwitchEtherTypePreempted, etsysESwitchProtocolReceivePort=etsysESwitchProtocolReceivePort, etsysESwitchEtherTypeValue=etsysESwitchEtherTypeValue, etsysESwitchCompliances=etsysESwitchCompliances, etsysESwitchProtocolVlanId=etsysESwitchProtocolVlanId, etsysESwitchProtocolEntry=etsysESwitchProtocolEntry, etsysESwitchProtocolStatus=etsysESwitchProtocolStatus, etsysESwitchAdminStatus=etsysESwitchAdminStatus, etsysESwitchRateLimitingTable=etsysESwitchRateLimitingTable, PYSNMP_MODULE_ID=enterasysESwitchMIB, etsysESwitchProtocolTable=etsysESwitchProtocolTable, etsysESwitchEtherTypeIndex=etsysESwitchEtherTypeIndex, etsysESwitchEtherTypeTable=etsysESwitchEtherTypeTable, etsysESwitchProtocolIndex=etsysESwitchProtocolIndex, etsysESwitchConformance=etsysESwitchConformance, etsysESwitchAddrFilterEntry=etsysESwitchAddrFilterEntry, enterasysESwitchMIB=enterasysESwitchMIB, etsysESwitchProtocolObjects=etsysESwitchProtocolObjects, etsysESwitchCompliance=etsysESwitchCompliance, etsysESwitchFilter=etsysESwitchFilter, etsysESwitchProtocolPreempted=etsysESwitchProtocolPreempted, etsysESwitchObjects=etsysESwitchObjects, etsysESwitchRateLimitingEntry=etsysESwitchRateLimitingEntry, etsysESwitchProtocolType=etsysESwitchProtocolType)