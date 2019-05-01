#
# PySNMP MIB module CISCO-CDMA-PDSN-CRP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-CDMA-PDSN-CRP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:52:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Gauge32, ObjectIdentity, IpAddress, iso, Unsigned32, MibIdentifier, Counter64, Integer32, TimeTicks, Counter32, NotificationType, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Gauge32", "ObjectIdentity", "IpAddress", "iso", "Unsigned32", "MibIdentifier", "Counter64", "Integer32", "TimeTicks", "Counter32", "NotificationType", "Bits")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
ciscoCdmaPdsnCrpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 957))
ciscoCdmaPdsnCrpMIB.setRevisions(('2004-07-27 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoCdmaPdsnCrpMIB.setRevisionsDescriptions(('Initial revision of this MIB module.',))
if mibBuilder.loadTexts: ciscoCdmaPdsnCrpMIB.setLastUpdated('200407270000Z')
if mibBuilder.loadTexts: ciscoCdmaPdsnCrpMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoCdmaPdsnCrpMIB.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cdma@cisco.com')
if mibBuilder.loadTexts: ciscoCdmaPdsnCrpMIB.setDescription("This MIB is to support the Closed RP feature of CDMA PDSN that supports wireless data communication through 3G CDMA radio access technology. PDSN acts as a foreign agent that establishes, maintains and terminates the link layer to a mobile station. The high level architecture of a third generation CDMA2000 network is shown below: +========+=+ +=========+ +=========+ | RAdio |P| | | Data | Home | | Network|C|- Closed RP -| PDSN |- Core -| Network | | (RAN) |F| Interface | | Network | | +========+=+ +=========+ (DCN) +=========+ /|\\ Foreign Agent Home Agent | (FA) (HA) | Visited Access | Provider Network | \\|/ +========+ | Mobile | | Station| | (MS) | +========+ The following diagram illustrates protocols usage by the CDMA2000 network elements: MS ===== RAN ======== PDSN ======== DCN ====== Home Network | | Closed RP | | | +=signaling==+ | | | | | +...L2TP/L2F tunnelling..+ | | | +======== PPP ========+ | | | | | +..Mobile IP tunnelling..+ | | | | | | +=================Mobile IP====================+ | | | | +======================data====================+ The CDMA PDSN CRP MIB provides operational information for a Closed RP implementation. The following areas are managed: 1) Global PDSN information. This area contains generic information such as the number of incoming call requests, incoming call replies etc., Acronyms and terms: CDMA Code Division Multiple Access DCN Data Core Network ESN Electronic Serial Number FA Foreign Agent HA Home Agent IMSI International Mobile Station Identifier IS In service IRM International Roaming MIN MC Mobile Client MIN Mobile Identifier Number MSID Mobile Station Identifier MS Mobile Station MN Mobile Node MoIP Mobile IP NAI Network Access Identifier OOS Out of service PCF Packet Control Function PDSN Packet Data Serving Node RAN Radio Network RP Radio Packet CANID Current Access Network Identifier PANID Previous Access Network Identifier BSID Base Station Identifier CVSE Customer/Vendor Specific Extension SO/So Service Option. The Service Option is a parameter that specifies the air interface between MS and RN for packet data service. Mobile Station/ A host or router that changes its Mobile Node point of attachment from one network or subnetwork to another. A mobile node may change its location without changing its IP address. Mobile IP Protocol enhancements that allow transparent routing of IP datagrams to mobile nodes. Refer to RFC 2002 for more details. Mobile Client A component which can interact with MoIP entities such as Foreign Agent and Home Agent. Home Agent A router on a mobile node's home network which tunnels datagrams for delivery to the mobile node when it is away from home, and maintains current location information for the mobile node. Refer to RFC 2002 for more details. Foreign Agent A router on a mobile node's visited network which provides routing services to the mobile node while registered. The foreign agent delivers datagrams to the mobile node that were tunneled by the mobile node's home agent. For datagrams sent by a mobile node, the foreign agent may serve as a default router for registered mobile nodes. Refer to RFC 2002 for more details. Proxy Mechanism used by PDSN to provide Mobile Ip MoIP services to a MS which does not implement a mobile client. PDSN will be the proxy MC for the MS. Simple IP IP routing used by a MS when MoIP services are not needed. PDSN flow A conversation between one user (identified by an IP address) and a HA using a PDSN session. PDSN session A PPP connection between a MS and the PDSN. One session may contain one or multiple PDSN flows. PCF Physical interface connecting the RAN to a PDSN L2TP Layer 2 Tunneling Protocol ICRQ Incoming Call Request ICRP Incoming Call Reply ICCN Incoming Call Connected CDN Call Disconnect.")
ccpcMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 957, 1))
ccpcSystemInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 957, 1, 1))
ccpcPerfStats = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 957, 1, 2))
ccpcEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 957, 1, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccpcEnabled.setStatus('current')
if mibBuilder.loadTexts: ccpcEnabled.setDescription('An indication of whether CRP feature is enabled.')
ccpcSessionTotal = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 957, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccpcSessionTotal.setStatus('current')
if mibBuilder.loadTexts: ccpcSessionTotal.setDescription('The total number of sessions currently established with this system.')
ccpcPcfPerfStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 957, 1, 2, 1), )
if mibBuilder.loadTexts: ccpcPcfPerfStatsTable.setStatus('current')
if mibBuilder.loadTexts: ccpcPcfPerfStatsTable.setDescription('PDSN PCF table. Contains the reference about PCF in the RAN currently interacting with the PDSN. An entry is created when a L2TP tunnel is established with PCF. An entry is deleted when the tunnel is deleted.')
ccpcPcfPerfStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 957, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-CDMA-PDSN-CRP-MIB", "ccpcPcfIpAddressType"), (0, "CISCO-CDMA-PDSN-CRP-MIB", "ccpcPcfIpAddress"))
if mibBuilder.loadTexts: ccpcPcfPerfStatsEntry.setStatus('current')
if mibBuilder.loadTexts: ccpcPcfPerfStatsEntry.setDescription('A conceptual row in the PCF CRP Stats table.')
ccpcPcfIpAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 957, 1, 2, 1, 1, 1), InetAddressType())
if mibBuilder.loadTexts: ccpcPcfIpAddressType.setStatus('current')
if mibBuilder.loadTexts: ccpcPcfIpAddressType.setDescription('Represents the type of the address specified by ccpcPcfIpAddress.')
ccpcPcfIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 957, 1, 2, 1, 1, 2), InetAddress())
if mibBuilder.loadTexts: ccpcPcfIpAddress.setStatus('current')
if mibBuilder.loadTexts: ccpcPcfIpAddress.setDescription('The IP address of the PCF that serves the mobile node.')
ccpcPcfRcvdIcrqs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 957, 1, 2, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccpcPcfRcvdIcrqs.setStatus('current')
if mibBuilder.loadTexts: ccpcPcfRcvdIcrqs.setDescription('Total number of Incoming-Call-Requests received to establish a L2TP session since the L2TP tunnel was established with PCF.')
ccpcPcfAcptdIcrqs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 957, 1, 2, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccpcPcfAcptdIcrqs.setStatus('current')
if mibBuilder.loadTexts: ccpcPcfAcptdIcrqs.setDescription('Total number of Incoming-Call-Requests accepted since the L2TP tunnel was established with PCF.')
ccpcPcfDroppedIcrqs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 957, 1, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccpcPcfDroppedIcrqs.setStatus('current')
if mibBuilder.loadTexts: ccpcPcfDroppedIcrqs.setDescription('Total number of Incoming-Call-Requests denied since the L2TP tunnel was established with PCF.')
ccpcPcfSentIcrps = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 957, 1, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccpcPcfSentIcrps.setStatus('current')
if mibBuilder.loadTexts: ccpcPcfSentIcrps.setDescription('Total number of Incoming-Call-Replies sent since the L2TP tunnel was established with PCF.')
ccpcPcfRcvdIccns = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 957, 1, 2, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccpcPcfRcvdIccns.setStatus('current')
if mibBuilder.loadTexts: ccpcPcfRcvdIccns.setDescription('Total number of Incoming-Call-Connected messages received since the L2TP tunnel was established with PCF.')
ccpcPcfAcptdIccns = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 957, 1, 2, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccpcPcfAcptdIccns.setStatus('current')
if mibBuilder.loadTexts: ccpcPcfAcptdIccns.setDescription('Total number of Incoming-Call-Connected messages accepted since the L2TP tunnel was established with PCF.')
ccpcPcfDroppedIccns = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 957, 1, 2, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccpcPcfDroppedIccns.setStatus('current')
if mibBuilder.loadTexts: ccpcPcfDroppedIccns.setDescription('Total number of Incoming-Call-Connected messages accepted since the L2TP tunnel was established with PCF.')
ccpcPcfRcvdCdns = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 957, 1, 2, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccpcPcfRcvdCdns.setStatus('current')
if mibBuilder.loadTexts: ccpcPcfRcvdCdns.setDescription('Total number of Call-Disconnect-Notify messages received to tear down L2TP session since the L2TP tunnel was established with PCF.')
ccpcPcfSentCdns = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 957, 1, 2, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccpcPcfSentCdns.setStatus('current')
if mibBuilder.loadTexts: ccpcPcfSentCdns.setDescription('Total number of Call-Disconnect-Notify messages sent to PCF to tear down L2TP session since the L2TP tunnel was established with PCF.')
ccpcPcfDroppedCdns = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 957, 1, 2, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccpcPcfDroppedCdns.setStatus('current')
if mibBuilder.loadTexts: ccpcPcfDroppedCdns.setDescription('Total number of Call-Disconnect-Notify messages dropped since the L2TP tunnel was established with PCF.')
ccpcPcfRcvdZlbs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 957, 1, 2, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccpcPcfRcvdZlbs.setStatus('current')
if mibBuilder.loadTexts: ccpcPcfRcvdZlbs.setDescription('Total number of Zero-Length-Buffer messages received since the L2TP tunnel was established with PCF.')
ccpcPcfSentZlbs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 957, 1, 2, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccpcPcfSentZlbs.setStatus('current')
if mibBuilder.loadTexts: ccpcPcfSentZlbs.setDescription('Total number of Zero-Length-Buffer messages sent since the L2TP tunnel was established with PCF.')
ccpcMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 957, 2))
ccpcMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 957, 2, 1))
ccpcMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 957, 2, 2))
ccpcMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 957, 2, 1, 1)).setObjects(("CISCO-CDMA-PDSN-CRP-MIB", "ccpcSystemGrp"), ("CISCO-CDMA-PDSN-CRP-MIB", "ccpcPerfGrp"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccpcMIBCompliance = ccpcMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ccpcMIBCompliance.setDescription('The compliance statement for entities which implement the CDMA PDSN Management MIB for R2.0')
ccpcSystemGrp = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 957, 2, 2, 1)).setObjects(("CISCO-CDMA-PDSN-CRP-MIB", "ccpcEnabled"), ("CISCO-CDMA-PDSN-CRP-MIB", "ccpcSessionTotal"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccpcSystemGrp = ccpcSystemGrp.setStatus('current')
if mibBuilder.loadTexts: ccpcSystemGrp.setDescription('A collection of objects needed for PDSN R2.1 network management.')
ccpcPerfGrp = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 957, 2, 2, 2)).setObjects(("CISCO-CDMA-PDSN-CRP-MIB", "ccpcPcfRcvdIcrqs"), ("CISCO-CDMA-PDSN-CRP-MIB", "ccpcPcfAcptdIcrqs"), ("CISCO-CDMA-PDSN-CRP-MIB", "ccpcPcfDroppedIcrqs"), ("CISCO-CDMA-PDSN-CRP-MIB", "ccpcPcfSentIcrps"), ("CISCO-CDMA-PDSN-CRP-MIB", "ccpcPcfRcvdIccns"), ("CISCO-CDMA-PDSN-CRP-MIB", "ccpcPcfAcptdIccns"), ("CISCO-CDMA-PDSN-CRP-MIB", "ccpcPcfDroppedIccns"), ("CISCO-CDMA-PDSN-CRP-MIB", "ccpcPcfRcvdCdns"), ("CISCO-CDMA-PDSN-CRP-MIB", "ccpcPcfSentCdns"), ("CISCO-CDMA-PDSN-CRP-MIB", "ccpcPcfDroppedCdns"), ("CISCO-CDMA-PDSN-CRP-MIB", "ccpcPcfRcvdZlbs"), ("CISCO-CDMA-PDSN-CRP-MIB", "ccpcPcfSentZlbs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccpcPerfGrp = ccpcPerfGrp.setStatus('current')
if mibBuilder.loadTexts: ccpcPerfGrp.setDescription('A collection of objects needed for PDSN R1.2 network management.')
mibBuilder.exportSymbols("CISCO-CDMA-PDSN-CRP-MIB", ccpcMIBCompliances=ccpcMIBCompliances, ccpcPerfGrp=ccpcPerfGrp, ccpcSystemInfo=ccpcSystemInfo, ccpcPcfPerfStatsTable=ccpcPcfPerfStatsTable, ciscoCdmaPdsnCrpMIB=ciscoCdmaPdsnCrpMIB, ccpcPcfRcvdIccns=ccpcPcfRcvdIccns, ccpcPcfDroppedCdns=ccpcPcfDroppedCdns, ccpcMIBConformance=ccpcMIBConformance, ccpcMIBGroups=ccpcMIBGroups, ccpcPcfIpAddressType=ccpcPcfIpAddressType, ccpcPerfStats=ccpcPerfStats, ccpcPcfDroppedIcrqs=ccpcPcfDroppedIcrqs, PYSNMP_MODULE_ID=ciscoCdmaPdsnCrpMIB, ccpcPcfSentZlbs=ccpcPcfSentZlbs, ccpcPcfIpAddress=ccpcPcfIpAddress, ccpcPcfPerfStatsEntry=ccpcPcfPerfStatsEntry, ccpcPcfRcvdIcrqs=ccpcPcfRcvdIcrqs, ccpcSessionTotal=ccpcSessionTotal, ccpcPcfAcptdIcrqs=ccpcPcfAcptdIcrqs, ccpcPcfRcvdCdns=ccpcPcfRcvdCdns, ccpcPcfRcvdZlbs=ccpcPcfRcvdZlbs, ccpcPcfSentIcrps=ccpcPcfSentIcrps, ccpcPcfSentCdns=ccpcPcfSentCdns, ccpcPcfDroppedIccns=ccpcPcfDroppedIccns, ccpcPcfAcptdIccns=ccpcPcfAcptdIccns, ccpcSystemGrp=ccpcSystemGrp, ccpcMIBObjects=ccpcMIBObjects, ccpcMIBCompliance=ccpcMIBCompliance, ccpcEnabled=ccpcEnabled)
