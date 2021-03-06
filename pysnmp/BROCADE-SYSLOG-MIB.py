#
# PySNMP MIB module BROCADE-SYSLOG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BROCADE-SYSLOG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:24:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
brcdSysLog, = mibBuilder.importSymbols("FOUNDRY-SN-ROOT-MIB", "brcdSysLog")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Gauge32, Counter32, Unsigned32, TimeTicks, Counter64, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, MibIdentifier, ObjectIdentity, NotificationType, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Gauge32", "Counter32", "Unsigned32", "TimeTicks", "Counter64", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "MibIdentifier", "ObjectIdentity", "NotificationType", "Bits")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
brocadeSysLogMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1991, 1, 1, 11, 1))
brocadeSysLogMIB.setRevisions(('2011-11-04 00:00',))
if mibBuilder.loadTexts: brocadeSysLogMIB.setLastUpdated('201111040000Z')
if mibBuilder.loadTexts: brocadeSysLogMIB.setOrganization('Brocade Communications Systems, Inc.')
brcdSysLogGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 1, 11, 1, 1))
brcdSysLogServerTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 1, 11, 1, 1, 1), )
if mibBuilder.loadTexts: brcdSysLogServerTable.setStatus('current')
brcdSysLogServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 1, 11, 1, 1, 1, 1), ).setIndexNames((0, "BROCADE-SYSLOG-MIB", "brcdSysLogServerAddrType"), (0, "BROCADE-SYSLOG-MIB", "brcdSysLogServerAddr"), (0, "BROCADE-SYSLOG-MIB", "brcdSysLogServerUDPPort"))
if mibBuilder.loadTexts: brcdSysLogServerEntry.setStatus('current')
brcdSysLogServerAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 11, 1, 1, 1, 1, 1), InetAddressType())
if mibBuilder.loadTexts: brcdSysLogServerAddrType.setStatus('current')
brcdSysLogServerAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 11, 1, 1, 1, 1, 2), InetAddress())
if mibBuilder.loadTexts: brcdSysLogServerAddr.setStatus('current')
brcdSysLogServerUDPPort = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 11, 1, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: brcdSysLogServerUDPPort.setStatus('current')
brcdSysLogServerOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 11, 1, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brcdSysLogServerOutPkts.setStatus('current')
brcdSysLogServerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 11, 1, 1, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: brcdSysLogServerRowStatus.setStatus('current')
mibBuilder.exportSymbols("BROCADE-SYSLOG-MIB", brcdSysLogServerAddrType=brcdSysLogServerAddrType, brocadeSysLogMIB=brocadeSysLogMIB, brcdSysLogServerUDPPort=brcdSysLogServerUDPPort, brcdSysLogServerRowStatus=brcdSysLogServerRowStatus, brcdSysLogGroup=brcdSysLogGroup, brcdSysLogServerAddr=brcdSysLogServerAddr, PYSNMP_MODULE_ID=brocadeSysLogMIB, brcdSysLogServerEntry=brcdSysLogServerEntry, brcdSysLogServerTable=brcdSysLogServerTable, brcdSysLogServerOutPkts=brcdSysLogServerOutPkts)
