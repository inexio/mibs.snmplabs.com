#
# PySNMP MIB module CISCO-DMN-DSG-PROTOCOLS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DMN-DSG-PROTOCOLS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:37:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
ciscoDSGUtilities, = mibBuilder.importSymbols("CISCO-DMN-DSG-ROOT-MIB", "ciscoDSGUtilities")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, NotificationType, ObjectIdentity, Bits, Counter64, MibIdentifier, iso, Gauge32, IpAddress, Unsigned32, TimeTicks, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "NotificationType", "ObjectIdentity", "Bits", "Counter64", "MibIdentifier", "iso", "Gauge32", "IpAddress", "Unsigned32", "TimeTicks", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoDSGProtocols = ModuleIdentity((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 39))
ciscoDSGProtocols.setRevisions(('2013-07-10 19:03', '2012-03-07 07:30',))
if mibBuilder.loadTexts: ciscoDSGProtocols.setLastUpdated('201307101903Z')
if mibBuilder.loadTexts: ciscoDSGProtocols.setOrganization('Cisco Systems, Inc.')
protocolsCtrlTelnet = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 39, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: protocolsCtrlTelnet.setStatus('current')
protocolsCtrlSSH = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 39, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: protocolsCtrlSSH.setStatus('current')
protocolsCtrlHTTP = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 39, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2), ("secure", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: protocolsCtrlHTTP.setStatus('current')
protocolsCtrlSNMP = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 39, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: protocolsCtrlSNMP.setStatus('current')
protocolsCtrlRIP = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 39, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: protocolsCtrlRIP.setStatus('current')
protocolsCtrlMPE = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 39, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("fwdNone", 1), ("fwdAll", 2), ("fwdFiltered", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: protocolsCtrlMPE.setStatus('current')
protocolsCtrlIGMP = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 39, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disable", 1), ("v3", 2), ("v2", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: protocolsCtrlIGMP.setStatus('current')
protocolslTimeoutsIdleSessonGlobal = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 39, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1209600))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: protocolslTimeoutsIdleSessonGlobal.setStatus('current')
protocolsCtrlSyslog = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 39, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("disable", 1), ("legacy", 2), ("syslogTcp", 3), ("syslogUdp", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: protocolsCtrlSyslog.setStatus('current')
protocolsCtrlSyslogCfgIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 39, 11), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: protocolsCtrlSyslogCfgIpAddr.setStatus('current')
protocolsCtrlSyslogCfgPort = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 39, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: protocolsCtrlSyslogCfgPort.setStatus('current')
mibBuilder.exportSymbols("CISCO-DMN-DSG-PROTOCOLS-MIB", protocolsCtrlMPE=protocolsCtrlMPE, PYSNMP_MODULE_ID=ciscoDSGProtocols, ciscoDSGProtocols=ciscoDSGProtocols, protocolsCtrlHTTP=protocolsCtrlHTTP, protocolsCtrlSSH=protocolsCtrlSSH, protocolsCtrlSyslog=protocolsCtrlSyslog, protocolsCtrlRIP=protocolsCtrlRIP, protocolslTimeoutsIdleSessonGlobal=protocolslTimeoutsIdleSessonGlobal, protocolsCtrlSyslogCfgIpAddr=protocolsCtrlSyslogCfgIpAddr, protocolsCtrlSyslogCfgPort=protocolsCtrlSyslogCfgPort, protocolsCtrlTelnet=protocolsCtrlTelnet, protocolsCtrlIGMP=protocolsCtrlIGMP, protocolsCtrlSNMP=protocolsCtrlSNMP)