#
# PySNMP MIB module RUCKUS-WLINK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RUCKUS-WLINK-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:59:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ruckusCommonWLINKModule, = mibBuilder.importSymbols("RUCKUS-ROOT-MIB", "ruckusCommonWLINKModule")
RuckusSSID, = mibBuilder.importSymbols("RUCKUS-TC-MIB", "RuckusSSID")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, MibIdentifier, ModuleIdentity, IpAddress, Integer32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Unsigned32, Bits, Counter32, Gauge32, TimeTicks, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "ModuleIdentity", "IpAddress", "Integer32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Unsigned32", "Bits", "Counter32", "Gauge32", "TimeTicks", "ObjectIdentity")
MacAddress, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TextualConvention", "DisplayString")
ruckusWLINKMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1))
if mibBuilder.loadTexts: ruckusWLINKMIB.setLastUpdated('201010150800Z')
if mibBuilder.loadTexts: ruckusWLINKMIB.setOrganization('Ruckus Wireless, Inc.')
if mibBuilder.loadTexts: ruckusWLINKMIB.setContactInfo('Ruckus Wireless, Inc. Postal: 880 W Maude Ave Sunnyvale, CA 94085 USA EMail: support@ruckuswireless.com Phone: +1-650-265-4200')
if mibBuilder.loadTexts: ruckusWLINKMIB.setDescription('Ruckus Wireless Link mib')
ruckusWLINKObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1))
ruckusWLINKInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1))
ruckusWLINKEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 2))
ruckusWLINKTable = MibTable((1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 1), )
if mibBuilder.loadTexts: ruckusWLINKTable.setStatus('current')
if mibBuilder.loadTexts: ruckusWLINKTable.setDescription('WLINK table.')
ruckusWLINKEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ruckusWLINKEntry.setStatus('current')
if mibBuilder.loadTexts: ruckusWLINKEntry.setDescription('Specifies each WLINK entry.')
ruckusWLINKSSID = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 1, 1, 1), RuckusSSID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusWLINKSSID.setStatus('current')
if mibBuilder.loadTexts: ruckusWLINKSSID.setDescription('Specifies the name of the SSID.')
ruckusWLINKRole = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("rootBridge", 1), ("nonRootBridge", 2), ("notDecided", 3), ("notAvailable", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusWLINKRole.setStatus('current')
if mibBuilder.loadTexts: ruckusWLINKRole.setDescription('Specifies the name of the SSID.')
ruckusWLINKLocalMAC = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 1, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusWLINKLocalMAC.setStatus('current')
if mibBuilder.loadTexts: ruckusWLINKLocalMAC.setDescription('It is the 48-bit MAC address of the wireless interface of local side.')
ruckusWLINKRemoteMAC = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 1, 1, 4), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusWLINKRemoteMAC.setStatus('current')
if mibBuilder.loadTexts: ruckusWLINKRemoteMAC.setDescription('It is the 48-bit MAC address of the wireless interface of remote side.')
ruckusWLINKTxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusWLINKTxPkts.setStatus('current')
if mibBuilder.loadTexts: ruckusWLINKTxPkts.setDescription('Number of tx packets.')
ruckusWLINKTxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusWLINKTxBytes.setStatus('current')
if mibBuilder.loadTexts: ruckusWLINKTxBytes.setDescription('Number of tx bytes.')
ruckusWLINKRxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusWLINKRxPkts.setStatus('current')
if mibBuilder.loadTexts: ruckusWLINKRxPkts.setDescription('Number of rx packets.')
ruckusWLINKRxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusWLINKRxBytes.setStatus('current')
if mibBuilder.loadTexts: ruckusWLINKRxBytes.setDescription('Number of rx bytes.')
ruckusWLINKEstablishTime = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 1, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusWLINKEstablishTime.setStatus('current')
if mibBuilder.loadTexts: ruckusWLINKEstablishTime.setDescription('The establish time of the link (UTC).')
ruckusWLINKUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 1, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusWLINKUpTime.setStatus('current')
if mibBuilder.loadTexts: ruckusWLINKUpTime.setDescription('The up time of the link in seconds.')
ruckusWLINKRssi = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusWLINKRssi.setStatus('current')
if mibBuilder.loadTexts: ruckusWLINKRssi.setDescription('Link RSSI.')
ruckusWLINKUpCount = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusWLINKUpCount.setStatus('current')
if mibBuilder.loadTexts: ruckusWLINKUpCount.setDescription('The link up count during its uptime.')
ruckusWLINKDownCount = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusWLINKDownCount.setStatus('current')
if mibBuilder.loadTexts: ruckusWLINKDownCount.setDescription('The link down count during its uptime.')
mibBuilder.exportSymbols("RUCKUS-WLINK-MIB", ruckusWLINKLocalMAC=ruckusWLINKLocalMAC, ruckusWLINKMIB=ruckusWLINKMIB, ruckusWLINKRole=ruckusWLINKRole, ruckusWLINKRxPkts=ruckusWLINKRxPkts, ruckusWLINKEntry=ruckusWLINKEntry, ruckusWLINKTable=ruckusWLINKTable, ruckusWLINKTxPkts=ruckusWLINKTxPkts, ruckusWLINKDownCount=ruckusWLINKDownCount, ruckusWLINKRssi=ruckusWLINKRssi, ruckusWLINKTxBytes=ruckusWLINKTxBytes, ruckusWLINKUpCount=ruckusWLINKUpCount, ruckusWLINKEvents=ruckusWLINKEvents, ruckusWLINKRxBytes=ruckusWLINKRxBytes, ruckusWLINKEstablishTime=ruckusWLINKEstablishTime, ruckusWLINKUpTime=ruckusWLINKUpTime, ruckusWLINKObjects=ruckusWLINKObjects, PYSNMP_MODULE_ID=ruckusWLINKMIB, ruckusWLINKRemoteMAC=ruckusWLINKRemoteMAC, ruckusWLINKSSID=ruckusWLINKSSID, ruckusWLINKInfo=ruckusWLINKInfo)
