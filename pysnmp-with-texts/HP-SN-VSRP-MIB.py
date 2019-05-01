#
# PySNMP MIB module HP-SN-VSRP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-SN-MIBS
# Produced by pysmi-0.3.4 at Wed May  1 13:36:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
snVsrp, = mibBuilder.importSymbols("HP-SN-SWITCH-GROUP-MIB", "snVsrp")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, MibIdentifier, TimeTicks, Integer32, NotificationType, Unsigned32, iso, Counter64, Gauge32, ObjectIdentity, Counter32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibIdentifier", "TimeTicks", "Integer32", "NotificationType", "Unsigned32", "iso", "Counter64", "Gauge32", "ObjectIdentity", "Counter32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class MacAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

snVsrpGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3, 21, 1))
snVsrpIfIntf = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3, 21, 2))
snVsrpVirRtr = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3, 21, 3))
snVsrpGroupOperModeVsrp = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3, 21, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snVsrpGroupOperModeVsrp.setStatus('mandatory')
if mibBuilder.loadTexts: snVsrpGroupOperModeVsrp.setDescription('The VSRP is configured on this system either enabled or disabled and thedefault is disabled mode. disabled(0)..........disable VSRP enabled(1)...........activate VSRP')
snVsrpIfStateChangeTrap = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3, 21, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snVsrpIfStateChangeTrap.setStatus('mandatory')
if mibBuilder.loadTexts: snVsrpIfStateChangeTrap.setDescription('Indicates whether the SNMP agent process is permitted to generate VSRP interface state change traps.')
snVsrpIfMaxNumVridPerIntf = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3, 21, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVsrpIfMaxNumVridPerIntf.setStatus('mandatory')
if mibBuilder.loadTexts: snVsrpIfMaxNumVridPerIntf.setDescription('Indicates the maximum number of VRID per interface.')
snVsrpIfMaxNumVridPerSystem = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3, 21, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVsrpIfMaxNumVridPerSystem.setStatus('mandatory')
if mibBuilder.loadTexts: snVsrpIfMaxNumVridPerSystem.setDescription('Indicates the maximum number of VRID per system.')
snVsrpClearVrrpStat = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3, 21, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("normal", 0), ("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snVsrpClearVrrpStat.setStatus('mandatory')
if mibBuilder.loadTexts: snVsrpClearVrrpStat.setDescription('Clear VSRP statistics command.')
snVsrpIfTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3, 21, 2, 1), )
if mibBuilder.loadTexts: snVsrpIfTable.setStatus('mandatory')
if mibBuilder.loadTexts: snVsrpIfTable.setDescription('The VSRP Interface Table describes the interfaces from the viewpoint of VSRP.')
snVsrpIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3, 21, 2, 1, 1), ).setIndexNames((0, "HP-SN-VSRP-MIB", "snVsrpIfVlanId"))
if mibBuilder.loadTexts: snVsrpIfEntry.setStatus('mandatory')
if mibBuilder.loadTexts: snVsrpIfEntry.setDescription('The VSRP Interface Entry describes one interface from the viewpoint of VSRP.')
snVsrpIfVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3, 21, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVsrpIfVlanId.setStatus('mandatory')
if mibBuilder.loadTexts: snVsrpIfVlanId.setDescription('Vlan index.')
snVsrpIfAuthType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3, 21, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("noAuth", 0), ("simpleTextPasswd", 1), ("ipAuthHeader", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snVsrpIfAuthType.setStatus('mandatory')
if mibBuilder.loadTexts: snVsrpIfAuthType.setDescription('The authentication type of this interface.')
snVsrpIfAuthPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3, 21, 2, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snVsrpIfAuthPassword.setStatus('mandatory')
if mibBuilder.loadTexts: snVsrpIfAuthPassword.setDescription('The simple text password is allowed if only if the snVsrpIfAuthType type is simpleTextPasswd.')
snVsrpVirRtrTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3, 21, 3, 1), )
if mibBuilder.loadTexts: snVsrpVirRtrTable.setStatus('mandatory')
if mibBuilder.loadTexts: snVsrpVirRtrTable.setDescription('The vsrp virtual router Entry describes one virtual router from the viewpoint of vsrp.')
snVsrpVirRtrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3, 21, 3, 1, 1), ).setIndexNames((0, "HP-SN-VSRP-MIB", "snVsrpVirRtrVlanId"), (0, "HP-SN-VSRP-MIB", "snVsrpVirRtrId"))
if mibBuilder.loadTexts: snVsrpVirRtrEntry.setStatus('mandatory')
if mibBuilder.loadTexts: snVsrpVirRtrEntry.setDescription('The vsrp virtual router Entry describes one virtual router from the viewpoint of vsrp.')
snVsrpVirRtrVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3, 21, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVsrpVirRtrVlanId.setStatus('mandatory')
if mibBuilder.loadTexts: snVsrpVirRtrVlanId.setDescription('Vlan index.')
snVsrpVirRtrId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3, 21, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVsrpVirRtrId.setStatus('mandatory')
if mibBuilder.loadTexts: snVsrpVirRtrId.setDescription('One of the virtual router ID of this vsrp interface.')
snVsrpVirRtrOwnership = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3, 21, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("incomplete", 0), ("owner", 1), ("backup", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snVsrpVirRtrOwnership.setStatus('mandatory')
if mibBuilder.loadTexts: snVsrpVirRtrOwnership.setDescription('The ownership of this vsrp router interface can be set to backup(2). VirRtr SNMP-GET returns incomplete(0), it means no IP address has assigned to this vsrp router interface.')
snVsrpVirRtrCfgPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3, 21, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 254)).clone(100)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snVsrpVirRtrCfgPriority.setStatus('mandatory')
if mibBuilder.loadTexts: snVsrpVirRtrCfgPriority.setDescription('The higher the number the higher the priority is. This parameter decides which backup router should becomes the Active Router for the interface. A backup Router with higher priority selected to becomes the Active Router. Therefore, this Object can be set if only if snVsrpVirRtrOwnership is set to backup(2).')
snVsrpVirRtrTrackPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3, 21, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 254))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snVsrpVirRtrTrackPriority.setStatus('mandatory')
if mibBuilder.loadTexts: snVsrpVirRtrTrackPriority.setDescription('The higher the number the higher the priority is. after this object is configured, the snVsrpVirRtrCurrPriority of this interface will be adjusted dynamically with this track priority when the Track Port states first changes from UP to DOWN.')
snVsrpVirRtrCurrPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3, 21, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 254))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVsrpVirRtrCurrPriority.setStatus('mandatory')
if mibBuilder.loadTexts: snVsrpVirRtrCurrPriority.setDescription('The higher the number the higher the priority is. This object will be adjusted dynamically with the track priority when the Track Port states first changes from UP to DOWN.')
snVsrpVirRtrHelloInt = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3, 21, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 84)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snVsrpVirRtrHelloInt.setStatus('mandatory')
if mibBuilder.loadTexts: snVsrpVirRtrHelloInt.setDescription('Time interval between advertisements (seconds).')
snVsrpVirRtrDeadInt = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3, 21, 3, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 84)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snVsrpVirRtrDeadInt.setStatus('mandatory')
if mibBuilder.loadTexts: snVsrpVirRtrDeadInt.setDescription('Dead interval (seconds).')
snVsrpVirRtrPreemptMode = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3, 21, 3, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snVsrpVirRtrPreemptMode.setStatus('mandatory')
if mibBuilder.loadTexts: snVsrpVirRtrPreemptMode.setDescription('This mode controls whether a higher priority Backup router preempts a lower priority Master. The mode with enabled(1) allow preemption and disabled(0) prohibit preemption.')
snVsrpVirRtrState = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3, 21, 3, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("init", 0), ("master", 1), ("backup", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVsrpVirRtrState.setStatus('mandatory')
if mibBuilder.loadTexts: snVsrpVirRtrState.setDescription("This object specifies the vsrp Router's interface state as: init(0)...initialization state. master(1)...master state. backup(2)...backup state.")
snVsrpVirRtrIpAddrMask = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3, 21, 3, 1, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(64, 64)).setFixedLength(64)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snVsrpVirRtrIpAddrMask.setStatus('mandatory')
if mibBuilder.loadTexts: snVsrpVirRtrIpAddrMask.setDescription('The numbers of IP Addresses of this virtual router of this interface, this holds good for L3 vsrp.')
snVsrpVirRtrActivate = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3, 21, 3, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snVsrpVirRtrActivate.setStatus('mandatory')
if mibBuilder.loadTexts: snVsrpVirRtrActivate.setDescription("This object specifies the vsrp Router's activate command as: disabled(0)...deactivate this vsrp Router. enabled(1)....activate this vsrp Router.")
snVsrpVirRtrTrackPortList = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3, 21, 3, 1, 1, 13), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snVsrpVirRtrTrackPortList.setStatus('mandatory')
if mibBuilder.loadTexts: snVsrpVirRtrTrackPortList.setDescription("This object specifies the identity of the physical port and virtual ports whose state is to be monitored. Each port index is an ifIndex, if there are consecutive 4 or more ifIndex then they will be encoded like below. Encoding and decoding scheme is range based: Each range prefix with 0000 (2 octets) where 0000 is not valid ifIndex. Next 2 octets indicates lower range ifIndex, followed by 2 octets of higher range ifIndex. Individual(non range) ones will be displayed as it is. Ex: port list: 0001..0005 0015 0032..0047 Port list in PDU: 0000 0001 0005 000f 0000 0020 002f. If this object is configured then the Preference Level of this interface will be adjusted dynamically depending on the state of the Track Port. The interface's Preference Level is reduced by value of Preference Level parameter when the Track Port states first changes from UP to DOWN. When the Track Port next comes up the interface's Preference Level is increased by the amount specified by the Preference Level. The router VSRP physical track port membership.")
snVsrpVirRtrAdvertiseBackup = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3, 21, 3, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snVsrpVirRtrAdvertiseBackup.setStatus('mandatory')
if mibBuilder.loadTexts: snVsrpVirRtrAdvertiseBackup.setDescription('Set Advertise this backup router to master ')
snVsrpVirRtrHoldDownInt = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3, 21, 3, 1, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 84)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snVsrpVirRtrHoldDownInt.setStatus('mandatory')
if mibBuilder.loadTexts: snVsrpVirRtrHoldDownInt.setDescription('VSRP protection mechanism, an extra delay for a switch in backup mode to upgrade itself to master mode')
snVsrpVirRtrInitTtl = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3, 21, 3, 1, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snVsrpVirRtrInitTtl.setStatus('mandatory')
if mibBuilder.loadTexts: snVsrpVirRtrInitTtl.setDescription('VSRP:TTL in the hello packet to regulate the distance that a hello packet can travel. It prevents the flooding of VSRP hello packets in the network')
snVsrpVirRtrIncPortList = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3, 21, 3, 1, 1, 17), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snVsrpVirRtrIncPortList.setStatus('mandatory')
if mibBuilder.loadTexts: snVsrpVirRtrIncPortList.setDescription('Include all free ports of the VLAN into its control ports')
snVsrpVirRtrSave = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3, 21, 3, 1, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snVsrpVirRtrSave.setStatus('mandatory')
if mibBuilder.loadTexts: snVsrpVirRtrSave.setDescription('Set VSRP to save current parameters value')
snVsrpVirRtrBackupInt = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3, 21, 3, 1, 1, 19), Integer32().subtype(subtypeSpec=ValueRangeConstraint(60, 3600)).clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snVsrpVirRtrBackupInt.setStatus('mandatory')
if mibBuilder.loadTexts: snVsrpVirRtrBackupInt.setDescription('Time interval between backup routers hello message advertisements (seconds).')
snVsrpVirRtrRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3, 21, 3, 1, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("invalid", 1), ("valid", 2), ("delete", 3), ("create", 4), ("modify", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snVsrpVirRtrRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: snVsrpVirRtrRowStatus.setDescription("This object is used to create and delete row in the table and control if they are used. The values that can be written are: delete(3)...deletes the row create(4)...creates a new row modify(5)...modifies an existing row VirRtr the row exists, then a SET with value of create(4) returns error 'badValue'. Deleted rows go away immediately. The following values can be returned on reads: noSuch(0)...no such row invalid(1)...Setting it to 'invalid' has the effect of rendering it inoperative.. valid(2)....the row exists and is valid")
snVsrpVirRtrRxArpPktDropCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3, 21, 3, 1, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVsrpVirRtrRxArpPktDropCnts.setStatus('mandatory')
if mibBuilder.loadTexts: snVsrpVirRtrRxArpPktDropCnts.setDescription('The received vsrp ARP Packet Drop Counts.')
snVsrpVirRtrRxIpPktDropCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3, 21, 3, 1, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVsrpVirRtrRxIpPktDropCnts.setStatus('mandatory')
if mibBuilder.loadTexts: snVsrpVirRtrRxIpPktDropCnts.setDescription('The received VSRP IP Packet Drop Counts.')
snVsrpVirRtrRxPortMismatchCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3, 21, 3, 1, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVsrpVirRtrRxPortMismatchCnts.setStatus('mandatory')
if mibBuilder.loadTexts: snVsrpVirRtrRxPortMismatchCnts.setDescription('The received vsrp Port mismatching Counts.')
snVsrpVirRtrRxNumOfIpMismatchCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3, 21, 3, 1, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVsrpVirRtrRxNumOfIpMismatchCnts.setStatus('mandatory')
if mibBuilder.loadTexts: snVsrpVirRtrRxNumOfIpMismatchCnts.setDescription('The received VSRP Number of IP Addresses mismatching Counts.')
snVsrpVirRtrRxIpMismatchCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3, 21, 3, 1, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVsrpVirRtrRxIpMismatchCnts.setStatus('mandatory')
if mibBuilder.loadTexts: snVsrpVirRtrRxIpMismatchCnts.setDescription('The received vsrp IP Address mismatching Counts.')
snVsrpVirRtrRxHelloIntMismatchCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3, 21, 3, 1, 1, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVsrpVirRtrRxHelloIntMismatchCnts.setStatus('mandatory')
if mibBuilder.loadTexts: snVsrpVirRtrRxHelloIntMismatchCnts.setDescription('The counts of the virtual router interface with hello interval mismatch counts.')
snVsrpVirRtrRxPriorityZeroFromMasterCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3, 21, 3, 1, 1, 27), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVsrpVirRtrRxPriorityZeroFromMasterCnts.setStatus('mandatory')
if mibBuilder.loadTexts: snVsrpVirRtrRxPriorityZeroFromMasterCnts.setDescription('The counts of the virtual router interface with Priority zero from the master.')
snVsrpVirRtrRxHigherPriorityCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3, 21, 3, 1, 1, 28), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVsrpVirRtrRxHigherPriorityCnts.setStatus('mandatory')
if mibBuilder.loadTexts: snVsrpVirRtrRxHigherPriorityCnts.setDescription('The counts of the virtual router interface with higher Priority.')
snVsrpVirRtrTransToMasterStateCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3, 21, 3, 1, 1, 29), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVsrpVirRtrTransToMasterStateCnts.setStatus('mandatory')
if mibBuilder.loadTexts: snVsrpVirRtrTransToMasterStateCnts.setDescription('The counts of the virtual router interface transition to master state.')
snVsrpVirRtrTransToBackupStateCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3, 21, 3, 1, 1, 30), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVsrpVirRtrTransToBackupStateCnts.setStatus('mandatory')
if mibBuilder.loadTexts: snVsrpVirRtrTransToBackupStateCnts.setDescription('The counts of the virtual router interface transition to backup state.')
snVsrpVirRtrCurrDeadInt = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3, 21, 3, 1, 1, 31), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVsrpVirRtrCurrDeadInt.setStatus('mandatory')
if mibBuilder.loadTexts: snVsrpVirRtrCurrDeadInt.setDescription('Current Dead interval (in 100 milliseconds).')
snVsrpVirRtrCurHelloInt = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3, 21, 3, 1, 1, 32), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 84))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVsrpVirRtrCurHelloInt.setStatus('mandatory')
if mibBuilder.loadTexts: snVsrpVirRtrCurHelloInt.setDescription('Set backup router hello interval')
snVsrpVirRtrCurHoldDownInt = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3, 21, 3, 1, 1, 33), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 84))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVsrpVirRtrCurHoldDownInt.setStatus('mandatory')
if mibBuilder.loadTexts: snVsrpVirRtrCurHoldDownInt.setDescription('VSRP protection mechanism, an extra delay for a switch in backup mode to upgrade itself to master mode')
snVsrpVirRtrCurInitTtl = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3, 21, 3, 1, 1, 34), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVsrpVirRtrCurInitTtl.setStatus('mandatory')
if mibBuilder.loadTexts: snVsrpVirRtrCurInitTtl.setDescription('VSRP:TTL in the hello packet to regulate the distance that a hello packet can travel. It prevents the flooding of VSRP hello packets in the network')
snVsrpVirRtrHelloMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3, 21, 3, 1, 1, 35), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVsrpVirRtrHelloMacAddress.setStatus('mandatory')
if mibBuilder.loadTexts: snVsrpVirRtrHelloMacAddress.setDescription('Hello MAC address.')
snVsrpVirRtrMasterIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3, 21, 3, 1, 1, 36), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVsrpVirRtrMasterIpAddr.setStatus('mandatory')
if mibBuilder.loadTexts: snVsrpVirRtrMasterIpAddr.setDescription("The master router's real/virtual (primary) IP address. This is the IP address listed as the source in vsrp advertisement last received by this virtual router.")
mibBuilder.exportSymbols("HP-SN-VSRP-MIB", snVsrpVirRtrTrackPortList=snVsrpVirRtrTrackPortList, snVsrpVirRtrRxIpMismatchCnts=snVsrpVirRtrRxIpMismatchCnts, snVsrpIfMaxNumVridPerIntf=snVsrpIfMaxNumVridPerIntf, snVsrpVirRtrHelloInt=snVsrpVirRtrHelloInt, snVsrpVirRtrDeadInt=snVsrpVirRtrDeadInt, snVsrpGroupOperModeVsrp=snVsrpGroupOperModeVsrp, snVsrpVirRtrOwnership=snVsrpVirRtrOwnership, snVsrpVirRtrTrackPriority=snVsrpVirRtrTrackPriority, snVsrpVirRtrIncPortList=snVsrpVirRtrIncPortList, snVsrpVirRtrRxPortMismatchCnts=snVsrpVirRtrRxPortMismatchCnts, snVsrpVirRtrCurHoldDownInt=snVsrpVirRtrCurHoldDownInt, snVsrpVirRtrTable=snVsrpVirRtrTable, snVsrpIfIntf=snVsrpIfIntf, snVsrpVirRtrCurInitTtl=snVsrpVirRtrCurInitTtl, MacAddress=MacAddress, snVsrpIfAuthPassword=snVsrpIfAuthPassword, snVsrpVirRtrRxNumOfIpMismatchCnts=snVsrpVirRtrRxNumOfIpMismatchCnts, snVsrpVirRtrRxIpPktDropCnts=snVsrpVirRtrRxIpPktDropCnts, snVsrpVirRtrCurHelloInt=snVsrpVirRtrCurHelloInt, snVsrpVirRtrSave=snVsrpVirRtrSave, snVsrpVirRtrState=snVsrpVirRtrState, snVsrpVirRtrRxArpPktDropCnts=snVsrpVirRtrRxArpPktDropCnts, snVsrpVirRtrRxPriorityZeroFromMasterCnts=snVsrpVirRtrRxPriorityZeroFromMasterCnts, snVsrpVirRtrRxHigherPriorityCnts=snVsrpVirRtrRxHigherPriorityCnts, snVsrpVirRtrCurrDeadInt=snVsrpVirRtrCurrDeadInt, snVsrpVirRtrEntry=snVsrpVirRtrEntry, snVsrpVirRtrIpAddrMask=snVsrpVirRtrIpAddrMask, snVsrpIfStateChangeTrap=snVsrpIfStateChangeTrap, snVsrpIfEntry=snVsrpIfEntry, snVsrpVirRtrId=snVsrpVirRtrId, snVsrpVirRtrCurrPriority=snVsrpVirRtrCurrPriority, snVsrpVirRtrPreemptMode=snVsrpVirRtrPreemptMode, snVsrpVirRtrMasterIpAddr=snVsrpVirRtrMasterIpAddr, snVsrpVirRtrInitTtl=snVsrpVirRtrInitTtl, snVsrpIfVlanId=snVsrpIfVlanId, snVsrpVirRtrTransToMasterStateCnts=snVsrpVirRtrTransToMasterStateCnts, snVsrpIfTable=snVsrpIfTable, snVsrpVirRtrCfgPriority=snVsrpVirRtrCfgPriority, snVsrpIfMaxNumVridPerSystem=snVsrpIfMaxNumVridPerSystem, snVsrpVirRtrRxHelloIntMismatchCnts=snVsrpVirRtrRxHelloIntMismatchCnts, snVsrpVirRtrHoldDownInt=snVsrpVirRtrHoldDownInt, snVsrpVirRtrActivate=snVsrpVirRtrActivate, snVsrpGlobal=snVsrpGlobal, snVsrpVirRtrAdvertiseBackup=snVsrpVirRtrAdvertiseBackup, snVsrpVirRtrBackupInt=snVsrpVirRtrBackupInt, snVsrpVirRtr=snVsrpVirRtr, snVsrpVirRtrHelloMacAddress=snVsrpVirRtrHelloMacAddress, snVsrpVirRtrVlanId=snVsrpVirRtrVlanId, snVsrpVirRtrRowStatus=snVsrpVirRtrRowStatus, snVsrpClearVrrpStat=snVsrpClearVrrpStat, snVsrpVirRtrTransToBackupStateCnts=snVsrpVirRtrTransToBackupStateCnts, snVsrpIfAuthType=snVsrpIfAuthType)
