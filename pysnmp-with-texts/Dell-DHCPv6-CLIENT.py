#
# PySNMP MIB module Dell-DHCPv6-CLIENT (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Dell-DHCPv6-CLIENT
# Produced by pysmi-0.3.4 at Wed May  1 12:55:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
rlDhcpv6Client, = mibBuilder.importSymbols("Dell-DHCPv6", "rlDhcpv6Client")
InterfaceIndex, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
InetAddressIPv6, InetAddressPrefixLength, InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressIPv6", "InetAddressPrefixLength", "InetAddress", "InetAddressType")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Counter32, Unsigned32, ObjectIdentity, TimeTicks, Counter64, iso, Bits, MibIdentifier, IpAddress, Integer32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter32", "Unsigned32", "ObjectIdentity", "TimeTicks", "Counter64", "iso", "Bits", "MibIdentifier", "IpAddress", "Integer32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32")
TextualConvention, RowStatus, MacAddress, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "MacAddress", "DisplayString", "TruthValue")
rlDhcpv6ClientMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 89, 214, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpv6ClientMibVersion.setStatus('current')
if mibBuilder.loadTexts: rlDhcpv6ClientMibVersion.setDescription('')
rlDhcpv6ClientSupported = MibScalar((1, 3, 6, 1, 4, 1, 89, 214, 2, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpv6ClientSupported.setStatus('current')
if mibBuilder.loadTexts: rlDhcpv6ClientSupported.setDescription('')
rlDhcpv6ClientTable = MibTable((1, 3, 6, 1, 4, 1, 89, 214, 2, 3), )
if mibBuilder.loadTexts: rlDhcpv6ClientTable.setStatus('current')
if mibBuilder.loadTexts: rlDhcpv6ClientTable.setDescription(' The table saved ipv6 DHCP clients and their services.')
rlDhcpv6ClientEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 214, 2, 3, 1), ).setIndexNames((0, "Dell-DHCPv6-CLIENT", "rlDhcpv6ClientIfIndex"))
if mibBuilder.loadTexts: rlDhcpv6ClientEntry.setStatus('current')
if mibBuilder.loadTexts: rlDhcpv6ClientEntry.setDescription('An entry in rlDhcpv6Client.')
rlDhcpv6ClientIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 2, 3, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpv6ClientIfIndex.setStatus('current')
if mibBuilder.loadTexts: rlDhcpv6ClientIfIndex.setDescription(' The interface that ipv6 DHCP client is running on. ')
rlDhcpv6ClientPd = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpv6ClientPd.setStatus('current')
if mibBuilder.loadTexts: rlDhcpv6ClientPd.setDescription('Enables Prefix Delegation service on the interface.')
rlDhcpv6ClientStateless = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpv6ClientStateless.setStatus('current')
if mibBuilder.loadTexts: rlDhcpv6ClientStateless.setDescription('Enables Stateless service on the interface.')
rlDhcpv6ClientReconfigure = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 2, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpv6ClientReconfigure.setStatus('current')
if mibBuilder.loadTexts: rlDhcpv6ClientReconfigure.setDescription('Enables reconfiguration service on the interface.')
rlDhcpv6ClientInfoRefreshMin = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 2, 3, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(600, 4294967295)).clone(86400)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpv6ClientInfoRefreshMin.setStatus('current')
if mibBuilder.loadTexts: rlDhcpv6ClientInfoRefreshMin.setDescription('Defines the minimum refresh time between information-request packets on the same interface.')
rlDhcpv6ClientInfoRefreshConf = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 2, 3, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(86400, 4294967295)).clone(86400)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpv6ClientInfoRefreshConf.setStatus('current')
if mibBuilder.loadTexts: rlDhcpv6ClientInfoRefreshConf.setDescription('Defines the refresh time between information-request packets on the same interface.')
rlDhcpv6ClientInfoRefreshReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 2, 3, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpv6ClientInfoRefreshReceived.setStatus('current')
if mibBuilder.loadTexts: rlDhcpv6ClientInfoRefreshReceived.setDescription('Shows the received time from DHCP server untill next information-request packet.')
rlDhcpv6ClientInfoRefreshRemain = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 2, 3, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpv6ClientInfoRefreshRemain.setStatus('current')
if mibBuilder.loadTexts: rlDhcpv6ClientInfoRefreshRemain.setDescription('Shows the remain time untill next information-request packet.')
rlDhcpv6ClientDhcpServerInetAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 2, 3, 1, 9), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpv6ClientDhcpServerInetAddressType.setStatus('current')
if mibBuilder.loadTexts: rlDhcpv6ClientDhcpServerInetAddressType.setDescription('Contains Inet address Type of current DHCPv6 server.')
rlDhcpv6ClientDhcpServerInetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 2, 3, 1, 10), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpv6ClientDhcpServerInetAddress.setStatus('current')
if mibBuilder.loadTexts: rlDhcpv6ClientDhcpServerInetAddress.setDescription('Contains Inet address of current DHCPv6 server.')
rlDhcpv6ClientDhcpServerDuid = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 2, 3, 1, 11), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpv6ClientDhcpServerDuid.setStatus('current')
if mibBuilder.loadTexts: rlDhcpv6ClientDhcpServerDuid.setDescription('Contains DUID of current DHCPv6 server.')
rlDhcpv6ClientDhcpServerPreference = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 2, 3, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpv6ClientDhcpServerPreference.setStatus('current')
if mibBuilder.loadTexts: rlDhcpv6ClientDhcpServerPreference.setDescription('Contains preference of current DHCPv6 server.')
rlDhcpv6ClientState = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 2, 3, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("idle", 1), ("configuring", 2), ("configured", 3))).clone('idle')).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpv6ClientState.setStatus('current')
if mibBuilder.loadTexts: rlDhcpv6ClientState.setDescription('shows the state machine.')
rlDhcpv6ClientTftpServerName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 2, 3, 1, 14), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 160))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpv6ClientTftpServerName.setStatus('current')
if mibBuilder.loadTexts: rlDhcpv6ClientTftpServerName.setDescription('The Tftp server name received by DHCPv6 stateless service.')
rlDhcpv6ClientTftpFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 2, 3, 1, 15), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 160))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpv6ClientTftpFileName.setStatus('current')
if mibBuilder.loadTexts: rlDhcpv6ClientTftpFileName.setDescription('Name of file to use in configuration process received by DHCPv6 stateless service.')
rlDhcpv6ClientTimeZone = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 2, 3, 1, 16), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpv6ClientTimeZone.setStatus('current')
if mibBuilder.loadTexts: rlDhcpv6ClientTimeZone.setDescription('The timezone received by DHCPv6 stateless service')
rlDhcpv6ClientOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 2, 3, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpv6ClientOperStatus.setStatus('current')
if mibBuilder.loadTexts: rlDhcpv6ClientOperStatus.setDescription('The operational status of this entry. Enabled or Disabled .')
rlDhcpv6ClientDisableReason = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 2, 3, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("ipv6Disable", 2), ("portDown", 3), ("portDownAndIpv6Disable", 4))).clone('none')).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpv6ClientDisableReason.setStatus('current')
if mibBuilder.loadTexts: rlDhcpv6ClientDisableReason.setDescription('The disable operational status reason.')
rlDhcpv6ClientStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 2, 3, 1, 19), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlDhcpv6ClientStatus.setStatus('current')
if mibBuilder.loadTexts: rlDhcpv6ClientStatus.setDescription('The status of this entry. Creating the entry when ipv6 DHCP is enabled OR ipv6 DHCP stateless in enabled OR ipv6 DHCP pd is enabled.')
rlDhcpv6ClientInfoRefreshIsReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 2, 3, 1, 20), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpv6ClientInfoRefreshIsReceived.setStatus('current')
if mibBuilder.loadTexts: rlDhcpv6ClientInfoRefreshIsReceived.setDescription('Shows whether information-request option is received.')
rlDhcpv6ClientIndirectImageFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 2, 3, 1, 21), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 160))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpv6ClientIndirectImageFileName.setStatus('current')
if mibBuilder.loadTexts: rlDhcpv6ClientIndirectImageFileName.setDescription('Name of file to use in autoupdate process received by DHCPv6 stateless service.')
rlDhcpv6ClientAuxDnsServerListTable = MibTable((1, 3, 6, 1, 4, 1, 89, 214, 2, 4), )
if mibBuilder.loadTexts: rlDhcpv6ClientAuxDnsServerListTable.setStatus('current')
if mibBuilder.loadTexts: rlDhcpv6ClientAuxDnsServerListTable.setDescription(' The table saved the list of DNS servers received by DHCPv6 stateless service. This is an auxulary table for rlDhcpv6ClientEntry.')
rlDhcpv6ClientAuxDnsServerListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 214, 2, 4, 1), ).setIndexNames((0, "Dell-DHCPv6-CLIENT", "rlDhcpv6ClientAuxDnsServerListIfIndex"), (0, "Dell-DHCPv6-CLIENT", "rlDhcpv6ClientAuxDnsServerListPriority"))
if mibBuilder.loadTexts: rlDhcpv6ClientAuxDnsServerListEntry.setStatus('current')
if mibBuilder.loadTexts: rlDhcpv6ClientAuxDnsServerListEntry.setDescription('An entry in rlDhcpv6ClientAuxDnsServerListTable.')
rlDhcpv6ClientAuxDnsServerListIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 2, 4, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: rlDhcpv6ClientAuxDnsServerListIfIndex.setStatus('current')
if mibBuilder.loadTexts: rlDhcpv6ClientAuxDnsServerListIfIndex.setDescription(' The IfIndex in rlDhcpv6ClientAuxDnsServerListEntry. ')
rlDhcpv6ClientAuxDnsServerListPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 2, 4, 1, 2), Integer32())
if mibBuilder.loadTexts: rlDhcpv6ClientAuxDnsServerListPriority.setStatus('current')
if mibBuilder.loadTexts: rlDhcpv6ClientAuxDnsServerListPriority.setDescription(' The priority of the entry. ')
rlDhcpv6ClientAuxDnsServerListAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 2, 4, 1, 3), InetAddressIPv6()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpv6ClientAuxDnsServerListAddress.setStatus('current')
if mibBuilder.loadTexts: rlDhcpv6ClientAuxDnsServerListAddress.setDescription('DNS server address received by DHCPv6 stateless service')
rlDhcpv6ClientAuxSntpServerListTable = MibTable((1, 3, 6, 1, 4, 1, 89, 214, 2, 5), )
if mibBuilder.loadTexts: rlDhcpv6ClientAuxSntpServerListTable.setStatus('current')
if mibBuilder.loadTexts: rlDhcpv6ClientAuxSntpServerListTable.setDescription(' The table saved the list of Sntp servers received by DHCPv6 stateless service. This is an auxulary table for rlDhcpv6ClientEntry.')
rlDhcpv6ClientAuxSntpServerListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 214, 2, 5, 1), ).setIndexNames((0, "Dell-DHCPv6-CLIENT", "rlDhcpv6ClientAuxSntpServerListIfIndex"), (0, "Dell-DHCPv6-CLIENT", "rlDhcpv6ClientAuxSntpServerListPriority"))
if mibBuilder.loadTexts: rlDhcpv6ClientAuxSntpServerListEntry.setStatus('current')
if mibBuilder.loadTexts: rlDhcpv6ClientAuxSntpServerListEntry.setDescription('An entry in rlDhcpv6ClientAuxSntpServerListTable.')
rlDhcpv6ClientAuxSntpServerListIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 2, 5, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: rlDhcpv6ClientAuxSntpServerListIfIndex.setStatus('current')
if mibBuilder.loadTexts: rlDhcpv6ClientAuxSntpServerListIfIndex.setDescription(' The IfIndex in rlDhcpv6ClientAuxSntpServerEntry. ')
rlDhcpv6ClientAuxSntpServerListPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 2, 5, 1, 2), Integer32())
if mibBuilder.loadTexts: rlDhcpv6ClientAuxSntpServerListPriority.setStatus('current')
if mibBuilder.loadTexts: rlDhcpv6ClientAuxSntpServerListPriority.setDescription(' The priority of the entry. ')
rlDhcpv6ClientAuxSntpServerListAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 2, 5, 1, 3), InetAddressIPv6()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpv6ClientAuxSntpServerListAddress.setStatus('current')
if mibBuilder.loadTexts: rlDhcpv6ClientAuxSntpServerListAddress.setDescription('Sntp server address received by DHCPv6 stateless service')
rlDhcpv6ClientAuxDomainNameSearchListTable = MibTable((1, 3, 6, 1, 4, 1, 89, 214, 2, 6), )
if mibBuilder.loadTexts: rlDhcpv6ClientAuxDomainNameSearchListTable.setStatus('current')
if mibBuilder.loadTexts: rlDhcpv6ClientAuxDomainNameSearchListTable.setDescription(' The table saved the list of Domain Name Search received by DHCPv6 stateless service. This is an auxulary table for rlDhcpv6ClientEntry.')
rlDhcpv6ClientAuxDomainNameSearchListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 214, 2, 6, 1), ).setIndexNames((0, "Dell-DHCPv6-CLIENT", "rlDhcpv6ClientAuxDomainNameSearchListIfIndex"), (0, "Dell-DHCPv6-CLIENT", "rlDhcpv6ClientAuxDomainNameSearchListPriority"))
if mibBuilder.loadTexts: rlDhcpv6ClientAuxDomainNameSearchListEntry.setStatus('current')
if mibBuilder.loadTexts: rlDhcpv6ClientAuxDomainNameSearchListEntry.setDescription('An entry in rlDhcpv6ClientAuxDomainNameSearchListTable.')
rlDhcpv6ClientAuxDomainNameSearchListIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 2, 6, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: rlDhcpv6ClientAuxDomainNameSearchListIfIndex.setStatus('current')
if mibBuilder.loadTexts: rlDhcpv6ClientAuxDomainNameSearchListIfIndex.setDescription(' The IfIndex in rlDhcpv6ClientAuxDomainNameSearchEntry. ')
rlDhcpv6ClientAuxDomainNameSearchListPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 2, 6, 1, 2), Integer32())
if mibBuilder.loadTexts: rlDhcpv6ClientAuxDomainNameSearchListPriority.setStatus('current')
if mibBuilder.loadTexts: rlDhcpv6ClientAuxDomainNameSearchListPriority.setDescription(' The priority of the entry. ')
rlDhcpv6ClientAuxDomainNameSearchListName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 2, 6, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 160))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpv6ClientAuxDomainNameSearchListName.setStatus('current')
if mibBuilder.loadTexts: rlDhcpv6ClientAuxDomainNameSearchListName.setDescription('Domain Name in DomainNameSearchList received by DHCPv6 stateless service')
rlDhcpv6ClientCommandTable = MibTable((1, 3, 6, 1, 4, 1, 89, 214, 2, 7), ).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpv6ClientCommandTable.setStatus('current')
if mibBuilder.loadTexts: rlDhcpv6ClientCommandTable.setDescription('Action MIB for DHCP v6 Renew command.')
rlDhcpv6ClientCommandEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 214, 2, 7, 1), ).setIndexNames((0, "Dell-DHCPv6-CLIENT", "rlDhcpv6ClientCommandIfIndex"))
if mibBuilder.loadTexts: rlDhcpv6ClientCommandEntry.setStatus('current')
if mibBuilder.loadTexts: rlDhcpv6ClientCommandEntry.setDescription('The row definition for this table.')
rlDhcpv6ClientCommandIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 2, 7, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: rlDhcpv6ClientCommandIfIndex.setStatus('current')
if mibBuilder.loadTexts: rlDhcpv6ClientCommandIfIndex.setDescription(' The IfIndex in rlDhcpv6ClientAuxDomainNameSearchEntry. ')
rlDhcpv6ClientCommandAction = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 2, 7, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("none", 0), ("renew", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpv6ClientCommandAction.setStatus('current')
if mibBuilder.loadTexts: rlDhcpv6ClientCommandAction.setDescription('Action to apply. The default value is none.')
rlDhcpv6ClientEnabledByDefaultRemovedIfindex = MibScalar((1, 3, 6, 1, 4, 1, 89, 214, 2, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpv6ClientEnabledByDefaultRemovedIfindex.setStatus('current')
if mibBuilder.loadTexts: rlDhcpv6ClientEnabledByDefaultRemovedIfindex.setDescription('DHCPv6 Client flag is relevant when mtsc parameter DHCPv6_client_enabled_by_default is TRUE. If the MIB has non zero value the meaning is that DHCP client has removed from configuration by the user on the interface and signs to application not to add DHCPv6 client entry. Otherwise (zero value) - the meaning is that DHCPv6 client entry must be added. ')
mibBuilder.exportSymbols("Dell-DHCPv6-CLIENT", rlDhcpv6ClientIndirectImageFileName=rlDhcpv6ClientIndirectImageFileName, rlDhcpv6ClientTimeZone=rlDhcpv6ClientTimeZone, rlDhcpv6ClientAuxSntpServerListTable=rlDhcpv6ClientAuxSntpServerListTable, rlDhcpv6ClientAuxDomainNameSearchListIfIndex=rlDhcpv6ClientAuxDomainNameSearchListIfIndex, rlDhcpv6ClientDhcpServerDuid=rlDhcpv6ClientDhcpServerDuid, rlDhcpv6ClientInfoRefreshRemain=rlDhcpv6ClientInfoRefreshRemain, rlDhcpv6ClientTftpServerName=rlDhcpv6ClientTftpServerName, rlDhcpv6ClientAuxSntpServerListEntry=rlDhcpv6ClientAuxSntpServerListEntry, rlDhcpv6ClientCommandTable=rlDhcpv6ClientCommandTable, rlDhcpv6ClientAuxDnsServerListTable=rlDhcpv6ClientAuxDnsServerListTable, rlDhcpv6ClientInfoRefreshIsReceived=rlDhcpv6ClientInfoRefreshIsReceived, rlDhcpv6ClientStatus=rlDhcpv6ClientStatus, rlDhcpv6ClientAuxSntpServerListPriority=rlDhcpv6ClientAuxSntpServerListPriority, rlDhcpv6ClientAuxSntpServerListAddress=rlDhcpv6ClientAuxSntpServerListAddress, rlDhcpv6ClientTftpFileName=rlDhcpv6ClientTftpFileName, rlDhcpv6ClientSupported=rlDhcpv6ClientSupported, rlDhcpv6ClientDhcpServerInetAddress=rlDhcpv6ClientDhcpServerInetAddress, rlDhcpv6ClientAuxDomainNameSearchListEntry=rlDhcpv6ClientAuxDomainNameSearchListEntry, rlDhcpv6ClientAuxDnsServerListAddress=rlDhcpv6ClientAuxDnsServerListAddress, rlDhcpv6ClientPd=rlDhcpv6ClientPd, rlDhcpv6ClientCommandEntry=rlDhcpv6ClientCommandEntry, rlDhcpv6ClientAuxDnsServerListEntry=rlDhcpv6ClientAuxDnsServerListEntry, rlDhcpv6ClientAuxDomainNameSearchListName=rlDhcpv6ClientAuxDomainNameSearchListName, rlDhcpv6ClientCommandAction=rlDhcpv6ClientCommandAction, rlDhcpv6ClientAuxDnsServerListIfIndex=rlDhcpv6ClientAuxDnsServerListIfIndex, rlDhcpv6ClientIfIndex=rlDhcpv6ClientIfIndex, rlDhcpv6ClientAuxDomainNameSearchListPriority=rlDhcpv6ClientAuxDomainNameSearchListPriority, rlDhcpv6ClientTable=rlDhcpv6ClientTable, rlDhcpv6ClientAuxSntpServerListIfIndex=rlDhcpv6ClientAuxSntpServerListIfIndex, rlDhcpv6ClientEnabledByDefaultRemovedIfindex=rlDhcpv6ClientEnabledByDefaultRemovedIfindex, rlDhcpv6ClientInfoRefreshConf=rlDhcpv6ClientInfoRefreshConf, rlDhcpv6ClientInfoRefreshMin=rlDhcpv6ClientInfoRefreshMin, rlDhcpv6ClientStateless=rlDhcpv6ClientStateless, rlDhcpv6ClientState=rlDhcpv6ClientState, rlDhcpv6ClientEntry=rlDhcpv6ClientEntry, rlDhcpv6ClientDhcpServerInetAddressType=rlDhcpv6ClientDhcpServerInetAddressType, rlDhcpv6ClientMibVersion=rlDhcpv6ClientMibVersion, rlDhcpv6ClientAuxDomainNameSearchListTable=rlDhcpv6ClientAuxDomainNameSearchListTable, rlDhcpv6ClientOperStatus=rlDhcpv6ClientOperStatus, rlDhcpv6ClientCommandIfIndex=rlDhcpv6ClientCommandIfIndex, rlDhcpv6ClientReconfigure=rlDhcpv6ClientReconfigure, rlDhcpv6ClientInfoRefreshReceived=rlDhcpv6ClientInfoRefreshReceived, rlDhcpv6ClientDisableReason=rlDhcpv6ClientDisableReason, rlDhcpv6ClientAuxDnsServerListPriority=rlDhcpv6ClientAuxDnsServerListPriority, rlDhcpv6ClientDhcpServerPreference=rlDhcpv6ClientDhcpServerPreference)
