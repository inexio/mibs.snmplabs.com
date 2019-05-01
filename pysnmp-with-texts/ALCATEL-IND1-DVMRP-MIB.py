#
# PySNMP MIB module ALCATEL-IND1-DVMRP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALCATEL-IND1-DVMRP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:17:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
routingIND1Dvmrp, = mibBuilder.importSymbols("ALCATEL-IND1-BASE", "routingIND1Dvmrp")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
dvmrpInterfaceEntry, = mibBuilder.importSymbols("DVMRP-STD-MIB", "dvmrpInterfaceEntry")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
IpAddress, Integer32, iso, Bits, Gauge32, ObjectIdentity, NotificationType, enterprises, MibIdentifier, Counter64, ModuleIdentity, Counter32, TimeTicks, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Integer32", "iso", "Bits", "Gauge32", "ObjectIdentity", "NotificationType", "enterprises", "MibIdentifier", "Counter64", "ModuleIdentity", "Counter32", "TimeTicks", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
alcatelIND1DVMRPMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1))
alcatelIND1DVMRPMIB.setRevisions(('2007-04-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: alcatelIND1DVMRPMIB.setRevisionsDescriptions(('The latest version of this MIB Module.',))
if mibBuilder.loadTexts: alcatelIND1DVMRPMIB.setLastUpdated('200704030000Z')
if mibBuilder.loadTexts: alcatelIND1DVMRPMIB.setOrganization('Alcatel-Lucent')
if mibBuilder.loadTexts: alcatelIND1DVMRPMIB.setContactInfo('Please consult with Customer Service to ensure the most appropriate version of this document is used with the products in question: Alcatel-Lucent, Enterprise Solutions Division (Formerly Alcatel Internetworking, Incorporated) 26801 West Agoura Road Agoura Hills, CA 91301-5122 United States Of America Telephone: North America +1 800 995 2696 Latin America +1 877 919 9526 Europe +31 23 556 0100 Asia +65 394 7933 All Other +1 818 878 4507 Electronic Mail: support@ind.alcatel.com World Wide Web: http://alcatel-lucent.com/wps/portal/enterprise File Transfer Protocol: ftp://ftp.ind.alcatel.com/pub/products/mibs')
if mibBuilder.loadTexts: alcatelIND1DVMRPMIB.setDescription('This module describes an authoritative enterprise-specific Simple Network Management Protocol (SNMP) Management Information Base (MIB): This MIB contains management information for Coronado Layer 3 Hardware Routing Engine (HRE) management. The right to make changes in specification and other information contained in this document without prior notice is reserved. No liability shall be assumed for any incidental, indirect, special, or consequential damages whatsoever arising from or related to this document or the information contained herein. Vendors, end-users, and other interested parties are granted non-exclusive license to use this specification in connection with management of the products for which it is intended to be used. Copyright (C) 1995-2007 Alcatel-Lucent ALL RIGHTS RESERVED WORLDWIDE')
alcatelIND1DVMRPMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1))
alaDvmrpGlobalConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 1))
alaDvmrpDebugConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 2))
alaDvmrpTunnelXIfTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 3), )
if mibBuilder.loadTexts: alaDvmrpTunnelXIfTable.setStatus('current')
if mibBuilder.loadTexts: alaDvmrpTunnelXIfTable.setDescription('A list of attributes that are associated with the internal assigned tunnel index when a DVMRP tunnel is created. This table contains additional objects that are not present in the tunnelMIB tunnelIfTable.')
alaDvmrpAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2), ("unrestrictedEnable", 3))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDvmrpAdminStatus.setStatus('current')
if mibBuilder.loadTexts: alaDvmrpAdminStatus.setDescription('Administratively enables/disables the DVMRP protocol on this router.')
alaDvmrpRouteReportInterval = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 2000)).clone(60)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDvmrpRouteReportInterval.setStatus('current')
if mibBuilder.loadTexts: alaDvmrpRouteReportInterval.setDescription('The Route Report Interval determines how often a router will send its complete routing tables to neighboring routers running DVMRP.')
alaDvmrpFlashUpdateInterval = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 86400)).clone(5)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDvmrpFlashUpdateInterval.setStatus('current')
if mibBuilder.loadTexts: alaDvmrpFlashUpdateInterval.setDescription('The minimum Flash Update Interval defines how often routing table change messages are sent to neighboring DVMRP routers. Since these messages are sent between the transmission of complete routing tables, the flash update interval value must be shorter than that of the route report interval.')
alaDvmrpNeighborTimeout = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 86400)).clone(35)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDvmrpNeighborTimeout.setStatus('current')
if mibBuilder.loadTexts: alaDvmrpNeighborTimeout.setDescription('The Neighbor Timeout value specifies how long, without any activity from a neighboring DVMRP router, the router will wait before assuming that the inactive router is down.')
alaDvmrpRouteExpirationTimeout = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(20, 4000)).clone(140)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDvmrpRouteExpirationTimeout.setStatus('current')
if mibBuilder.loadTexts: alaDvmrpRouteExpirationTimeout.setDescription("The Route Expiration Timeout value specifies how long the router will wait before aging out a route. When this value expires, the route is advertised as inactive until either it's activity resumes or it is deleted.")
alaDvmrpRouteHoldDown = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 86400)).clone(120)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDvmrpRouteHoldDown.setStatus('current')
if mibBuilder.loadTexts: alaDvmrpRouteHoldDown.setDescription('Specifies the time during which DVMRP routes are kept in a hold-down state. A hold-down state refers to the time that a route to an inactive network continues to be advertised.')
alaDvmrpNeighborProbeInterval = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 30)).clone(10)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDvmrpNeighborProbeInterval.setStatus('current')
if mibBuilder.loadTexts: alaDvmrpNeighborProbeInterval.setDescription('The Neighbor Probe Interval value specifies how often probes will be transmitted to those interfaces with attached DVMRP neighbors.')
alaDvmrpPruneLifetime = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(180, 86400)).clone(7200)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDvmrpPruneLifetime.setStatus('current')
if mibBuilder.loadTexts: alaDvmrpPruneLifetime.setDescription('The Prune Lifetime value defines the value whereby a source-rooted multicast tree will be pruned.')
alaDvmrpPruneRetransmission = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(30, 86400)).clone(30)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDvmrpPruneRetransmission.setStatus('current')
if mibBuilder.loadTexts: alaDvmrpPruneRetransmission.setDescription('The Prune Packet Retransmission value is the duration of time that the router will wait, if it continues to receive unwanted multicast traffic, before retransmitting a prune message.')
alaDvmrpGraftRetransmission = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 86400)).clone(5)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDvmrpGraftRetransmission.setStatus('current')
if mibBuilder.loadTexts: alaDvmrpGraftRetransmission.setDescription('The Graft message Retransmission value defines the duration of time that the router will wait before retransmitting a graft message, if it has not already received an acknowledgement from its neighbor.')
alaDvmrpInitNbrAsSubord = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 1, 11), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDvmrpInitNbrAsSubord.setStatus('current')
if mibBuilder.loadTexts: alaDvmrpInitNbrAsSubord.setDescription('The value true(1) indicates neighbors, on initial discovery, are considered subordinate. This means traffic may be resumed slightly quicker on network disruptions. But, if the neighbor has trouble handling huge initial blasts of traffic, it may be wise to wait until route reports have been exchanged and the neighbor has requested dependency, before forwarding traffic.')
alaDvmrpBfdStatus = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDvmrpBfdStatus.setStatus('current')
if mibBuilder.loadTexts: alaDvmrpBfdStatus.setDescription('Enables/Disables Bfd for DVMRP Protocol.')
alaDvmrpBfdAllInterfaceStatus = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDvmrpBfdAllInterfaceStatus.setStatus('current')
if mibBuilder.loadTexts: alaDvmrpBfdAllInterfaceStatus.setDescription('Enables/Disables Bfd for all DVMRP interfaces.')
alaDvmrpDebugLevel = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDvmrpDebugLevel.setStatus('deprecated')
if mibBuilder.loadTexts: alaDvmrpDebugLevel.setDescription('This Object is deprecated in favour of alaDrcTmDvmrpDebug Configuration')
alaDvmrpDebugError = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDvmrpDebugError.setStatus('deprecated')
if mibBuilder.loadTexts: alaDvmrpDebugError.setDescription('This Object is deprecated in favour of alaDrcTmDvmrpDebugError MIB Object of alaDrcTmDvmrpDebug Configuration')
alaDvmrpDebugNbr = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDvmrpDebugNbr.setStatus('deprecated')
if mibBuilder.loadTexts: alaDvmrpDebugNbr.setDescription('This Object is deprecated in favour of alaDrcTmDvmrpDebugNbr MIB Object of alaDrcTmDvmrpDebug Configuration')
alaDvmrpDebugRoutes = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDvmrpDebugRoutes.setStatus('deprecated')
if mibBuilder.loadTexts: alaDvmrpDebugRoutes.setDescription('This Object is deprecated in favour of alaDrcTmDvmrpDebugRoutes MIB Object of alaDrcTmDvmrpDebug Configuration')
alaDvmrpDebugProbes = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 2, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDvmrpDebugProbes.setStatus('deprecated')
if mibBuilder.loadTexts: alaDvmrpDebugProbes.setDescription('This Object is deprecated in favour of alaDrcTmDvmrpDebugProbes MIB Object of alaDrcTmDvmrpDebug Configuration')
alaDvmrpDebugPrunes = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 2, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDvmrpDebugPrunes.setStatus('deprecated')
if mibBuilder.loadTexts: alaDvmrpDebugPrunes.setDescription('This Object is deprecated in favour of alaDrcTmDvmrpDebugPrunes MIB Object of alaDrcTmDvmrpDebug Configuration')
alaDvmrpDebugGrafts = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 2, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDvmrpDebugGrafts.setStatus('deprecated')
if mibBuilder.loadTexts: alaDvmrpDebugGrafts.setDescription('This Object is deprecated in favour of alaDrcTmDvmrpDebugGrafts MIB Object of alaDrcTmDvmrpDebug Configuration')
alaDvmrpDebugTime = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 2, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDvmrpDebugTime.setStatus('deprecated')
if mibBuilder.loadTexts: alaDvmrpDebugTime.setDescription('This Object is deprecated in favour of alaDrcTmDvmrpDebugTime MIB Object of alaDrcTmDvmrpDebug Configuration')
alaDvmrpDebugIgmp = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 2, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDvmrpDebugIgmp.setStatus('deprecated')
if mibBuilder.loadTexts: alaDvmrpDebugIgmp.setDescription('This Object is deprecated in favour of alaDrcTmDvmrpDebugIgmp MIB Object of alaDrcTmDvmrpDebug Configuration')
alaDvmrpDebugFlash = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 2, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDvmrpDebugFlash.setStatus('deprecated')
if mibBuilder.loadTexts: alaDvmrpDebugFlash.setDescription('This Object is deprecated in favour of alaDrcTmDvmrpDebugFlash MIB Object of alaDrcTmDvmrpDebug Configuration')
alaDvmrpDebugMip = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 2, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDvmrpDebugMip.setStatus('deprecated')
if mibBuilder.loadTexts: alaDvmrpDebugMip.setDescription('This Object is deprecated in favour of alaDrcTmDvmrpDebugMip MIB Object of alaDrcTmDvmrpDebug Configuration')
alaDvmrpDebugInit = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 2, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDvmrpDebugInit.setStatus('deprecated')
if mibBuilder.loadTexts: alaDvmrpDebugInit.setDescription('This Object is deprecated in favour of alaDrcTmDvmrpDebugInit MIB Object of alaDrcTmDvmrpDebug Configuration')
alaDvmrpDebugTm = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 2, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDvmrpDebugTm.setStatus('deprecated')
if mibBuilder.loadTexts: alaDvmrpDebugTm.setDescription('This Object is deprecated in favour of alaDrcTmDvmrpDebugTm MIB Object of alaDrcTmDvmrpDebug Configuration')
alaDvmrpDebugIpmrm = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 2, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDvmrpDebugIpmrm.setStatus('deprecated')
if mibBuilder.loadTexts: alaDvmrpDebugIpmrm.setDescription('This Object is deprecated in favour of alaDrcTmDvmrpDebugIpmrm MIB Object of alaDrcTmDvmrpDebug Configuration')
alaDvmrpDebugMisc = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 2, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDvmrpDebugMisc.setStatus('deprecated')
if mibBuilder.loadTexts: alaDvmrpDebugMisc.setDescription('This Object is deprecated in favour of alaDrcTmDvmrpDebugMisc MIB Object of alaDrcTmDvmrpDebug Configuration')
alaDvmrpDebugAll = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 2, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDvmrpDebugAll.setStatus('deprecated')
if mibBuilder.loadTexts: alaDvmrpDebugAll.setDescription('This Object is deprecated in favour of alaDrcTmDvmrpDebugAll MIB Object of alaDrcTmDvmrpDebug Configuration')
alaDvmrpTunnelXIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 3, 1), ).setIndexNames((0, "ALCATEL-IND1-DVMRP-MIB", "alaDvmrpTunnelIndex"))
if mibBuilder.loadTexts: alaDvmrpTunnelXIfEntry.setStatus('current')
if mibBuilder.loadTexts: alaDvmrpTunnelXIfEntry.setDescription('An entry containing additional attributes associated with a DVMRP tunnel.')
alaDvmrpTunnelIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 3, 1, 1), Unsigned32())
if mibBuilder.loadTexts: alaDvmrpTunnelIndex.setStatus('current')
if mibBuilder.loadTexts: alaDvmrpTunnelIndex.setDescription('The tunnel index of the DVMRP tunnel.')
alaDvmrpLocalIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 3, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaDvmrpLocalIfIndex.setStatus('current')
if mibBuilder.loadTexts: alaDvmrpLocalIfIndex.setDescription('The interface index of the local end-point of the DVMRP tunnel.')
alaDvmrpIfAugTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 4), )
if mibBuilder.loadTexts: alaDvmrpIfAugTable.setStatus('current')
if mibBuilder.loadTexts: alaDvmrpIfAugTable.setDescription('Expansion for Dvmrp Intf table.')
alaDvmrpIfAugEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 4, 1), )
dvmrpInterfaceEntry.registerAugmentions(("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpIfAugEntry"))
alaDvmrpIfAugEntry.setIndexNames(*dvmrpInterfaceEntry.getIndexNames())
if mibBuilder.loadTexts: alaDvmrpIfAugEntry.setStatus('current')
if mibBuilder.loadTexts: alaDvmrpIfAugEntry.setDescription('An entry of alaDvmrpIfAugEntry.')
alaDvmrpIfBfdStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaDvmrpIfBfdStatus.setStatus('current')
if mibBuilder.loadTexts: alaDvmrpIfBfdStatus.setDescription('This object enables/disables BFD for this DVMRP interface.')
alcatelIND1DVMRPMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 2))
alcatelIND1DVMRPMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 2, 1))
alcatelIND1DVMRPMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 2, 2))
alaDvmrpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 2, 1, 1)).setObjects(("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpConfigMIBGroup"), ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpDebugMIBGroup"), ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpTunnelXIfMIBGroup"), ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpIfConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaDvmrpCompliance = alaDvmrpCompliance.setStatus('current')
if mibBuilder.loadTexts: alaDvmrpCompliance.setDescription('The compliance statement for routers running DVMRP and implementing the ALCATEL-IND1-DVMRP MIB.')
alaDvmrpConfigMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 2, 2, 1)).setObjects(("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpAdminStatus"), ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpRouteReportInterval"), ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpFlashUpdateInterval"), ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpNeighborTimeout"), ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpRouteExpirationTimeout"), ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpRouteHoldDown"), ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpNeighborProbeInterval"), ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpPruneLifetime"), ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpPruneRetransmission"), ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpGraftRetransmission"), ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpInitNbrAsSubord"), ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpBfdStatus"), ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpBfdAllInterfaceStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaDvmrpConfigMIBGroup = alaDvmrpConfigMIBGroup.setStatus('current')
if mibBuilder.loadTexts: alaDvmrpConfigMIBGroup.setDescription('A collection of objects to support the management of global configuration parameters on DVMRP routers.')
alaDvmrpDebugMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 2, 2, 2)).setObjects(("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpDebugLevel"), ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpDebugError"), ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpDebugNbr"), ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpDebugRoutes"), ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpDebugProbes"), ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpDebugPrunes"), ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpDebugGrafts"), ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpDebugTime"), ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpDebugIgmp"), ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpDebugFlash"), ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpDebugMip"), ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpDebugInit"), ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpDebugTm"), ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpDebugIpmrm"), ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpDebugMisc"), ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpDebugAll"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaDvmrpDebugMIBGroup = alaDvmrpDebugMIBGroup.setStatus('current')
if mibBuilder.loadTexts: alaDvmrpDebugMIBGroup.setDescription('A collection of optional objects to provide debugging support on DVMRP routers.')
alaDvmrpTunnelXIfMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 2, 2, 3)).setObjects(("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpLocalIfIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaDvmrpTunnelXIfMIBGroup = alaDvmrpTunnelXIfMIBGroup.setStatus('current')
if mibBuilder.loadTexts: alaDvmrpTunnelXIfMIBGroup.setDescription('These objects are required to provide additional information about configured DVMRP tunnels not found in the standard tunnel MIB.')
alaDvmrpIfConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 2, 2, 4)).setObjects(("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpIfBfdStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaDvmrpIfConfigGroup = alaDvmrpIfConfigGroup.setStatus('current')
if mibBuilder.loadTexts: alaDvmrpIfConfigGroup.setDescription('These objects are required to provide additional information about configured DVMRP interfaces not found in the standard tunnel MIB.')
mibBuilder.exportSymbols("ALCATEL-IND1-DVMRP-MIB", alaDvmrpPruneLifetime=alaDvmrpPruneLifetime, alaDvmrpDebugGrafts=alaDvmrpDebugGrafts, alcatelIND1DVMRPMIBCompliances=alcatelIND1DVMRPMIBCompliances, alaDvmrpCompliance=alaDvmrpCompliance, alaDvmrpBfdStatus=alaDvmrpBfdStatus, alaDvmrpInitNbrAsSubord=alaDvmrpInitNbrAsSubord, alcatelIND1DVMRPMIBConformance=alcatelIND1DVMRPMIBConformance, alaDvmrpIfConfigGroup=alaDvmrpIfConfigGroup, alaDvmrpRouteReportInterval=alaDvmrpRouteReportInterval, alaDvmrpDebugMip=alaDvmrpDebugMip, alaDvmrpBfdAllInterfaceStatus=alaDvmrpBfdAllInterfaceStatus, alcatelIND1DVMRPMIBObjects=alcatelIND1DVMRPMIBObjects, alaDvmrpIfBfdStatus=alaDvmrpIfBfdStatus, alaDvmrpDebugIpmrm=alaDvmrpDebugIpmrm, alaDvmrpConfigMIBGroup=alaDvmrpConfigMIBGroup, alaDvmrpGlobalConfig=alaDvmrpGlobalConfig, alaDvmrpDebugConfig=alaDvmrpDebugConfig, alaDvmrpIfAugTable=alaDvmrpIfAugTable, alaDvmrpNeighborTimeout=alaDvmrpNeighborTimeout, alaDvmrpDebugTm=alaDvmrpDebugTm, alaDvmrpDebugPrunes=alaDvmrpDebugPrunes, alaDvmrpDebugTime=alaDvmrpDebugTime, alaDvmrpLocalIfIndex=alaDvmrpLocalIfIndex, alaDvmrpPruneRetransmission=alaDvmrpPruneRetransmission, alaDvmrpRouteExpirationTimeout=alaDvmrpRouteExpirationTimeout, alaDvmrpDebugInit=alaDvmrpDebugInit, alaDvmrpTunnelXIfEntry=alaDvmrpTunnelXIfEntry, alaDvmrpDebugError=alaDvmrpDebugError, alaDvmrpDebugMisc=alaDvmrpDebugMisc, alaDvmrpDebugProbes=alaDvmrpDebugProbes, PYSNMP_MODULE_ID=alcatelIND1DVMRPMIB, alaDvmrpDebugIgmp=alaDvmrpDebugIgmp, alaDvmrpDebugFlash=alaDvmrpDebugFlash, alaDvmrpDebugLevel=alaDvmrpDebugLevel, alaDvmrpGraftRetransmission=alaDvmrpGraftRetransmission, alaDvmrpTunnelXIfMIBGroup=alaDvmrpTunnelXIfMIBGroup, alaDvmrpDebugAll=alaDvmrpDebugAll, alaDvmrpTunnelXIfTable=alaDvmrpTunnelXIfTable, alaDvmrpAdminStatus=alaDvmrpAdminStatus, alcatelIND1DVMRPMIB=alcatelIND1DVMRPMIB, alaDvmrpIfAugEntry=alaDvmrpIfAugEntry, alaDvmrpDebugMIBGroup=alaDvmrpDebugMIBGroup, alaDvmrpRouteHoldDown=alaDvmrpRouteHoldDown, alaDvmrpNeighborProbeInterval=alaDvmrpNeighborProbeInterval, alaDvmrpFlashUpdateInterval=alaDvmrpFlashUpdateInterval, alaDvmrpTunnelIndex=alaDvmrpTunnelIndex, alaDvmrpDebugNbr=alaDvmrpDebugNbr, alaDvmrpDebugRoutes=alaDvmrpDebugRoutes, alcatelIND1DVMRPMIBGroups=alcatelIND1DVMRPMIBGroups)
