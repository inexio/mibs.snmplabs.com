#
# PySNMP MIB module CISCO-ETHER-CFM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ETHER-CFM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:57:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
VlanId, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanId")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, Gauge32, ModuleIdentity, NotificationType, Integer32, TimeTicks, Counter64, IpAddress, Bits, iso, ObjectIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Gauge32", "ModuleIdentity", "NotificationType", "Integer32", "TimeTicks", "Counter64", "IpAddress", "Bits", "iso", "ObjectIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32")
DisplayString, TimeStamp, MacAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TimeStamp", "MacAddress", "TextualConvention")
ciscoEtherCfmMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 461))
ciscoEtherCfmMIB.setRevisions(('2004-12-28 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoEtherCfmMIB.setRevisionsDescriptions(('The initial revision of this MIB.',))
if mibBuilder.loadTexts: ciscoEtherCfmMIB.setLastUpdated('200412280000Z')
if mibBuilder.loadTexts: ciscoEtherCfmMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoEtherCfmMIB.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-ethermibs@cisco.com')
if mibBuilder.loadTexts: ciscoEtherCfmMIB.setDescription('This MIB module defines the managed objects and notifications for Ethernet Connectivity Fault Management (CFM). CFM is an end-to-end per service instance Ethernet layer Operations, Administration and Management (OAM) protocol. CFM events include: - Maintenance End-Point (MEP) coming up: establishing connectivity - Maintenance End-Point going down: losing connectivity - Maintenance End-Point unknown: unexpected - Maintenance End-Point missing: expected but not reachable - Continuity Check Configuration Error: collision in MEP IDs - Continuity Check Loop: forwarding loop in network - Continuity Check Cross-connect: cross-connected forwarding path. The following acronyms are used in this module: - MEP: Maintenance End Point - MEPID: Maintenance End Point Identifier - CC: Continuity Check - CCDB: Continuity Check Database - SVLAN: Service Provider Virtual Local Area Network - VLAN: Virtual Local Area Network - CLI: Command Line Interface. - OAM: Operations Administration and Management.')
ciscoEtherCfmMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 461, 0))
ciscoEtherCfmMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 461, 1))
ciscoEtherCfmMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 461, 2))
cecCfmEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1))
class CfmMepid(TextualConvention, Unsigned32):
    description = 'The identifier of a maintenance end point.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 8191)

cEtherCfmMaxEventIndex = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cEtherCfmMaxEventIndex.setStatus('current')
if mibBuilder.loadTexts: cEtherCfmMaxEventIndex.setDescription('This object specifies the maximum upper value supported for the cEtherCfmEventIndex index by this agent.')
cEtherCfmEventTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2), )
if mibBuilder.loadTexts: cEtherCfmEventTable.setStatus('current')
if mibBuilder.loadTexts: cEtherCfmEventTable.setDescription("This table contains a collection of Ethernet CFM notifications generated by the device. The notifications correspond to events recognized by the device and fall into the following classes: - MEP-Up - MEP-Down - Configuration Error - Forwarding Loop - Cross-connected Ethernet Connection - Crosscheck Missing MEP - Crosscheck Unknown MEP - Crosscheck Service Up A conceptual row is created in this table whenever the device encounters one of the events listed above. Rows can only be created by the agent, and not at the request of the management station. Rows are deleted at the request of a management station by setting the cEtherCfmEventDeleteRow object to 'delete'. Another way of deleting rows is through the CLI. Although this table may be indexed uniquely by the cEtherCfmEventIndex index, the first two indices (cEtherCfmEventDomainIndex and cEtherCfmEventSvlan) are used to speed-up queries per maintenance domain and per customer service instance. Furthermore, these two indices will help in defining the MIB views easily in order to restrict access to the MIB to particular entities (be it a service provider, or operator, or customer).")
cEtherCfmEventEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-ETHER-CFM-MIB", "cEtherCfmEventDomainIndex"), (0, "CISCO-ETHER-CFM-MIB", "cEtherCfmEventSvlan"), (0, "CISCO-ETHER-CFM-MIB", "cEtherCfmEventIndex"))
if mibBuilder.loadTexts: cEtherCfmEventEntry.setStatus('current')
if mibBuilder.loadTexts: cEtherCfmEventEntry.setDescription('An entry in this table is created for every event reported by Ethernet CFM.')
cEtherCfmEventDomainIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: cEtherCfmEventDomainIndex.setStatus('current')
if mibBuilder.loadTexts: cEtherCfmEventDomainIndex.setDescription('This object represents the ID which uniquely identifies a CFM maintenance domain on the device. Every domain can be uniquely identified by its user-defined name (cEtherCfmEventDomainName) or device-assigned ID (this object).')
cEtherCfmEventSvlan = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1, 2), VlanId())
if mibBuilder.loadTexts: cEtherCfmEventSvlan.setStatus('current')
if mibBuilder.loadTexts: cEtherCfmEventSvlan.setDescription('The service VLAN identifier of the customer service instance to which the event belongs.')
cEtherCfmEventIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: cEtherCfmEventIndex.setStatus('current')
if mibBuilder.loadTexts: cEtherCfmEventIndex.setDescription('A monotonically increasing integer for the sole purpose of indexing CFM events. When it reaches the maximum value supported by the agent, as defined in the cEtherCfmMaxEventIndex object, the agent wraps the value back to 1 and may flush existing entries.')
cEtherCfmEventDomainName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cEtherCfmEventDomainName.setStatus('current')
if mibBuilder.loadTexts: cEtherCfmEventDomainName.setDescription('The name of the CFM maintenance domain.')
cEtherCfmEventType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("mepUp", 1), ("mepDown", 2), ("xconnect", 3), ("loop", 4), ("config", 5), ("xcheckMissing", 6), ("xcheckUnknown", 7), ("xcheckServiceUp", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cEtherCfmEventType.setStatus('current')
if mibBuilder.loadTexts: cEtherCfmEventType.setDescription('This object informs the management station of how to interpret the rest of the objects within a row, as summarized in the following table: Legend I: Ignored Object V: Valid Object Object cEtherCfmEventType | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 ================================================================ | | | | | | | | cEtherCfmEventDomainIndex | V | V | V | V | V | V | V | V | | | | | | | | cEtherCfmEventSvlan | V | V | V | V | V | V | V | V | | | | | | | | cEtherCfmEventIndex | V | V | V | V | V | V | V | V | | | | | | | | cEtherCfmEventLastChange | V | V | V | V | V | V | V | V | | | | | | | | cEtherCfmEventServiceId | V | V | V | V | V | V | V | V | | | | | | | | cEtherCfmEventDomainName | V | V | V | V | V | V | V | V | | | | | | | | cEtherCfmEventLclMepid | I | I | I | V | V | I | I | I | | | | | | | | cEtherCfmEventLclMacAddress | V | V | V | V | V | V | V | V | | | | | | | | cEtherCfmEventLclMepCount | V | V | I | I | I | I | I | I | | | | | | | | cEtherCfmEventLclIfCount | V | V | I | I | I | I | I | I | | | | | | | | cEtherCfmEventRmtMepid | V | V | V | I | I | V | V | I | | | | | | | | cEtherCfmEventRmtMacAddress | V | V | V | I | V | V | V | I | | | | | | | | cEtherCfmEventRmtPortState | V | I | I | I | I | I | I | I | | | | | | | | cEtherCfmEventRmtServiceId | I | I | V | I | I | I | I | I | | | | | | | | cEtherCfmEventCode | V | V | I | I | I | I | I | I | | | | | | | | cEtherCfmEventDeleteRow | V | V | V | V | V | V | V | V | | | | | | | | Note: When reading any ignored object, a value of 0 will be returned by the agent.')
cEtherCfmEventLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1, 6), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cEtherCfmEventLastChange.setStatus('current')
if mibBuilder.loadTexts: cEtherCfmEventLastChange.setDescription('The value of sysUpTime at the time when this row was created.')
cEtherCfmEventServiceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1, 7), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cEtherCfmEventServiceId.setStatus('current')
if mibBuilder.loadTexts: cEtherCfmEventServiceId.setDescription('The customer service instance to which the event belongs.')
cEtherCfmEventLclMepid = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1, 8), CfmMepid()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cEtherCfmEventLclMepid.setStatus('current')
if mibBuilder.loadTexts: cEtherCfmEventLclMepid.setDescription('The identifier of the local MEP impacted by the event.')
cEtherCfmEventLclMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1, 9), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cEtherCfmEventLclMacAddress.setStatus('current')
if mibBuilder.loadTexts: cEtherCfmEventLclMacAddress.setDescription('The MAC address of the device reporting the event.')
cEtherCfmEventLclMepCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cEtherCfmEventLclMepCount.setStatus('current')
if mibBuilder.loadTexts: cEtherCfmEventLclMepCount.setDescription('The number of local MEPs affected by the event.')
cEtherCfmEventLclIfCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cEtherCfmEventLclIfCount.setStatus('current')
if mibBuilder.loadTexts: cEtherCfmEventLclIfCount.setDescription('The number of local interfaces affected by the event.')
cEtherCfmEventRmtMepid = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1, 12), CfmMepid()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cEtherCfmEventRmtMepid.setStatus('current')
if mibBuilder.loadTexts: cEtherCfmEventRmtMepid.setDescription('The maintenance end-point identifier of the remote MEP causing the event entry to be logged.')
cEtherCfmEventRmtMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1, 13), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cEtherCfmEventRmtMacAddress.setStatus('current')
if mibBuilder.loadTexts: cEtherCfmEventRmtMacAddress.setDescription('The MAC address of the remote maintenance point for which the event entry is being logged.')
cEtherCfmEventRmtPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("adminDown", 3), ("test", 4), ("remoteExcessiveErrors", 5), ("localExcessiveErrors", 6), ("localNoData", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cEtherCfmEventRmtPortState.setReference('IEEE 802.1ag Draft 1.0: Section 19.4.9.1 and IEEE 802.3ah-2004: Clause 57.')
if mibBuilder.loadTexts: cEtherCfmEventRmtPortState.setStatus('current')
if mibBuilder.loadTexts: cEtherCfmEventRmtPortState.setDescription("The operational state of the port on which the remote MEP is configured. This information is derived from the port-state as indicated in the CC message. The possible values are: 'up' - The port is operationally up. 'down' - The port is operationally (but not administratively) down. 'adminDown' - The port is administratively down. 'test' - The port is in test mode (perhaps due to an IEEE Standard 802.3ah OAM intrusive loopback operation). 'remoteExcessiveErrors' - 802.3ah OAM reports that the other end of the link is receiving an excessive number of invalid frames. 'localExcessiveErrors' - 802.3ah OAM reports that this end of the link is receiving an excessive number of invalid frames. 'localNoData' - No data and no CFM messages have been received for an excessive length of time.")
cEtherCfmEventRmtServiceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1, 15), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cEtherCfmEventRmtServiceId.setStatus('current')
if mibBuilder.loadTexts: cEtherCfmEventRmtServiceId.setDescription('The ID that the remote device has configured for the customer service instance (VLAN).')
cEtherCfmEventCode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("new", 1), ("returning", 2), ("portState", 3), ("lastGasp", 4), ("timeout", 5), ("configClear", 6), ("loopClear", 7), ("xconnectClear", 8), ("unknownClear", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cEtherCfmEventCode.setStatus('current')
if mibBuilder.loadTexts: cEtherCfmEventCode.setDescription("This object is used in decoding 'mepUp' and 'mepDown' events. ** For 'mepUp', the following codes are relevant: 'new' - This is the very first time the device receives a CC message from the remote MEP. 'returning' - The device received a CC message from a remote MEP for which it had an expired CCDB entry. 'portState' - The device received a CC message from a remote MEP for which it has a valid CCDB entry, and the message indicates a port status change. ** For 'mepDown', the following codes are relevant: 'lastGasp' - The device received a CC message from a remote MEP with zero lifetime. 'timeout' - The local CCDB entry for the remote MEP expired. 'configClear' - A previous CC message from a MEP that triggered a configuration error event is cleared. 'loopClear' - A previous CC message from a MEP that triggered a loop error event is cleared. 'xconnectClear' - A previous CC message from a MEP that triggered a crossconnect error event is cleared. 'unknownClear' - A previous CC message from a MEP that triggered an unknown MEP event is cleared.")
cEtherCfmEventDeleteRow = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noop", 1), ("delete", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cEtherCfmEventDeleteRow.setStatus('current')
if mibBuilder.loadTexts: cEtherCfmEventDeleteRow.setDescription("This object allows the management station to delete a row in the cEtherCfmEventTable in order to free system resources. When reading this object the value of 'noop' will be returned. This object can only be set to 'delete'. When this object is set to 'delete', the conceptual row corresponding to this object will be deleted to free system resources. This is equivalent to clearing the event log. Should the trigger that caused the event to be logged reoccur, the event will be re-asserted but in a different conceptual row.")
ciscoEtherCfmNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 461, 0, 0))
cEtherCfmCcMepUp = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 461, 0, 0, 1)).setObjects(("CISCO-ETHER-CFM-MIB", "cEtherCfmEventServiceId"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclMacAddress"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclMepCount"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclIfCount"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventRmtMepid"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventRmtMacAddress"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventCode"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventRmtPortState"))
if mibBuilder.loadTexts: cEtherCfmCcMepUp.setStatus('current')
if mibBuilder.loadTexts: cEtherCfmCcMepUp.setDescription('This notification is generated in the following cases: - when a remote MEP first comes up, that is when we receive a CC message from that MEP for the first time. - when the device receives a CC message from a MEP for which it has an expired CCDB entry. - when a CC message is received for a remote MEP for which the device already has a CCDB entry and the port-state in the received CC message is different from the cached previous state.')
cEtherCfmCcMepDown = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 461, 0, 0, 2)).setObjects(("CISCO-ETHER-CFM-MIB", "cEtherCfmEventServiceId"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclMacAddress"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclMepCount"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclIfCount"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventRmtMepid"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventRmtMacAddress"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventCode"))
if mibBuilder.loadTexts: cEtherCfmCcMepDown.setStatus('current')
if mibBuilder.loadTexts: cEtherCfmCcMepDown.setDescription('This notification is generated when a remote MEP goes down; i.e. the entry in CCDB corresponding to this MEP times out or the device receives a CC message with zero hold-time.')
cEtherCfmCcCrossconnect = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 461, 0, 0, 3)).setObjects(("CISCO-ETHER-CFM-MIB", "cEtherCfmEventServiceId"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclMacAddress"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventRmtMepid"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventRmtMacAddress"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventRmtServiceId"))
if mibBuilder.loadTexts: cEtherCfmCcCrossconnect.setStatus('current')
if mibBuilder.loadTexts: cEtherCfmCcCrossconnect.setDescription('This notification is generated when a device receives a CC message with the service ID not matching the one locally configured for the VLAN in question.')
cEtherCfmCcLoop = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 461, 0, 0, 4)).setObjects(("CISCO-ETHER-CFM-MIB", "cEtherCfmEventServiceId"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclMacAddress"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclMepid"))
if mibBuilder.loadTexts: cEtherCfmCcLoop.setStatus('current')
if mibBuilder.loadTexts: cEtherCfmCcLoop.setDescription('This notification is generated when a device receives a CC message with the same MEPID and MAC address as those of the device itself, indicating that there is a forwarding loop and that the device is receiving its own CC messages.')
cEtherCfmCcConfigError = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 461, 0, 0, 5)).setObjects(("CISCO-ETHER-CFM-MIB", "cEtherCfmEventServiceId"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclMacAddress"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclMepid"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventRmtMacAddress"))
if mibBuilder.loadTexts: cEtherCfmCcConfigError.setStatus('current')
if mibBuilder.loadTexts: cEtherCfmCcConfigError.setDescription('This notification is generated when a device receives a CC message with the same MEPID but different MAC address as those of the device itself, indicating that there is a mis-configuration in the network where a remote device has the same MEPID configured.')
cEtherCfmXCheckMissing = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 461, 0, 0, 6)).setObjects(("CISCO-ETHER-CFM-MIB", "cEtherCfmEventServiceId"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclMacAddress"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventRmtMepid"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventRmtMacAddress"))
if mibBuilder.loadTexts: cEtherCfmXCheckMissing.setStatus('current')
if mibBuilder.loadTexts: cEtherCfmXCheckMissing.setDescription('This notification is generated when an expected (configured) MEP does not come up during the cross-check start timeout interval.')
cEtherCfmXCheckUnknown = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 461, 0, 0, 7)).setObjects(("CISCO-ETHER-CFM-MIB", "cEtherCfmEventServiceId"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclMacAddress"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventRmtMepid"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventRmtMacAddress"))
if mibBuilder.loadTexts: cEtherCfmXCheckUnknown.setStatus('current')
if mibBuilder.loadTexts: cEtherCfmXCheckUnknown.setDescription('This notification is generated when an unexpected MEP comes up.')
cEtherCfmXCheckServiceUp = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 461, 0, 0, 8)).setObjects(("CISCO-ETHER-CFM-MIB", "cEtherCfmEventServiceId"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclMacAddress"))
if mibBuilder.loadTexts: cEtherCfmXCheckServiceUp.setStatus('current')
if mibBuilder.loadTexts: cEtherCfmXCheckServiceUp.setDescription('This notification is generated when all the MEPs belonging to a customer service instance come up before the expiration of the cross-check start timeout interval.')
ciscoEtherCfmMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 461, 2, 1))
ciscoEtherCfmMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 461, 2, 2))
ciscoEtherCfmMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 461, 2, 1, 1)).setObjects(("CISCO-ETHER-CFM-MIB", "ciscoEtherCfmMIBEventGroup"), ("CISCO-ETHER-CFM-MIB", "ciscoEtherCfmMIBNotifGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEtherCfmMIBCompliance = ciscoEtherCfmMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoEtherCfmMIBCompliance.setDescription('Compliance statement for agents that support the Ethernet CFM MIB.')
ciscoEtherCfmMIBEventGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 461, 2, 2, 1)).setObjects(("CISCO-ETHER-CFM-MIB", "cEtherCfmMaxEventIndex"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventDomainName"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventType"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLastChange"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventServiceId"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclMepid"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclMacAddress"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclMepCount"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclIfCount"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventRmtMepid"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventRmtMacAddress"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventRmtPortState"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventRmtServiceId"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventCode"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventDeleteRow"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEtherCfmMIBEventGroup = ciscoEtherCfmMIBEventGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoEtherCfmMIBEventGroup.setDescription('Set of objects needed for CFM events.')
ciscoEtherCfmMIBNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 461, 2, 2, 2)).setObjects(("CISCO-ETHER-CFM-MIB", "cEtherCfmCcMepUp"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmCcMepDown"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmCcCrossconnect"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmCcLoop"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmCcConfigError"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmXCheckMissing"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmXCheckUnknown"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmXCheckServiceUp"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEtherCfmMIBNotifGroup = ciscoEtherCfmMIBNotifGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoEtherCfmMIBNotifGroup.setDescription('Set of notifications implemented in this module.')
mibBuilder.exportSymbols("CISCO-ETHER-CFM-MIB", PYSNMP_MODULE_ID=ciscoEtherCfmMIB, cEtherCfmXCheckMissing=cEtherCfmXCheckMissing, ciscoEtherCfmMIB=ciscoEtherCfmMIB, ciscoEtherCfmMIBObjects=ciscoEtherCfmMIBObjects, ciscoEtherCfmMIBGroups=ciscoEtherCfmMIBGroups, cEtherCfmMaxEventIndex=cEtherCfmMaxEventIndex, cEtherCfmCcCrossconnect=cEtherCfmCcCrossconnect, cEtherCfmEventType=cEtherCfmEventType, cEtherCfmEventDomainIndex=cEtherCfmEventDomainIndex, cEtherCfmEventLclMepid=cEtherCfmEventLclMepid, cEtherCfmCcConfigError=cEtherCfmCcConfigError, cEtherCfmEventLclMacAddress=cEtherCfmEventLclMacAddress, cEtherCfmXCheckUnknown=cEtherCfmXCheckUnknown, cEtherCfmEventDomainName=cEtherCfmEventDomainName, cEtherCfmEventRmtServiceId=cEtherCfmEventRmtServiceId, cEtherCfmEventDeleteRow=cEtherCfmEventDeleteRow, cEtherCfmEventSvlan=cEtherCfmEventSvlan, cEtherCfmCcLoop=cEtherCfmCcLoop, cEtherCfmEventLastChange=cEtherCfmEventLastChange, cEtherCfmEventLclMepCount=cEtherCfmEventLclMepCount, ciscoEtherCfmMIBNotifs=ciscoEtherCfmMIBNotifs, cEtherCfmEventRmtPortState=cEtherCfmEventRmtPortState, ciscoEtherCfmMIBConform=ciscoEtherCfmMIBConform, CfmMepid=CfmMepid, cEtherCfmEventIndex=cEtherCfmEventIndex, cEtherCfmEventLclIfCount=cEtherCfmEventLclIfCount, cEtherCfmEventCode=cEtherCfmEventCode, ciscoEtherCfmMIBCompliances=ciscoEtherCfmMIBCompliances, ciscoEtherCfmMIBCompliance=ciscoEtherCfmMIBCompliance, cEtherCfmEventTable=cEtherCfmEventTable, ciscoEtherCfmMIBEventGroup=ciscoEtherCfmMIBEventGroup, cEtherCfmEventRmtMepid=cEtherCfmEventRmtMepid, cEtherCfmEventServiceId=cEtherCfmEventServiceId, cEtherCfmCcMepUp=cEtherCfmCcMepUp, cEtherCfmXCheckServiceUp=cEtherCfmXCheckServiceUp, cEtherCfmEventRmtMacAddress=cEtherCfmEventRmtMacAddress, cecCfmEvents=cecCfmEvents, ciscoEtherCfmNotificationPrefix=ciscoEtherCfmNotificationPrefix, ciscoEtherCfmMIBNotifGroup=ciscoEtherCfmMIBNotifGroup, cEtherCfmEventEntry=cEtherCfmEventEntry, cEtherCfmCcMepDown=cEtherCfmCcMepDown)
