#
# PySNMP MIB module ZYXEL-DHCP-CLIENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-DHCP-CLIENT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:49:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Gauge32, MibIdentifier, ModuleIdentity, Unsigned32, Integer32, iso, Counter32, TimeTicks, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Gauge32", "MibIdentifier", "ModuleIdentity", "Unsigned32", "Integer32", "iso", "Counter32", "TimeTicks", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelDhcpClient = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 103))
if mibBuilder.loadTexts: zyxelDhcpClient.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelDhcpClient.setOrganization('Enterprise Solution ZyXEL')
if mibBuilder.loadTexts: zyxelDhcpClient.setContactInfo('')
if mibBuilder.loadTexts: zyxelDhcpClient.setDescription('The subtree for DHCP client')
zyxelDhcpClientSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 103, 1))
zyxelDhcpClientStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 103, 2))
zyxelDhcpClientMaxNumberOfClient = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 103, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyxelDhcpClientMaxNumberOfClient.setStatus('current')
if mibBuilder.loadTexts: zyxelDhcpClientMaxNumberOfClient.setDescription('The maximum number of DHCP client entries that can be created.')
zyxelDhcpClientTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 103, 1, 2), )
if mibBuilder.loadTexts: zyxelDhcpClientTable.setStatus('current')
if mibBuilder.loadTexts: zyxelDhcpClientTable.setDescription('The table contains DHCP client configuration.')
zyxelDhcpClientEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 103, 1, 2, 1), ).setIndexNames((0, "ZYXEL-DHCP-CLIENT-MIB", "zyDhcpClientID"))
if mibBuilder.loadTexts: zyxelDhcpClientEntry.setStatus('current')
if mibBuilder.loadTexts: zyxelDhcpClientEntry.setDescription('An entry contains DHCP client configuration.')
zyDhcpClientID = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 103, 1, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: zyDhcpClientID.setStatus('current')
if mibBuilder.loadTexts: zyDhcpClientID.setDescription('The VLAN ID to which these DHCP settings apply.')
zyDhcpClientRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 103, 1, 2, 1, 2), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyDhcpClientRowStatus.setStatus('current')
if mibBuilder.loadTexts: zyDhcpClientRowStatus.setDescription('This object allows DHCP client entries to be created and deleted.')
zyxelDhcpClientInfoTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 103, 2, 1), )
if mibBuilder.loadTexts: zyxelDhcpClientInfoTable.setStatus('current')
if mibBuilder.loadTexts: zyxelDhcpClientInfoTable.setDescription('The table contains DHCP client information.')
zyxelDhcpClientInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 103, 2, 1, 1), ).setIndexNames((0, "ZYXEL-DHCP-CLIENT-MIB", "zyDhcpClientInfoID"))
if mibBuilder.loadTexts: zyxelDhcpClientInfoEntry.setStatus('current')
if mibBuilder.loadTexts: zyxelDhcpClientInfoEntry.setDescription('An entry contains DHCP client information.')
zyDhcpClientInfoID = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 103, 2, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: zyDhcpClientInfoID.setStatus('current')
if mibBuilder.loadTexts: zyDhcpClientInfoID.setDescription('DHCP client ID.')
zyDhcpClientInfoIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 103, 2, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyDhcpClientInfoIpAddress.setStatus('current')
if mibBuilder.loadTexts: zyDhcpClientInfoIpAddress.setDescription('This field displays the IP address of the client.')
zyDhcpClientInfoMask = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 103, 2, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyDhcpClientInfoMask.setStatus('current')
if mibBuilder.loadTexts: zyDhcpClientInfoMask.setDescription('This field displays teh mask of the client.')
zyDhcpClientInfoLeaseTime = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 103, 2, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyDhcpClientInfoLeaseTime.setStatus('current')
if mibBuilder.loadTexts: zyDhcpClientInfoLeaseTime.setDescription('This field displays the lease time of the client.')
zyDhcpClientInfoRenewTime = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 103, 2, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyDhcpClientInfoRenewTime.setStatus('current')
if mibBuilder.loadTexts: zyDhcpClientInfoRenewTime.setDescription('This field displays the renew time of the client.')
zyDhcpClientInfoRebindTime = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 103, 2, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyDhcpClientInfoRebindTime.setStatus('current')
if mibBuilder.loadTexts: zyDhcpClientInfoRebindTime.setDescription('This field displays the rebind time of the client.')
zyDhcpClientInfoLeaseFrom = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 103, 2, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyDhcpClientInfoLeaseFrom.setStatus('current')
if mibBuilder.loadTexts: zyDhcpClientInfoLeaseFrom.setDescription('Start time of the lease.')
zyDhcpClientInfoLeaseTo = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 103, 2, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyDhcpClientInfoLeaseTo.setStatus('current')
if mibBuilder.loadTexts: zyDhcpClientInfoLeaseTo.setDescription('End time of the lease.')
zyDhcpClientInfoDhcpServer = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 103, 2, 1, 1, 9), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyDhcpClientInfoDhcpServer.setStatus('current')
if mibBuilder.loadTexts: zyDhcpClientInfoDhcpServer.setDescription('DHCP server IP address.')
zyDhcpClientInfoDnsServer1 = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 103, 2, 1, 1, 10), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyDhcpClientInfoDnsServer1.setStatus('current')
if mibBuilder.loadTexts: zyDhcpClientInfoDnsServer1.setDescription('DNS server address assigned to the client.')
zyDhcpClientInfoDnsServer2 = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 103, 2, 1, 1, 11), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyDhcpClientInfoDnsServer2.setStatus('current')
if mibBuilder.loadTexts: zyDhcpClientInfoDnsServer2.setDescription('DNS server address assigned to the client.')
zyDhcpClientInfoDefaultGateway = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 103, 2, 1, 1, 12), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyDhcpClientInfoDefaultGateway.setStatus('current')
if mibBuilder.loadTexts: zyDhcpClientInfoDefaultGateway.setDescription('Gateway address assigned to the client.')
zyDhcpClientInfoRelease = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 103, 2, 1, 1, 13), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyDhcpClientInfoRelease.setStatus('current')
if mibBuilder.loadTexts: zyDhcpClientInfoRelease.setDescription('Release IP address provided by a DHCP server.')
zyDhcpClientInfoRenew = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 103, 2, 1, 1, 14), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyDhcpClientInfoRenew.setStatus('current')
if mibBuilder.loadTexts: zyDhcpClientInfoRenew.setDescription('Updates teh IP address provided by a DHCP server.')
mibBuilder.exportSymbols("ZYXEL-DHCP-CLIENT-MIB", zyDhcpClientInfoLeaseTime=zyDhcpClientInfoLeaseTime, zyDhcpClientInfoLeaseFrom=zyDhcpClientInfoLeaseFrom, zyDhcpClientRowStatus=zyDhcpClientRowStatus, zyxelDhcpClientEntry=zyxelDhcpClientEntry, zyDhcpClientInfoDefaultGateway=zyDhcpClientInfoDefaultGateway, zyDhcpClientInfoRelease=zyDhcpClientInfoRelease, zyDhcpClientInfoID=zyDhcpClientInfoID, zyxelDhcpClient=zyxelDhcpClient, zyxelDhcpClientSetup=zyxelDhcpClientSetup, zyxelDhcpClientInfoTable=zyxelDhcpClientInfoTable, PYSNMP_MODULE_ID=zyxelDhcpClient, zyxelDhcpClientTable=zyxelDhcpClientTable, zyDhcpClientInfoDnsServer1=zyDhcpClientInfoDnsServer1, zyxelDhcpClientInfoEntry=zyxelDhcpClientInfoEntry, zyDhcpClientInfoRenew=zyDhcpClientInfoRenew, zyDhcpClientInfoLeaseTo=zyDhcpClientInfoLeaseTo, zyDhcpClientInfoMask=zyDhcpClientInfoMask, zyxelDhcpClientMaxNumberOfClient=zyxelDhcpClientMaxNumberOfClient, zyDhcpClientInfoIpAddress=zyDhcpClientInfoIpAddress, zyDhcpClientInfoRebindTime=zyDhcpClientInfoRebindTime, zyDhcpClientInfoDnsServer2=zyDhcpClientInfoDnsServer2, zyDhcpClientInfoRenewTime=zyDhcpClientInfoRenewTime, zyDhcpClientInfoDhcpServer=zyDhcpClientInfoDhcpServer, zyxelDhcpClientStatus=zyxelDhcpClientStatus, zyDhcpClientID=zyDhcpClientID)
