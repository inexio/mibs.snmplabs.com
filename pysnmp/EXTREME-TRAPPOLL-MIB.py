#
# PySNMP MIB module EXTREME-TRAPPOLL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EXTREME-BASE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:53:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
extremeAgent, = mibBuilder.importSymbols("EXTREME-BASE-MIB", "extremeAgent")
trapDestIndex, = mibBuilder.importSymbols("RMON2-MIB", "trapDestIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, iso, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Bits, MibIdentifier, ModuleIdentity, Counter64, Counter32, NotificationType, Integer32, IpAddress, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "iso", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Bits", "MibIdentifier", "ModuleIdentity", "Counter64", "Counter32", "NotificationType", "Integer32", "IpAddress", "TimeTicks")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
extremeTrapPoll = ModuleIdentity((1, 3, 6, 1, 4, 1, 1916, 1, 6))
if mibBuilder.loadTexts: extremeTrapPoll.setLastUpdated('9801090000Z')
if mibBuilder.loadTexts: extremeTrapPoll.setOrganization('Extreme Networks, Inc.')
extremeSmartTrapRulesTable = MibTable((1, 3, 6, 1, 4, 1, 1916, 1, 6, 1), )
if mibBuilder.loadTexts: extremeSmartTrapRulesTable.setStatus('current')
extremeSmartTrapRulesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1916, 1, 6, 1, 1), ).setIndexNames((0, "EXTREME-TRAPPOLL-MIB", "extremeSmartTrapRulesIndex"))
if mibBuilder.loadTexts: extremeSmartTrapRulesEntry.setStatus('current')
extremeSmartTrapRulesIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 6, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeSmartTrapRulesIndex.setStatus('current')
extremeSmartTrapRulesRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 6, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: extremeSmartTrapRulesRowStatus.setStatus('current')
extremeSmartTrapRulesDesiredOID = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 6, 1, 1, 3), ObjectIdentifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: extremeSmartTrapRulesDesiredOID.setStatus('current')
extremeSmartTrapRulesSupportedOID = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 6, 1, 1, 4), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeSmartTrapRulesSupportedOID.setStatus('current')
extremeSmartTrapRulesOperation = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 6, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("add", 1), ("delete", 2), ("modify", 3), ("any", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: extremeSmartTrapRulesOperation.setStatus('current')
extremeSmartTrapRulesTrapDestIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 6, 1, 1, 6), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: extremeSmartTrapRulesTrapDestIndex.setStatus('current')
extremeSmartTrapInstanceTable = MibTable((1, 3, 6, 1, 4, 1, 1916, 1, 6, 2), )
if mibBuilder.loadTexts: extremeSmartTrapInstanceTable.setStatus('current')
extremeSmartTrapInstanceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1916, 1, 6, 2, 1), ).setIndexNames((0, "RMON2-MIB", "trapDestIndex"), (0, "EXTREME-TRAPPOLL-MIB", "extremeSmartTrapInstanceSubindex"))
if mibBuilder.loadTexts: extremeSmartTrapInstanceEntry.setStatus('current')
extremeSmartTrapInstanceSubindex = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 6, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeSmartTrapInstanceSubindex.setStatus('current')
extremeSmartTrapInstanceRule = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 6, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeSmartTrapInstanceRule.setStatus('current')
extremeSmartTrapInstanceChangedOid = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 6, 2, 1, 3), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeSmartTrapInstanceChangedOid.setStatus('current')
extremeSmartTrapInstanceActualOperation = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 6, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("add", 1), ("delete", 2), ("modify", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeSmartTrapInstanceActualOperation.setStatus('current')
extremeSmartTrapInstanceChangeTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 6, 2, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeSmartTrapInstanceChangeTime.setStatus('current')
extremeSmartTrapFlushInstanceTableIndex = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 6, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extremeSmartTrapFlushInstanceTableIndex.setStatus('current')
mibBuilder.exportSymbols("EXTREME-TRAPPOLL-MIB", extremeSmartTrapRulesEntry=extremeSmartTrapRulesEntry, extremeSmartTrapRulesRowStatus=extremeSmartTrapRulesRowStatus, extremeSmartTrapInstanceTable=extremeSmartTrapInstanceTable, extremeSmartTrapRulesSupportedOID=extremeSmartTrapRulesSupportedOID, extremeSmartTrapInstanceRule=extremeSmartTrapInstanceRule, PYSNMP_MODULE_ID=extremeTrapPoll, extremeSmartTrapInstanceSubindex=extremeSmartTrapInstanceSubindex, extremeSmartTrapInstanceEntry=extremeSmartTrapInstanceEntry, extremeSmartTrapInstanceChangedOid=extremeSmartTrapInstanceChangedOid, extremeSmartTrapRulesOperation=extremeSmartTrapRulesOperation, extremeSmartTrapRulesTable=extremeSmartTrapRulesTable, extremeSmartTrapInstanceChangeTime=extremeSmartTrapInstanceChangeTime, extremeSmartTrapFlushInstanceTableIndex=extremeSmartTrapFlushInstanceTableIndex, extremeTrapPoll=extremeTrapPoll, extremeSmartTrapRulesDesiredOID=extremeSmartTrapRulesDesiredOID, extremeSmartTrapRulesIndex=extremeSmartTrapRulesIndex, extremeSmartTrapInstanceActualOperation=extremeSmartTrapInstanceActualOperation, extremeSmartTrapRulesTrapDestIndex=extremeSmartTrapRulesTrapDestIndex)
