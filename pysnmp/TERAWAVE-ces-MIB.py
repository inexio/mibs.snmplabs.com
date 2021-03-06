#
# PySNMP MIB module TERAWAVE-ces-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TERAWAVE-ces-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:08:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
enterprises, Counter64, Bits, TimeTicks, IpAddress, iso, Counter32, NotificationType, Integer32, ModuleIdentity, ObjectIdentity, Gauge32, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "Counter64", "Bits", "TimeTicks", "IpAddress", "iso", "Counter32", "NotificationType", "Integer32", "ModuleIdentity", "ObjectIdentity", "Gauge32", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
atmForum = MibIdentifier((1, 3, 6, 1, 4, 1, 353))
atmForumNetworkManagment = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 5))
atmfCESmib = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 5, 2))
atmfCES = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 5, 2, 2))
atmfCESObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1))
atmfCESConTable = MibTable((1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 1), )
if mibBuilder.loadTexts: atmfCESConTable.setStatus('mandatory')
atmfCESConTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 1, 1), ).setIndexNames((0, "TERAWAVE-ces-MIB", "atmfCESCbrIndex"))
if mibBuilder.loadTexts: atmfCESConTableEntry.setStatus('mandatory')
atmfCESCbrIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfCESCbrIndex.setStatus('mandatory')
atmfCESAtmIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmfCESAtmIndex.setStatus('mandatory')
atmfCESAtmVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmfCESAtmVpi.setStatus('mandatory')
atmfCESAtmVci = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmfCESAtmVci.setStatus('mandatory')
atmfCESCbrService = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("unstructured", 1), ("structured", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmfCESCbrService.setStatus('mandatory')
atmfCESCbrClockMode = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("synchronous", 1), ("srts", 2), ("adaptive", 3), ("looped", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmfCESCbrClockMode.setStatus('mandatory')
atmfCESCas = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("basic", 1), ("e1Cas", 2), ("ds1SfCas", 3), ("ds1EsfCas", 4), ("j2Cas", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmfCESCas.setStatus('mandatory')
atmfCESPartialFill = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 47))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmfCESPartialFill.setStatus('mandatory')
atmfCESBufMaxSize = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 510))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmfCESBufMaxSize.setStatus('mandatory')
atmfCESCdvtRxT = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmfCESCdvtRxT.setStatus('mandatory')
atmfCESCellLossIntegrationPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1000, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmfCESCellLossIntegrationPeriod.setStatus('mandatory')
atmfCESConnType = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("pvc", 2), ("activeSvc", 3), ("passiveSvc", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmfCESConnType.setStatus('mandatory')
atmfCESLocalAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 1, 1, 13), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmfCESLocalAddr.setStatus('mandatory')
atmfCESAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmfCESAdminStatus.setStatus('mandatory')
atmfCESOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("unknown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfCESOperStatus.setStatus('mandatory')
atmCESConfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("active", 1), ("notInService", 2), ("notReady", 3), ("createAndGo", 4), ("createAndWait", 5), ("destroy", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmCESConfRowStatus.setStatus('mandatory')
atmfCESMappingTable = MibTable((1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 2), )
if mibBuilder.loadTexts: atmfCESMappingTable.setStatus('mandatory')
atmfCESMappingTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 2, 1), ).setIndexNames((0, "TERAWAVE-ces-MIB", "atmfCESAtmIndex"), (0, "TERAWAVE-ces-MIB", "atmfCESAtmVpi"), (0, "TERAWAVE-ces-MIB", "atmfCESAtmVci"))
if mibBuilder.loadTexts: atmfCESMappingTableEntry.setStatus('mandatory')
atmfCESMappingCbrIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfCESMappingCbrIndex.setStatus('mandatory')
atmfCESStatsTable = MibTable((1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 3), )
if mibBuilder.loadTexts: atmfCESStatsTable.setStatus('mandatory')
atmfCESStatsTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 3, 1), ).setIndexNames((0, "TERAWAVE-ces-MIB", "atmfCESCbrIndex"))
if mibBuilder.loadTexts: atmfCESStatsTableEntry.setStatus('mandatory')
atmfCESReassCells = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 3, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfCESReassCells.setStatus('mandatory')
atmfCESHdrErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfCESHdrErrors.setStatus('mandatory')
atmfCESPointerReframes = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfCESPointerReframes.setStatus('mandatory')
atmfCESPointerParityErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfCESPointerParityErrors.setStatus('mandatory')
atmfCESAal1SeqErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfCESAal1SeqErrors.setStatus('mandatory')
atmfCESLostCells = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfCESLostCells.setStatus('mandatory')
atmfCESMisinsertedCells = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfCESMisinsertedCells.setStatus('mandatory')
atmfCESBufUnderflows = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfCESBufUnderflows.setStatus('mandatory')
atmfCESBufOverflows = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfCESBufOverflows.setStatus('mandatory')
atmfCESCellLossStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 3, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noloss", 1), ("loss", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfCESCellLossStatus.setStatus('mandatory')
atmfCESActiveSvcTable = MibTable((1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 4), )
if mibBuilder.loadTexts: atmfCESActiveSvcTable.setStatus('mandatory')
atmfCESActiveSvcTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 4, 1), ).setIndexNames((0, "TERAWAVE-ces-MIB", "atmfCESCbrIndex"))
if mibBuilder.loadTexts: atmfCESActiveSvcTableEntry.setStatus('mandatory')
atmfCESRemoteAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 4, 1, 1), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmfCESRemoteAddr.setStatus('mandatory')
atmfCESFirstRetryInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 3600))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmfCESFirstRetryInterval.setStatus('mandatory')
atmfCESRetryTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 86400))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfCESRetryTimer.setStatus('mandatory')
atmfCESRetryLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 4, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmfCESRetryLimit.setStatus('mandatory')
atmfCESRetryFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 4, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfCESRetryFailures.setStatus('mandatory')
atmfCESActiveSvcRestart = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 4, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("restart", 1), ("noop", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmfCESActiveSvcRestart.setStatus('mandatory')
atmfCESActiveSvcOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 4, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfCESActiveSvcOperStatus.setStatus('mandatory')
atmfCESLastReleaseCause = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 4, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfCESLastReleaseCause.setStatus('mandatory')
atmfCESLastReleaseDiagnostics = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 4, 1, 9), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfCESLastReleaseDiagnostics.setStatus('mandatory')
mibBuilder.exportSymbols("TERAWAVE-ces-MIB", atmfCES=atmfCES, atmForumNetworkManagment=atmForumNetworkManagment, atmfCESOperStatus=atmfCESOperStatus, atmfCESConnType=atmfCESConnType, atmfCESLocalAddr=atmfCESLocalAddr, atmfCESCbrClockMode=atmfCESCbrClockMode, atmfCESHdrErrors=atmfCESHdrErrors, atmfCESBufUnderflows=atmfCESBufUnderflows, atmfCESActiveSvcTable=atmfCESActiveSvcTable, atmfCESAtmVpi=atmfCESAtmVpi, atmfCESCdvtRxT=atmfCESCdvtRxT, atmfCESLastReleaseDiagnostics=atmfCESLastReleaseDiagnostics, atmfCESAal1SeqErrors=atmfCESAal1SeqErrors, atmfCESBufOverflows=atmfCESBufOverflows, atmfCESAtmVci=atmfCESAtmVci, atmfCESAtmIndex=atmfCESAtmIndex, atmfCESActiveSvcOperStatus=atmfCESActiveSvcOperStatus, atmfCESCbrService=atmfCESCbrService, atmCESConfRowStatus=atmCESConfRowStatus, atmfCESLostCells=atmfCESLostCells, atmfCESActiveSvcRestart=atmfCESActiveSvcRestart, atmfCESMappingTableEntry=atmfCESMappingTableEntry, atmfCESRetryTimer=atmfCESRetryTimer, atmfCESActiveSvcTableEntry=atmfCESActiveSvcTableEntry, atmfCESmib=atmfCESmib, atmfCESBufMaxSize=atmfCESBufMaxSize, atmfCESAdminStatus=atmfCESAdminStatus, atmfCESConTableEntry=atmfCESConTableEntry, atmfCESReassCells=atmfCESReassCells, atmfCESCellLossStatus=atmfCESCellLossStatus, atmfCESRemoteAddr=atmfCESRemoteAddr, atmfCESStatsTableEntry=atmfCESStatsTableEntry, atmfCESPointerReframes=atmfCESPointerReframes, atmfCESCbrIndex=atmfCESCbrIndex, atmfCESRetryLimit=atmfCESRetryLimit, atmfCESCellLossIntegrationPeriod=atmfCESCellLossIntegrationPeriod, atmfCESRetryFailures=atmfCESRetryFailures, atmfCESConTable=atmfCESConTable, atmfCESMisinsertedCells=atmfCESMisinsertedCells, atmfCESMappingTable=atmfCESMappingTable, atmfCESMappingCbrIndex=atmfCESMappingCbrIndex, atmfCESStatsTable=atmfCESStatsTable, atmfCESObjects=atmfCESObjects, atmForum=atmForum, atmfCESPointerParityErrors=atmfCESPointerParityErrors, atmfCESPartialFill=atmfCESPartialFill, atmfCESLastReleaseCause=atmfCESLastReleaseCause, atmfCESCas=atmfCESCas, atmfCESFirstRetryInterval=atmfCESFirstRetryInterval)
