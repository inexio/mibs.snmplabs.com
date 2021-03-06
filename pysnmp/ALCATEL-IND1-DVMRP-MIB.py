#
# PySNMP MIB module ALCATEL-IND1-DVMRP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALCATEL-IND1-DVMRP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:01:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
routingIND1Dvmrp, = mibBuilder.importSymbols("ALCATEL-IND1-BASE", "routingIND1Dvmrp")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
dvmrpInterfaceEntry, = mibBuilder.importSymbols("DVMRP-STD-MIB", "dvmrpInterfaceEntry")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
enterprises, Counter32, ObjectIdentity, Integer32, Bits, NotificationType, IpAddress, TimeTicks, Gauge32, Counter64, MibIdentifier, Unsigned32, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "Counter32", "ObjectIdentity", "Integer32", "Bits", "NotificationType", "IpAddress", "TimeTicks", "Gauge32", "Counter64", "MibIdentifier", "Unsigned32", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
alcatelIND1DVMRPMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1))
alcatelIND1DVMRPMIB.setRevisions(('2007-04-03 00:00',))
if mibBuilder.loadTexts: alcatelIND1DVMRPMIB.setLastUpdated('200704030000Z')
if mibBuilder.loadTexts: alcatelIND1DVMRPMIB.setOrganization('Alcatel-Lucent')
alcatelIND1DVMRPMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1))
alaDvmrpGlobalConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 1))
alaDvmrpDebugConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 2))
alaDvmrpTunnelXIfTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 3), )
if mibBuilder.loadTexts: alaDvmrpTunnelXIfTable.setStatus('current')
alaDvmrpAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2), ("unrestrictedEnable", 3))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDvmrpAdminStatus.setStatus('current')
alaDvmrpRouteReportInterval = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 2000)).clone(60)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDvmrpRouteReportInterval.setStatus('current')
alaDvmrpFlashUpdateInterval = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 86400)).clone(5)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDvmrpFlashUpdateInterval.setStatus('current')
alaDvmrpNeighborTimeout = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 86400)).clone(35)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDvmrpNeighborTimeout.setStatus('current')
alaDvmrpRouteExpirationTimeout = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(20, 4000)).clone(140)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDvmrpRouteExpirationTimeout.setStatus('current')
alaDvmrpRouteHoldDown = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 86400)).clone(120)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDvmrpRouteHoldDown.setStatus('current')
alaDvmrpNeighborProbeInterval = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 30)).clone(10)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDvmrpNeighborProbeInterval.setStatus('current')
alaDvmrpPruneLifetime = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(180, 86400)).clone(7200)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDvmrpPruneLifetime.setStatus('current')
alaDvmrpPruneRetransmission = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(30, 86400)).clone(30)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDvmrpPruneRetransmission.setStatus('current')
alaDvmrpGraftRetransmission = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 86400)).clone(5)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDvmrpGraftRetransmission.setStatus('current')
alaDvmrpInitNbrAsSubord = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 1, 11), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDvmrpInitNbrAsSubord.setStatus('current')
alaDvmrpBfdStatus = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDvmrpBfdStatus.setStatus('current')
alaDvmrpBfdAllInterfaceStatus = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDvmrpBfdAllInterfaceStatus.setStatus('current')
alaDvmrpDebugLevel = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDvmrpDebugLevel.setStatus('deprecated')
alaDvmrpDebugError = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDvmrpDebugError.setStatus('deprecated')
alaDvmrpDebugNbr = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDvmrpDebugNbr.setStatus('deprecated')
alaDvmrpDebugRoutes = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDvmrpDebugRoutes.setStatus('deprecated')
alaDvmrpDebugProbes = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 2, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDvmrpDebugProbes.setStatus('deprecated')
alaDvmrpDebugPrunes = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 2, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDvmrpDebugPrunes.setStatus('deprecated')
alaDvmrpDebugGrafts = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 2, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDvmrpDebugGrafts.setStatus('deprecated')
alaDvmrpDebugTime = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 2, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDvmrpDebugTime.setStatus('deprecated')
alaDvmrpDebugIgmp = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 2, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDvmrpDebugIgmp.setStatus('deprecated')
alaDvmrpDebugFlash = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 2, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDvmrpDebugFlash.setStatus('deprecated')
alaDvmrpDebugMip = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 2, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDvmrpDebugMip.setStatus('deprecated')
alaDvmrpDebugInit = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 2, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDvmrpDebugInit.setStatus('deprecated')
alaDvmrpDebugTm = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 2, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDvmrpDebugTm.setStatus('deprecated')
alaDvmrpDebugIpmrm = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 2, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDvmrpDebugIpmrm.setStatus('deprecated')
alaDvmrpDebugMisc = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 2, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDvmrpDebugMisc.setStatus('deprecated')
alaDvmrpDebugAll = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 2, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDvmrpDebugAll.setStatus('deprecated')
alaDvmrpTunnelXIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 3, 1), ).setIndexNames((0, "ALCATEL-IND1-DVMRP-MIB", "alaDvmrpTunnelIndex"))
if mibBuilder.loadTexts: alaDvmrpTunnelXIfEntry.setStatus('current')
alaDvmrpTunnelIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 3, 1, 1), Unsigned32())
if mibBuilder.loadTexts: alaDvmrpTunnelIndex.setStatus('current')
alaDvmrpLocalIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 3, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaDvmrpLocalIfIndex.setStatus('current')
alaDvmrpIfAugTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 4), )
if mibBuilder.loadTexts: alaDvmrpIfAugTable.setStatus('current')
alaDvmrpIfAugEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 4, 1), )
dvmrpInterfaceEntry.registerAugmentions(("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpIfAugEntry"))
alaDvmrpIfAugEntry.setIndexNames(*dvmrpInterfaceEntry.getIndexNames())
if mibBuilder.loadTexts: alaDvmrpIfAugEntry.setStatus('current')
alaDvmrpIfBfdStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaDvmrpIfBfdStatus.setStatus('current')
alcatelIND1DVMRPMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 2))
alcatelIND1DVMRPMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 2, 1))
alcatelIND1DVMRPMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 2, 2))
alaDvmrpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 2, 1, 1)).setObjects(("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpConfigMIBGroup"), ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpDebugMIBGroup"), ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpTunnelXIfMIBGroup"), ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpIfConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaDvmrpCompliance = alaDvmrpCompliance.setStatus('current')
alaDvmrpConfigMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 2, 2, 1)).setObjects(("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpAdminStatus"), ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpRouteReportInterval"), ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpFlashUpdateInterval"), ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpNeighborTimeout"), ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpRouteExpirationTimeout"), ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpRouteHoldDown"), ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpNeighborProbeInterval"), ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpPruneLifetime"), ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpPruneRetransmission"), ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpGraftRetransmission"), ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpInitNbrAsSubord"), ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpBfdStatus"), ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpBfdAllInterfaceStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaDvmrpConfigMIBGroup = alaDvmrpConfigMIBGroup.setStatus('current')
alaDvmrpDebugMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 2, 2, 2)).setObjects(("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpDebugLevel"), ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpDebugError"), ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpDebugNbr"), ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpDebugRoutes"), ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpDebugProbes"), ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpDebugPrunes"), ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpDebugGrafts"), ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpDebugTime"), ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpDebugIgmp"), ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpDebugFlash"), ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpDebugMip"), ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpDebugInit"), ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpDebugTm"), ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpDebugIpmrm"), ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpDebugMisc"), ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpDebugAll"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaDvmrpDebugMIBGroup = alaDvmrpDebugMIBGroup.setStatus('current')
alaDvmrpTunnelXIfMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 2, 2, 3)).setObjects(("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpLocalIfIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaDvmrpTunnelXIfMIBGroup = alaDvmrpTunnelXIfMIBGroup.setStatus('current')
alaDvmrpIfConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 2, 2, 4)).setObjects(("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpIfBfdStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaDvmrpIfConfigGroup = alaDvmrpIfConfigGroup.setStatus('current')
mibBuilder.exportSymbols("ALCATEL-IND1-DVMRP-MIB", alaDvmrpTunnelXIfEntry=alaDvmrpTunnelXIfEntry, alaDvmrpGraftRetransmission=alaDvmrpGraftRetransmission, alaDvmrpRouteHoldDown=alaDvmrpRouteHoldDown, alaDvmrpDebugIgmp=alaDvmrpDebugIgmp, alaDvmrpDebugProbes=alaDvmrpDebugProbes, alaDvmrpIfAugEntry=alaDvmrpIfAugEntry, alaDvmrpNeighborProbeInterval=alaDvmrpNeighborProbeInterval, PYSNMP_MODULE_ID=alcatelIND1DVMRPMIB, alcatelIND1DVMRPMIBGroups=alcatelIND1DVMRPMIBGroups, alaDvmrpDebugLevel=alaDvmrpDebugLevel, alaDvmrpIfBfdStatus=alaDvmrpIfBfdStatus, alaDvmrpAdminStatus=alaDvmrpAdminStatus, alcatelIND1DVMRPMIB=alcatelIND1DVMRPMIB, alaDvmrpDebugTime=alaDvmrpDebugTime, alaDvmrpDebugInit=alaDvmrpDebugInit, alaDvmrpRouteReportInterval=alaDvmrpRouteReportInterval, alaDvmrpDebugMIBGroup=alaDvmrpDebugMIBGroup, alaDvmrpDebugPrunes=alaDvmrpDebugPrunes, alaDvmrpDebugFlash=alaDvmrpDebugFlash, alaDvmrpTunnelIndex=alaDvmrpTunnelIndex, alaDvmrpDebugNbr=alaDvmrpDebugNbr, alaDvmrpIfConfigGroup=alaDvmrpIfConfigGroup, alaDvmrpGlobalConfig=alaDvmrpGlobalConfig, alaDvmrpBfdStatus=alaDvmrpBfdStatus, alaDvmrpFlashUpdateInterval=alaDvmrpFlashUpdateInterval, alaDvmrpDebugError=alaDvmrpDebugError, alaDvmrpDebugMisc=alaDvmrpDebugMisc, alcatelIND1DVMRPMIBConformance=alcatelIND1DVMRPMIBConformance, alaDvmrpLocalIfIndex=alaDvmrpLocalIfIndex, alaDvmrpDebugMip=alaDvmrpDebugMip, alaDvmrpTunnelXIfTable=alaDvmrpTunnelXIfTable, alaDvmrpPruneLifetime=alaDvmrpPruneLifetime, alaDvmrpDebugTm=alaDvmrpDebugTm, alaDvmrpTunnelXIfMIBGroup=alaDvmrpTunnelXIfMIBGroup, alaDvmrpDebugConfig=alaDvmrpDebugConfig, alcatelIND1DVMRPMIBObjects=alcatelIND1DVMRPMIBObjects, alaDvmrpDebugIpmrm=alaDvmrpDebugIpmrm, alaDvmrpInitNbrAsSubord=alaDvmrpInitNbrAsSubord, alaDvmrpDebugGrafts=alaDvmrpDebugGrafts, alaDvmrpDebugAll=alaDvmrpDebugAll, alaDvmrpBfdAllInterfaceStatus=alaDvmrpBfdAllInterfaceStatus, alcatelIND1DVMRPMIBCompliances=alcatelIND1DVMRPMIBCompliances, alaDvmrpIfAugTable=alaDvmrpIfAugTable, alaDvmrpPruneRetransmission=alaDvmrpPruneRetransmission, alaDvmrpNeighborTimeout=alaDvmrpNeighborTimeout, alaDvmrpConfigMIBGroup=alaDvmrpConfigMIBGroup, alaDvmrpRouteExpirationTimeout=alaDvmrpRouteExpirationTimeout, alaDvmrpDebugRoutes=alaDvmrpDebugRoutes, alaDvmrpCompliance=alaDvmrpCompliance)
