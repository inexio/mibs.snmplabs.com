#
# PySNMP MIB module LIGO-W-JET-MIMO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/LIGO-W-JET-MIMO-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:56:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ligoMgmt, = mibBuilder.importSymbols("LIGOWAVE-MIB", "ligoMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, iso, MibIdentifier, TimeTicks, Gauge32, ObjectIdentity, Unsigned32, IpAddress, Counter64, Integer32, Counter32, ModuleIdentity, NotificationType, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "MibIdentifier", "TimeTicks", "Gauge32", "ObjectIdentity", "Unsigned32", "IpAddress", "Counter64", "Integer32", "Counter32", "ModuleIdentity", "NotificationType", "Bits")
TextualConvention, MacAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "MacAddress", "DisplayString")
ligoWJetMimoMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 32750, 3, 9))
ligoWJetMimoMIB.setRevisions(('2010-03-22 00:00',))
if mibBuilder.loadTexts: ligoWJetMimoMIB.setLastUpdated('201003220000Z')
if mibBuilder.loadTexts: ligoWJetMimoMIB.setOrganization('LigoWave')
ligoWJetMimoMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 32750, 3, 9, 1))
ligoWJetMimoNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 32750, 3, 9, 1, 0))
ligoWJetMimoInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 32750, 3, 9, 1, 1))
ligoWJetMimoConf = MibIdentifier((1, 3, 6, 1, 4, 1, 32750, 3, 9, 1, 2))
ligoWJetMimoStats = MibIdentifier((1, 3, 6, 1, 4, 1, 32750, 3, 9, 1, 3))
wJetMimoStatsTable = MibTable((1, 3, 6, 1, 4, 1, 32750, 3, 9, 1, 3, 1), )
if mibBuilder.loadTexts: wJetMimoStatsTable.setStatus('current')
wJetMimoStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 32750, 3, 9, 1, 3, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "LIGO-W-JET-MIMO-MIB", "wJetMimoPeerIndex"))
if mibBuilder.loadTexts: wJetMimoStatsEntry.setStatus('current')
wJetMimoPeerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 9, 1, 3, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: wJetMimoPeerIndex.setStatus('current')
wJetMimoMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 9, 1, 3, 1, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wJetMimoMacAddress.setStatus('current')
wJetMimoTxTokens = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 9, 1, 3, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wJetMimoTxTokens.setStatus('current')
wJetMimoRxTokens = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 9, 1, 3, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wJetMimoRxTokens.setStatus('current')
wJetMimoDupTokens = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 9, 1, 3, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wJetMimoDupTokens.setStatus('current')
wJetMimoLostTokens = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 9, 1, 3, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wJetMimoLostTokens.setStatus('current')
wJetMimoDroppedTokens = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 9, 1, 3, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wJetMimoDroppedTokens.setStatus('current')
wJetMimoTxFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 9, 1, 3, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wJetMimoTxFailures.setStatus('current')
wJetMimoReinjectedTokens = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 9, 1, 3, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wJetMimoReinjectedTokens.setStatus('current')
mibBuilder.exportSymbols("LIGO-W-JET-MIMO-MIB", wJetMimoTxFailures=wJetMimoTxFailures, wJetMimoStatsTable=wJetMimoStatsTable, wJetMimoMacAddress=wJetMimoMacAddress, ligoWJetMimoConf=ligoWJetMimoConf, wJetMimoPeerIndex=wJetMimoPeerIndex, ligoWJetMimoMIBObjects=ligoWJetMimoMIBObjects, wJetMimoRxTokens=wJetMimoRxTokens, wJetMimoReinjectedTokens=wJetMimoReinjectedTokens, wJetMimoDupTokens=wJetMimoDupTokens, ligoWJetMimoMIB=ligoWJetMimoMIB, wJetMimoTxTokens=wJetMimoTxTokens, wJetMimoDroppedTokens=wJetMimoDroppedTokens, ligoWJetMimoNotifs=ligoWJetMimoNotifs, wJetMimoLostTokens=wJetMimoLostTokens, wJetMimoStatsEntry=wJetMimoStatsEntry, ligoWJetMimoStats=ligoWJetMimoStats, ligoWJetMimoInfo=ligoWJetMimoInfo, PYSNMP_MODULE_ID=ligoWJetMimoMIB)
