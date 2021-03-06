#
# PySNMP MIB module Wellfleet-WFMPC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Wellfleet-WFMPC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:35:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, ObjectIdentity, MibIdentifier, Bits, TimeTicks, ModuleIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Gauge32, Integer32, iso, Counter32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ObjectIdentity", "MibIdentifier", "Bits", "TimeTicks", "ModuleIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Gauge32", "Integer32", "iso", "Counter32", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
wfmpcObjects, = mibBuilder.importSymbols("Wellfleet-COMMON-MIB", "wfmpcObjects")
wfmpcEntryTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 1), )
if mibBuilder.loadTexts: wfmpcEntryTable.setStatus('mandatory')
wfmpcEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 1, 1), ).setIndexNames((0, "Wellfleet-WFMPC-MIB", "wfmpcSlot"))
if mibBuilder.loadTexts: wfmpcEntry.setStatus('mandatory')
wfmpcDelete = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfmpcDelete.setStatus('mandatory')
wfmpcDisable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfmpcDisable.setStatus('mandatory')
wfmpcSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfmpcSlot.setStatus('mandatory')
wfmpcCct = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 1, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfmpcCct.setStatus('mandatory')
wfmpcMsgNum = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 1, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfmpcMsgNum.setStatus('mandatory')
wfmpcMsgSendEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfmpcMsgSendEnable.setStatus('mandatory')
wfmpcMPSAtmAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 1, 1, 7), OctetString().clone('0x390000000000000000000000000000A2CB2C2804')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfmpcMPSAtmAddr.setStatus('mandatory')
wfmpcSetupVCtoMPS = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfmpcSetupVCtoMPS.setStatus('mandatory')
wfmpcMPCAtmAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 1, 1, 9), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfmpcMPCAtmAddr.setStatus('mandatory')
wfmpcCIPNackFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfmpcCIPNackFlag.setStatus('mandatory')
wfmpcStatisticsTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 2), )
if mibBuilder.loadTexts: wfmpcStatisticsTable.setStatus('mandatory')
wfmpcStatisticsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 2, 1), ).setIndexNames((0, "Wellfleet-WFMPC-MIB", "wfmpcStatSlot"), (0, "Wellfleet-WFMPC-MIB", "wfmpcStatIndex"))
if mibBuilder.loadTexts: wfmpcStatisticsEntry.setStatus('mandatory')
wfmpcStatIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfmpcStatIndex.setStatus('mandatory')
wfmpcStatRxMpoaResolveRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfmpcStatRxMpoaResolveRequests.setStatus('mandatory')
wfmpcStatTxMpoaResolveReplyAcks = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfmpcStatTxMpoaResolveReplyAcks.setStatus('mandatory')
wfmpcStatTxMpoaResolveReplyInsufECResources = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfmpcStatTxMpoaResolveReplyInsufECResources.setStatus('mandatory')
wfmpcStatTxMpoaResolveReplyInsufSCResources = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfmpcStatTxMpoaResolveReplyInsufSCResources.setStatus('mandatory')
wfmpcStatTxMpoaResolveReplyInsufEitherResources = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfmpcStatTxMpoaResolveReplyInsufEitherResources.setStatus('mandatory')
wfmpcStatTxMpoaResolveReplyUnsupportedInetProt = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfmpcStatTxMpoaResolveReplyUnsupportedInetProt.setStatus('mandatory')
wfmpcStatTxMpoaResolveReplyUnsupportedMacEncaps = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfmpcStatTxMpoaResolveReplyUnsupportedMacEncaps.setStatus('mandatory')
wfmpcStatTxMpoaResolveReplyUnspecifiedOther = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfmpcStatTxMpoaResolveReplyUnspecifiedOther.setStatus('mandatory')
wfmpcStatTxMpoaResolveReplyOtherOther = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfmpcStatTxMpoaResolveReplyOtherOther.setStatus('mandatory')
wfmpcStatGiveupTimeExpireds = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfmpcStatGiveupTimeExpireds.setStatus('mandatory')
wfmpcStatTxMpoaImpRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfmpcStatTxMpoaImpRequests.setStatus('mandatory')
wfmpcStatRxMpoaImpReplyAcks = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfmpcStatRxMpoaImpReplyAcks.setStatus('mandatory')
wfmpcStatRxMpoaImpReplyInsufECResources = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfmpcStatRxMpoaImpReplyInsufECResources.setStatus('mandatory')
wfmpcStatRxMpoaImpReplyInsufSCResources = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 2, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfmpcStatRxMpoaImpReplyInsufSCResources.setStatus('mandatory')
wfmpcStatRxMpoaImpReplyInsufEitherResources = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 2, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfmpcStatRxMpoaImpReplyInsufEitherResources.setStatus('mandatory')
wfmpcStatRxMpoaImpReplyUnsupportedInetProt = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 2, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfmpcStatRxMpoaImpReplyUnsupportedInetProt.setStatus('mandatory')
wfmpcStatRxMpoaImpReplyUnsupportedMacEncaps = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 2, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfmpcStatRxMpoaImpReplyUnsupportedMacEncaps.setStatus('mandatory')
wfmpcStatRxMpoaImpReplyUnspecifiedOther = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 2, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfmpcStatRxMpoaImpReplyUnspecifiedOther.setStatus('mandatory')
wfmpcStatRxMpoaImpReplyOtherOther = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 2, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfmpcStatRxMpoaImpReplyOtherOther.setStatus('mandatory')
wfmpcStatRxMpoaEgressCachePurgeRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 2, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfmpcStatRxMpoaEgressCachePurgeRequests.setStatus('mandatory')
wfmpcStatTxMpoaEgressCachePurgeReplies = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 2, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfmpcStatTxMpoaEgressCachePurgeReplies.setStatus('mandatory')
wfmpcStatTxMpoaTriggers = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 2, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfmpcStatTxMpoaTriggers.setStatus('mandatory')
wfmpcStatSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14, 2, 1, 24), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfmpcStatSlot.setStatus('mandatory')
mibBuilder.exportSymbols("Wellfleet-WFMPC-MIB", wfmpcMsgNum=wfmpcMsgNum, wfmpcStatRxMpoaImpReplyUnsupportedInetProt=wfmpcStatRxMpoaImpReplyUnsupportedInetProt, wfmpcStatTxMpoaResolveReplyInsufSCResources=wfmpcStatTxMpoaResolveReplyInsufSCResources, wfmpcCIPNackFlag=wfmpcCIPNackFlag, wfmpcStatRxMpoaResolveRequests=wfmpcStatRxMpoaResolveRequests, wfmpcStatRxMpoaImpReplyUnsupportedMacEncaps=wfmpcStatRxMpoaImpReplyUnsupportedMacEncaps, wfmpcStatTxMpoaTriggers=wfmpcStatTxMpoaTriggers, wfmpcStatRxMpoaImpReplyInsufEitherResources=wfmpcStatRxMpoaImpReplyInsufEitherResources, wfmpcStatTxMpoaResolveReplyUnsupportedInetProt=wfmpcStatTxMpoaResolveReplyUnsupportedInetProt, wfmpcStatisticsEntry=wfmpcStatisticsEntry, wfmpcStatRxMpoaEgressCachePurgeRequests=wfmpcStatRxMpoaEgressCachePurgeRequests, wfmpcEntry=wfmpcEntry, wfmpcStatTxMpoaResolveReplyUnspecifiedOther=wfmpcStatTxMpoaResolveReplyUnspecifiedOther, wfmpcCct=wfmpcCct, wfmpcStatRxMpoaImpReplyOtherOther=wfmpcStatRxMpoaImpReplyOtherOther, wfmpcStatTxMpoaEgressCachePurgeReplies=wfmpcStatTxMpoaEgressCachePurgeReplies, wfmpcStatGiveupTimeExpireds=wfmpcStatGiveupTimeExpireds, wfmpcStatTxMpoaImpRequests=wfmpcStatTxMpoaImpRequests, wfmpcMsgSendEnable=wfmpcMsgSendEnable, wfmpcStatisticsTable=wfmpcStatisticsTable, wfmpcDelete=wfmpcDelete, wfmpcStatRxMpoaImpReplyAcks=wfmpcStatRxMpoaImpReplyAcks, wfmpcStatSlot=wfmpcStatSlot, wfmpcMPCAtmAddr=wfmpcMPCAtmAddr, wfmpcStatTxMpoaResolveReplyOtherOther=wfmpcStatTxMpoaResolveReplyOtherOther, wfmpcStatRxMpoaImpReplyInsufECResources=wfmpcStatRxMpoaImpReplyInsufECResources, wfmpcSetupVCtoMPS=wfmpcSetupVCtoMPS, wfmpcStatIndex=wfmpcStatIndex, wfmpcStatTxMpoaResolveReplyInsufECResources=wfmpcStatTxMpoaResolveReplyInsufECResources, wfmpcStatRxMpoaImpReplyUnspecifiedOther=wfmpcStatRxMpoaImpReplyUnspecifiedOther, wfmpcStatTxMpoaResolveReplyUnsupportedMacEncaps=wfmpcStatTxMpoaResolveReplyUnsupportedMacEncaps, wfmpcStatRxMpoaImpReplyInsufSCResources=wfmpcStatRxMpoaImpReplyInsufSCResources, wfmpcDisable=wfmpcDisable, wfmpcEntryTable=wfmpcEntryTable, wfmpcMPSAtmAddr=wfmpcMPSAtmAddr, wfmpcStatTxMpoaResolveReplyInsufEitherResources=wfmpcStatTxMpoaResolveReplyInsufEitherResources, wfmpcStatTxMpoaResolveReplyAcks=wfmpcStatTxMpoaResolveReplyAcks, wfmpcSlot=wfmpcSlot)
