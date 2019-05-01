#
# PySNMP MIB module CISCO-STUN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-STUN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:13:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
IpAddress, ObjectIdentity, TimeTicks, MibIdentifier, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, NotificationType, Bits, iso, Gauge32, Integer32, ModuleIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ObjectIdentity", "TimeTicks", "MibIdentifier", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "NotificationType", "Bits", "iso", "Gauge32", "Integer32", "ModuleIdentity", "Counter32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
ciscoStunMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 30))
ciscoStunMIB.setRevisions(('1995-08-21 00:00', '1995-03-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoStunMIB.setRevisionsDescriptions(('Added revision clause, formatting cleanup.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoStunMIB.setLastUpdated('9508210000Z')
if mibBuilder.loadTexts: ciscoStunMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoStunMIB.setContactInfo(' Cisco Systems Customer Service Postal: 170 W. Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS e-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoStunMIB.setDescription("The MIB module for serial Tunneling. Overview of STUN MIB MIB description The STUN MIB provides the configuration and operational information on Cisco's serial tunnelling implementation. The following entities are managed: 1) Global STUN information 2) STUN groups 3) STUN ports 4) STUN routes The following example configuration shows how the STUN MIB returns STUN information, from either CISCO A or CISCO B. HOST == SDLC == Cisco A == IP Network == Cisco B == SDLC == SDLC line line device 1) The STUN global entry identifies the IP address by which the router is known to other STUN peers. 2) The STUN group table identifies the STUN group number and protocol type that Cisco A and Cisco B use to route SDLC traffic over the IP network. The table contains an entry for each STUN group defined on the router. 3) The STUN port table identifies the serial interface to the SDLC line for which the router is doing serial tunnelling. The MIB also identifies the STUN group this interface is defined for, and identifies the default routing for unrecognized SDLC addresses. There is a port entry for each STUN-enabled interface on the router. 4) The STUN route table has an entry for each address defined for routing within the STUN group, and an entry for the default routing if the 'stun route all' command is configured. The route entry includes identification of the STUN peer, priority, state, whether local acknowledgment is enabled, and packet and byte counters. ")
stunObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 30, 1))
stunGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 1))
stunGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 2))
stunPorts = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 3))
stunRoutes = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 4))
stunIPAddr = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stunIPAddr.setStatus('current')
if mibBuilder.loadTexts: stunIPAddr.setDescription('The configured IP address used for all serial tunnelling in this router.')
stunGroupTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 2, 1), )
if mibBuilder.loadTexts: stunGroupTable.setStatus('current')
if mibBuilder.loadTexts: stunGroupTable.setDescription('A table of entries representing STUN groups configured on the router. Each STUN-enabled interface is assigned to a STUN group, and packets can only travel between STUN-enabled interfaces in the same group.')
stunGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-STUN-MIB", "stunGroupIndex"))
if mibBuilder.loadTexts: stunGroupEntry.setStatus('current')
if mibBuilder.loadTexts: stunGroupEntry.setDescription('Status and parameter values for a group.')
stunGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: stunGroupIndex.setStatus('current')
if mibBuilder.loadTexts: stunGroupIndex.setDescription('The configured STUN group number.')
stunProtocolType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("basic", 1), ("sdlc", 2), ("sdlctg", 3), ("custom", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: stunProtocolType.setStatus('current')
if mibBuilder.loadTexts: stunProtocolType.setDescription('The protocol type for this STUN group.')
stunPortTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 3, 1), )
if mibBuilder.loadTexts: stunPortTable.setStatus('current')
if mibBuilder.loadTexts: stunPortTable.setDescription('A list of STUN-enabled interfaces (ports).')
stunPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 3, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: stunPortEntry.setStatus('current')
if mibBuilder.loadTexts: stunPortEntry.setDescription('Status and parameter values for a STUN port.')
stunPortGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: stunPortGroupIndex.setStatus('current')
if mibBuilder.loadTexts: stunPortGroupIndex.setDescription('The group number to which the stun port belongs. Frames will only be routed to other ports (on this or another router) in the same stun group. This group must match a stunGroupIndex in the stunGroupTable.')
stunPortDefaultPeerType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("ip", 2), ("direct", 3), ("frameRelay", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: stunPortDefaultPeerType.setStatus('current')
if mibBuilder.loadTexts: stunPortDefaultPeerType.setDescription("The type of identification of the default partner for unrecognized addresses. If there is no default route then the stunRouteType field of stunPortDefaultRemote is 'other'. If ip then the value is in stunRouteIP; if serial or serialDirect then the value is in stunRouteSerial.")
stunPortDefaultPeerIP = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 3, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stunPortDefaultPeerIP.setStatus('current')
if mibBuilder.loadTexts: stunPortDefaultPeerIP.setDescription('The ip address of the remote default STUN partner, for unrecognized addresses. 0.0.0.0 is returned if the default route type is not ip.')
stunPortDefaultPeerSerialInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 3, 1, 1, 4), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stunPortDefaultPeerSerialInterface.setStatus('current')
if mibBuilder.loadTexts: stunPortDefaultPeerSerialInterface.setDescription('If stunRouteType is serial then this is the serial interface index of the point-to-point link to the remote partner; if stunRouteType is serialDirect then the partner is in the local STUN. if stunRouteType is ip then this field is 0.')
stunRouteTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 4, 1), )
if mibBuilder.loadTexts: stunRouteTable.setStatus('current')
if mibBuilder.loadTexts: stunRouteTable.setDescription('A table containing information about specific SDLC addresses. There is one table entry for each SDLC address configured by the STUN ROUTE command.')
stunRouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 4, 1, 1), ).setIndexNames((0, "CISCO-STUN-MIB", "stunGroupIndex"), (0, "CISCO-STUN-MIB", "stunRouteStationAddress"))
if mibBuilder.loadTexts: stunRouteEntry.setStatus('current')
if mibBuilder.loadTexts: stunRouteEntry.setDescription('The information regarding a single STUN address.')
stunRouteStationAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 256)))
if mibBuilder.loadTexts: stunRouteStationAddress.setStatus('current')
if mibBuilder.loadTexts: stunRouteStationAddress.setDescription('The poll address of the station. 256 indicates the ALL parameter on the STUN ROUTE command, which is the route for all unrecognized addresses.')
stunRouteType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("ip", 2), ("direct", 3), ("frameRelay", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: stunRouteType.setStatus('current')
if mibBuilder.loadTexts: stunRouteType.setDescription('The type of identification of the remote partner.')
stunRouteRemoteIP = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 4, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stunRouteRemoteIP.setStatus('current')
if mibBuilder.loadTexts: stunRouteRemoteIP.setDescription('The ip address of the remote STUN partner. 0.0.0.0 if partner type is not ip.')
stunRouteSerialInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 4, 1, 1, 4), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stunRouteSerialInterface.setStatus('current')
if mibBuilder.loadTexts: stunRouteSerialInterface.setDescription('The local interface index to the remote partner. 0 is returned if the partner type is not direct or frameRelay.')
stunRoutePriority = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 4, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("low", 1), ("normal", 2), ("medium", 3), ("high", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: stunRoutePriority.setStatus('current')
if mibBuilder.loadTexts: stunRoutePriority.setDescription("The priority with which this station's traffic will be routed across the network.")
stunRoutePeerState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 4, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("dead", 1), ("closed", 2), ("opening", 3), ("openWait", 4), ("connected", 5), ("direct", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: stunRoutePeerState.setStatus('current')
if mibBuilder.loadTexts: stunRoutePeerState.setDescription('The state of the peer connection through the STUN tunnel.')
stunRouteLocalAck = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 4, 1, 1, 7), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stunRouteLocalAck.setStatus('current')
if mibBuilder.loadTexts: stunRouteLocalAck.setDescription('Indicates if the STUN connection is locally acknowledged. TRUE-> STUN connection is locally acknowledged FALSE-> STUN connection is not locally acknowledged ')
stunRouteRxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 4, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stunRouteRxPackets.setStatus('current')
if mibBuilder.loadTexts: stunRouteRxPackets.setDescription("Count of frames received from the serial interface with this station's address.")
stunRouteTxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 4, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stunRouteTxPackets.setStatus('current')
if mibBuilder.loadTexts: stunRouteTxPackets.setDescription("Count of frames transmitted at the serial interface with this station's address.")
stunRouteRxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 4, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stunRouteRxBytes.setStatus('current')
if mibBuilder.loadTexts: stunRouteRxBytes.setDescription("Count of bytes received from the serial interface with this station's address.")
stunRouteTxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 4, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stunRouteTxBytes.setStatus('current')
if mibBuilder.loadTexts: stunRouteTxBytes.setDescription("Count of bytes transmitted at the serial interface with this station's address.")
stunNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 30, 2))
stunNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 30, 2, 0))
stunPeerStateChangeNotification = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 30, 2, 0, 1)).setObjects(("CISCO-STUN-MIB", "stunRoutePeerState"))
if mibBuilder.loadTexts: stunPeerStateChangeNotification.setStatus('current')
if mibBuilder.loadTexts: stunPeerStateChangeNotification.setDescription('This notification indicates that the state of a STUN route has transitioned to active (connected or direct) or inactive (dead or closed).')
stunMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 30, 3))
stunMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 30, 3, 1))
stunMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 30, 3, 2))
stunMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 30, 3, 1, 1)).setObjects(("CISCO-STUN-MIB", "stunGlobalGroup"), ("CISCO-STUN-MIB", "stunGroupGroup"), ("CISCO-STUN-MIB", "stunPortGroup"), ("CISCO-STUN-MIB", "stunRouteGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    stunMibCompliance = stunMibCompliance.setStatus('current')
if mibBuilder.loadTexts: stunMibCompliance.setDescription('The compliance statement for STUN.')
stunGlobalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 30, 3, 2, 1)).setObjects(("CISCO-STUN-MIB", "stunIPAddr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    stunGlobalGroup = stunGlobalGroup.setStatus('current')
if mibBuilder.loadTexts: stunGlobalGroup.setDescription('A collection of objects providing global STUN information.')
stunGroupGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 30, 3, 2, 2)).setObjects(("CISCO-STUN-MIB", "stunProtocolType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    stunGroupGroup = stunGroupGroup.setStatus('current')
if mibBuilder.loadTexts: stunGroupGroup.setDescription('A collection of objects providing information about STUN groups .')
stunPortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 30, 3, 2, 3)).setObjects(("CISCO-STUN-MIB", "stunPortGroupIndex"), ("CISCO-STUN-MIB", "stunPortDefaultPeerType"), ("CISCO-STUN-MIB", "stunPortDefaultPeerIP"), ("CISCO-STUN-MIB", "stunPortDefaultPeerSerialInterface"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    stunPortGroup = stunPortGroup.setStatus('current')
if mibBuilder.loadTexts: stunPortGroup.setDescription('A collection of objects providing information about STUN enabled interfaces.')
stunRouteGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 30, 3, 2, 4)).setObjects(("CISCO-STUN-MIB", "stunRouteType"), ("CISCO-STUN-MIB", "stunRouteRemoteIP"), ("CISCO-STUN-MIB", "stunRouteSerialInterface"), ("CISCO-STUN-MIB", "stunRoutePriority"), ("CISCO-STUN-MIB", "stunRoutePeerState"), ("CISCO-STUN-MIB", "stunRouteLocalAck"), ("CISCO-STUN-MIB", "stunRouteRxPackets"), ("CISCO-STUN-MIB", "stunRouteTxPackets"), ("CISCO-STUN-MIB", "stunRouteRxBytes"), ("CISCO-STUN-MIB", "stunRouteTxBytes"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    stunRouteGroup = stunRouteGroup.setStatus('current')
if mibBuilder.loadTexts: stunRouteGroup.setDescription('A collection of objects providing information about STUN defined routes.')
mibBuilder.exportSymbols("CISCO-STUN-MIB", stunObjects=stunObjects, stunGroupTable=stunGroupTable, stunRouteType=stunRouteType, stunPortEntry=stunPortEntry, stunIPAddr=stunIPAddr, stunProtocolType=stunProtocolType, stunPorts=stunPorts, stunRouteLocalAck=stunRouteLocalAck, stunPortDefaultPeerType=stunPortDefaultPeerType, stunGlobal=stunGlobal, stunRoutes=stunRoutes, stunNotificationPrefix=stunNotificationPrefix, stunRouteTxPackets=stunRouteTxPackets, stunGroupGroup=stunGroupGroup, stunRouteEntry=stunRouteEntry, stunRoutePriority=stunRoutePriority, stunPortGroup=stunPortGroup, stunPortDefaultPeerSerialInterface=stunPortDefaultPeerSerialInterface, stunGroupEntry=stunGroupEntry, stunMibCompliances=stunMibCompliances, stunGroups=stunGroups, ciscoStunMIB=ciscoStunMIB, stunRouteTxBytes=stunRouteTxBytes, stunPortDefaultPeerIP=stunPortDefaultPeerIP, stunRouteSerialInterface=stunRouteSerialInterface, stunMibCompliance=stunMibCompliance, stunPortTable=stunPortTable, stunRouteRxBytes=stunRouteRxBytes, stunGlobalGroup=stunGlobalGroup, stunRouteStationAddress=stunRouteStationAddress, stunPortGroupIndex=stunPortGroupIndex, stunRouteRxPackets=stunRouteRxPackets, stunMibConformance=stunMibConformance, stunRouteRemoteIP=stunRouteRemoteIP, stunRoutePeerState=stunRoutePeerState, stunPeerStateChangeNotification=stunPeerStateChangeNotification, stunRouteGroup=stunRouteGroup, stunNotifications=stunNotifications, PYSNMP_MODULE_ID=ciscoStunMIB, stunMibGroups=stunMibGroups, stunRouteTable=stunRouteTable, stunGroupIndex=stunGroupIndex)
