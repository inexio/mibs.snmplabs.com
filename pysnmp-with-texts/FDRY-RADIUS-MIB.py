#
# PySNMP MIB module FDRY-RADIUS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FDRY-RADIUS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:13:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
fdryRadius, = mibBuilder.importSymbols("FOUNDRY-SN-ROOT-MIB", "fdryRadius")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, iso, ObjectIdentity, Unsigned32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Gauge32, Counter64, TimeTicks, Bits, Integer32, ModuleIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "iso", "ObjectIdentity", "Unsigned32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Gauge32", "Counter64", "TimeTicks", "Bits", "Integer32", "ModuleIdentity", "IpAddress")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
fdryRadiusMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1991, 1, 1, 8, 1))
fdryRadiusMIB.setRevisions(('2010-06-02 00:00', '2008-02-25 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: fdryRadiusMIB.setRevisionsDescriptions(('Changed the ORGANIZATION, CONTACT-INFO and DESCRIPTION fields.', 'Initial version, obsoletes the earlier snRadiusServerTable.',))
if mibBuilder.loadTexts: fdryRadiusMIB.setLastUpdated('201006020000Z')
if mibBuilder.loadTexts: fdryRadiusMIB.setOrganization('Brocade Communications Systems, Inc.')
if mibBuilder.loadTexts: fdryRadiusMIB.setContactInfo('Technical Support Center 130 Holger Way, San Jose, CA 95134 Email: ipsupport@brocade.com Phone: 1-800-752-8061 URL: www.brocade.com')
if mibBuilder.loadTexts: fdryRadiusMIB.setDescription("The Brocade proprietary MIB module for Radius Authentication Servers It has new table combines Ipv4 and Ipv6 Radius Authentication Servers configuration. Copyright 1996-2010 Brocade Communications Systems, Inc. All rights reserved. This Brocade Communications Systems SNMP Management Information Base Specification embodies Brocade Communications Systems' confidential and proprietary intellectual property. Brocade Communications Systems retains all title and ownership in the Specification, including any revisions. This Specification is supplied AS IS, and Brocade Communications Systems makes no warranty, either express or implied, as to the use, operation, condition, or performance of the specification, and any unintended consequence it may on the user environment.")
class ServerUsage(TextualConvention, Integer32):
    description = 'Represents usage of the server for Authentication, Authorization or Accounting purpose.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("default", 1), ("authenticationOnly", 2), ("authorizationOnly", 3), ("accountingOnly", 4))

fdryRadiusServer = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 1, 8, 1, 1))
fdryRadiusServerTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 1, 8, 1, 1, 1), )
if mibBuilder.loadTexts: fdryRadiusServerTable.setStatus('current')
if mibBuilder.loadTexts: fdryRadiusServerTable.setDescription('Radius server table, listing the RADIUS authentication servers. This table is currently supported by FastIron platform.')
fdryRadiusServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 1, 8, 1, 1, 1, 1), ).setIndexNames((0, "FDRY-RADIUS-MIB", "fdryRadiusServerIndex"))
if mibBuilder.loadTexts: fdryRadiusServerEntry.setStatus('current')
if mibBuilder.loadTexts: fdryRadiusServerEntry.setDescription('An entry in the Radius server table. This table uses running index as the Index to the table. Reasons to go for running index Scheme than IP addresses: 1. The table will be Virtual Routing and Forwarding(VRF) independent that multiple VRFs could share the same address type and address. 2. Index with address type and address could be potentially 17 unsigned integer, parsing and finding next index takes CPU time. The PDU gets to be huge too! 3. IP address is just another attribute, they are supposed to be list of servers.')
fdryRadiusServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 8, 1, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: fdryRadiusServerIndex.setStatus('current')
if mibBuilder.loadTexts: fdryRadiusServerIndex.setDescription('The index to the Radius server Table. FastIron platform supports upto 8 servers.')
fdryRadiusServerAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 8, 1, 1, 1, 1, 2), InetAddressType().clone('ipv4')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryRadiusServerAddrType.setStatus('current')
if mibBuilder.loadTexts: fdryRadiusServerAddrType.setDescription('Radius server IP address Type. FastIron supports address types of ipv4(1) and ipv6(2).')
fdryRadiusServerAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 8, 1, 1, 1, 1, 3), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryRadiusServerAddr.setStatus('current')
if mibBuilder.loadTexts: fdryRadiusServerAddr.setDescription('Radius server IP address.')
fdryRadiusServerAuthPort = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 8, 1, 1, 1, 1, 4), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryRadiusServerAuthPort.setStatus('current')
if mibBuilder.loadTexts: fdryRadiusServerAuthPort.setDescription('Authentication UDP port number. FastIron platform supports default value 1645.')
fdryRadiusServerAcctPort = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 8, 1, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryRadiusServerAcctPort.setStatus('current')
if mibBuilder.loadTexts: fdryRadiusServerAcctPort.setDescription('Account UDP port number. FastIron platform supports default value 1646.')
fdryRadiusServerRowKey = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 8, 1, 1, 1, 1, 6), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryRadiusServerRowKey.setStatus('current')
if mibBuilder.loadTexts: fdryRadiusServerRowKey.setDescription('Authentication key displayed as encrypted text. FastIron platform supports keysize upto 32 characters.')
fdryRadiusServerUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 8, 1, 1, 1, 1, 7), ServerUsage().clone('default')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryRadiusServerUsage.setStatus('current')
if mibBuilder.loadTexts: fdryRadiusServerUsage.setDescription('To allow this server to be dedicated for a particular AAA activity.')
fdryRadiusServerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 8, 1, 1, 1, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryRadiusServerRowStatus.setStatus('current')
if mibBuilder.loadTexts: fdryRadiusServerRowStatus.setDescription('This variable is used to create, modify, or delete a row in this table. When a row in this table is in active(1) state, no objects in that row can be modified except this object. ')
mibBuilder.exportSymbols("FDRY-RADIUS-MIB", fdryRadiusServerAcctPort=fdryRadiusServerAcctPort, fdryRadiusServerEntry=fdryRadiusServerEntry, ServerUsage=ServerUsage, fdryRadiusServerRowKey=fdryRadiusServerRowKey, fdryRadiusServerAddrType=fdryRadiusServerAddrType, fdryRadiusServerUsage=fdryRadiusServerUsage, fdryRadiusServerAuthPort=fdryRadiusServerAuthPort, fdryRadiusServer=fdryRadiusServer, fdryRadiusServerIndex=fdryRadiusServerIndex, fdryRadiusServerRowStatus=fdryRadiusServerRowStatus, PYSNMP_MODULE_ID=fdryRadiusMIB, fdryRadiusServerTable=fdryRadiusServerTable, fdryRadiusMIB=fdryRadiusMIB, fdryRadiusServerAddr=fdryRadiusServerAddr)
