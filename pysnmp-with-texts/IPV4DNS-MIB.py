#
# PySNMP MIB module IPV4DNS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IPV4DNS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:56:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
apIpv4Dns, = mibBuilder.importSymbols("APENT-MIB", "apIpv4Dns")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Counter32, Unsigned32, iso, Gauge32, IpAddress, ObjectIdentity, Counter64, ModuleIdentity, Bits, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter32", "Unsigned32", "iso", "Gauge32", "IpAddress", "ObjectIdentity", "Counter64", "ModuleIdentity", "Bits", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "MibIdentifier")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
apIpv4DnsMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2467, 1, 9, 7, 1))
if mibBuilder.loadTexts: apIpv4DnsMib.setLastUpdated('9801282000Z')
if mibBuilder.loadTexts: apIpv4DnsMib.setOrganization('ArrowPoint Communications Inc.')
if mibBuilder.loadTexts: apIpv4DnsMib.setContactInfo('Postal: ArrowPoint Communications Inc. 50 Nagog Park Acton, Massachusetts 01720 Tel: +1 978-206-3000 option 1 E-Mail: support@arrowpoint.com')
if mibBuilder.loadTexts: apIpv4DnsMib.setDescription('This MIB module describes the ArrowPoint enterprise MIB support for IPv4 DNS configuration')
apIpv4DnsDefaultSuffix = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 9, 7, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apIpv4DnsDefaultSuffix.setStatus('current')
if mibBuilder.loadTexts: apIpv4DnsDefaultSuffix.setDescription('The default Suffix to be used in conjunction with DSN queries')
apIpv4DnsPrimary = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 9, 7, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apIpv4DnsPrimary.setStatus('current')
if mibBuilder.loadTexts: apIpv4DnsPrimary.setDescription('The default DNS address to use for DNS queries')
apIpv4DnsTable = MibTable((1, 3, 6, 1, 4, 1, 2467, 1, 9, 7, 4), )
if mibBuilder.loadTexts: apIpv4DnsTable.setStatus('current')
if mibBuilder.loadTexts: apIpv4DnsTable.setDescription('A table of secondary DNS addresses')
apIpv4DnsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2467, 1, 9, 7, 4, 1), ).setIndexNames((0, "IPV4DNS-MIB", "apIpv4DnsSecondaryIP"))
if mibBuilder.loadTexts: apIpv4DnsEntry.setStatus('current')
if mibBuilder.loadTexts: apIpv4DnsEntry.setDescription('ArrowPoint secondary DNS record')
apIpv4DnsSecondaryIP = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 9, 7, 4, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apIpv4DnsSecondaryIP.setStatus('current')
if mibBuilder.loadTexts: apIpv4DnsSecondaryIP.setDescription('The secondary DNS IP Address')
apIpv4DnsStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 9, 7, 4, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apIpv4DnsStatus.setStatus('current')
if mibBuilder.loadTexts: apIpv4DnsStatus.setDescription('Status object for this row')
mibBuilder.exportSymbols("IPV4DNS-MIB", apIpv4DnsTable=apIpv4DnsTable, apIpv4DnsEntry=apIpv4DnsEntry, apIpv4DnsPrimary=apIpv4DnsPrimary, apIpv4DnsSecondaryIP=apIpv4DnsSecondaryIP, apIpv4DnsDefaultSuffix=apIpv4DnsDefaultSuffix, apIpv4DnsStatus=apIpv4DnsStatus, apIpv4DnsMib=apIpv4DnsMib, PYSNMP_MODULE_ID=apIpv4DnsMib)
