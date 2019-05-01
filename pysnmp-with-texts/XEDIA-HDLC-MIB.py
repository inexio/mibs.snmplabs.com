#
# PySNMP MIB module XEDIA-HDLC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/XEDIA-HDLC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:42:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter32, MibIdentifier, IpAddress, Integer32, ModuleIdentity, ObjectIdentity, iso, Bits, Gauge32, NotificationType, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter32", "MibIdentifier", "IpAddress", "Integer32", "ModuleIdentity", "ObjectIdentity", "iso", "Bits", "Gauge32", "NotificationType", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
xediaMibs, = mibBuilder.importSymbols("XEDIA-REG", "xediaMibs")
xediaHdlcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 838, 3, 7))
if mibBuilder.loadTexts: xediaHdlcMIB.setLastUpdated('9703252155Z')
if mibBuilder.loadTexts: xediaHdlcMIB.setOrganization('Xedia Corp.')
if mibBuilder.loadTexts: xediaHdlcMIB.setContactInfo('support@xedia.com')
if mibBuilder.loadTexts: xediaHdlcMIB.setDescription("This module defines proprietary objects that extend those in IETF's the Ethernet-Like Interface MIB.")
xhdlcObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 7, 1))
xhdlcConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 7, 2))
xhdlcStatsTable = MibTable((1, 3, 6, 1, 4, 1, 838, 3, 7, 1, 1), )
if mibBuilder.loadTexts: xhdlcStatsTable.setStatus('current')
if mibBuilder.loadTexts: xhdlcStatsTable.setDescription('Additional Xedia proprietary statistics for hdlc-like interfaces.')
xhdlcStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 838, 3, 7, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: xhdlcStatsEntry.setStatus('current')
if mibBuilder.loadTexts: xhdlcStatsEntry.setDescription('Additional Xedia proprietary statistics for single hdlc-like interface.')
xhdlcStatsOutErrorUnderFlows = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 7, 1, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xhdlcStatsOutErrorUnderFlows.setStatus('current')
if mibBuilder.loadTexts: xhdlcStatsOutErrorUnderFlows.setDescription('A count of TX Errorunderflows on a particular interface.')
xhdlcStatsInAborts = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 7, 1, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xhdlcStatsInAborts.setStatus('current')
if mibBuilder.loadTexts: xhdlcStatsInAborts.setDescription('A count of RX Aborts on a particular interface.')
xhdlcStatsInResidualBits = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 7, 1, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xhdlcStatsInResidualBits.setStatus('current')
if mibBuilder.loadTexts: xhdlcStatsInResidualBits.setDescription('The count of residual bit errors.')
xhdlcStatsInInvalidLen = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 7, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xhdlcStatsInInvalidLen.setStatus('current')
if mibBuilder.loadTexts: xhdlcStatsInInvalidLen.setDescription('A count of RX invalid lengths on a particular interface.')
xhdlcStatsInOverrun = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 7, 1, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xhdlcStatsInOverrun.setStatus('current')
if mibBuilder.loadTexts: xhdlcStatsInOverrun.setDescription('A count of RX Overruns on a particular interface.')
xhdlcConfigTable = MibTable((1, 3, 6, 1, 4, 1, 838, 3, 7, 1, 2), )
if mibBuilder.loadTexts: xhdlcConfigTable.setStatus('current')
if mibBuilder.loadTexts: xhdlcConfigTable.setDescription('Xedia proprietary configuration parameters for hdlc-like interfaces.')
xhdlcConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 838, 3, 7, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: xhdlcConfigEntry.setStatus('current')
if mibBuilder.loadTexts: xhdlcConfigEntry.setDescription('Xedia proprietary configuration parameters for single hdlc-like interface.')
xhdlcConfigClocking = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 7, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("internal", 1), ("external", 2), ("loopback", 3))).clone('external')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xhdlcConfigClocking.setStatus('current')
if mibBuilder.loadTexts: xhdlcConfigClocking.setDescription('The configured clocking of the interface.')
xhdlcConfigCrcMode = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 7, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("crc16", 1), ("crc32", 2), ("crcnone", 3))).clone('crc16')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xhdlcConfigCrcMode.setStatus('current')
if mibBuilder.loadTexts: xhdlcConfigCrcMode.setDescription('The configured CRC mode of the interface.')
xhdlcCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 7, 2, 1))
xhdlcGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 7, 2, 2))
xhdlcCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 838, 3, 7, 2, 1, 1)).setObjects(("XEDIA-HDLC-MIB", "xhdlcGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    xhdlcCompliance = xhdlcCompliance.setStatus('current')
if mibBuilder.loadTexts: xhdlcCompliance.setDescription('The compliance statement for all agents that support this MIB. A compliant agent implements all objects defined in this MIB.')
xhdlcGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 838, 3, 7, 2, 2, 1)).setObjects(("XEDIA-HDLC-MIB", "xhdlcStatsOutErrorUnderFlows"), ("XEDIA-HDLC-MIB", "xhdlcStatsInAborts"), ("XEDIA-HDLC-MIB", "xhdlcStatsInResidualBits"), ("XEDIA-HDLC-MIB", "xhdlcStatsInInvalidLen"), ("XEDIA-HDLC-MIB", "xhdlcStatsInOverrun"), ("XEDIA-HDLC-MIB", "xhdlcConfigClocking"), ("XEDIA-HDLC-MIB", "xhdlcConfigCrcMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    xhdlcGroup = xhdlcGroup.setStatus('current')
if mibBuilder.loadTexts: xhdlcGroup.setDescription('The set of all accessible objects in this MIB.')
mibBuilder.exportSymbols("XEDIA-HDLC-MIB", xhdlcConfigClocking=xhdlcConfigClocking, xhdlcStatsOutErrorUnderFlows=xhdlcStatsOutErrorUnderFlows, xhdlcStatsInAborts=xhdlcStatsInAborts, xhdlcConformance=xhdlcConformance, xhdlcStatsInResidualBits=xhdlcStatsInResidualBits, xhdlcConfigEntry=xhdlcConfigEntry, xhdlcConfigCrcMode=xhdlcConfigCrcMode, xhdlcConfigTable=xhdlcConfigTable, xediaHdlcMIB=xediaHdlcMIB, xhdlcStatsEntry=xhdlcStatsEntry, xhdlcObjects=xhdlcObjects, xhdlcGroup=xhdlcGroup, xhdlcStatsInInvalidLen=xhdlcStatsInInvalidLen, xhdlcStatsTable=xhdlcStatsTable, xhdlcStatsInOverrun=xhdlcStatsInOverrun, xhdlcGroups=xhdlcGroups, xhdlcCompliances=xhdlcCompliances, PYSNMP_MODULE_ID=xediaHdlcMIB, xhdlcCompliance=xhdlcCompliance)
