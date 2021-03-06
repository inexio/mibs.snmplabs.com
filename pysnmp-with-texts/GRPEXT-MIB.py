#
# PySNMP MIB module GRPEXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/GRPEXT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:19:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
grpExt, = mibBuilder.importSymbols("APENT-MIB", "grpExt")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, ObjectIdentity, MibIdentifier, Unsigned32, TimeTicks, Bits, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, Integer32, Gauge32, iso, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ObjectIdentity", "MibIdentifier", "Unsigned32", "TimeTicks", "Bits", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "Integer32", "Gauge32", "iso", "ModuleIdentity")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
apGrpExtMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2467, 1, 17, 1))
if mibBuilder.loadTexts: apGrpExtMib.setLastUpdated('9710092000Z')
if mibBuilder.loadTexts: apGrpExtMib.setOrganization('ArrowPoint Communications Inc.')
if mibBuilder.loadTexts: apGrpExtMib.setContactInfo(' Postal: ArrowPoint Communications Inc. 50 Nagog Park Acton, Massachusetts 01720 Tel: +1 978-206-3000 option 1 E-Mail: support@arrowpoint.com')
if mibBuilder.loadTexts: apGrpExtMib.setDescription('The MIB module used to describe the ArrowPoint Communications content rule table')
apGrpTable = MibTable((1, 3, 6, 1, 4, 1, 2467, 1, 17, 2), )
if mibBuilder.loadTexts: apGrpTable.setStatus('current')
if mibBuilder.loadTexts: apGrpTable.setDescription('A list of content rule entries.')
apGrpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2467, 1, 17, 2, 1), ).setIndexNames((0, "GRPEXT-MIB", "apGrpName"))
if mibBuilder.loadTexts: apGrpEntry.setStatus('current')
if mibBuilder.loadTexts: apGrpEntry.setDescription('A group of information to uniquely identify a content providing service.')
apGrpName = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 17, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apGrpName.setStatus('current')
if mibBuilder.loadTexts: apGrpName.setDescription('The name of the content providing service.')
apGrpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 17, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apGrpIndex.setStatus('current')
if mibBuilder.loadTexts: apGrpIndex.setDescription('The unique service index assigned to the name by the SCM.')
apGrpIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 17, 2, 1, 3), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apGrpIPAddress.setStatus('current')
if mibBuilder.loadTexts: apGrpIPAddress.setDescription('The IP Address the of the content providing service.')
apGrpIPProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 17, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(6, 17))).clone(namedValues=NamedValues(("tcp", 6), ("udp", 17))).clone('tcp')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apGrpIPProtocol.setStatus('current')
if mibBuilder.loadTexts: apGrpIPProtocol.setDescription('The IP Protocol the of the content providing service.')
apGrpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 17, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apGrpPort.setStatus('current')
if mibBuilder.loadTexts: apGrpPort.setDescription('The UDP or TCP port of the content providing service.')
apGrpEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 17, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1))).clone('disable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apGrpEnable.setStatus('current')
if mibBuilder.loadTexts: apGrpEnable.setDescription('The state of the group, either enable or disabled')
apGrpStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 17, 2, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apGrpStatus.setStatus('current')
if mibBuilder.loadTexts: apGrpStatus.setDescription('Status entry for this row ')
apPortMapCrateBasePort = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 17, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(8192, 65530)).clone(8192)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apPortMapCrateBasePort.setStatus('current')
if mibBuilder.loadTexts: apPortMapCrateBasePort.setDescription('The base port for the entire unit when mapping ports.')
apPortMapAvailPortsPerSfp = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 17, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10000)).clone(1024)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apPortMapAvailPortsPerSfp.setStatus('current')
if mibBuilder.loadTexts: apPortMapAvailPortsPerSfp.setDescription('The number of ports to allow per SFP when mapping ports.')
apGrpHitCount = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 17, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apGrpHitCount.setStatus('current')
if mibBuilder.loadTexts: apGrpHitCount.setDescription('Number of times the group has been used.')
apGrpByteCount = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 17, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apGrpByteCount.setStatus('current')
if mibBuilder.loadTexts: apGrpByteCount.setDescription('Number of Bytes passed through the group.')
apGrpFrameCount = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 17, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apGrpFrameCount.setStatus('current')
if mibBuilder.loadTexts: apGrpFrameCount.setDescription('Number of frames passed through the group.')
apGrpCurConnections = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 17, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apGrpCurConnections.setStatus('current')
if mibBuilder.loadTexts: apGrpCurConnections.setDescription('Number of current connections through the group.')
apGrpTotConnections = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 17, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apGrpTotConnections.setStatus('current')
if mibBuilder.loadTexts: apGrpTotConnections.setDescription('Total number of connections through the group.')
apGrpCurFTPControl = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 17, 2, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apGrpCurFTPControl.setStatus('current')
if mibBuilder.loadTexts: apGrpCurFTPControl.setDescription('Number of current FTP control connections through the group.')
apGrpTotFTPControl = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 17, 2, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apGrpTotFTPControl.setStatus('current')
if mibBuilder.loadTexts: apGrpTotFTPControl.setDescription('Total number of FTP control connections through the group.')
mibBuilder.exportSymbols("GRPEXT-MIB", apGrpFrameCount=apGrpFrameCount, apGrpIndex=apGrpIndex, apGrpCurConnections=apGrpCurConnections, apGrpTable=apGrpTable, apGrpIPAddress=apGrpIPAddress, apGrpCurFTPControl=apGrpCurFTPControl, apGrpHitCount=apGrpHitCount, apGrpStatus=apGrpStatus, apGrpPort=apGrpPort, apGrpTotConnections=apGrpTotConnections, apGrpByteCount=apGrpByteCount, apGrpEntry=apGrpEntry, apGrpEnable=apGrpEnable, PYSNMP_MODULE_ID=apGrpExtMib, apGrpIPProtocol=apGrpIPProtocol, apGrpTotFTPControl=apGrpTotFTPControl, apPortMapAvailPortsPerSfp=apPortMapAvailPortsPerSfp, apPortMapCrateBasePort=apPortMapCrateBasePort, apGrpExtMib=apGrpExtMib, apGrpName=apGrpName)
