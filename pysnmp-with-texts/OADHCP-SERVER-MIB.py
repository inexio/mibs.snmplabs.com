#
# PySNMP MIB module OADHCP-SERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/OADHCP-SERVER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:32:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, ObjectIdentity, MibIdentifier, enterprises, Bits, ModuleIdentity, Unsigned32, TimeTicks, Gauge32, Counter64, Counter32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Integer32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ObjectIdentity", "MibIdentifier", "enterprises", "Bits", "ModuleIdentity", "Unsigned32", "TimeTicks", "Gauge32", "Counter64", "Counter32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Integer32", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class HostName(DisplayString):
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 32)

class EntryStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("valid", 1), ("invalid", 2), ("insert", 3))

class ObjectStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("enable", 1), ("disable", 2), ("other", 3))

oaccess = MibIdentifier((1, 3, 6, 1, 4, 1, 6926))
oaManagement = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 1))
oaDhcp = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 1, 11))
oaDhcpServer = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 1, 11, 1))
oaDhcpServerGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 1))
oaDhcpServerStatus = MibScalar((1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 1, 1), ObjectStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oaDhcpServerStatus.setStatus('mandatory')
if mibBuilder.loadTexts: oaDhcpServerStatus.setDescription('Setting enable(2) enables generation of DHCP Configuration.')
oaDhcpNetbiosNodeType = MibScalar((1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("B-node", 2), ("P-node", 3), ("M-node", 4), ("H-node", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oaDhcpNetbiosNodeType.setStatus('mandatory')
if mibBuilder.loadTexts: oaDhcpNetbiosNodeType.setDescription('the type of the NetBios Server is general for the whole configuration')
oaDhcpDomainName = MibScalar((1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 1, 3), HostName()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oaDhcpDomainName.setStatus('mandatory')
if mibBuilder.loadTexts: oaDhcpDomainName.setDescription('.')
oaDhcpDefaultLeaseTime = MibScalar((1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oaDhcpDefaultLeaseTime.setStatus('mandatory')
if mibBuilder.loadTexts: oaDhcpDefaultLeaseTime.setDescription('.')
oaDhcpMaxLeaseTime = MibScalar((1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oaDhcpMaxLeaseTime.setStatus('mandatory')
if mibBuilder.loadTexts: oaDhcpMaxLeaseTime.setDescription('.')
oaDhcpDNSTable = MibTable((1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 2), )
if mibBuilder.loadTexts: oaDhcpDNSTable.setStatus('mandatory')
if mibBuilder.loadTexts: oaDhcpDNSTable.setDescription('The DHCP configuration can have more then one DNS servers')
oaDhcpDNSEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 2, 1), ).setIndexNames((0, "OADHCP-SERVER-MIB", "oaDhcpDNSNum"))
if mibBuilder.loadTexts: oaDhcpDNSEntry.setStatus('mandatory')
if mibBuilder.loadTexts: oaDhcpDNSEntry.setDescription('The entries (records).')
oaDhcpDNSNum = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oaDhcpDNSNum.setStatus('mandatory')
if mibBuilder.loadTexts: oaDhcpDNSNum.setDescription('Index of the DNS (priority) ')
oaDhcpDNSIp = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 2, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oaDhcpDNSIp.setStatus('mandatory')
if mibBuilder.loadTexts: oaDhcpDNSIp.setDescription('IP of the DNS ')
oaDhcpDNSStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 2, 1, 3), EntryStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oaDhcpDNSStatus.setStatus('mandatory')
if mibBuilder.loadTexts: oaDhcpDNSStatus.setDescription('.')
oaDhcpNetbiosServersTable = MibTable((1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 3), )
if mibBuilder.loadTexts: oaDhcpNetbiosServersTable.setStatus('mandatory')
if mibBuilder.loadTexts: oaDhcpNetbiosServersTable.setDescription('The DHCP configuration can have more then one NetBios servers')
oaDhcpNetbiosServersEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 3, 1), ).setIndexNames((0, "OADHCP-SERVER-MIB", "oaDhcpNetbiosServerNum"))
if mibBuilder.loadTexts: oaDhcpNetbiosServersEntry.setStatus('mandatory')
if mibBuilder.loadTexts: oaDhcpNetbiosServersEntry.setDescription('The entries (records).')
oaDhcpNetbiosServerNum = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oaDhcpNetbiosServerNum.setStatus('mandatory')
if mibBuilder.loadTexts: oaDhcpNetbiosServerNum.setDescription('.')
oaDhcpNetbiosServerIp = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 3, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oaDhcpNetbiosServerIp.setStatus('mandatory')
if mibBuilder.loadTexts: oaDhcpNetbiosServerIp.setDescription('.')
oaDhcpNetbiosServerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 3, 1, 3), EntryStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oaDhcpNetbiosServerStatus.setStatus('mandatory')
if mibBuilder.loadTexts: oaDhcpNetbiosServerStatus.setDescription('.')
oaDhcpSubnetConfigTable = MibTable((1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 4), )
if mibBuilder.loadTexts: oaDhcpSubnetConfigTable.setStatus('mandatory')
if mibBuilder.loadTexts: oaDhcpSubnetConfigTable.setDescription('.')
oaDhcpSubnetConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 4, 1), ).setIndexNames((0, "OADHCP-SERVER-MIB", "oaDhcpInterfaceName"), (0, "OADHCP-SERVER-MIB", "oaDhcpSubnetIp"), (0, "OADHCP-SERVER-MIB", "oaDhcpSubnetMask"))
if mibBuilder.loadTexts: oaDhcpSubnetConfigEntry.setStatus('mandatory')
if mibBuilder.loadTexts: oaDhcpSubnetConfigEntry.setDescription('The entries (records).')
oaDhcpInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 4, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oaDhcpInterfaceName.setStatus('mandatory')
if mibBuilder.loadTexts: oaDhcpInterfaceName.setDescription("The Interface is not always configured; in these case agent support special dummy value '-'. ")
oaDhcpSubnetIp = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 4, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oaDhcpSubnetIp.setStatus('mandatory')
if mibBuilder.loadTexts: oaDhcpSubnetIp.setDescription('IP address of a curtain subnet .')
oaDhcpSubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 4, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oaDhcpSubnetMask.setStatus('mandatory')
if mibBuilder.loadTexts: oaDhcpSubnetMask.setDescription('The Mask of that subnet')
oaDhcpOptionSubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 4, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oaDhcpOptionSubnetMask.setStatus('mandatory')
if mibBuilder.loadTexts: oaDhcpOptionSubnetMask.setDescription('This is an optional field. This is part of the configuration that the client can get from the DHCP server.')
oaDhcpIsOptionMask = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 4, 1, 5), ObjectStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oaDhcpIsOptionMask.setStatus('mandatory')
if mibBuilder.loadTexts: oaDhcpIsOptionMask.setDescription('.')
oaDhcpSubnetConfigStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 4, 1, 6), EntryStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oaDhcpSubnetConfigStatus.setStatus('mandatory')
if mibBuilder.loadTexts: oaDhcpSubnetConfigStatus.setDescription('.')
oaDhcpIpRangeTable = MibTable((1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 5), )
if mibBuilder.loadTexts: oaDhcpIpRangeTable.setStatus('mandatory')
if mibBuilder.loadTexts: oaDhcpIpRangeTable.setDescription('This table keeps all the IP addresses ranges of each subnet address.')
oaDhcpIpRangeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 5, 1), ).setIndexNames((0, "OADHCP-SERVER-MIB", "oaDhcpIpRangeSubnetIp"), (0, "OADHCP-SERVER-MIB", "oaDhcpIpRangeSubnetMask"), (0, "OADHCP-SERVER-MIB", "oaDhcpIpRangeStart"))
if mibBuilder.loadTexts: oaDhcpIpRangeEntry.setStatus('mandatory')
if mibBuilder.loadTexts: oaDhcpIpRangeEntry.setDescription('The entries (records).')
oaDhcpIpRangeSubnetIp = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 5, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oaDhcpIpRangeSubnetIp.setStatus('mandatory')
if mibBuilder.loadTexts: oaDhcpIpRangeSubnetIp.setDescription('.')
oaDhcpIpRangeSubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 5, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oaDhcpIpRangeSubnetMask.setStatus('mandatory')
if mibBuilder.loadTexts: oaDhcpIpRangeSubnetMask.setDescription('.')
oaDhcpIpRangeStart = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 5, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oaDhcpIpRangeStart.setStatus('mandatory')
if mibBuilder.loadTexts: oaDhcpIpRangeStart.setDescription('The first IP address in a range of addresses')
oaDhcpIpRangeEnd = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 5, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oaDhcpIpRangeEnd.setStatus('mandatory')
if mibBuilder.loadTexts: oaDhcpIpRangeEnd.setDescription('The last IP address in a range of addresses')
oaDhcpIpRangeStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 5, 1, 5), EntryStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oaDhcpIpRangeStatus.setStatus('mandatory')
if mibBuilder.loadTexts: oaDhcpIpRangeStatus.setDescription('status of the entry. A range can be added or deleted')
oaDhcpDefaultGWTable = MibTable((1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 6), )
if mibBuilder.loadTexts: oaDhcpDefaultGWTable.setStatus('mandatory')
if mibBuilder.loadTexts: oaDhcpDefaultGWTable.setDescription('This table keeps all the default gateways each subnet has. Each subnet can hold more then one default GW.')
oaDhcpDefaultGWEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 6, 1), ).setIndexNames((0, "OADHCP-SERVER-MIB", "oaDhcpDefaultGWSubnetIp"), (0, "OADHCP-SERVER-MIB", "oaDhcpDefaultGWSubnetMask"), (0, "OADHCP-SERVER-MIB", "oaDhcpDefaultGWIp"))
if mibBuilder.loadTexts: oaDhcpDefaultGWEntry.setStatus('mandatory')
if mibBuilder.loadTexts: oaDhcpDefaultGWEntry.setDescription('The entries (records).')
oaDhcpDefaultGWSubnetIp = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 6, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oaDhcpDefaultGWSubnetIp.setStatus('mandatory')
if mibBuilder.loadTexts: oaDhcpDefaultGWSubnetIp.setDescription('.')
oaDhcpDefaultGWSubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 6, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oaDhcpDefaultGWSubnetMask.setStatus('mandatory')
if mibBuilder.loadTexts: oaDhcpDefaultGWSubnetMask.setDescription('.')
oaDhcpDefaultGWIp = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 6, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oaDhcpDefaultGWIp.setStatus('mandatory')
if mibBuilder.loadTexts: oaDhcpDefaultGWIp.setDescription('.')
oaDhcpDefaultGWStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 1, 11, 1, 6, 1, 4), EntryStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oaDhcpDefaultGWStatus.setStatus('mandatory')
if mibBuilder.loadTexts: oaDhcpDefaultGWStatus.setDescription('A default GW can be added or deleted')
oaDhcpRelay = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 1, 11, 2))
oaDhcpRelayGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 1, 11, 2, 1))
oaDhcpRelayStatus = MibScalar((1, 3, 6, 1, 4, 1, 6926, 1, 11, 2, 1, 1), ObjectStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oaDhcpRelayStatus.setStatus('mandatory')
if mibBuilder.loadTexts: oaDhcpRelayStatus.setDescription('Setting enable(2) enables the demon of DHCP relay .')
oaDhcpRelayClearConfig = MibScalar((1, 3, 6, 1, 4, 1, 6926, 1, 11, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("None", 1), ("ResetConfig", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oaDhcpRelayClearConfig.setStatus('mandatory')
if mibBuilder.loadTexts: oaDhcpRelayClearConfig.setDescription('If this field is set to reset conig it causes to remove all the data in the tables')
oaDhcpRelayServerTable = MibTable((1, 3, 6, 1, 4, 1, 6926, 1, 11, 2, 2), )
if mibBuilder.loadTexts: oaDhcpRelayServerTable.setStatus('mandatory')
if mibBuilder.loadTexts: oaDhcpRelayServerTable.setDescription('This table keeps the servers that the dhcp relay is going to forward to the dhcp packets.')
oaDhcpRelayServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6926, 1, 11, 2, 2, 1), ).setIndexNames((0, "OADHCP-SERVER-MIB", "oaDhcpRelayServerIp"))
if mibBuilder.loadTexts: oaDhcpRelayServerEntry.setStatus('mandatory')
if mibBuilder.loadTexts: oaDhcpRelayServerEntry.setDescription('The entries (records).')
oaDhcpRelayServerIp = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 1, 11, 2, 2, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oaDhcpRelayServerIp.setStatus('mandatory')
if mibBuilder.loadTexts: oaDhcpRelayServerIp.setDescription("Server's IP. There should be at least one.")
oaDhcpRelayServerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 1, 11, 2, 2, 1, 2), EntryStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oaDhcpRelayServerStatus.setStatus('mandatory')
if mibBuilder.loadTexts: oaDhcpRelayServerStatus.setDescription('A server can be added or deleted')
oaDhcpRelayInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 6926, 1, 11, 2, 3), )
if mibBuilder.loadTexts: oaDhcpRelayInterfaceTable.setStatus('mandatory')
if mibBuilder.loadTexts: oaDhcpRelayInterfaceTable.setDescription('This table keeps the interfaces name that the dhcp relay listens to. If the table is empty it listens to all the interfaces.')
oaDhcpRelayInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6926, 1, 11, 2, 3, 1), ).setIndexNames((0, "OADHCP-SERVER-MIB", "oaDhcpRelayIfName"))
if mibBuilder.loadTexts: oaDhcpRelayInterfaceEntry.setStatus('mandatory')
if mibBuilder.loadTexts: oaDhcpRelayInterfaceEntry.setDescription('The entries (records).')
oaDhcpRelayIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 1, 11, 2, 3, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oaDhcpRelayIfName.setStatus('mandatory')
if mibBuilder.loadTexts: oaDhcpRelayIfName.setDescription('The names of the interfaces of the router that are being listened . The names shoult be of an existing interface.')
oaDhcpRelayIfStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 1, 11, 2, 3, 1, 2), EntryStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oaDhcpRelayIfStatus.setStatus('mandatory')
if mibBuilder.loadTexts: oaDhcpRelayIfStatus.setDescription('An interface name can be added or deleted')
mibBuilder.exportSymbols("OADHCP-SERVER-MIB", oaDhcpNetbiosServerNum=oaDhcpNetbiosServerNum, oaccess=oaccess, oaDhcpIpRangeSubnetIp=oaDhcpIpRangeSubnetIp, oaDhcpRelay=oaDhcpRelay, oaDhcpRelayServerEntry=oaDhcpRelayServerEntry, oaDhcpDNSEntry=oaDhcpDNSEntry, oaManagement=oaManagement, oaDhcpServerGeneral=oaDhcpServerGeneral, oaDhcpNetbiosServersEntry=oaDhcpNetbiosServersEntry, oaDhcpIpRangeEntry=oaDhcpIpRangeEntry, oaDhcpRelayServerStatus=oaDhcpRelayServerStatus, oaDhcpIpRangeSubnetMask=oaDhcpIpRangeSubnetMask, oaDhcpDefaultGWStatus=oaDhcpDefaultGWStatus, oaDhcpRelayInterfaceTable=oaDhcpRelayInterfaceTable, oaDhcpRelayGeneral=oaDhcpRelayGeneral, oaDhcpRelayServerIp=oaDhcpRelayServerIp, oaDhcpDefaultGWSubnetIp=oaDhcpDefaultGWSubnetIp, oaDhcpRelayIfName=oaDhcpRelayIfName, oaDhcpDNSStatus=oaDhcpDNSStatus, oaDhcpDNSTable=oaDhcpDNSTable, oaDhcpDefaultGWIp=oaDhcpDefaultGWIp, oaDhcpRelayServerTable=oaDhcpRelayServerTable, oaDhcpSubnetConfigTable=oaDhcpSubnetConfigTable, EntryStatus=EntryStatus, oaDhcpServer=oaDhcpServer, oaDhcpSubnetMask=oaDhcpSubnetMask, oaDhcpSubnetIp=oaDhcpSubnetIp, oaDhcpRelayStatus=oaDhcpRelayStatus, oaDhcpDomainName=oaDhcpDomainName, ObjectStatus=ObjectStatus, oaDhcpNetbiosNodeType=oaDhcpNetbiosNodeType, oaDhcpDefaultGWTable=oaDhcpDefaultGWTable, oaDhcpIpRangeStart=oaDhcpIpRangeStart, oaDhcpDNSNum=oaDhcpDNSNum, oaDhcpRelayInterfaceEntry=oaDhcpRelayInterfaceEntry, oaDhcpServerStatus=oaDhcpServerStatus, oaDhcp=oaDhcp, oaDhcpIpRangeTable=oaDhcpIpRangeTable, oaDhcpDNSIp=oaDhcpDNSIp, oaDhcpDefaultGWSubnetMask=oaDhcpDefaultGWSubnetMask, oaDhcpNetbiosServerIp=oaDhcpNetbiosServerIp, oaDhcpDefaultLeaseTime=oaDhcpDefaultLeaseTime, oaDhcpNetbiosServerStatus=oaDhcpNetbiosServerStatus, oaDhcpSubnetConfigEntry=oaDhcpSubnetConfigEntry, oaDhcpMaxLeaseTime=oaDhcpMaxLeaseTime, oaDhcpInterfaceName=oaDhcpInterfaceName, oaDhcpOptionSubnetMask=oaDhcpOptionSubnetMask, oaDhcpIsOptionMask=oaDhcpIsOptionMask, oaDhcpIpRangeEnd=oaDhcpIpRangeEnd, HostName=HostName, oaDhcpIpRangeStatus=oaDhcpIpRangeStatus, oaDhcpSubnetConfigStatus=oaDhcpSubnetConfigStatus, oaDhcpNetbiosServersTable=oaDhcpNetbiosServersTable, oaDhcpRelayIfStatus=oaDhcpRelayIfStatus, oaDhcpRelayClearConfig=oaDhcpRelayClearConfig, oaDhcpDefaultGWEntry=oaDhcpDefaultGWEntry)
