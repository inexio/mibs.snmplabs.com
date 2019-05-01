#
# PySNMP MIB module RUCKUS-ETH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RUCKUS-ETH-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:58:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
ruckusCommonEthModule, = mibBuilder.importSymbols("RUCKUS-ROOT-MIB", "ruckusCommonEthModule")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Counter32, Unsigned32, ObjectIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, NotificationType, iso, Bits, MibIdentifier, Counter64, ModuleIdentity, Integer32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Unsigned32", "ObjectIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "NotificationType", "iso", "Bits", "MibIdentifier", "Counter64", "ModuleIdentity", "Integer32", "Gauge32")
MacAddress, TextualConvention, DisplayString, TruthValue, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TextualConvention", "DisplayString", "TruthValue", "RowStatus")
ruckusEthMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 25053, 1, 1, 13, 1))
if mibBuilder.loadTexts: ruckusEthMIB.setLastUpdated('201010150800Z')
if mibBuilder.loadTexts: ruckusEthMIB.setOrganization('Ruckus Wireless, Inc.')
if mibBuilder.loadTexts: ruckusEthMIB.setContactInfo('Ruckus Wireless, Inc. Postal: 880 W Maude Ave Sunnyvale, CA 94085 USA EMail: support@ruckuswireless.com Phone: +1-650-265-4200')
if mibBuilder.loadTexts: ruckusEthMIB.setDescription('Ruckus Eth mib')
ruckusEthObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 13, 1, 1))
ruckusEthInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 13, 1, 1, 1))
ruckusEthEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 13, 1, 2))
ruckusEthStatsTable = MibTable((1, 3, 6, 1, 4, 1, 25053, 1, 1, 13, 1, 1, 1, 1), )
if mibBuilder.loadTexts: ruckusEthStatsTable.setStatus('current')
if mibBuilder.loadTexts: ruckusEthStatsTable.setDescription('Eth statistics table')
ruckusEthStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25053, 1, 1, 13, 1, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ruckusEthStatsEntry.setStatus('current')
if mibBuilder.loadTexts: ruckusEthStatsEntry.setDescription('Specifies each Eth statictics entry.')
ruckusEthName = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 13, 1, 1, 1, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusEthName.setStatus('current')
if mibBuilder.loadTexts: ruckusEthName.setDescription('Specifies the name of the eth interface.')
ruckusEthStatsRxRate = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 13, 1, 1, 1, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusEthStatsRxRate.setStatus('current')
if mibBuilder.loadTexts: ruckusEthStatsRxRate.setDescription('Receipt throughput.')
ruckusEthStatsRxErrorRate = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 13, 1, 1, 1, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusEthStatsRxErrorRate.setStatus('current')
if mibBuilder.loadTexts: ruckusEthStatsRxErrorRate.setDescription('Receipt packet error rate.')
ruckusEthStatsTxRate = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 13, 1, 1, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusEthStatsTxRate.setStatus('current')
if mibBuilder.loadTexts: ruckusEthStatsTxRate.setDescription('Transmit throughput.')
ruckusEthStatsTxErrorRate = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 13, 1, 1, 1, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusEthStatsTxErrorRate.setStatus('current')
if mibBuilder.loadTexts: ruckusEthStatsTxErrorRate.setDescription('Transmit packet error rate.')
mibBuilder.exportSymbols("RUCKUS-ETH-MIB", ruckusEthObjects=ruckusEthObjects, ruckusEthMIB=ruckusEthMIB, ruckusEthStatsRxRate=ruckusEthStatsRxRate, PYSNMP_MODULE_ID=ruckusEthMIB, ruckusEthEvents=ruckusEthEvents, ruckusEthStatsEntry=ruckusEthStatsEntry, ruckusEthStatsTxRate=ruckusEthStatsTxRate, ruckusEthInfo=ruckusEthInfo, ruckusEthStatsTable=ruckusEthStatsTable, ruckusEthName=ruckusEthName, ruckusEthStatsTxErrorRate=ruckusEthStatsTxErrorRate, ruckusEthStatsRxErrorRate=ruckusEthStatsRxErrorRate)
