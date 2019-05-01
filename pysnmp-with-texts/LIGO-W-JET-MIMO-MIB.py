#
# PySNMP MIB module LIGO-W-JET-MIMO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/LIGO-W-JET-MIMO-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:07:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ligoMgmt, = mibBuilder.importSymbols("LIGOWAVE-MIB", "ligoMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Counter64, Counter32, Integer32, Gauge32, Unsigned32, Bits, ModuleIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, MibIdentifier, ObjectIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter64", "Counter32", "Integer32", "Gauge32", "Unsigned32", "Bits", "ModuleIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "MibIdentifier", "ObjectIdentity", "TimeTicks")
TextualConvention, MacAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "MacAddress", "DisplayString")
ligoWJetMimoMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 32750, 3, 9))
ligoWJetMimoMIB.setRevisions(('2010-03-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ligoWJetMimoMIB.setRevisionsDescriptions(('First revision.',))
if mibBuilder.loadTexts: ligoWJetMimoMIB.setLastUpdated('201003220000Z')
if mibBuilder.loadTexts: ligoWJetMimoMIB.setOrganization('LigoWave')
if mibBuilder.loadTexts: ligoWJetMimoMIB.setContactInfo(' LigoWave Customer Support E-mail: support@ligowave.com')
if mibBuilder.loadTexts: ligoWJetMimoMIB.setDescription('The LigoWave W-Jet MIMO Protocol MIB.')
ligoWJetMimoMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 32750, 3, 9, 1))
ligoWJetMimoNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 32750, 3, 9, 1, 0))
ligoWJetMimoInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 32750, 3, 9, 1, 1))
ligoWJetMimoConf = MibIdentifier((1, 3, 6, 1, 4, 1, 32750, 3, 9, 1, 2))
ligoWJetMimoStats = MibIdentifier((1, 3, 6, 1, 4, 1, 32750, 3, 9, 1, 3))
wJetMimoStatsTable = MibTable((1, 3, 6, 1, 4, 1, 32750, 3, 9, 1, 3, 1), )
if mibBuilder.loadTexts: wJetMimoStatsTable.setStatus('current')
if mibBuilder.loadTexts: wJetMimoStatsTable.setDescription('W-Jet MIMO protocol statistics table.')
wJetMimoStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 32750, 3, 9, 1, 3, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "LIGO-W-JET-MIMO-MIB", "wJetMimoPeerIndex"))
if mibBuilder.loadTexts: wJetMimoStatsEntry.setStatus('current')
if mibBuilder.loadTexts: wJetMimoStatsEntry.setDescription('W-Jet MIMO protocol statistics table entry.')
wJetMimoPeerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 9, 1, 3, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: wJetMimoPeerIndex.setStatus('current')
if mibBuilder.loadTexts: wJetMimoPeerIndex.setDescription('Peer index. Local device has index 0.')
wJetMimoMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 9, 1, 3, 1, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wJetMimoMacAddress.setStatus('current')
if mibBuilder.loadTexts: wJetMimoMacAddress.setDescription('Peer MAC address.')
wJetMimoTxTokens = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 9, 1, 3, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wJetMimoTxTokens.setStatus('current')
if mibBuilder.loadTexts: wJetMimoTxTokens.setDescription('Number of transmitted tokens.')
wJetMimoRxTokens = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 9, 1, 3, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wJetMimoRxTokens.setStatus('current')
if mibBuilder.loadTexts: wJetMimoRxTokens.setDescription('Number of received tokens.')
wJetMimoDupTokens = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 9, 1, 3, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wJetMimoDupTokens.setStatus('current')
if mibBuilder.loadTexts: wJetMimoDupTokens.setDescription('Number of duplicate tokens.')
wJetMimoLostTokens = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 9, 1, 3, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wJetMimoLostTokens.setStatus('current')
if mibBuilder.loadTexts: wJetMimoLostTokens.setDescription('Number of lost tokens.')
wJetMimoDroppedTokens = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 9, 1, 3, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wJetMimoDroppedTokens.setStatus('current')
if mibBuilder.loadTexts: wJetMimoDroppedTokens.setDescription('Number of dropped tokens.')
wJetMimoTxFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 9, 1, 3, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wJetMimoTxFailures.setStatus('current')
if mibBuilder.loadTexts: wJetMimoTxFailures.setDescription('Number of token transmissions failures.')
wJetMimoReinjectedTokens = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 9, 1, 3, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wJetMimoReinjectedTokens.setStatus('current')
if mibBuilder.loadTexts: wJetMimoReinjectedTokens.setDescription('Number of reinjected tokens.')
mibBuilder.exportSymbols("LIGO-W-JET-MIMO-MIB", ligoWJetMimoInfo=ligoWJetMimoInfo, wJetMimoStatsTable=wJetMimoStatsTable, wJetMimoMacAddress=wJetMimoMacAddress, wJetMimoDroppedTokens=wJetMimoDroppedTokens, wJetMimoTxFailures=wJetMimoTxFailures, wJetMimoReinjectedTokens=wJetMimoReinjectedTokens, wJetMimoRxTokens=wJetMimoRxTokens, wJetMimoLostTokens=wJetMimoLostTokens, ligoWJetMimoStats=ligoWJetMimoStats, ligoWJetMimoConf=ligoWJetMimoConf, wJetMimoDupTokens=wJetMimoDupTokens, PYSNMP_MODULE_ID=ligoWJetMimoMIB, wJetMimoStatsEntry=wJetMimoStatsEntry, ligoWJetMimoMIB=ligoWJetMimoMIB, wJetMimoPeerIndex=wJetMimoPeerIndex, wJetMimoTxTokens=wJetMimoTxTokens, ligoWJetMimoMIBObjects=ligoWJetMimoMIBObjects, ligoWJetMimoNotifs=ligoWJetMimoNotifs)
