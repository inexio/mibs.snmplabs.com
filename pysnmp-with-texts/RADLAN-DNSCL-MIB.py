#
# PySNMP MIB module RADLAN-DNSCL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RADLAN-DNSCL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:46:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
dnsResConfigSbeltEntry, = mibBuilder.importSymbols("DNS-RESOLVER-MIB", "dnsResConfigSbeltEntry")
DnsName, = mibBuilder.importSymbols("DNS-SERVER-MIB", "DnsName")
rlDnsCl, = mibBuilder.importSymbols("RADLAN-MIB", "rlDnsCl")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, iso, Counter32, Counter64, ModuleIdentity, Integer32, Bits, Unsigned32, NotificationType, MibIdentifier, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "iso", "Counter32", "Counter64", "ModuleIdentity", "Integer32", "Bits", "Unsigned32", "NotificationType", "MibIdentifier", "TimeTicks")
DisplayString, TextualConvention, RowStatus, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus", "TruthValue")
DisplayString, = mibBuilder.importSymbols("SNMPv2-TC-v1", "DisplayString")
rlDnsClMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 89, 93, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDnsClMibVersion.setStatus('current')
if mibBuilder.loadTexts: rlDnsClMibVersion.setDescription("MIB's version, the current version is 1.")
rlDnsClEnable = MibScalar((1, 3, 6, 1, 4, 1, 89, 93, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDnsClEnable.setStatus('current')
if mibBuilder.loadTexts: rlDnsClEnable.setDescription('Enable or Disable the use of the DNS client feature.')
rlDnsClDomainNameTable = MibTable((1, 3, 6, 1, 4, 1, 89, 93, 3), )
if mibBuilder.loadTexts: rlDnsClDomainNameTable.setStatus('current')
if mibBuilder.loadTexts: rlDnsClDomainNameTable.setDescription('The domain names table.')
rlDnsClDomainNameEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 93, 3, 1), ).setIndexNames((0, "RADLAN-DNSCL-MIB", "rlDnsClDomainNameName"))
if mibBuilder.loadTexts: rlDnsClDomainNameEntry.setStatus('current')
if mibBuilder.loadTexts: rlDnsClDomainNameEntry.setDescription(' The row definition for this table.')
rlDnsClDomainNameName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 93, 3, 1, 1), DnsName()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDnsClDomainNameName.setStatus('current')
if mibBuilder.loadTexts: rlDnsClDomainNameName.setDescription('The domain name for this ifIndex.')
rlDnsClDomainNameOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 93, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("static", 1), ("dhcp", 2))).clone('static')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDnsClDomainNameOwner.setStatus('current')
if mibBuilder.loadTexts: rlDnsClDomainNameOwner.setDescription('The Domain Name owner. Static if Domain Name defined by user, dhcp if received by boot protocol like DHCP.')
rlDnsClDomainNameRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 93, 3, 1, 3), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDnsClDomainNameRowStatus.setStatus('current')
if mibBuilder.loadTexts: rlDnsClDomainNameRowStatus.setDescription('The row status variable, used according to row installation and removal conventions.')
rlDnsClMaxNumOfRetransmissions = MibScalar((1, 3, 6, 1, 4, 1, 89, 93, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDnsClMaxNumOfRetransmissions.setStatus('current')
if mibBuilder.loadTexts: rlDnsClMaxNumOfRetransmissions.setDescription('The maximum number of retransmissions for each query.')
rlDnsClMinRetransmissionInterval = MibScalar((1, 3, 6, 1, 4, 1, 89, 93, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 15)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDnsClMinRetransmissionInterval.setStatus('current')
if mibBuilder.loadTexts: rlDnsClMinRetransmissionInterval.setDescription('The minimum number of seconds that must elapsed before retransmission for each query.')
rlDnsClNamesTable = MibTable((1, 3, 6, 1, 4, 1, 89, 93, 6), )
if mibBuilder.loadTexts: rlDnsClNamesTable.setStatus('current')
if mibBuilder.loadTexts: rlDnsClNamesTable.setDescription('The Names table.')
rlDnsClNamesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 93, 6, 1), ).setIndexNames((0, "RADLAN-DNSCL-MIB", "rlDnsClNamesName"), (0, "RADLAN-DNSCL-MIB", "rlDnsClNamesOwner"), (0, "RADLAN-DNSCL-MIB", "rlDnsClNamesIndex"))
if mibBuilder.loadTexts: rlDnsClNamesEntry.setStatus('current')
if mibBuilder.loadTexts: rlDnsClNamesEntry.setDescription(' The row definition for this table.')
rlDnsClNamesName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 93, 6, 1, 1), DnsName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDnsClNamesName.setStatus('current')
if mibBuilder.loadTexts: rlDnsClNamesName.setDescription('The host name.')
rlDnsClNamesOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 93, 6, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("static", 1), ("dhcp", 2))).clone('static')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDnsClNamesOwner.setStatus('current')
if mibBuilder.loadTexts: rlDnsClNamesOwner.setDescription('The Host Name Entry owner. Static if Host Name Entry defined by user, dhcp if received by boot protocol like DHCP.')
rlDnsClNamesIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 93, 6, 1, 3), Integer32())
if mibBuilder.loadTexts: rlDnsClNamesIndex.setStatus('current')
if mibBuilder.loadTexts: rlDnsClNamesIndex.setDescription('A value which makes entries in the table unique when the other index values (rlDnsClNamesName) do not provide a unique index.')
rlDnsClNamesAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 93, 6, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDnsClNamesAddr.setStatus('current')
if mibBuilder.loadTexts: rlDnsClNamesAddr.setDescription('The host IP address')
rlDnsClNamesRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 93, 6, 1, 5), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDnsClNamesRowStatus.setStatus('current')
if mibBuilder.loadTexts: rlDnsClNamesRowStatus.setDescription('The row status variable, used according to row installation and removal conventions.')
dnsResConfigSbeltExtTable = MibTable((1, 3, 6, 1, 4, 1, 89, 93, 7), )
if mibBuilder.loadTexts: dnsResConfigSbeltExtTable.setStatus('current')
if mibBuilder.loadTexts: dnsResConfigSbeltExtTable.setDescription('Augmenting dnsResConfigSbeltTable (dns resolver safety belt table) for added info')
dnsResConfigSbeltExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 93, 7, 1), )
dnsResConfigSbeltEntry.registerAugmentions(("RADLAN-DNSCL-MIB", "dnsResConfigSbeltExtEntry"))
dnsResConfigSbeltExtEntry.setIndexNames(*dnsResConfigSbeltEntry.getIndexNames())
if mibBuilder.loadTexts: dnsResConfigSbeltExtEntry.setStatus('current')
if mibBuilder.loadTexts: dnsResConfigSbeltExtEntry.setDescription('A row of the table dnsResConfigSbeltTable Extended by this definition.')
dnsResConfigSbeltOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 93, 7, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("static", 1), ("dhcp", 2))).clone('static')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dnsResConfigSbeltOwner.setStatus('current')
if mibBuilder.loadTexts: dnsResConfigSbeltOwner.setDescription('The DNS server Entry owner. Static if DNS server Entry defined by user, dhcp if received by boot protocol like DHCP.')
mibBuilder.exportSymbols("RADLAN-DNSCL-MIB", rlDnsClNamesName=rlDnsClNamesName, dnsResConfigSbeltExtEntry=dnsResConfigSbeltExtEntry, rlDnsClDomainNameRowStatus=rlDnsClDomainNameRowStatus, rlDnsClNamesAddr=rlDnsClNamesAddr, rlDnsClDomainNameEntry=rlDnsClDomainNameEntry, rlDnsClNamesRowStatus=rlDnsClNamesRowStatus, rlDnsClEnable=rlDnsClEnable, rlDnsClMaxNumOfRetransmissions=rlDnsClMaxNumOfRetransmissions, rlDnsClDomainNameTable=rlDnsClDomainNameTable, rlDnsClMibVersion=rlDnsClMibVersion, rlDnsClMinRetransmissionInterval=rlDnsClMinRetransmissionInterval, dnsResConfigSbeltOwner=dnsResConfigSbeltOwner, rlDnsClNamesIndex=rlDnsClNamesIndex, rlDnsClDomainNameName=rlDnsClDomainNameName, dnsResConfigSbeltExtTable=dnsResConfigSbeltExtTable, rlDnsClNamesTable=rlDnsClNamesTable, rlDnsClNamesEntry=rlDnsClNamesEntry, rlDnsClDomainNameOwner=rlDnsClDomainNameOwner, rlDnsClNamesOwner=rlDnsClNamesOwner)
