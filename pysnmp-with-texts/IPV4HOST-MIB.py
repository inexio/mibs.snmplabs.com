#
# PySNMP MIB module IPV4HOST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IPV4HOST-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:56:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
apIpv4Host, = mibBuilder.importSymbols("APENT-MIB", "apIpv4Host")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, TimeTicks, NotificationType, IpAddress, ObjectIdentity, Bits, Gauge32, Unsigned32, Counter32, iso, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "TimeTicks", "NotificationType", "IpAddress", "ObjectIdentity", "Bits", "Gauge32", "Unsigned32", "Counter32", "iso", "Integer32")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
apIpv4HostMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2467, 1, 9, 6, 1))
if mibBuilder.loadTexts: apIpv4HostMib.setLastUpdated('9801282000Z')
if mibBuilder.loadTexts: apIpv4HostMib.setOrganization('ArrowPoint Communications Inc.')
if mibBuilder.loadTexts: apIpv4HostMib.setContactInfo('PPostal: ArrowPoint Communications Inc. 50 Nagog Park Acton, Massachusetts 01720 Tel: +1 978-206-3000 option 1 E-Mail: support@arrowpoint.com')
if mibBuilder.loadTexts: apIpv4HostMib.setDescription('This MIB module describes the ArrowPoint enterprise MIB support for IPv4 Host table')
apIpv4HostTable = MibTable((1, 3, 6, 1, 4, 1, 2467, 1, 9, 6, 2), )
if mibBuilder.loadTexts: apIpv4HostTable.setStatus('current')
if mibBuilder.loadTexts: apIpv4HostTable.setDescription('A table of Host table entries.')
apIpv4HostEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2467, 1, 9, 6, 2, 1), ).setIndexNames((0, "IPV4HOST-MIB", "apIpv4HostName"))
if mibBuilder.loadTexts: apIpv4HostEntry.setStatus('current')
if mibBuilder.loadTexts: apIpv4HostEntry.setDescription('ArrowPoint Host Table entries')
apIpv4HostName = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 9, 6, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 16))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apIpv4HostName.setStatus('current')
if mibBuilder.loadTexts: apIpv4HostName.setDescription('The host name')
apIpv4HostIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 9, 6, 2, 1, 2), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apIpv4HostIpAddress.setStatus('current')
if mibBuilder.loadTexts: apIpv4HostIpAddress.setDescription('The IP Address associated with the host name.')
apIpv4HostStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 9, 6, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apIpv4HostStatus.setStatus('current')
if mibBuilder.loadTexts: apIpv4HostStatus.setDescription('Status object for this row')
mibBuilder.exportSymbols("IPV4HOST-MIB", apIpv4HostIpAddress=apIpv4HostIpAddress, apIpv4HostMib=apIpv4HostMib, apIpv4HostName=apIpv4HostName, apIpv4HostTable=apIpv4HostTable, apIpv4HostEntry=apIpv4HostEntry, PYSNMP_MODULE_ID=apIpv4HostMib, apIpv4HostStatus=apIpv4HostStatus)
