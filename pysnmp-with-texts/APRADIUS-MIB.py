#
# PySNMP MIB module APRADIUS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/APRADIUS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:24:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
acmepacketMgmt, = mibBuilder.importSymbols("ACMEPACKET-SMI", "acmepacketMgmt")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
InetAddress, InetPortNumber, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetPortNumber", "InetAddressType")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
ModuleIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, TimeTicks, Bits, NotificationType, Unsigned32, IpAddress, Counter32, Counter64, Gauge32, Integer32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "TimeTicks", "Bits", "NotificationType", "Unsigned32", "IpAddress", "Counter32", "Counter64", "Gauge32", "Integer32", "ObjectIdentity")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
apRadiusServerModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 9148, 3, 18))
if mibBuilder.loadTexts: apRadiusServerModule.setLastUpdated('201203150000Z')
if mibBuilder.loadTexts: apRadiusServerModule.setOrganization('Acme Packet, Inc')
if mibBuilder.loadTexts: apRadiusServerModule.setContactInfo(' Customer Service Postal: Acme Packet, Inc 100 Crosby Drive Bedford, MA 01730 US Tel: 1-781-328-4400 E-mail: support@acmepacket.com')
if mibBuilder.loadTexts: apRadiusServerModule.setDescription('The Net-Net RADIUS MIB for Acme Packet')
apRadiusServerMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 18, 1))
apRadiusServerStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9148, 3, 18, 1, 1), )
if mibBuilder.loadTexts: apRadiusServerStatsTable.setStatus('current')
if mibBuilder.loadTexts: apRadiusServerStatsTable.setDescription('The table of RADIUS statistics per RADIUS server.')
apRadiusServerStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9148, 3, 18, 1, 1, 1), ).setIndexNames((0, "APRADIUS-MIB", "apRadiusServerAddressType"), (0, "APRADIUS-MIB", "apRadiusServerAddress"))
if mibBuilder.loadTexts: apRadiusServerStatsEntry.setStatus('current')
if mibBuilder.loadTexts: apRadiusServerStatsEntry.setDescription('RADIUS negotiation statistics for an RADIUS server.')
apRadiusServerAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 18, 1, 1, 1, 1), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apRadiusServerAddressType.setStatus('current')
if mibBuilder.loadTexts: apRadiusServerAddressType.setDescription('IPAddress type of the RADIUS server')
apRadiusServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 18, 1, 1, 1, 2), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apRadiusServerAddress.setStatus('current')
if mibBuilder.loadTexts: apRadiusServerAddress.setDescription('IPAddress of the RADIUS server')
apRadiusServerRoundTripTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 18, 1, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apRadiusServerRoundTripTime.setStatus('current')
if mibBuilder.loadTexts: apRadiusServerRoundTripTime.setDescription('Average Round Trip Time for response on this RADIUS Server')
apRadiusServerMalformedAccessResponse = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 18, 1, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apRadiusServerMalformedAccessResponse.setStatus('current')
if mibBuilder.loadTexts: apRadiusServerMalformedAccessResponse.setDescription('The count of Malformed Access Response on this RADIUS Server')
apRadiusServerAccessRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 18, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apRadiusServerAccessRequests.setStatus('current')
if mibBuilder.loadTexts: apRadiusServerAccessRequests.setDescription('The count of Access Requests on this RADIUS Server')
apRadiusServerDisconnectRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 18, 1, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apRadiusServerDisconnectRequests.setStatus('current')
if mibBuilder.loadTexts: apRadiusServerDisconnectRequests.setDescription('The count of Disconnect Requests on this RADIUS Server')
apRadiusServerDisconnectACKs = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 18, 1, 1, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apRadiusServerDisconnectACKs.setStatus('current')
if mibBuilder.loadTexts: apRadiusServerDisconnectACKs.setDescription('The count of Disconnect ACKs on this RADIUS Server')
apRadiusServerDisconnectNACks = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 18, 1, 1, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apRadiusServerDisconnectNACks.setStatus('current')
if mibBuilder.loadTexts: apRadiusServerDisconnectNACks.setDescription('The count of Disconnect NACKs on this RADIUS Server')
apRadiusServerBadAuthenticators = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 18, 1, 1, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apRadiusServerBadAuthenticators.setStatus('current')
if mibBuilder.loadTexts: apRadiusServerBadAuthenticators.setDescription('The count of Bad Authenticators on this RADIUS Server')
apRadiusServerAccessRetransmissions = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 18, 1, 1, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apRadiusServerAccessRetransmissions.setStatus('current')
if mibBuilder.loadTexts: apRadiusServerAccessRetransmissions.setDescription('The count of Access Retransmissions on this RADIUS Server')
apRadiusServerAccessAccepts = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 18, 1, 1, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apRadiusServerAccessAccepts.setStatus('current')
if mibBuilder.loadTexts: apRadiusServerAccessAccepts.setDescription('The count of Access Accepts on this RADIUS Server')
apRadiusServerTimeouts = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 18, 1, 1, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apRadiusServerTimeouts.setStatus('current')
if mibBuilder.loadTexts: apRadiusServerTimeouts.setDescription('The count of Timeouts for response on this RADIUS Server')
apRadiusServerAccessRejects = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 18, 1, 1, 1, 13), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apRadiusServerAccessRejects.setStatus('current')
if mibBuilder.loadTexts: apRadiusServerAccessRejects.setDescription('The count of Access Rejects on this RADIUS Server')
apRadiusServerUnknownPDUTypes = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 18, 1, 1, 1, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apRadiusServerUnknownPDUTypes.setStatus('current')
if mibBuilder.loadTexts: apRadiusServerUnknownPDUTypes.setDescription('The count of Unknown PDU Types received on this RADIUS Server')
apRadiusServerAccessChallenges = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 18, 1, 1, 1, 15), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apRadiusServerAccessChallenges.setStatus('current')
if mibBuilder.loadTexts: apRadiusServerAccessChallenges.setDescription('The count of Access Challenges on this RADIUS Server')
apRadiusServerConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 18, 2))
apRadiusObjectGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 18, 2, 1))
apRadiusInterfaceStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9148, 3, 18, 2, 1, 1)).setObjects(("APRADIUS-MIB", "apRadiusServerRoundTripTime"), ("APRADIUS-MIB", "apRadiusServerMalformedAccessResponse"), ("APRADIUS-MIB", "apRadiusServerAccessRequests"), ("APRADIUS-MIB", "apRadiusServerDisconnectRequests"), ("APRADIUS-MIB", "apRadiusServerDisconnectACKs"), ("APRADIUS-MIB", "apRadiusServerDisconnectNACks"), ("APRADIUS-MIB", "apRadiusServerBadAuthenticators"), ("APRADIUS-MIB", "apRadiusServerAccessRetransmissions"), ("APRADIUS-MIB", "apRadiusServerAccessAccepts"), ("APRADIUS-MIB", "apRadiusServerTimeouts"), ("APRADIUS-MIB", "apRadiusServerAccessRejects"), ("APRADIUS-MIB", "apRadiusServerUnknownPDUTypes"), ("APRADIUS-MIB", "apRadiusServerAccessChallenges"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apRadiusInterfaceStatsGroup = apRadiusInterfaceStatsGroup.setStatus('current')
if mibBuilder.loadTexts: apRadiusInterfaceStatsGroup.setDescription('A collection of statistics for RADIUS server.')
mibBuilder.exportSymbols("APRADIUS-MIB", apRadiusServerTimeouts=apRadiusServerTimeouts, apRadiusServerUnknownPDUTypes=apRadiusServerUnknownPDUTypes, apRadiusServerRoundTripTime=apRadiusServerRoundTripTime, apRadiusServerBadAuthenticators=apRadiusServerBadAuthenticators, apRadiusServerMIBObjects=apRadiusServerMIBObjects, apRadiusServerAccessChallenges=apRadiusServerAccessChallenges, apRadiusServerAddressType=apRadiusServerAddressType, apRadiusServerAccessRetransmissions=apRadiusServerAccessRetransmissions, apRadiusServerAccessRequests=apRadiusServerAccessRequests, apRadiusObjectGroups=apRadiusObjectGroups, apRadiusServerAddress=apRadiusServerAddress, apRadiusInterfaceStatsGroup=apRadiusInterfaceStatsGroup, apRadiusServerAccessAccepts=apRadiusServerAccessAccepts, apRadiusServerDisconnectNACks=apRadiusServerDisconnectNACks, apRadiusServerStatsEntry=apRadiusServerStatsEntry, apRadiusServerDisconnectRequests=apRadiusServerDisconnectRequests, PYSNMP_MODULE_ID=apRadiusServerModule, apRadiusServerConformance=apRadiusServerConformance, apRadiusServerStatsTable=apRadiusServerStatsTable, apRadiusServerDisconnectACKs=apRadiusServerDisconnectACKs, apRadiusServerAccessRejects=apRadiusServerAccessRejects, apRadiusServerMalformedAccessResponse=apRadiusServerMalformedAccessResponse, apRadiusServerModule=apRadiusServerModule)
